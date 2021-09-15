from odoo import models,api,fields
from datetime import date,datetime
from odoo.exceptions import ValidationError


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher Data"

    name = fields.Char(string='Teacher Name',required=True)
    date_of_birth = fields.Date(required=True)
    age = fields.Integer(compute='compute_age')
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],
                                default='male',required=True)
    image = fields.Binary(string="Teacher Image")
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email Id")
    street = fields.Char()
    city = fields.Char(required=True)
    state_id = fields.Many2one('res.country.state',string='State',required=True)
    country_id = fields.Many2one('res.country',string='Country',required=True)
    zip = fields.Char()
    active = fields.Boolean(default=True)
    department = fields.Char()
    designation = fields.Char()
    course_ids = fields.Many2many('school.course',string='Courses')
    subject_ids = fields.One2many('school.subject','subject_id',string='Subjects')


    
    def compute_age(self):
        today_date=date.today()
        for student_ in self:
            if student_.date_of_birth:
                date_of_birth=fields.Datetime.to_datetime(student_.date_of_birth).date()
                total_age=str(int((today_date-date_of_birth).days/365))
                student_.age=total_age

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for record in self:
            if self.date_of_birth >date.today():
                raise ValidationError("It is not possible to select future date")
    

    
   


