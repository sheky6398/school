from odoo import models,fields

class SchoolSubject(models.Model):
    _name = "school.subject"
    _description = "Subjects Data"


    name = fields.Char(string='Subject Name',required=True)
    description = fields.Html(string="Description")
    department = fields.Char(string="Department",required=True)
    subject_id = fields.Many2one('school.subject',string='Subject')
    course_id = fields.Many2one('school.course',string='Course',required=True)