import stripe
from django.views import View
from django.views.generic import TemplateView
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Item
from django.shortcuts import render

stripe.api_key = 'sk_test_51LgsIxDOqQHVZ6140CbuDPJ1OGcgTY5kPKaAPdSvpt34AWYoYuGquZ2hyNdMBUAbN1qXpqnmgeGfnNsH5ccJTEDw00BeQEoV7v'


class ItemView(TemplateView):
    template_name = 'templates/item.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        item = Item.objects.get(pk=pk)
        context = super(ItemView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': stripe.api_key
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': item.price,
                        'item_data': {
                            'name': item.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "item_id": item.id
            },
            mode='payment',
        )
        return JsonResponse({
            'id': session.id
        })

    def item_router(request, item_id):
        item = Item.objects.get(id=item_id)
        return render(request, "templates/item.html", context=model_to_dict(item))

