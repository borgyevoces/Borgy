from django.urls import path
from . import views
from .views import PaymentView

urlpatterns = [
   
    path('home/', views.home_page, name="homePage"),
    path('about/', views.about_page, name="aboutPage"),
    path('contact/', views.contact_page, name="contactPage"),
    path('membership/', views.membership_page, name="membershipPage"),
    path('payment/', views.PaymentView.as_view(), name='payment_form'),


]
    
    
    
    
