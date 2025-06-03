from django.shortcuts import render, redirect, get_object_or_404
from .models import Reminder
from .forms import ReminderForm

def index(request):
    reminders = Reminder.objects.all().order_by('-important', 'createdAt')
    return render(request, 'reminders/index.html', {'reminders': reminders})

def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReminderForm()
    return render(request, 'reminders/form.html', {'form': form, 'title': 'Crear Recordatorio'})

def update_reminder(request, id):
    reminder = get_object_or_404(Reminder, id=id)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'reminders/form.html', {'form': form, 'title': 'Actualizar Recordatorio'})

def delete_reminder(request, id):
    reminder = get_object_or_404(Reminder, id=id)
    if request.method == 'POST':
        reminder.delete()
        return redirect('index')
    return render(request, 'reminders/confirm_delete.html', {'reminder': reminder})

