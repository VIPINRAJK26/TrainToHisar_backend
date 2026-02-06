from rest_framework import serializers
from .models import Location, Expense


class LocationSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='place',read_only=True)
    class Meta:
        model = Location
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.place',read_only=True)
    people = serializers.CharField(source='location.people',read_only=True)
    class Meta:
        model = Expense
        fields = '__all__'