from django.db import models

# Create your models here.
class PaymentMethod(models.Model):
    method = models.CharField(max_length=25)

    def __str__(self):
        return self.method

class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"

    status = models.CharField(max_length=25)

    def __str__(self):
        return self.status

# Handles the customer information of a reservation
class Client(models.Model):
    name  = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.last_name} {self.phone_number}"

# Handles the status/payment method/customer throught a foreign key,
# Done this way to easily add new options.

class Reservation(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    room_details = models.TextField()
    days = models.IntegerField()
    paid_amount = models.FloatField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    # Handles the billing information
    
    fiscal_adress = models.CharField(max_length=15)
    tax_number = models.CharField(max_length=15)

    # Always a good practice to save when the record is created/updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_details[0:30]