from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name="about"),
    path('vision/', views.vision, name="vision"),
    path('mission/', views.mission, name="mission"),
    path('corevalue/', views.corevalue, name="corevalue"),
    path('brands/', views.brands, name="brands"),
    path('products/', views.products, name="products"),
    path('services/', views.services, name="services"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('contact/', views.contact, name="contact"),

]