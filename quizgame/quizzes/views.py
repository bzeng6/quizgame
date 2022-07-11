from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from datetime import datetime
from django.contrib.auth.decorators import login_required
from quizzes.forms import EditProfileForm
from quizzes.models import Question, Exam
from django.http import Http404

def index(request):
	exam_list = Exam.objects.all()
	args = {'exam_list': exam_list}
	return render(request, 'quizzes/index.html', args)

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/quizzes')
	else:
		form = UserCreationForm()
		current_date = datetime.now()
		args = {'form': form, 'date': current_date}
		return render(request, 'quizzes/register.html', args)

@login_required
def view_profile(request):
	args = {'user': request.user}
	return render(request, 'quizzes/profile.html', args)

@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/quizzes/profile')
	else:
		form = EditProfileForm(instance=request.user)
		current_date = datetime.now()
		args = {'form': form, 'date': current_date}
		return render(request, 'quizzes/edit_profile.html', args) 

@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/quizzes/profile')
	else:
		form = PasswordChangeForm(user=request.user)
		current_date = datetime.now()
		args = {'form': form, 'date': current_date}
		return render(request, 'quizzes/change_password.html', args) 

def quiz(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
		args = {'question': question}
	except Question.DoesNotExist:
		raise Http404('This question is not in the database.')
	return render(request, 'quizzes/quiz.html', args)

def check_answer(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return quiz(request, question_id)
	else:
		if selected_choice.is_correct:
			return render(request, 'quizzes/correct.html')
		else:
			return render(request, 'quizzes/incorrect.html')

