from rest_framework.views import APIView
from Clothing.models import Category, Product, DetailProduct, ImageProduct
from Clothing.serializer import (
    CategorySerializer,
    DetailProductSerializer,
    ImageProductSerializer,
    ProductSerializer,
)
from rest_framework.response import Response
from rest_framework import status


class CategoryList(APIView):
    def get(self, request):
        category = Category.objects.all()  # Complex Data
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class CategoryCreate(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCategory(APIView):
    def get_category_by_pk(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            return category
        except:
            return Response(
                {"error": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk):
        category = self.get_category_by_pk(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_category_by_pk(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_category_by_pk(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()  # Complex Data
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductCreate(APIView):
    def post(self, request):
        serializerProduct = ProductSerializer(data=request.data)
        if serializerProduct.is_valid():
            product = serializerProduct.save()
            if "details" in request.data and request.data["details"] is not None:
                for detail in request.data["details"]:
                    if detail is None:
                        continue
                    detail["product_id"] = product.id
                    serializerDetailProduct = DetailProductSerializer(data=detail)
                    if serializerDetailProduct.is_valid():
                        detailProduct = serializerDetailProduct.save()
                        if "image" in detail and detail["image"] is not None:
                            for image in detail["image"]:
                                serializerImageProduct = ImageProductSerializer(
                                    data={
                                        "image": image,
                                        "detail_product_id": detailProduct.id,
                                    }
                                )
                                if serializerImageProduct.is_valid():
                                    serializerImageProduct.save()
                                else:
                                    return Response(
                                        serializerImageProduct.errors,
                                        status=status.HTTP_400_BAD_REQUEST,
                                    )
                        else:
                            print("Khong tìm thấy ảnh")
                    else:
                        return Response(
                            serializerDetailProduct.errors,
                            status=status.HTTP_400_BAD_REQUEST,
                        )
            else:
                return Response(
                    {"message": "Vui lòng điền ít nhất một DetailProduct"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response({"message": "Thêm sản phẩm thành công"})
        else:
            return Response(
                serializerProduct.errors, status=status.HTTP_400_BAD_REQUEST
            )


class GetProduct(APIView):
    def get_product_by_pk(self, pk):
        try:
            product = Product.objects.get(pk=pk)
            return product
        except:
            return Response(
                {"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk):
        try:
            product = self.get_product_by_pk(pk)
            # Lấy tất cả các detail liên quan đến sản phẩm
                
            details = DetailProduct.objects.filter(product_id=product.id)
            # Tạo danh sách chứa thông tin các detail và images của sản phẩm
            product_details = []
            for detail in details:
                images = ImageProduct.objects.filter(detail_product_id=detail.id)
                # Serialize detail và images thành dạng JSON
                serializerDetail = DetailProductSerializer(detail)
                serializerImages = ImageProductSerializer(images, many=True)
                # Gộp thông tin detail và images vào một đối tượng JSON
                detail_data = serializerDetail.data
                detail_data["images"] = serializerImages.data
                product_details.append(detail_data)

            # Serialize thông tin của sản phẩm
            serializerProduct = ProductSerializer(product)
            return Response({"product": serializerProduct.data, "details": product_details})
        except:
            return Response(
                {"message": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        

    def put(self, request, pk):
        product = self.get_product_by_pk(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_product_by_pk(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
