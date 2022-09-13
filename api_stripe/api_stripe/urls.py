from django.contrib import admin
from django.urls import path
from api.views import ItemView, CreateCheckoutSessionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:pk>/', ItemView.as_view(), name='item'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
