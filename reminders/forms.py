from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['content', 'important']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu recordatorio',
                'maxlength': '120',
                'required': 'required'
            }),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("El contenido no puede estar vacío.")
        return content
