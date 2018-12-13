from django.urls import path

from . import views

urlpatterns = [
    # /
    path('', views.index, name='index'),
    # /x
    path('<int:question_id>/', views.detail, name='detail'),
    # /x/results
    path('<int:question_id>/results/', views.results, name='results'),
    # /x/vote
    path('<int:question_id>/vote/', views.vote, name='vote')
]