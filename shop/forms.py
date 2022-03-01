from django import forms 

class BuyProductForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity')
    