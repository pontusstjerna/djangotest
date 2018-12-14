from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    # /
    path('', views.IndexView.as_view(), name='index'),
    # /x
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /x/vote
    path('<int:question_id>/vote/', views.vote, name='vote')
]