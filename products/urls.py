from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("products/<int:pk>/", views.ProductView.as_view()),
    path("products/<int:pk>/item/", views.ProductBuyView.as_view()),
    path("products/cart/", views.ProductBuyListView.as_view()),
]
