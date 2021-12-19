from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Brianna. You're at the quizzes index!")