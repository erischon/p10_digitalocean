from django import forms


class RequestForm(forms.Form):
    user_request = forms.CharField(label='Your request', max_length=200)
