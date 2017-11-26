# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CustomerData(models.Model):
    custmer_id = models.IntegerField(unique=True)
    limit_bal = models.IntegerField()
    sex = models.IntegerField()
    education = models.IntegerField()
    marriage = models.IntegerField()
    age = models.IntegerField()
    pay_september = models.IntegerField()
    pay_august = models.IntegerField()
    pay_july = models.IntegerField()
    pay_june = models.IntegerField()
    pay_may = models.IntegerField()
    pay_april = models.IntegerField()
    bill_september = models.IntegerField()
    bill_august = models.IntegerField()
    bill_july = models.IntegerField()
    bill_june = models.IntegerField()
    bill_may = models.IntegerField()
    bill_april = models.IntegerField()
    pay_amt_september = models.IntegerField()
    pay_amt_august = models.IntegerField()
    pay_amt_july = models.IntegerField()
    pay_amt_june = models.IntegerField()
    pay_amt_may = models.IntegerField()
    pay_amt_april = models.IntegerField()

    def __unicode__(self):
        return 'Customer ID: {}'.format(self.custmer_id)
