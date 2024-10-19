from django import forms
from .models import Post, Report

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Content']  # Include the fields you want in your form

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['Content'].widget.attrs.update({
            'placeholder': 'Enter your post content here...',
            'rows': 4,
            'cols': 50,
            'class': 'form-control'
        })
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['message']  # Only need the message for reporting

