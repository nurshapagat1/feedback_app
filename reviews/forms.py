from django import forms
from .models import Review

class review_form(forms.ModelForm):
    upload_photo = forms.ImageField(
        label="Upload a photo:",
        required=False,
        error_messages={
            "invalid_image": "Please upload a valid image file."
        }
    )

    class Meta:
        model = Review
        fields = ["username", "reviewtext", "rating"]
        labels = {
            "username": "Your name:",
            "reviewtext": "Your review:",
            "rating": "Rating (1–5)",
        }

    