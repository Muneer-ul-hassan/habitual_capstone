from .models import Badge, UserBadge, Habit

def check_and_award_badges(user):
    # Award 7-day streak badge
    for habit in Habit.objects.filter(user=user):
        if habit.current_streak() >= 7:
            badge = Badge.objects.get_or_create(name="7-Day Streak", description="Maintained a habit for 7 consecutive days.")[0]
            UserBadge.objects.get_or_create(user=user, badge=badge)