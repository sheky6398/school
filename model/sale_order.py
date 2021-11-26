from odoo import models
from odoo.exceptions import Warning
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_test(self):
        _logger.info(f'\n{self}\n')
        raise Warning(f'{self.name} has order Goods of {self.amount_total}')