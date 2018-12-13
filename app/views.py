from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[0:5]

    response = '<h1>Djangotest</h1>'
    response += '<ol>' + ''.join(list(map(lambda q : '<li>' + q.question_text + '</li>', latest_questions))) + '</ol>'

    return HttpResponse("%s" % response)

def detail(request, question_id):

    response = 'Question %s not found :(' % question_id

    try: 
        response = "<h1>%s</h1>" % Question.objects.get(pk=question_id).question_text
    except:
        print("Error")

    return HttpResponse(response)

def results(request, question_id):
    return HttpResponse("You are looking at the result of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)