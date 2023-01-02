from django.urls import path     
from . import views
urlpatterns = [
    path('shows/new', views.index),	   
    path('addshow', views.addshow),
    path('showtwo/<int:id>',views.showtwo,name="viewshow"),
    path('shows',views.shows),
    path('delete/<int:id>',views.delete,name="del_show"),
    path('shows/<int:id>/edit',views.edit,name="edit_show"),
    path('editshow/<int:id>',views.editshow),

]