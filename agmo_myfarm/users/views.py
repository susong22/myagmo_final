from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm

def main(request):
    if request.method == "GET":
        return render(request, 'users/main.html')
    elif request.method == "POST":
        username = request.POST["username"]  # 필드 이름을 "name"에서 "username"으로 수정
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home:index'))
        else:
            return render(request, 'users/main.html', {'error_message': '로그인에 실패했습니다.'})
        
def signup(request):
    if request.method == "GET":
        form = SignupForm()

        return render(request, 'users/signup.html',{'form': form})
    elif request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home:index'))
        return render(request, 'users/main.html', {'error_message': '로그인에 실패했습니다.'})