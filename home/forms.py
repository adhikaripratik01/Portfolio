from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full mt-2 px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-700 focus:outline-none focus:ring-2 focus:ring-purple-500 dark:bg-gray-900 dark:text-white',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full mt-2 px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-700 focus:outline-none focus:ring-2 focus:ring-purple-500 dark:bg-gray-900 dark:text-white',
                'placeholder': 'you@example.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full mt-2 px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-700 focus:outline-none focus:ring-2 focus:ring-purple-500 dark:bg-gray-900 dark:text-white',
                'placeholder': 'Write your message...',
                'rows': 4
            }),
        }

