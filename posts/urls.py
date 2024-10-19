from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create_post, name='create'),
    path('report/', views.report_post, name='report'),
    path('postlist/', views.post_list, name='post list'),

]