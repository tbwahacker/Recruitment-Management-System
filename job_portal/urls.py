from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.job_list, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_created/', views.user_created, name='user_created'),
    path('profile/' , views.profile, name='profile'),
    path('create_job/', views.create_job, name='create_job'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:user_id>/<int:job_id>/apply/', views.job_application, name='job_application'),
    path('job/search/', views.job_search, name='job_search'),
    path('payment/', views.payment_page, name='payment_page'),
]
