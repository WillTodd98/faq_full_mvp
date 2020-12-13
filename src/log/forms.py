from django import forms
from .models import Question, Category, Tag

choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

tag_choices = Tag.objects.all().values_list('name','name')
tag_choice_list = []

for item in tag_choices:
    tag_choice_list.append(item)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # tag = forms.MultipleChoiceField(choices = tag_choices, initial="No Tags", required=False)
        fields = [
            'question_text',
            'answer_text',
            'answered',
            'category',
            'tag',
            'author'
        ]
        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'tag': forms.SelectMultiple(choices=tag_choice_list, attrs={'class':'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'name'
        ]