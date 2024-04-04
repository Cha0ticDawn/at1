from django.core import serializers
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Question
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import QuestionForm

@login_required
def index(request):
    questions = Question.objects.all()
    questions_json = serializers.serialize('json', questions)
    return render(request, 'eduprod/index.html', {'questions_json': questions_json})

def landing_page(request):
    return render(request, 'eduprod/index.html')

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'eduprod/question_form.html'
    success_url = reverse_lazy('eduprod:question_list')  # Redirect to the question list page after creating

class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'eduprod/question_form.html'
    success_url = reverse_lazy('eduprod:question_list')  # Redirect to the question list page after updating

class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'eduprod/question_confirm_delete.html'
    success_url = reverse_lazy('eduprod:question_list')  # Redirect to the question list page after deleting

class QuestionList(LoginRequiredMixin, ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'eduprod/question_list.html'