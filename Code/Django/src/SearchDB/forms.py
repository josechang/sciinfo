from django import forms

class TextForm(forms.Form):
    your_text = forms.CharField(label='Your text')
