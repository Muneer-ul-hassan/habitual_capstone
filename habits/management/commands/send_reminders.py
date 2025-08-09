from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from habits.models import Reminder
import pytz

class Command(BaseCommand):
    help = 'Sends habit reminders to users'

    def handle(self, *args, **options):
        now = timezone.now()
        reminders = Reminder.objects.filter(is_active=True)

        for reminder in reminders:
            user_timezone = pytz.timezone(reminder.habit.user.timezone)
            local_time = now.astimezone(user_timezone)

            if reminder.reminder_time == local_time.time():
                send_mail(
                    'Habit Reminder',
                    f'Don\'t forget to complete your habit: {reminder.habit.name}',
                    'from@example.com',
                    [reminder.habit.user.email],
                    fail_silently=False,
                )
                self.stdout.write(self.style.SUCCESS(f'Sent reminder to {reminder.habit.user.email}'))