from django.urls import path

from . import views

urlpatterns = [
    path( '', views.index, name='index'),
    path( '<int:pk>/', views.DetailView.as_view(), name='detail'),
    path( '<int:pk>/results/', views.Resultsview.as_view(), name='results'),
    path( '<int:question_id>/vote/', views.vote, name='vote'),
]
