import phonenumbers
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import CharField, ValidationError
from django.utils.translation import ugettext_lazy as _
from django_countries.widgets import CountrySelectWidget

from .models import OjosUser


class OjosUserCreationForm(UserCreationForm):
    phone_number = CharField(required=True, max_length=20)

    class Meta(UserCreationForm.Meta):
        model = OjosUser
        fields = ('email', 'country', 'phone_number', 'first_name', 'last_name')
        widgets = {'country': CountrySelectWidget(
            layout="""'{widget}<img class="country-select-flag" id="{flag_id}" style="margin-left: 1em;" src="{country.flag}">'"""
        )}

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if not data.isnumeric():
            raise ValidationError('Phone number must be numeric')
        return data

    def clean(self):
        cleaned_data = super().clean()
        country = cleaned_data.get("country")
        phone_number = cleaned_data.get("phone_number")
        if phone_number and country:
            phone = phonenumbers.parse(phone_number, country)
            if not phonenumbers.is_valid_number(phone):
                raise ValidationError("Phone number is not valid")
            self.cleaned_data['phone_number'] = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)


class OjosUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = OjosUser


class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not OjosUser.objects.filter(email__iexact=email, is_active=True).exists():
            msg = _("There is no user registered with the specified E-Mail address.")
            self.add_error('email', msg)
        return email
