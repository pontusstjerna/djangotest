from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.

def index(request):
    # template = loader.get_template('app/index.html')
    #return HttpResponse(template.render({'latest_questions': latest_questions}, request))
    
    latest_questions = Question.objects.order_by('-pub_date')[0:5]
    return render(request, 'app/index.html', {'latest_questions': latest_questions})

def detail(request, question_id):

    #try: 
     #   response = "<h1>%s</h1>" % Question.objects.get(pk=question_id).question_text
    #except:
        #raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'app/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("You are looking at the result of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)