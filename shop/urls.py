from django.urls import path
from . import views
app_name= 'shop'
urlpatterns = [

    path('', views.index, name='index'),
    path('list/', views.product_list, name='product_list'),
    path('productDetails/<slug:product_slug>/', views.product_detail, name='product_details'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]