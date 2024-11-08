from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин")
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Введите пароль")
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Повторите пароль")
    age = forms.IntegerField(label="Введите свой возраст")


    def clean(self):
        users = ['user1', 'user2']
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают - clean")

        return cleaned_data

        # elif age and age < 18:
        #     raise forms.ValidationError("Вы должны быть старше 18 - clean")
        # elif username and username in users:
        #     raise forms.ValidationError("Пользователь уже существует - clean")
