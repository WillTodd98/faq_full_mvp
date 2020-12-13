from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import UpdateView
from django import forms

from django.http import Http404
from log.models import Question, Category, Tag
from .forms import QuestionForm, CategoryForm, TagForm

def question_create_view(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
          form.save()
          return redirect("http://127.0.0.1:8000/questionslist")
    context = {
        'form': form
    }
    return render(request, "question_create.html", context)

def question_lookup_view(request, my_id):
    obj = get_object_or_404(Question, id=my_id)   
    context = {
        'object': obj
    }
    return render(request, "question_detail.html", context)

def question_delete_view(request, my_id):
    obj = get_object_or_404(Question, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect("http://127.0.0.1:8000/questionslist")
    context = {
        "object": obj
    }
    return render(request, "question_delete.html", context)

def question_list_view(request):
    queryset = Question.objects.all() 
    context = {
        "object_list": queryset 
    }
    return render(request, "questions_list.html", context)

def category_view(request, cats):
    category_questions = Question.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats, 'category_questions': category_questions})

# def category_list_view(request):
#     queryset = Question.objects.all()
#     context = {
#         "object_list": queryset 
#     }
#     return render(request, "category_list.html", context)

def category_list_view(request):
    cat_list = Category.objects.all()
    context = {
        "object_list": cat_list
    }
    return render(request, "category_list.html", context)

def search_results_view(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', None)
        result = Question.objects.all().filter(question_text__icontains=search_query)
    context = {
        "result": result
    }
    return render(request, "search_results.html", context)

from .models import Question, Category, Tag

choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

tag_choices = Tag.objects.all().values_list('name','name')
tag_choice_list = []

for item in tag_choices:
    tag_choice_list.append(item)

class edit_question_view(UpdateView):
    model = Question
    template_name = 'question_edit.html'
    form_class = QuestionForm
    # fields = [
    #     'question_text', 
    #     'tag', 
    #     'category'
    #     ]
    # widgets = {
    #         'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
    #         'tag': forms.SelectMultiple(choices=tag_choice_list, attrs={'class':'form-control'})
    #     }