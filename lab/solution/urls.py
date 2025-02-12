from django.urls import path
from . import views

app_name = "solution"

urlpatterns = [
path("", views.home_page, name="home"),
path("blog/read/", views.read_blog, name="read_blog"),
path("blog/add/", views.add_blog, name="add_blog")
]