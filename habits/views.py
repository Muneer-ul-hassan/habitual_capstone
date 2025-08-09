from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, HabitForm, MoodLogForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Habit, HabitLog, MoodLog
from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from datetime import timedelta
from .badges import check_and_award_badges
import csv

@login_required
def index(request):
    habits = Habit.objects.filter(user=request.user)
    mood_logs = MoodLog.objects.filter(user=request.user).order_by('-logged_at')[:7]
    
    # Calculate statistics
    total_streaks = sum(habit.current_streak() for habit in habits)
    today = timezone.now().date()
    completed_today = HabitLog.objects.filter(
        habit__user=request.user,
        completed_at=today,
        is_completed=True
    ).count()
    total_habits = habits.count()
    
    context = {
        'habits': habits,
        'mood_logs': mood_logs,
        'total_streaks': total_streaks,
        'completed_today': completed_today,
        'total_habits': total_habits,
    }
    return render(request, 'habits/index.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('habits:index')
    else:
        form = RegisterForm()
    return render(request, 'habits/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('habits:index')
    else:
        form = AuthenticationForm()
    return render(request, 'habits/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('habits:login')

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habits:index')
    else:
        form = HabitForm()
    return render(request, 'habits/add_habit.html', {'form': form})

@login_required
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('habits:index')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habits/habit_detail.html', {'form': form, 'habit': habit})

@login_required
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        habit.delete()
        return redirect('habits:index')
    return render(request, 'habits/habit_detail.html', {'habit': habit})

@login_required
def log_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    today = timezone.now().date()
    log, created = HabitLog.objects.get_or_create(habit=habit, completed_at=today)
    log.is_completed = not log.is_completed
    log.save()
    check_and_award_badges(request.user)
    return JsonResponse({'is_completed': log.is_completed})

@login_required
def habit_data(request):
    habits = Habit.objects.filter(user=request.user)
    labels = [habit.name for habit in habits]
    values = [habit.logs.filter(is_completed=True).count() for habit in habits]
    return JsonResponse({'labels': labels, 'values': values})

@login_required
def log_mood(request):
    if request.method == 'POST':
        form = MoodLogForm(request.POST)
        if form.is_valid():
            mood_log = form.save(commit=False)
            mood_log.user = request.user
            mood_log.logged_at = timezone.now().date()
            mood_log.save()
            return redirect('habits:index')
    else:
        form = MoodLogForm()
    return render(request, 'habits/log_mood.html', {'form': form})

@login_required
def mood_habit_data(request):
    today = timezone.now().date()
    seven_days_ago = today - timedelta(days=7)
    
    mood_logs = MoodLog.objects.filter(user=request.user, logged_at__range=[seven_days_ago, today]).order_by('logged_at')
    habit_logs = HabitLog.objects.filter(habit__user=request.user, completed_at__range=[seven_days_ago, today], is_completed=True).values('completed_at').annotate(count=Count('id')).order_by('completed_at')
    
    mood_data = {log.logged_at.strftime('%Y-%m-%d'): log.mood for log in mood_logs}
    habit_data = {log['completed_at'].strftime('%Y-%m-%d'): log['count'] for log in habit_logs}
    
    labels = [(seven_days_ago + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(8)]
    mood_values = [mood_data.get(date, 0) for date in labels]
    habit_values = [habit_data.get(date, 0) for date in labels]
    
    return JsonResponse({'labels': labels, 'mood_values': mood_values, 'habit_values': habit_values})

@login_required
def export_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="habit_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Habit', 'Date', 'Completed'])

    habits = Habit.objects.filter(user=request.user)
    for habit in habits:
        logs = habit.logs.all()
        for log in logs:
            writer.writerow([habit.name, log.completed_at, log.is_completed])

    return response
