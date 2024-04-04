from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    # Added a new path to a new page #
    path("teacher", views.teacher_view, name="teacher"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]