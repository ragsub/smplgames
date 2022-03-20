from email.policy import default
from django import forms

class CountForm(forms.Form):
    count = forms.IntegerField(
        initial = 0,
        widget = forms.HiddenInput (
            attrs = ({
                'x-ref':'count',
                'x-model':'count_xmodel',
            })
        )
    )