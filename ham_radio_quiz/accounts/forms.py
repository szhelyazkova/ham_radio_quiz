from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email',)
        field_classes = {'username': auth_forms.UsernameField, }


class UserBaseForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'call_sign', )
        field_classes = {'username': auth_forms.UsernameField}

    def clean_call_sign(self):
        if self.cleaned_data["call_sign"]:
            return self.cleaned_data["call_sign"].upper()
        return self.cleaned_data["call_sign"]
