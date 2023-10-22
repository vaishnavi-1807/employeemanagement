from django.urls import path
from home import views

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('display/', views.display_employees, name='display_employees'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
]
