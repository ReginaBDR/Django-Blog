from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    
    class Meta:
        model = Comment
        fields = ('content', )


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'What do you want to say?',
        'rows': '4'
        })
    )
    contact_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Your name'})
    contact_email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Your email'})

  