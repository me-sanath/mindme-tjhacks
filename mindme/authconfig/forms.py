# forms.py
from django import forms

class ResponseForm(forms.Form):
    selected_choice = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        options = kwargs.pop('options')
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.fields['selected_choice'].choices = [(option['text'], option['text']) for option in options]
