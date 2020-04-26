from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home', views.post_home, name="post_home"),
    path('new', views.post_new, name="post_new"),
    path('detail/<int:post_pk>/', views.post_detail, name="post_detail")
]