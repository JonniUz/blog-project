from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm
                    
def register(request):
    if not request.user.is_authenticated:
        form = UserRegisterForm()
        if request.method=="POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                form.save()
                messages.success(request, f'You have been registered as succesfully "{username}"')
                return redirect('login') 
        return render(request, 'registration/register.html', {'form': form})

    else:
        return redirect('book.all')        