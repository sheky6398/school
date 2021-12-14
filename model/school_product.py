from odoo import models
from odoo.exceptions import Warning


class SchoolProduct(models.Model):
    _inherit = "product.product"



    def action_product(self):
        raise Warning(f'{self.name},whose public price is {self.lst_price}, and it"s Cost is {self.standard_price} has Clicked this button')