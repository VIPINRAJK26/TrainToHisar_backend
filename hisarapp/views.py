from django.shortcuts import render
from hisarapp.models import Location, Expense
from hisarapp.serializers import LocationSerializer, ExpenseSerializer
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.



class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer