from django import forms
from django.shortcuts import render


users = ['user1', 'user2', 'user3']


class UserRegister(forms.Form):
    username = forms.CharField(label="Введите логин", max_length=30)
    password = forms.CharField(label="Введите пароль", min_length=8, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label="Повторите пароль", min_length=8, widget=forms.PasswordInput)
    age = forms.IntegerField(label="Введите свой возраст", max_value=150, min_value=0)


def sign_up_by_html(request):
    info = {'users': users}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and age >= 18 and username not in users:
                info['message'] = f"Приветствуем, {username}!"
            else:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif age < 18:
                    info['error'] = 'Вы должны быть старше 18'
                else:
                    info['error'] = 'Пользователь уже существует'
        else:
            info['error'] = 'Некорректные данные в форме'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_django(request):
    info = {}
    info['users'] = users
    return render(request, 'fifth_task/registration_page.html', info)