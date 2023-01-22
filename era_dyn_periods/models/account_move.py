# -*- coding: utf-8 -*-
from odoo import fields, models,api
from odoo.exceptions import ValidationError,UserError
from datetime import datetime, timedelta, date


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    inv_bill_duration = fields.Float("Inv/Bill Duration",store=True)
    payment_duration = fields.Float("Payment Duration",store=True)
  
   
   