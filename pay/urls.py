"""pay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from item.views import CheckoutView, CreateCheckoutSessionView, CancelView, SuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/item/', include('item.urls')),
    path('api/v1/item/<int:pk>/', CheckoutView.as_view(), name='checkout'),
    path('api/v1/item/cancel/', CancelView.as_view(), name='cancel'),
    path('api/v1/item/success/', SuccessView.as_view(), name='success'),
    path('api/v1/buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')


]
