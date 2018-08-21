from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Entry, File, Supervisor, OvertimeRequest
from .import forms
from django.utils import timezone
from .forms import StartAdventureForm, CloseAdventureForm, MediaUploadForm
from django.contrib import messages


@login_required(login_url='/accounts/login/')
def home(request):
    form = StartAdventureForm(initial={'supervisor': 1})

    entry_objs = Entry.objects.filter(
        writer=request.user, completed=True,
        date_ended__month=timezone.now().month).order_by('-date_ended')[:30]
    inc_entry_objs = Entry.objects.filter(writer=request.user, completed=False).order_by('-date_started')

    def format_duration(duration):
        hours = duration.total_seconds() // 3600
        minutes = (duration.total_seconds() % 3600) // 60
        if minutes < 10:
            return "%d:0%d" % (hours, minutes)
        return "%d:%d" % (hours, minutes)

    def format_time_counter(duration):  # just for the views
        duration = float(duration.total_seconds() / 3600)
        duration = float(format(duration, '.2f'))
        return duration

    time_spent = []
    time_counter = []  # I'm using this for the views
    for completed_entry in entry_objs:
        duration = completed_entry.date_ended - completed_entry.date_started
        time_spent.append(format_duration(duration))
        time_counter.append(format_time_counter(duration))

    entries = [entry for entry in zip(entry_objs, time_spent, time_counter)]
    inc_entries = [inc_entry for inc_entry in inc_entry_objs]

    context = {'form': form, 'entries': entries, 'inc_entries': inc_entries}
    return render(request, 'ntcadventures/home.html', context)


def media(request, entry_id):
    entry_media = File.objects.filter(entry=entry_id)
    entry = Entry.objects.get(id=entry_id)
    context = {'entry_media': entry_media, 'entry': entry}
    return render(request, 'ntcadventures/media.html', context)


@require_POST
def add_entry(request):
    form = forms.StartAdventureForm(request.POST)
    if form.is_valid():
        agenda = request.POST['agenda']
        writer = request.user
        supervisor = Supervisor.objects.get(id=request.POST['supervisor'])
        new_entry = Entry(agenda=agenda, supervisor=supervisor, writer=writer)
        new_entry.save()
        messages.success(request, "You have started a new adventure, see it under \"Current adventures\" section ")
    return redirect('ntcadventures:home')


def close_entry(request, entry_id='Default'):
    if request.method == 'POST':
        form = forms.CloseAdventureForm(request.POST)
        mediaform = forms.MediaUploadForm(request.POST, request.FILES)
        if form.is_valid() and mediaform.is_valid():
            update_entry = Entry.objects.get(id=entry_id)
            overtime = OvertimeRequest.objects.get(id=request.POST['request_overtime'])
            update_entry.date_ended = timezone.now()
            update_entry.completed = True
            update_entry.overtime = overtime
            update_entry.save()
            entry = Entry.objects.get(id=entry_id)
            if 'file' in request.FILES:
                for media in request.FILES.getlist('file'):
                    new_media = File(entry=entry, file=media)
                    new_media.save()
            messages.success(request, f"Adventure: {entry.date_started.date()} (Completed)")
            return redirect('ntcadventures:home')
        else:
            messages.error(request, mediaform.errors)
            return redirect('ntcadventures:home')
    else:
        entry_detail = Entry.objects.get(id=entry_id)
        form = CloseAdventureForm()
        mediaform = MediaUploadForm()
        context = {'entry_detail': entry_detail, 'form': form, 'mediaform': mediaform}
        return render(request, 'ntcadventures/close_entry.html', context)
