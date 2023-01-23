from django.urls import path
from blogs import views
urlpatterns = [
    path('',views.index),
    path('add/',views.add,name="add"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('insert/',views.insert,name="insert")
]