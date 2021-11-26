from odoo import models,fields


class SchoolFeePayment(models.Model):
    _name = "school.student.fee.line"
    _description = "Student Fee"

    def _default_currency_id(self):
        return self.env.user.company_id.currency_id

    student_fee_id = fields.Many2one('school.student.fee',readonly=True,string="Student Name")
    student_id = fields.Many2one('school.student',readonly=True,string="Student Name")
    amount_paid = fields.Monetary(required=True)
    date_paid = fields.Date(string="Paid Date",default=fields.Date.today())
    mode = fields.Selection([('cash','Cash'),('online','Online'),('cheque','Cheque')],default="cash",string="Payment Mode",required=True)
    currency_id = fields.Many2one('res.currency',string="Currency", default=_default_currency_id)