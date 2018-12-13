from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.

def index(request):
    # template = loader.get_template('app/index.html')
    #return HttpResponse(template.render({'latest_questions': latest_questions}, request))
    
    latest_questions = Question.objects.order_by('-pub_date')[0:5]
    return render(request, 'app/index.html', {'latest_questions': latest_questions})

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