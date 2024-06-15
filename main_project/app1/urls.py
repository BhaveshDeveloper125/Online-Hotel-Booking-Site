from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index , name='index'),
    path('feedback/',views.feedback , name='feedback'),
    path('about/',views.about , name='about'),
    path('rooms/<pk>',views.rooms, name='rooms'),
    path('privacy/', views.privacy ,name='privacy'),
    path('terms and condition/',views.tc ,name='tc'),
    path('addhotel/' ,views.addhotel ,name="addhotel"),
    path('hotelogin/', views.hotelogin, name='hotelogin'),
    path('hotel_logout' , views.hotel_logout , name='hotel_logout'),
    path('search/', views.search, name='search'),
    path('sorting/', views.sorting, name='sorting'),
    path('bookinghotel/<pk>', views.bookinghotel, name='bookinghotel'),
    path('hotels/<int:category>/',views.categories, name='index'),
    path('payment/',views.payment, name='payment'),
    path('hotel/<str:hotel_hname>/', views.hotel_detail, name='hotel_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

