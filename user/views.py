from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def register(request):
    if request.method== 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            #if the features of the form are valid, characters from the password etc, save form
            form.save()
            return redirect('user-login')
    else:
        form=CreateUserForm()

    context= {
        'form':form
    }
    return render(request, 'user/register.html', context)
