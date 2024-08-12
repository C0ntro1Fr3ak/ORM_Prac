
from django.urls import path


from polls.views import index, list_questions

urlpatterns = [
    path('', index, name='index'),
    path('list_questions/', list_questions,  name='questions')
]
