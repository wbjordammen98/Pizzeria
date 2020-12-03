from django import forms
from .models import Topping

class CommentForm(forms.ModelForm):
    class Meta:

        model = Topping
        fields = ['text']

        # Gives the 'text' field a blank label.
        labels = {'text':''}

        # The widget attribute overrides Django's default widget(html from element) choices.
        # This attribute customizes the input for the 'text' field so the area will be 80 columns wide instead of 40.
        widgets = {'text':forms.Textarea(attrs={'cols':80})}