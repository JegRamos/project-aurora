from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os


class Supervisor(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}"


class OvertimeRequest(models.Model):
    desc = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id}. {self.desc}"


class Entry(models.Model):
    writer = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    date_started = models.DateTimeField(default=timezone.now)
    agenda = models.TextField()
    completed = models.BooleanField(default=False)
    date_ended = models.DateTimeField(default=None, null=True, blank=True)
    overtime = models.ForeignKey(OvertimeRequest, null=True, default=3, on_delete=models.PROTECT)
    supervisor = models.ForeignKey(Supervisor, null=True, default=1, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        date = str(self.date_started).split(' ')[0]
        return f"{self.id}. {date} | Written by {self.writer.get_full_name()}: {self.agenda}"


class File(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    file = models.FileField(upload_to='entry_media', blank=True, null=True)

    def __str__(self):
        return f"{self.entry.date_ended} - {self.file}"

    def filename(self):
        return os.path.basename(self.file.name)
