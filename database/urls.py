from django.urls import path
from . import views

urlpatterns = [path("", views.index),
path("contact/", views.contact),
path("alogin/", views.alogin),
path("tlogin/", views.tlogin),
path("slogin/", views.slogin),
path("thome/", views.thome),
path("tupload/", views.tupload),
path("shome/", views.shome),
path("supload/", views.supload),
path("tsubmissions/", views.tsubmissions),
path("tuploaded/", views.tuploaded),
path("tlogout/", views.tlogout),
path("snotes/", views.snotes),
path("slogout/", views.slogout),
path("suploadedfiles/", views.suploadedfiles),
]
