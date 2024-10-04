from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('user/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('listing/', include('listings.urls'), name= 'listing'),
    path('', HomeView.as_view(), name='home'),
]