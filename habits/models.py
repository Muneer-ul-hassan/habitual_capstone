from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
import pytz

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class UserBadge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="badges")
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'badge')

class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="habits")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    emoji = models.CharField(max_length=10, default='📝', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def current_streak(self):
        today = timezone.now().astimezone(pytz.timezone(self.user.timezone)).date()
        streak = 0
        logs = self.logs.filter(is_completed=True).order_by('-completed_at')
        
        if not logs:
            return 0
            
        if logs.first().completed_at == today or logs.first().completed_at == today - timedelta(days=1):
            last_date = logs.first().completed_at
            for log in logs:
                if log.completed_at == last_date:
                    streak += 1
                    last_date -= timedelta(days=1)
                else:
                    break
        return streak
    
    def completion_rate(self):
        """Calculate completion rate for the last 7 days"""
        today = timezone.now().date()
        week_ago = today - timedelta(days=7)
        total_days = 7
        completed_days = self.logs.filter(
            completed_at__range=[week_ago, today],
            is_completed=True
        ).count()
        return round((completed_days / total_days) * 100) if total_days > 0 else 0

class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="logs")
    completed_at = models.DateField()
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('habit', 'completed_at')

    def __str__(self):
        return f"{self.habit.name} on {self.completed_at}"

class MoodLog(models.Model):
    MOOD_CHOICES = (
        (1, 'Very Unhappy'),
        (2, 'Unhappy'),
        (3, 'Neutral'),
        (4, 'Happy'),
        (5, 'Very Happy'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mood_logs")
    mood = models.IntegerField(choices=MOOD_CHOICES)
    logged_at = models.DateField(unique=True)

    def __str__(self):
        return f"{self.user.username}'s mood on {self.logged_at}"

class Reminder(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="reminders")
    reminder_time = models.TimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Reminder for {self.habit.name} at {self.reminder_time}"
