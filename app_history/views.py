from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import SearchHistory
from . serializers import SearchHistorySerializer
# Create your views here.

class UsersSearchHistory(APIView):


    def get(self, request, format=None):
        try:
            histories = SearchHistory.objects.all()
            serializer = SearchHistorySerializer(histories, many=True)
            data = {
                        'results': serializer.data
                    }
            return Response(data=data,status=status.HTTP_200_OK)
        except:
            return Response(data={'errors': 'Bad Request Format'}, status=status.HTTP_400_BAD_REQUEST)
