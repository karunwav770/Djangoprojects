# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from testapp.models import Mymodel
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Mymodel
        fields='__all__'
    # def validate_esal(self,name):
    #     if name.lower()=='babu':
    #         raise serializers.ValidationError('Babu details we cant update sorry')
    #     return name

    