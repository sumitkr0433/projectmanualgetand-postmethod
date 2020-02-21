from django.urls import path

from . import views

urlpatterns = [
				path("", views.home, name="home"),
				path("result", views.clickwebsite, name="result"),
			  	#path("swigy", views.swigyform, name="swigy"),
			  ]

