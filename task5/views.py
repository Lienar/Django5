from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm


users = [["Vasya", "12345678", 29], ["Givi", "Rf3airg4", 30], ["Gena", "4rs34456", 45]]
info = {}

# Create your views here.
def main_page(request):
    return render(request, 'title_page.html')

def store_page(request):
    list = ["Эвердейл", "Мертвый сезон", "Манчкин", "Экипаж", "Simulo", "Мафия"]
    contecxt = {'list': list, }
    return render(request, 'store_page.html', contecxt)

def basket_page(request):
    return render(request, 'basket_page.html')

def sign_up_by_html(request):
    users = ["Vasya", "Givi", "Gena"]
    info = {'error': ' '}
    if request.method == 'POST':
        name = request.POST.get('name')
        for user in users:
            if user == name:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', info)

        password = request.POST.get('password')
        password_2 = request.POST.get('password2')
        if password != password_2:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', info)

        age = request.POST.get('age')
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'registration_page.html', info)

        return HttpResponse(f'Приветствуем, {name}!')
    return render(request, 'registration_page.html', info)

def sign_up_by_django(request):
    users = ["Vasya", "Givi", "Gena"]
    form = ContactForm()
    info = {'error': " ", 'form': form}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            for user in users:
                if user == name:
                    info['error'] = 'Пользователь уже существует'
                    return render(request, 'registration_page.html', info)

            password = form.cleaned_data['password']
            password_2 = form.cleaned_data['password2']
            if password != password_2:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', info)

            age = form.cleaned_data['age']
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', info)

        return HttpResponse(f'Приветствуем, {name}!')

    return render(request, 'registration_page.html', info)
