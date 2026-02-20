from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Halaman Umum
    path('', views.index, name='index'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    
    # Halaman Member (Auth)
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Login & Logout (Bawaan Django)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
