from odoo import http
from odoo.http import request
# from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging

_logger = logging.getLogger(__name__)



class Student(http.Controller):
    @http.route('/student_webform', type="http", website=True, auth='public')
    def student_webform(self, **kw):
        _logger.info(f'\nEXECUTION HERE-----------\n')
        return request.render("school.create_student_form", {})

    @http.route('/create/webstudent', type='http', auth='public',methods=['POST'], website=True)
    def create_studentform(self, **kw):
        _logger.info(f'\nDATA RECEIVED = {kw}-----------\n')
        request.env['school.student'].sudo().create(kw)
        # result = request.render('school.student_thanks',{})
        result = request.render('school.student_thanks',{})
        return result
        

    @http.route('/student-thank-you', type="http", website=True, auth='public')
    def student_thankyou(self, **kw):
        _logger.info(f'\nEXECUTION HERE-----------\n')
        result = request.render('school.student_thanks',{})
        return result
