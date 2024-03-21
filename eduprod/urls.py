from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.QuestionCreate.as_view(), name='question_add'),  # URL pattern for adding a question
    path('list/', views.QuestionList.as_view(), name='question_list'),  # URL pattern for listing questions
    path('edit/<int:pk>/', views.QuestionUpdate.as_view(), name='question_edit'),  # URL pattern for editing a question
    path('delete/<int:pk>/', views.QuestionDelete.as_view(), name='question_delete'),  # URL pattern for deleting a question
]