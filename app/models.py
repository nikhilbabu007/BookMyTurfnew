from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phno=models.IntegerField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class turf(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    owner=models.CharField(max_length=50)
    owner_image = models.FileField()
    owner_email = models.EmailField()
    owner_phno = models.IntegerField()
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    turf_type = models.CharField(max_length=50)
    surface_type = models.CharField(max_length=50)
    lighting = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.FileField()
    license = models.FileField()
    password=models.CharField(max_length=50)
    phno = models.IntegerField()
    pricing = models.IntegerField()
    action = models.CharField(max_length=50)
    no_of_slots = models.IntegerField()
    s_time = models.IntegerField()
    e_time = models.IntegerField()

    def __str__(self):
        return self.name


class owner(models.Model):
    owner = models.CharField(max_length=50)
    owner_image = models.FileField()
    owner_email = models.EmailField()
    owner_phno = models.IntegerField()

    def __str__(self):
        return self.owner


class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.IntegerField()

    def __str__(self):
        return self.username
class PasswordReset(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    token=models.CharField(max_length=4)


#contact
class contact_admin(models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField()
     contact_no = models.IntegerField()
     message = models.CharField(max_length=50)
     status= models.CharField()

     def __str__(self):
         return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf = models.ForeignKey(turf, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return f" {self.turf.name} - {self.date} {self.time}"

class Payment(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    turf = models.ForeignKey(turf, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=15)
    turf_name = models.CharField(max_length=100)
    turf_location = models.CharField(max_length=100)
    booking_date = models.DateField()
    booked_slots = models.TextField()  # Comma-separated or JSON slots
    amount = models.FloatField()
    payment_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.turf_name} - {self.amount}"







