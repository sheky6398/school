from odoo import models,fields,api

class RegisterPayment(models.TransientModel):
    _name = "register.payment.wizard"
    _description = "payment fee"


    student_id = fields.Many2one(string="Student Name")
    course_id = fields.Many2one(string="Course Name")
    amount_paid = fields.Float(string="Amount")
    date_payment = fields.Date(string="Payment Date")
    mode = fields.Selection([('cash','Cash'), ('online','Online'), 
                             ('cheque','Cheque')],default='cash')

    def pay_fee(self):
        context = self.env.context
        model = context['active_model']
        id = context['active_id']
        record = self.env[model].browse(id)
        result = record.write({'amount_paid':self.amount_paid})
        result = record.write({'student_id':self.student_id})
        result = record.write({'course_id':self.course_id})
        result = record.write({'date_payment':self.date_payment})
        result = record.write({'mode':self.mode})

    
