from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('home.html', views.home, name='homepage'),
    path('Services.html', views.Services, name='Services'),
    path('pawn_check.html', views.pawn_check, name='Pawn Checking'),
    path('pawn_user', views.pawn_user, name='Checking username'),
    path('pawn_pass', views.pawn_pass, name='Checking password'),
    path('vulnerability_check.html', views.vulnerability_check,
         name="Vulnerability Check"),
    path('vuln', views.vuln, name='Vulnerability analyser'),
    path('contact', views.contact, name='contact'),


]
