from django import forms
from .models import Comment, Contact

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']



class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        #fields = "__all__"
        fields = ('Name','email','subject','content')
        labels ={
             'Name':'',
            'email':'',
            'subject':'',
            'content':'',

        }
        widgets = {
            
            'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name','class':'col-5'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address','class':'col-5'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Subject','class':'col-5'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Content','rows':5,'class':'col-5'}),

        }