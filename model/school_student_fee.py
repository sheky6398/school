from odoo import models,fields,api


class SchoolStudentFee(models.Model):
    _name = "school.student.fee"
    _description = "Student Fee Data"
    _rec_name = 'student_id'


    total_fee = fields.Float()
    due_fee = fields.Float(compute='_compute_due_fee')
    amount_paid = fields.Float()
    date_paid = fields.Date(string='Paid Date')
    payment_mode = fields.Selection([('cash','Cash'), ('cheque','Cheque'), 
                                     ('online','Online')],default='online',required=True)
    student_id = fields.Many2one('school.student',string='Student',required=True)
    state = fields.Selection([('draft','Draft'), ('paid','Paid')],default='draft', string='status')


    
    @api.depends('amount_paid','total_fee')
    def _compute_due_fee(self):
        for record in self:
            record.due_fee = record.total_fee - record.amount_paid
            due_fee = record.due_fee


