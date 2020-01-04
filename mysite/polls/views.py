from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    for_frontend = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', for_frontend)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', { 'question': question })

def results(request, question_id):
    return HttpResponse(" nothing")

def vote(request, question_id):
    return HttpResponse(" nothing")
