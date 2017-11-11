from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render,render_to_response
from django.urls import reverse
from . forms import UserForm

"""
This view is created by followed the djangforbeginners.com and it's not 
working.

def signup(request):
    if request.method == 'post':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user= authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
        else:
            form = UserCreationForm()
        return render_to_response('signup.html')
"""

#This is for test registration
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Album.objects.filter(user=request.user)
                #return render(request, 'music/index.html', {'albums': albums})
                return redirect('post_list')
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)