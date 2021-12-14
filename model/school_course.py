from odoo import models,fields


class SchoolCourse(models.Model):
    _name = "school.course"
    _description = "Course Data"


    name = fields.Char(string="Course Name",required=True)
    description = fields.Text(string="Description")
    duration = fields.Selection([('2_year','2 Year'), ('3_year','3 Year'), 
                                 ('4_year','4 Year')],
                                 default='3_year',required=True,string="Duration")
    fee = fields.Float(string='Course Fee')
    department = fields.Char(required=True,string="Department")
    teacher_ids = fields.Many2many('school.teacher',string='Teachers')
    student_ids = fields.Many2many('school.student',string='Students')
    subject_ids = fields.Many2many('school.subject',string='Subjects')
    active = fields.Boolean(default=True)
    

    

