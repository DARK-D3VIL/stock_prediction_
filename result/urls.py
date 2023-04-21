from django.urls import path
from  result.views import ResultView

urlpatterns = [
     path('',ResultView.as_view(),name='results'),
     
 ]