from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

from django.shortcuts import render


def index(request):
    
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}   
    return render(request,'pybo/question_list.html',context)
    # return render(request,'pybo/base.html',context)

def detail(request,question_id):

    qes = Question.objects.get(id=question_id)
    context = {'question':qes}
    return render(request,'pybo/question_detail.html',context)

