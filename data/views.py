from .models import Gsm
from django.http import Http404
from .serializers import GsmSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import generic



# Create your views here.
class GsmView(APIView):
     #permission_classes = (permissions.AllowAny,)
     
    def get(self, request, format=None):
        users = Gsm.objects.all()
        serializer = GsmSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = GsmSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class GsmDetail(APIView):
     #permission_classes = (permissions.AllowAny,)
     
    def get_object(self,pk):
        try:
            return Gsm.objects.get(pk=pk)
        except Gsm.DoesNotExist:
            raise Http404

    def get(self,request,pk, format=None):
        user = self.get_object(pk)
        user = GsmSerializer(user)
        return Response(user.data)

    def post(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = GsmSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class cordinates(generic.ListView):
    model = Gsm
    template_name = 'cordinates/cordinate.html'

    def get_queryset(self):
        return Gsm.objects.all()
