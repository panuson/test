from django.urls import path
from blogs import views
urlpatterns = [
    path('',views.index),
    path('about/',views.about,name="about"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('insert/',views.insert,name="insert")
]