from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Book URLs
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    
    # Branch URLs
    path('branches/', views.branch_list, name='branch_list'),
    path('branches/create/', views.branch_create, name='branch_create'),
    path('branches/<int:pk>/edit/', views.branch_edit, name='branch_edit'),
    path('branches/<int:pk>/delete/', views.branch_delete, name='branch_delete'),
    
    # Inventory URLs
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/create/', views.inventory_create, name='inventory_create'),
    path('inventory/<int:pk>/edit/', views.inventory_edit, name='inventory_edit'),
    path('inventory/<int:pk>/delete/', views.inventory_delete, name='inventory_delete'),
]
