from odoo import models,fields,api

class SchoolSubject(models.Model):
    _name = "school.subject"
    _description = "Subjects Data"


    name = fields.Char(string='Subject Name',required=True)
    description = fields.Text()
    department = fields.Char()
    subject_id = fields.Many2one('school.subject',string='subject')