from odoo import models,fields,api


class SchoolStudentFee(models.Model):
    _name = "school.student.fee"
    _description = "Student Fee Data"
    _rec_name = 'student_id'
    _inherit = ['mail.thread']


    
    due_fee = fields.Float(compute='_compute_due_fee')
    amount_paid = fields.Float(help="Pay Your Fee here",compute='_compute_amount_paid')
    student_id = fields.Many2one('school.student',string='Student',required=True)
    state = fields.Selection([('draft','Pending'), ('paid','Paid')],default='draft', string='status',compute='_compute_state')
    course_id = fields.Many2one('school.course',string="Course",related="student_id.course_id")
    total_fee = fields.Float(related="student_id.course_id.fee",help="Total Course Fee")
    fee_line_ids = fields.One2many("school.student.fee.line","student_fee_id",string="Fees")


    @api.depends('amount_paid','total_fee')
    def _compute_due_fee(self):
        for record in self:
            record.due_fee = record.total_fee - record.amount_paid

    @api.depends('due_fee')
    def _compute_state(self):
        for record in self:
            if record.due_fee <= 0:
                record.state = 'paid'
            else:
                record.state = 'draft'

     
    @api.depends('fee_line_ids')
    def _compute_amount_paid(self):
        for fee in self:
            total_amount = 0
            for fee_line in fee.fee_line_ids:
                total_amount += fee_line.amount_paid
            fee.amount_paid = total_amount
    

        



