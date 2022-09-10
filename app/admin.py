from django.contrib import admin

from app.models import PaymentMethod, Reservation, Status

# Register your models here.
admin.site.register([Reservation, PaymentMethod, Status])