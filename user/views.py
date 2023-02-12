from django.shortcuts import render, redirect
from .forms import RegisterForm, loginForm

from django.contrib.auth.models import User # Django'nun içindeki User modelini sitemizdeki kullanıcıları oluşturmak için kullanıyoruz.
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

def register(request):
    # register formunda bilgileri alıp kullanıcı kaydı yapmanın bir yolu
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, 'Başarıyla Kayıt Oldunuz.')
        return redirect('index')
    
    context = {'form' : form}
    return render(request, 'register.html', context)

    # Bu da başka bir yolu
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Yeni kullanıcı bilgilerini database'e ekliyoruz.
            newUser = User(username = username)
            newUser.set_password(password) # set.password fonksiyonuyla oluşturulan şifreyi kullanıcıya şifreli şekilde atıyoruz.
            newUser.save() # Yeni kullanıcının database'e kaydı tamamlanıyor.
            login(request, newUser) # login fonksiyonu ile, kayıt olan kullanıcılar otomatik olarak login yapmış oluyor.
            return redirect('index') # otomatik login olan kullanıcıyı daha sonra anasayfaya yönlendiriyor.
        
        context = {'form' : form}
        return render(request, 'register.html', context)
    else:
        form = RegisterForm()
        context = {'form' : form}
        return render(request, 'register.html', context)
    """
def loginUser(request):
    form = loginForm(request.POST or None)
    context = { "form" : form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.warning(request, "Kullanıcı adı ya da parola hatalı")
            return render(request, 'login.html', context)
        
        messages.success(request, "Başarıyla giriş yaptınız.")
        login(request, user)
        return redirect('index')
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Çıkış Yapıldı")
    return redirect('index')