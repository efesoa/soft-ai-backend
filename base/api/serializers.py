from rest_framework.serializers import ModelSerializer
from base.models import Client, Employee


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'email', 'address', 'product', 'is_active']


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'address', 'title', 'is_suspended']
