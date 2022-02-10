from django.contrib import admin
from middleware_api.models import StripeRequest, StripeResponse

admin.site.register(StripeRequest)
admin.site.register(StripeResponse)
