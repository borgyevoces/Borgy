from django.urls import path
from . import views
from .views import delete_profile_image, delete_email, delete_contact

urlpatterns = [

 path('login_user', views.login_user, name="login" ),
 path('register_user', views.register_user, name="register_user" ),
 path('logout_user', views.logout_user, name="logout" ),
 path('profile/', views.user_profile, name="profile"),
 path('delete_profile_image/', delete_profile_image, name='delete_profile_image'),
 path('delete_email/', delete_email, name='delete_email'),
path('delete_contact/', delete_contact, name='delete_contact'),
    
    
]