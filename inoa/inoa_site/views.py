from django.shortcuts import render, get_object_or_404
from .models import User, UserDetail


# Create your views here.
def index(request):
    return render(request, 'inoa_site/index.html', {})


def validate_login(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    try:
        button = request.POST['login-button']
        username = request.POST['username']
        password = request.POST['password']

        print('O valor de button', button)
        if user.username == username and user.password == password:
            return render(request, 'inoa_site/home.html', {})
        else:
            return render(request, 'inoa_sites/index.html', {
                'error_message': 'choose username or password'
            })
    except ValueError:
        return render(request, 'inoa_site/index.html', {
            'error_message': 'choose username or password'
        })


def home(request, user_id):
    context = UserDetail.objects.get(id=user_id).first_name
    return render(request, 'inoa_site/home.html', context)
