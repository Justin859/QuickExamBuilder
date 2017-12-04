import uuid

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import *
from .student_forms import *
from .models import *

def user_is_candidate(user):
    users_in_group = Group.objects.get(name='Candidate').user_set.all()
    
    if user in users_in_group:
        return True
    else:
        return False

def student_login(request):

    if request.method == 'POST':
        form = CandidateLogin(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/student-dashboard/')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username or Password is incorrect.')
                # Return an 'invalid login' error message.
            else:
                messages.error(request, 'You have chosen an invalid user email or you are not listed as a candidate. Contact your exam administrator if the problem persists.')
    else:
        form = CandidateLogin()
    
    return render(request, 'student_accounts/login.html', {'form': form})

def dashboard(request):
    if user_is_candidate(request.user):
        return render(request, 'student_dashboard/dashboard.html', {})
    else:
        return HttpResponseRedirect('/student-dashboard/login/')
def upcoming_exams(request):
    if user_is_candidate(request.user):
        candidate = Candidates.objects.get(user_id = request.user.id)
        exams = Exam.objects.filter(user_id = candidate.admin_id)
        exam_by_group = ExamCandidateGroups.objects.filter(group_section = candidate.candidate_group, user_id = candidate.admin_id)

        exam_ids = []
        candidate_exams = []

        for exam in exam_by_group:
            exam_ids.append(int(exam.exam_id))

        for exam in exams:
            if exam.id in exam_ids:
                candidate_exams.append(exam)

        return render(request, 'student_dashboard/upcoming_exams.html', {'candidate_exams': candidate_exams})
    else:
        return HttpResponseRedirect('/student-dashboard/login/')
    return render(request, 'student_dashboard/upcoming_exams.html', {})