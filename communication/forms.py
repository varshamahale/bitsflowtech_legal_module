from django.forms import ModelForm
from .models import Article
from django import forms


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'



class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    message = forms.CharField(widget = forms.Textarea)

