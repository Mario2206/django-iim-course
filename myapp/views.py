from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from .forms import QuestionForm

# Create your views here.

def index(request):
    questions = Question.objects.all()
    return render(request, 'myapp/index.html', {'questions': questions})

def create(request) :
    if request.method == 'POST' :
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = Question(text=form.cleaned_data["text"])
            question.save()
            return HttpResponseRedirect('/myapp')
    else :
        form = QuestionForm()
    return render(request, 'myapp/create.html', { 'form': form })

def edit(request, id):
    question = Question.objects.get(id=id)
    if question is None :
        return HttpResponseRedirect('/myapp')
        
    if request.method == 'POST' :
        form = QuestionForm(request.POST)

        if form.is_valid():
            question.text = form.cleaned_data["text"]
            question.save()
            return HttpResponseRedirect('/myapp')
    else :
        form = QuestionForm(initial={"text": question.text})
    return render(request, 'myapp/create.html', { 'form': form, 'question': question })

def delete(request, id):
    question = Question.objects.get(id=id)
    if question is None :
        return HttpResponseRedirect('/myapp')

    question.delete()
    return HttpResponseRedirect('/myapp')