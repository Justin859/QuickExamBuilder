import uuid

from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, ExamForm, AddCandidate
from .models import Greeting, Question, MultipleChoice, Exam, Candidates, ExamQuestions

# Methods

def user_is_admin(user):
    users_in_group = Group.objects.get(name='Client Administrator').user_set.all()
    
    if user in users_in_group:
        return True
    else:
        return False

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

@login_required(login_url='/login/', redirect_field_name='/login/')
def main_page(request):
    if user_is_admin(request.user):

        return render(request, 'main_page.html')
    else:
        return redirect('/login/')

@login_required(login_url='/login/', redirect_field_name='/login/')
def profile(request):

    return render(request, 'accounts/profile.html', {})

@login_required(login_url='/login/', redirect_field_name='/login/')
def cadidates(request):

    if user_is_admin(request.user):
        if request.method == 'POST':
            form = AddCandidate(request.POST)

            if form.is_valid():

                firstname = form.cleaned_data['firstname']
                lastname = form.cleaned_data['lastname']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                candidate_group = form.cleaned_data['candidate_group']

                user = User.objects.create_user(email, email, password)
                user.last_name = lastname
                user.first_name = firstname
                group = Group.objects.get(name='Candidate')
                group.user_set.add(user)
                user.save()

                Candidates.objects.create(
                    admin_id = request.user.id,
                    user_id = user.id,
                    user_email = email,
                    first_name = firstname,
                    last_name = lastname,
                    candidate_group = candidate_group
                )
                return HttpResponseRedirect('/dashboard/candidates')
        else:
            form = AddCandidate()

        return render(request, 'dashboard/candidates.html')
    else:
        return redirect('/login/')

@login_required(login_url='/login/', redirect_field_name='/login/')
def create_exam(request):
    if user_is_admin(request.user):

        admin_exams = Exam.objects.filter(user_id = request.user.id)

        if request.method == 'POST':
            form = ExamForm(request.POST)

            if form.is_valid():

                exam_name = form.cleaned_data['exam_name']
                duration = form.cleaned_data['duration']
                question_picking = form.cleaned_data['question_picking']
                availability = form.cleaned_data['availability']
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                candidates = form.cleaned_data['candidates']
                number_of_questions = form.cleaned_data['number_of_questions']
                from_section = form.cleaned_data['from_section']

                Exam.objects.create(
                    user_id = request.user.id,
                    exam_name = exam_name,
                    duration = duration,
                    question_picking = question_picking,
                    availability = availability,
                    start_date = start_date,
                    end_date = end_date,
                    start_time = start_time,
                    end_time = end_time,
                    candidates = candidates,
                    number_of_questions = number_of_questions
                )

                return HttpResponseRedirect('/dashboard/exams/create')

        else:
            form = ExamForm()

        return render(request, 'dashboard/create_exam.html', {'form': form, 'admin_exams': admin_exams})
    else:
        return redirect('/login/')

@login_required(login_url='/login/', redirect_field_name='/login/')
def exams(request):
    if user_is_admin(request.user):

        admin_exams = Exam.objects.filter(user_id = request.user.id)

        return render(request, 'dashboard/exams.html', {'admin_exams': admin_exams})
    else:
        return redirect('/login/')

@login_required(login_url='/login/', redirect_field_name='/login/')
def questions(request):
    if user_is_admin(request.user):
        if request.method == 'POST':
            form = QuestionForm(request.POST)

            if form.is_valid():
                
                question_type = form.cleaned_data['question_type']
                section = form.cleaned_data['section']
                question_text = form.cleaned_data['question_text']
                answer_field_1 = form.cleaned_data['answer_field_1']
                answer_field_2 = form.cleaned_data['answer_field_2']
                answer_field_3 = form.cleaned_data['answer_field_3']
                answer_field_4 = form.cleaned_data['answer_field_4']
                correct_answer = form.cleaned_data['correct_answer']
                marks = form.cleaned_data['marks']
                
                uuid_question_id = str(uuid.uuid4())

                try:
                    Question.objects.create(
                        section = section,
                        question_text = question_text,
                        question_type = question_type,
                        question_id = uuid_question_id,
                        user_id = request.user.id,
                        marks = marks
                    )
                except:
                    print("There is a database error...")
                else:
                    try:
                        MultipleChoice.objects.create(
                            user_id = request.user.id,
                            question_id = uuid_question_id,
                            answer_field_1 = answer_field_1,
                            answer_field_2 = answer_field_2,
                            answer_field_3 = answer_field_3,
                            answer_field_4 = answer_field_4,
                            correct_answer = correct_answer
                        )
                    except:
                        print('There is a database error...')
                return HttpResponseRedirect('/dashboard/question-bank/')

                print(correct_answer)
        else:
            form = QuestionForm()

        return render(request, 'dashboard/questions.html', {'form': form})
    else:
        return redirect('/login/')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

