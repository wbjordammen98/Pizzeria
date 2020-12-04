# Forms correspond to a set of fields which are presented to the end user to enter some data in. 
from django import forms

# Import the topping model which is associated to where users will make comments. 
from .models import Topping

class CommentForm(forms.ModelForm):
    # This class will list the model it is based on and the field to include in the form. 
    class Meta:

        # Build the comment form from the Topping model.
        model = Topping

        # Include only the text field.
        fields = ['text']

        # Gives the 'text' field a blank label.
        labels = {'text':''}

        # The widget attribute overrides Django's default widget(html from element) choices.
        # This attribute customizes the input for the 'text' field so the area will be 80 columns wide instead of 40.
        widgets = {'text':forms.Textarea(attrs={'cols':80})}

# The second phase for displaying the form takes place in the urls.py file.