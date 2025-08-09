from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from .models import Habit, HabitLog, MoodLog, Reminder, Badge, UserBadge

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Habit)
admin.site.register(HabitLog)
admin.site.register(MoodLog)
admin.site.register(Reminder)
admin.site.register(Badge)
admin.site.register(UserBadge)
