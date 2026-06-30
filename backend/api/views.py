import json
from urllib import request

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from agents.email_agent import EmailAgent

from django.http import JsonResponse
from django.views import View


from django.shortcuts import render

from api.serializers import EmailRequestSerializer
from rag.load_data import Storing

# Create your views here.


class ProcessMailAPIView(APIView):

    
    def post(self, request):
        serializer=EmailRequestSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        agent=EmailAgent()
        result=agent.app.invoke(data)


        return JsonResponse(result)

class RebuildRAGAPIView(APIView):

    def post(self,request):
        
        store=Storing()

        store.load_data("rag/docs/knowledge_base.txt")

        return Response(
            {
                "message": "Vector store rebuilt successfully"
            },
            status=status.HTTP_200_OK
        )