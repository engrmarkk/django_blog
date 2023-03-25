from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("welcome", views.welcomepage, name="welcomepage"),
    path("logout", views.logout, name="logout"),
    path("delete/<int:post_id>", views.delete_post, name="delete post"),
    path("update/<int:post_id>", views.update_post, name="update post"),
    path("display/<int:post_id>", views.display_post, name="display post")
]
