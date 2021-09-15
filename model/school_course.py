from odoo import models,fields,api


class SchoolCourse(models.Model):
    _name = "school.course"
    _description = "Course Data"


    # name = fields.Char(string="Course Name",required=True)
    description = fields.Text()
    duration = fields.Selection([('2_year','2 Year'), ('3_year','3 Year'), 
                                 ('4_year','4 Year')],
                                 default='3_year',required=True)
    fee = fields.Float(string='Course Fee')
    name = fields.Selection([('btech','Btech'), ('bca','BCA'),                               
                                   ('bcom','Bcom'),('bba','BBA'),
                                   ('polytechnic','Polytechnic'),
                                   ('bsc','BSC'),('mba','MBA'),
                                   ('msc','MSC'), ('mca','MCA'), 
                                   ('mtech','Mtech'), ('mcom','Mcom')],
                                   default='btech',required=True)
    teacher_ids = fields.Many2many('school.teacher',string='Teachers')
    student_ids = fields.Many2many('school.student',string='Students')
    active = fields.Boolean(default=True)
    

    

