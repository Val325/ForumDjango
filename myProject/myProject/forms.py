from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions
from .models import textData, SubPost, UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
    """
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            
            
            Handles case when we are updating the user profile
            and do not supply a new avatar

            
            pass

        return avatar
        """
    class Meta:
        model = UserProfile
        fields = ("avatar",)

class UserForm(forms.ModelForm):
    textdata = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "cols": "40"}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'file_upload'}))
    class Meta:
        model = textData
        fields = ("textdata", "image")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class SubPostForm(forms.ModelForm):
    textdata = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "cols": "40"}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'file_upload'}))
    class Meta:
        model = SubPost
        fields = ('textdata','image')
        

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    