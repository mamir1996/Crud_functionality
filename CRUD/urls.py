from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('display_data/',views.display_data,name="display_data"),
    path('edit/<int:pk>/',views.edit_page,name="edit_page"),
    path('delete/<int:pk>/',views.delete_page,name="delete_page"),
]
