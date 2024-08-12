from django.shortcuts import render

from polls.models import Question


# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_questions(request):
    questions = Question.objects.all()
    return render(request, 'list_questions.html', {'questions': questions})