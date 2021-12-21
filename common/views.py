from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.conf import settings

# Create your views here.

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', status=404)

def internal_server_error(request):
    """
    500 Internal Server Error
    """
    return render(request, 'common/500.html', status=500)


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
    	
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('firstapp:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
