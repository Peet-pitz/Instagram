from django import forms
from .models import Image,Profile,Comment

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'photo_date','likes','comment','image_name']

# class NewProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['user']

# class NewCommentForm(forms.ModelForm):
#     class Meta :
#         model = Comment
#         exclude = ['username','comment_photo']