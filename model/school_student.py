from odoo import models,fields,api
from datetime import date, datetime
from odoo.exceptions import ValidationError


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student Data"


    name = fields.Char(string='Student Name',required=True)
    date_of_birth = fields.Date(required=True)
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],
                                 default='male', required=True)
    image = fields.Binary(string='Student Image')
    street = fields.Char()
    zip = fields.Char()
    age = fields.Integer(compute='compute_age')
    email = fields.Char(string='Email id')
    phone = fields.Char(string='Phone No')
    state_id = fields.Many2one('res.country.state',string='State',required=True)
    country_id = fields.Many2one('res.country',string='Country',required=True)
    state = fields.Selection([('new','New'), ('current','Current'),('pass_out','Pass Out')],
                            default='new',string='status')
    city = fields.Char()
    course_id = fields.Many2one('school.course',string='Course')
    subject_ids = fields.Many2many('school.subject',string='Subjects')
    active = fields.Boolean(default=True)
    
    


    
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

    def enroll_method(self):
        self.state = 'current'

    def pass_out_method(self):
        self.state = 'pass_out'
   


