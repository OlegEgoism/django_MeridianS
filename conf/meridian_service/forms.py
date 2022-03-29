from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Имя'}))
    phone = forms.CharField(label='', widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Телефон'}))
    message = forms.CharField(label='', widget=forms.Textarea(
        attrs={'style': 'margin:10px; padding:10px; height:150px', 'class': 'form-control col-sm-8',
               'placeholder': 'Сообщение'}))

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'message')
