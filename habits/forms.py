from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Habit, MoodLog

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class HabitForm(forms.ModelForm):
    emoji = forms.CharField(
        max_length=10,
        initial='📝',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True,
            'style': 'font-size: 2rem; text-align: center;'
        }),
        help_text="Click an emoji below to select it for your habit"
    )
    
    class Meta:
        model = Habit
        fields = ['name', 'description', 'emoji']

class MoodLogForm(forms.ModelForm):
    class Meta:
        model = MoodLog
        fields = ['mood']