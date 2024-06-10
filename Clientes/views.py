from django.shortcuts import render,redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def Profile_update(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_update.html', {'form': form})
