from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category,Product,Brand

from .serializers import CategorySerializer, ProductSerializer,BrandSerializer


class CategoryView(viewsets.ViewSet):
    
   queryset = Category.objects.all()
   
   def list(self,request):
       serializer = CategorySerializer(self.queryset, many=True)
       if serializer.is_valid():
        return Response(serializer.data)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
           
    
   
       
class ProductView(viewsets.ViewSet):
    
    queryset = Category.objects.all()
    
    def list(self,request):
        serializer= ProductSerializer(self.queryset, many=True)
        if serializer.is_valid():
          return Response(serializer.data)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class BrandView(viewsets.ViewSet):
    
    queryset = Brand.objects.all()
    
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)  
        
        if serializer.is_valid():
         return Response(serializer.data)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

