from django.urls import path
from. import views


urlpatterns=[
    path('dashboard/',views.admin_home),

]

