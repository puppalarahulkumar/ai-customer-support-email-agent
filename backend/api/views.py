import json
from urllib import request

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.http import JsonResponse
from django.views import View
from backend.agents.email_agent import app

from django.shortcuts import render

from backend.api.serializers import EmailRequestSerializer

# Create your views here.


class ProcessMailAPIView(APIView):

    
    def post(self, request):
        serializer=EmailRequestSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        

        return JsonResponse(result)