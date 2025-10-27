from django.urls import path
from . import views

urlpatterns=[
    path('',views.student_list, name='student_list'),
    path('api/student',views.std_api, name='api/student'),
    path('register/',views.register_user, name='register'),
    path('login/',views.login_user, name= 'login'),
    path('logout/', views.logout_user, name = 'logout'),
]