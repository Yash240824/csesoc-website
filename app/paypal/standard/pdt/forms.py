#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.paypal.standard.forms import PayPalStandardBaseForm
from app.paypal.standard.pdt.models import PayPalPDT


class PayPalPDTForm(PayPalStandardBaseForm):
    class Meta:
        model = PayPalPDT