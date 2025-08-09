from django.urls import path
from . import views

app_name = 'habits'

urlpatterns = [
    path('', views.index, name='index'),
    # Registration, Login, Logout URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_habit, name='add_habit'),
    path('edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('log/<int:habit_id>/', views.log_habit, name='log_habit'),
    path('habit-data/', views.habit_data, name='habit_data'),
    path('log-mood/', views.log_mood, name='log_mood'),
    path('mood-habit-data/', views.mood_habit_data, name='mood_habit_data'),
    path('export/', views.export_data, name='export_data'),
]