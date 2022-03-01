from django import forms 

class QuestionForm(forms.Form):
    text = forms.CharField(label='Text', max_length=200)