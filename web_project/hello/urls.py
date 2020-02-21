from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dbtest/", views.dbtest, name="dbtest"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("account/", views.account, name="account"),
    path("assignment/", views.assignment, name="assignment"),
    path("course/", views.course, name="course")
]