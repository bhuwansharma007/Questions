from ast import Delete
from functools import partial
from urllib import request
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bookshelf
from .serializers import BookshelfSerializer
# Create your views here.


class Books(APIView):

    def get(self, request, format=None):
        transformers = Bookshelf.objects.all()
        serializer = BookshelfSerializer( many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookshelfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request):
        try:
            books_obj = Bookshelf.objects.get(id = request.data['id'])
            serializer  = BookshelfSerializer(books_obj,data = request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors())
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'your data is saved'})
        except Exception as e:
            return Response({'status':200,'message':'invaild id'})

    def delete(self,request,format=None):
        try:
            id = request.GET.get('id')
            books_obj = Bookshelf.objects.get(id = id)
            books_obj.delete()
            return Response({'status':200,'message':'deleted'})

        except Exception as e:
            print(e)
            return Response('status':403,'message':'invalid id')
