import stripe
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.conf import settings
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from item.models import Item
from item.serializers import CheckoutSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


class CancelView(TemplateView):
    template_name = 'cancel.html'


class SuccessView(TemplateView):
    template_name = 'success.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs["pk"]
        product = Item.objects.get(id=item_id)
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(APIView):

    def get(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Item.objects.get(id=product_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.title,
                    },
                    'unit_amount': product.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/api/v1/item/success/',
            cancel_url='http://localhost:8000/api/v1/item/cancel/',
        )

        return redirect(session.url, code=303)






