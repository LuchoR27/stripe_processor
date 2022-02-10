from django.core.validators import MaxValueValidator
from django.db import models


class StripeRequest(models.Model):
    trans_id = models.CharField(max_length=32, primary_key=True, unique=True)
    cc_num = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    exp_month = models.IntegerField(validators=[MaxValueValidator(12)])
    exp_year = models.IntegerField(validators=[MaxValueValidator(9999)])
    errors = models.JSONField(blank=True, null=True)


class StripeResponse(models.Model):
    stripe_id = models.CharField(max_length=32, primary_key=True, unique=True)
    status = models.CharField(max_length=24)
    amount = models.IntegerField()
    action = models.CharField(max_length=24)
    request_id = models.ForeignKey(to=StripeRequest, on_delete=models.CASCADE)
