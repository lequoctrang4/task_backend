from django.urls import path
from Clothing.views import CategoryList, GetCategory, CategoryCreate, ProductList, ProductCreate, GetProduct

urlpatterns = [
    path("category/list/", CategoryList.as_view()),
    path("category/<int:pk>", GetCategory.as_view()),
    path("category/", CategoryCreate.as_view()),
    
    path("product/list", ProductList.as_view()),
    path("product/<int:pk>", GetProduct.as_view()),
    path("product/", ProductCreate.as_view()), 
]
