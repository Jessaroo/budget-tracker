from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page URL
    path('', views.home, name='home'),  # Home page URL
    path('add-expense/', views.add_expense, name='add_expense'),  # Add Expense page
    path('index/', views.index, name='index'),  # Index page (could show a list of expenses)
]