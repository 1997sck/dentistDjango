from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('contact.html', views.contact, name="contact"),
	path('about.html', views.about, name="about"),
	path('blog.html', views.blog, name="blog"),
	path('doctors.html', views.doctors, name="doctors"),
	path('services.html', views.services, name="services"),
	path('appointment.html', views.appointment, name="appointment"),

]