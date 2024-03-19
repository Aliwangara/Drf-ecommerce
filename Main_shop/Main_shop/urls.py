"""

"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from Main_shop.product import views

router =DefaultRouter()
router.register(r'Category', views.CategoryView),
router.register(r'Brand', views.BrandView),
router.register(r'Product', views.ProductView),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs",SpectacularSwaggerView.as_view(url_name="schema") ),
    
    
]
