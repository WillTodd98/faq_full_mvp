"""faq_log_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from members import views

from pages.views import home_view
from log.views import question_lookup_view, question_create_view, question_delete_view, question_list_view, category_view, category_list_view, search_results_view, edit_question_view
from members.views import UserRegisterView, PasswordsChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view, name='home'),
    path('', home_view, name='home'),
    path('questions/<int:my_id>/', question_lookup_view, name='questions-detail'),
    path('questionslist', question_list_view, name="questionlist"),
    path('submissions', question_create_view, name='submissons'),
    path('questions/<int:my_id>/delete/', question_delete_view, name="question-delete"),
    path('categories/<str:cats>/', category_view, name='category'),
    path('categories', category_list_view, name='category_list'),
    path('search_result', search_results_view, name='search_result'),
    path('members/', include('django.contrib.auth.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('password/', PasswordsChangeView.as_view(template_name='password_change.html')),
    path('password_success', views.password_success, name="password_success"),
    path('questions/<int:pk>/edit', edit_question_view.as_view(), name="edit_question")
]
