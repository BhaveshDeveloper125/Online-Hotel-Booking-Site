from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.http import HttpResponse
from .models import hotels , Feedback ,Hotel_request ,Hotel , user_comment , booking  , hotel_user , HotelImage
from django.db.models import Q 
from django.contrib.auth.models import  auth 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from background_task import background
from datetime import datetime, timedelta
from django.core.cache import cache
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail



def index(request):
    h1=hotels.objects.all()
    lhotel = hotels.objects.filter(is_luxury=True)
    h3 = hotels.objects.filter(is_luxury=True)[:2]
    h4 = hotels.objects.filter(is_luxury=False)[:3]
    h5 = hotels.objects.filter(is_luxury=True)[:1]
    user_name = request.user.username
    user_bookings = booking.objects.filter(user=user_name)
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking.objects.filter(id=booking_id).delete()
    return render(request , "index.html", {"h1":h1,'lhotel':lhotel ,  "h3":h3 , "h4":h4 , "h5":h5 , 'user_bookings': user_bookings})


def hotel_detail(request, hotel_hname):
    hotel = get_object_or_404(hotels, hname=hotel_hname)
    return render(request, 'rooms.html', {'hotel': hotel})


def rooms(request, pk):
    h2 = hotels.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        feedbackfromuser = request.POST['feedbackfromuser']
        feedback_user=user_comment(name=name , email=email , feedback=feedbackfromuser , hotel=h2)
        feedback_user.save()
        return redirect('/')
    
    comment = user_comment.objects.filter(hotel=h2)
    return render(request, "rooms.html", {'h2': h2,'comment':comment})


def about(request):
    return render(request , "about.html")


def feedback(request):  
    
    if request.method == 'POST':
       name = request.POST['name']
       email = request.POST['email']
       feedback_text = request.POST['feedbackfromuser']
       user_feedback = Feedback(name=name , email=email , feedback=feedback_text)
       user_feedback.save()
       return redirect('/')
    
    feedback_data = Feedback.objects.all()
    return render(request , "feedback.html",{'feedback_data':feedback_data})
    

def privacy(request):
    return render(request , "privacy.html")


def tc(request):
    return render(request , "terms and condition.html")


def addhotel(request):
    if request.method == 'POST':
        hotel_name = request.POST['hotel_name']
        availabel_room = request.POST['avl_room']
        per_person = request.POST['per_room']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        price_room = request.POST['pri_room']
        about = request.POST['about']
        cover = request.FILES.get('cover') 
        other = request.FILES.getlist('other_images')  
        email = request.POST['email']

        if Hotel_request.objects.filter(email=email).exists():
            return HttpResponse('Email you entered is already registered please use another Email')
        else:
            user = Hotel_request(hotel_name=hotel_name, availabel_room=availabel_room, per_person=per_person, address=address, city=city, state=state, price_room=price_room, about=about, cover=cover,  email=email)
            user.save()
            for i in other:
                HotelImage.objects.create(hotel=user, images=i)
            
            send_mail(
                'New Hotel Request',
                'You have another request for new hotel: ' + hotel_name,
                'g20projectmail@gmail.com',
                ['bhaveshlaptop90@gmail.com'],
                fail_silently=False,
            )
            return redirect('/')
        

    return render(request, 'addhotel.html')


def hotelogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password'] 
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            print('success login')
            return redirect('hotelogin')  #Assuming 'hotelogin' is the name of the view you want to redirect to
        else:
            messages.info(request, 'Invalid email or password')
            return redirect('/')  #Assuming 'hotelogin' is the name of the login view
    return render(request, "hotelogin.html")


def hotel_logout(request):
    auth.logout(request)
    return redirect('/')


def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        results = hotels.objects.filter(Q(hname__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query)) 
    return render(request, 'index.html', {'results': results })


def categories(request , category):
      cat = hotels.objects.filter(category_in_star=category)

      return render(request , "index.html", {"cat":cat })


def sorting(request):
    sort_order = request.GET.get('sort_order')
    if sort_order == 'price_low_high':
        srting = hotels.objects.order_by('price')
    elif sort_order == 'price_high_low':
        srting = hotels.objects.order_by('-price')
    elif sort_order == 'category_low_high':
        srting = hotels.objects.order_by('category_in_star')
    elif sort_order == 'category_high_low':
        srting = hotels.objects.order_by('-category_in_star')
    else:
        srting = hotels.objects.all()
    return render(request, 'index.html', {'srting': srting})


def bookinghotel(request,pk):
    if request.method == 'POST':
        h2 = hotels.objects.get(pk=pk)
        room = int(request.POST['rooms'])

        if room > h2.rooms:
            messages.info(request, 'The number of rooms entered is more than the available rooms.')
            
        else:
            arrival = datetime.strptime(request.POST['arrival'], "%Y-%m-%d")
            departure = datetime.strptime(request.POST['departure'], "%Y-%m-%d")
            total_price = request.POST['totalPrice']
            user = request.user.username


            booking_details = booking(booked_room_count=room , ariival_date=arrival , departure_date=departure , total_price=total_price , hotel=h2 , user=user)
            booking_details.save()
            current_room  =  h2.rooms
            final_room=current_room-room
            h2.rooms=final_room
            h2.save()

            time_gap = (departure - arrival).total_seconds()

            cache.set('subtract_rooms', room, time_gap)

            return redirect('/')


def payment(request):
    return render(request , "payment.html")

