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
        keyword = request.GET.get('keyword')

        try:
            histories = SearchHistory.objects.all()
            # if keyword != None:
            #     histories = [obj for obj in histories if obj.keyword==keyword]

            serializer = SearchHistorySerializer(histories, many=True)
            result = serializer.data
            return Response(data=result,status=status.HTTP_200_OK)
        except:
            return Response(data={'errors': 'Bad Request Format'}, status=status.HTTP_400_BAD_REQUEST)
