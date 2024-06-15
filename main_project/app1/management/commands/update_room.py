from django.core.management.base import BaseCommand
from django.utils import timezone
from app1.models import booking, hotels 

class Command(BaseCommand):
    def handle(self, *args, **options):
        past_bookings = booking.objects.filter(rooms_back_at__lte=timezone.now())
        for b in past_bookings:
            hotel = hotels.objects.get(pk=b.hotel.pk)
            hotel.rooms += b.booked_room_count
            hotel.save()
            b.rooms_back_at = None
            b.save() 