import stripe
import os
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Item
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv('STRIPE_PRIVATE_KEY')


class ItemView(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        item = Item.objects.get(pk=pk)
        context = super(ItemView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': stripe.api_key
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        item = Item.objects.get(pk=pk)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            metadata={
                "item_id": item.id
            },
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return JsonResponse({
            'id': session.id
        })
