from django.contrib import admin
from .models import hotels,himg,Feedback,booking , Hotel_request , user_comment , booking , HotelImage
from django.utils.html import format_html_join, format_html
from datetime import datetime
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User




admin.site.register(hotels)
admin.site.register(himg)
admin.site.register(HotelImage)

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1  # how many rows to show



@admin.register(Hotel_request)
class Hotel_requestAdmin(admin.ModelAdmin):
    list_display = ('hotel_name' , 'availabel_room' , 'per_person' , 'address' , 'city' , 'state' , 'price_room' , 'about' , 'cover' , 'email', 'display_images')
    inlines = [HotelImageInline]

    def display_images(self, obj):
        return format_html_join(' ', '<img src="{}" width="50" height="50" /><a href="{}" download>Download</a>',
                                ((image.images.url, image.images.url) for image in obj.hotel_images.all()))
    display_images.short_description = 'Images'



@admin.register(user_comment)
class user_commentadmin(admin.ModelAdmin):
    list_display  = ('hotel' , 'feedback' , 'name' , 'email')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback')


@admin.register(booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'hotel' , 'booked_room_count' , 'ariival_date', 'departure_date' , 'total_price'  )

