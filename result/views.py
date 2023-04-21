from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import random

class ResultView(APIView):
    def get(self,request):
        temp = requests.get("https://api.stockmarketapi.in/api/v1/topgainers?token=65b774fa414c9b01c854a597b7ae82c57e7757b1e12abcb736ab9a754ffb617a")
        response = temp.json()
        D = []
        i = random.randint(0,len(response['data'])-1)
        D.append(response['data'][i]['CompanyName'])
        i = random.randint(0,len(response['data'])-1)
        D.append(response['data'][i]['CompanyName'])
        i = random.randint(0,len(response['data'])-1)
        D.append(response['data'][i]['CompanyName'])
        return Response(D)
