from django.core.validators import MaxValueValidator
from django.db import models


class Request(models.Model):
    cc_num = models.CharField(max_length=16)
    cvv = models.IntegerField(validators=[MaxValueValidator(9999)])
    exp_month = models.IntegerField(validators=[MaxValueValidator(12)])
    exp_year = models.IntegerField(validators=[MaxValueValidator(9999)])
    trans_id = models.IntegerField()
