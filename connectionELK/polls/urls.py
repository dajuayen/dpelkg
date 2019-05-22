from django.urls import path

from . import views

# Namespace
app_name = 'polls'
urlpatterns = [
    # ex: /polls/old
    path('old', views.index, name='indexOld'),
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/old/5/
    path('old/<int:question_id>/', views.detail, name='detailOld'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/s/5/
    path('s/<int:question_id>/', views.shortcutDetail, name='shortcut_detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/old/5/results/
    path('old/<int:question_id>/results/', views.results, name='resultsOld'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
