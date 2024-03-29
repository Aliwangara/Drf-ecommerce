from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category,Product,Brand
from drf_spectacular.utils import extend_schema

from .serializers import CategorySerializer, ProductSerializer,BrandSerializer

@extend_schema(responses=CategorySerializer)
class CategoryView(viewsets.ViewSet):
    
   queryset = Category.objects.all()
   
   def list(self,request):
       serializer = CategorySerializer(self.queryset, many=True)
       
       return Response (serializer.data)
   
   
   
@extend_schema(responses=BrandSerializer)
class BrandView(viewsets.ViewSet):
    
   queryset = Brand.objects.all()
   
   
   
   def list(self,request):
       serializer = BrandSerializer(self.queryset, many=True)
       
       
       
       return Response (serializer.data)
   
   
class ProductView(viewsets.ViewSet):
    
   queryset = Product.objects.all()
   
   
   
   def list(self,request):
       serializer = ProductSerializer(self.queryset, many=True)
       
       return Response (serializer.data)
   
   

        
           

        
        
        
 
        
        

