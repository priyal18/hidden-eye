from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='homepage'),
    path('home.html', views.home,name='homepage'),
    path('pawn_check.html', views.Services,name='Services'),
    path('Contact.html', views.Contact,name='Contact'),
    path('pawn_check.html', views.pawn_check,name='Pawn Checking'),
    path('pawn_user', views.pawn_user,name='Checking username'),
    path('pawn_pass', views.pawn_pass,name='Checking password')


]
