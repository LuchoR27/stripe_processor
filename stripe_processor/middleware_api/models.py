from django.core.validators import MaxValueValidator
from django.db import models


class Request(models.Model):
    trans_id = models.IntegerField(primary_key=True, unique=True)
    cc_num = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    exp_month = models.IntegerField(validators=[MaxValueValidator(12)])
    exp_year = models.IntegerField(validators=[MaxValueValidator(9999)])


class Response(models.Model):
    amount = models.IntegerField()
    cc_num = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    exp_month = models.IntegerField(validators=[MaxValueValidator(12)])
    exp_year = models.IntegerField(validators=[MaxValueValidator(9999)])
    request_id = models.ForeignKey(to=Request, on_delete=models.CASCADE)
