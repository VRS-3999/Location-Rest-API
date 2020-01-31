from rest_framework import serializers
from .models import Gsm

class GsmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gsm
        fields = ['id','name','latitude','longitude']

