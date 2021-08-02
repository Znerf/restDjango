from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import user
from .serializers import userSerializer

from rest_framework.decorators import api_view
# @csrf_exempt
@api_view(['GET','POST'])
def user_list(request):
    if request.method=='GET':
        users=user.objects.all()
        serializer=userSerializer(users, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data,safe=False)
    elif request.method== 'POST':
        # data=JSONParser().parse(request)
        # serializer=userSerializer(data=data)
        serializer=userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return JsonResponse(serializer.data,status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse(serializer.errors, status=400)
    
@api_view(['GET','DELETE','PUT'])

def user_detail(request,pk):
    try:
        users= user.objects.get(pk=pk)
    except user.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer=userSerializer(users)
        return Response(serializer.data)

        # return JsonResponse(serializer.data)
    elif request.method=='PUT':
        serializer=userSerializer(users, data=request.data)

        # data=JSONParser().parse(request)
        # serializer=userSerializer(users, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            # return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors,status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        users.delete()
        # return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)
        


class userList(APIView):
    def get(self,request):
        user1=user.objects.all()
        serializer= userSerializer(user1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

