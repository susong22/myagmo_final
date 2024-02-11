from django import forms as django_form
from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms as django_form
#from allauth.account.forms import SignupForm
#from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    error_messages = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User
    
    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        
        raise ValidationError(self.error_messages["duplicated_username"])
    


class SignupForm(django_form.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','name','phone_number','email','area']
        
        AREA = [
        ('Seoul', '서울'),
        ('Suwon', '수원'),
        # 다른 선택지 추가 가능
        ]
  
        labels = {
            'username': 'id',
            'password': 'password',
            'name': '이름',
            'phone_number': '전화번호',
            'email': 'email',
			'area': '지역'
        }
        area = django_form.ChoiceField(choices=AREA, required=True)

        widgets = {
            'password': django_form.PasswordInput(),
        }
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }