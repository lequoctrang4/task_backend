from rest_framework import serializers
from Clothing.models import Category, DetailProduct, ImageProduct, Product
from django.forms import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def validate(self, data):
        if not len(data["name"]):
            raise ValidationError("Invalid name of category")
        return data
    
    
class DetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailProduct
        fields = "__all__"

    # def validate(self, data):
    #     if not len(data["name"]):
    #         raise ValidationError("Invalid name of category")
    #     return data
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

        
    def validate(self, data):
        return data
        
class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = "__all__"
