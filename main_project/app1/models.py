from django.db import models
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.views.decorators import staff_member_required
import logging
logger = logging.getLogger(__name__)



class hotels(models.Model):
    hname = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images' , default='835201.jpg')
    rooms = models.IntegerField()
    per = models.IntegerField()
    price = models.FloatField()
    about = models.TextField()
    address = models.TextField()
    email = models.EmailField(default='default@mail.com' , unique = True)
    state = models.CharField(max_length=20,default='Gujarat')
    city = models.CharField(max_length=20,default='Ahmedabad')
    category_in_star = models.IntegerField(choices=[(i, i) for i in range(1, 8)] , default=3)
    is_luxury = models.BooleanField(default =False)

    def __str__(self):
        return self.hname


class himg(models.Model):
    hotel = models.ForeignKey(hotels, related_name='images' ,on_delete=models.CASCADE)
    cimg = models.ImageField(upload_to='images/')
    main_img = models.ImageField(upload_to='images/')
    img1 = models.ImageField(upload_to='images/')
    img2 = models.ImageField(upload_to='images/')
    img3 = models.ImageField(upload_to='images/')
    img4 = models.ImageField(upload_to='images/')
    img5 = models.ImageField(upload_to='images/')
    img6 = models.ImageField(upload_to='images/')
    img7 = models.ImageField(upload_to='images/')


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    feedback = models.TextField()


class Hotel_request(models.Model):
    hotel_name = models.CharField(max_length=50)
    availabel_room = models.IntegerField()
    per_person = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    price_room = models.FloatField()
    about = models.TextField()
    cover = models.ImageField(upload_to='images')
    email = models.EmailField(default='default@mail.com')


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel_request, related_name='hotel_images', default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='documents/%Y/%m/%d/')


class Hotel(models.Model):
    hname = models.ForeignKey(hotels, on_delete=models.CASCADE, related_name='hotel_hname')
    rooms = models.ForeignKey(hotels, on_delete=models.CASCADE, related_name='hotel_rooms')


class user_comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    feedback = models.TextField()
    hotel = models.ForeignKey(hotels, on_delete=models.CASCADE)


class booking(models.Model):
    ariival_date = models.CharField(max_length = 100)
    departure_date = models.CharField(max_length= 100 )
    booked_room_count = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2 , default=0) 
    hotel = models.ForeignKey(hotels, related_name='b', on_delete=models.CASCADE, null=True, blank=True)
    rooms_back_at = models.DateTimeField(null=True, blank=True) 
    user = models.CharField(max_length = 50 , default = 'user_name')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        send_mail(
            'New booking request',
            f'You have a booking request of {self.booked_room_count} rooms by {self.user} from {self.ariival_date} to {self.departure_date} ,the amount of {self.total_price} booking is made.',
            'g20projectmail@gmail.com',
            [self.hotel.email],
            fail_silently=False,
        )


class hotel_user(models.Model):
    h_id = models.IntegerField()
    email = models.EmailField(unique = True)
    passs = models.CharField(max_length = 25,   default = 123456)

