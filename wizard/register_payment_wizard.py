from odoo import models,fields,api

import logging

_logger = logging.getLogger(__name__)

class RegisterPayment(models.TransientModel):
    _name = "register.payment.wizard"
    _description = "payment fee"

    def _default_currency_id(self):
        return self.env.user.company_id.currency_id


    student_id = fields.Many2one('school.student',string="Student Name")
    course_id = fields.Many2one('school.course',string="Course Name",related="student_id.course_id")
    amount_paid = fields.Monetary(string="Amount",required=True)
    date_payment = fields.Date(string="Payment Date", default=fields.Date.today())
    mode = fields.Selection([('cash','Cash'), ('online','Online'), 
                             ('cheque','Cheque')],default='cash',required=True)
    currency_id = fields.Many2one('res.currency',string="Currency", default=_default_currency_id)
    

    def pay_fee(self):       
        active_student_id = self.env.context.get('active_id')
        active_student_record = self.env['school.student'].browse(active_student_id)
        mode = self.mode
        amount_paid = self.amount_paid
        date_payment = self.date_payment
        active_fee_id = active_student_record.fee_id
        active_payment = self.env['school.student.fee.line'].create({
            'student_fee_id': active_fee_id.id,
            'amount_paid': amount_paid,
            'mode': mode,
            'date_paid': date_payment
        })

        
        
    
        
