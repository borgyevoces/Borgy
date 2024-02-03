from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.webp', upload_to='profile_pics/')
    contact = models.CharField(max_length=11, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    duration_days = models.IntegerField()

    def __str__(self):
        return self.title

class Planfeature(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    title = models.TextField(max_length=150)

    def __str__(self):
        return self.title
 

class Membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.plan} ({'Active' if self.is_active else 'Inactive'})"
    
class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    planchoices = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    ]

    paymentchoices = [
        ('gcash', 'Gcash'),
        ('paymaya', 'PayMaya'),
    ]
    plan = models.CharField(max_length=10, choices=planchoices)
    contact_number = models.CharField(max_length=15)
    payment_method = models.CharField(max_length=50, choices=paymentchoices)

    def __str__(self):
        return f"{self.user}'s Payment for {self.plan}"
    
class Member(models.Model):
    MEMBERSHIP_CHOICES = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES)

    def __str__(self):
        return f"{self.user.username}'s Membership: {self.membership_type}"