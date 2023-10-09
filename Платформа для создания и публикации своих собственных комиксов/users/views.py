from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from users.models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to admin dashboard or wherever you prefer
            return redirect('admin:index')
    else:
        form = UserCreationForm()
    return render(request, 'admin/register_user.html', {'form': form})
