from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Job, JobApplication
from .forms import JobForm, JobApplicationForm
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required


def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            print("User saved successfully:", user.username)  # Debug message
            return JsonResponse({'status': 'success'})
        else:
            print("Form errors:", user_form.errors)  # Debug message
    else:
        user_form = UserForm()
    return render(request, 'job_portal/create_user.html', {'user_form': user_form})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User exists and authentication successful
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            # Authentication failed or user does not exist
            return JsonResponse({'status': 'failure'})
    else:
        # GET request
        return render(request, 'job_portal/custom_login.html')


# logout page
def user_logout(request):
    logout(request)
    return redirect('home')


def user_created(request):
    return render(request, 'job_portal/user_created.html')


@login_required
def profile(request):
    user = request.user
    if user.is_superuser:  # Check if user is admin
        job_applications = JobApplication.objects.all()
        return render(request, 'job_portal/admin_profile.html', {'job_applications': job_applications})
    else:
        return render(request, 'job_portal/profile.html', {'user': user})


# @login_required
# def profile(request):
#     # Get the current user object
#     user = request.user
#
#     # Pass the user object to the template
#     context = {'user': user}
#
#     return render(request, 'job_portal/profile.html', context)

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to admin profile after job creation
    else:
        form = JobForm()
    return render(request, 'job_portal/create_job.html', {'form': form})


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_portal/job_list.html', {'jobs': jobs})


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'job_portal/job_detail.html', {'job': job})


def job_application(request, user_id, job_id):
    if request.method == 'POST':
        job = Job.objects.get(pk=job_id)
        user = User.objects.get(pk=user_id)
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.job = job
            form.instance.user = user
            form.save()
            return redirect('home', job_id=job_id)
    else:
        form = JobApplicationForm()
    return render(request, 'job_portal/job_application.html', {'form': form})


def job_search(request):
    query = request.GET.get('q', '')
    if query:
        # Filter jobs based on search query
        jobs = Job.objects.filter(title__icontains=query)
    else:
        jobs = Job.objects.all()

    context = {
        'jobs': jobs,
    }
    return render(request, 'job_portal/job_list.html', context)
