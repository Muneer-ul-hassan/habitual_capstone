from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Habit, MoodLog

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description']

class MoodLogForm(forms.ModelForm):
    class Meta:
        model = MoodLog
        fields = ['mood']