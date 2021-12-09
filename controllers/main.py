from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging

_logger = logging.getLogger(__name__)


class WebsiteSaleInherit(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
        print("Inherited Odoo Mates ....", res)
        return res


class Student(http.Controller):

    # Sample Controller Created
    @http.route('/student_webform', type="http", website=True, auth='public')
    def student_webform(self, **kw):
        _logger.info(f'\nEXECUTION HERE-----------\n')
        return request.render("school.create_student_form", {})

    @http.route('/create/webstudent', type='http', auth='public', webiste=True)
    def create_student_form(self, **kw):
        _logger.info(f'\nDATA RECEIVED = {kw}-----------\n')
        request.env['school.student'].sudo().create(kw)
        result = request.render('school.student_thanks',{})
        _logger.info(f'\nRESULT = {result}-----------\n')
        return result