from turtle import update
from django.urls import path
from. import views


urlpatterns = [
    path('', views.index),
    path('test/', views.testFunc),
    path('addproduct/', views.post_product),
    path('addcategory/', views.post_category),
    path('updateproduct/<int:product_id>', views.update_product),
    path('deleteproduct/<int:product_id>', views.delete_product),
    path('category/', views.show_category),
    path('updatecategory/<int:category_id>', views.update_category),
    path('deletecategory/<int:category_id>', views.delete_category)

]
