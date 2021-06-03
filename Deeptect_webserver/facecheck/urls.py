from django.urls import path

from . import views

urlpatterns = [
    path('member/', views.get_member, name="member"),
    path('D1/', views.get_D1, name="D1"),
    path('D2/', views.get_D2, name="D2"),
]