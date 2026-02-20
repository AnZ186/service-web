from django import forms
from django.contrib.auth.models import User
from .models import Review, Profile # <--- Pastikan Profile terpanggil

# Form Review Lama (Biarin aja kalau mau disimpen)
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

# === FORM BARU BUAT DASHBOARD ===
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
