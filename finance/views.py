from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
 queryset = Category.objects.all()
 serializer_class = CategorySerializer
 permission_classes = [IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
   serializer_class = TransactionSerializer
   permission_classes = [IsAuthenticated]
   
   def get_queryset(self):
      return Transaction.objects.filter(user=self.request.user)
   def perform_create(self, serializer):
      serializer.save(user=self.request.user)
