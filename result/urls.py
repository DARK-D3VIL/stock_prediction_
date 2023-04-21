from django.urls import path
from  result.views import ResultView

urlpatterns = [
     path('results/',ResultView.as_view(),name='results'),
     
 ]