from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Question, Choice

from django.views.generic import ListView, DetailView, View

import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', {'context':context})

class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        print request
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

class VoteView(View):
    def post(self, request, *args, **kwargs):
        logger.debug("VoteView.question.id: %s" % kwargs['pk'])
        p = get_object_or_404(Question, pk=kwargs['pk'])
        try:
            selected_choice = p.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': p,
                'error_message': "You didn't select a choice",
                })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

""" form test
"""
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=10)

def form_test(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['your_name']
            #return HttpResponseRedirect('')
    else:
        form = NameForm()
    return render(request, 'polls/form_test.html', {'form':form})

""" class view test
"""
from django.views.generic import View
from django.http import HttpResponse
class MyView(View):
    def get(self, request):
        return HttpResponse('result')
