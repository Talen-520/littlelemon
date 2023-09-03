from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

    # Add a custom widget for the 'time' field
    time = forms.DateTimeField(
        widget=forms.widgets.TextInput(attrs={'type': 'datetime-local'}),
    )
