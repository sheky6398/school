from odoo import models,fields
from odoo.exceptions import Warning
import logging
from datetime import date,datetime

_logger = logging.getLogger(__name__)


class ResPartnerInherited(models.Model):
    _inherit = 'res.partner'


    date_of_birth = fields.Date()
    customer_feedback = fields.Text()
    age =  fields.Integer()


    

    def calculate_age_method(self):
        today_date=date.today()
        if self.date_of_birth:
            date_of_birth = fields.Datetime.to_datetime(self.date_of_birth).date()
            total_age = str(int((today_date-date_of_birth).days/365))
            self.age = total_age
        else:
            raise Warning("Please Enter Date Of birth")
        

    def action_click_me(self):
        raise Warning(f"{self.name} called this method")


    
        

   
   
