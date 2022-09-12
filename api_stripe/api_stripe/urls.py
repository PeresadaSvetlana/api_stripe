from django.contrib import admin
from django.urls import path
from api.views import CreateCheckoutSessionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/{id}/', CreateCheckoutSessionView.as_view(), name='item'),
]
