"""

"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Main_shop.product import views

router =DefaultRouter()
router.register(r'Category', views.CategoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
