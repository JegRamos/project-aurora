from django import forms
from .models import Supervisor, File


class StartAdventureForm(forms.Form):
    agenda = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'name': 'agenda',
        'placeholder': '//Write here', 'rows': 3
    }))

    supervisor = forms.ModelChoiceField(queryset=Supervisor.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control col-sm-6 mb-3', 'name': 'supervisor'
    }))


class CloseAdventureForm(forms.Form):
    OVERTIME_OPTIONS = ((3, 'NO'), (1, 'YES'))
    request_overtime = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control col-md-8', 'name': 'request_overtime',
    }), choices=OVERTIME_OPTIONS)


class MediaUploadForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ('file', )
        widgets = {
            'file': forms.ClearableFileInput(attrs={
                'multiple': True, 'class': 'col-md-4', 'name': 'file'
            })
        }
