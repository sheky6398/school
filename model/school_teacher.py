from odoo import models,api,fields
from datetime import date,datetime
from odoo.exceptions import ValidationError


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher Data"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Teacher Name',required=True)
    date_of_birth = fields.Date(required=True,default=fields.Date.today())
    age = fields.Integer(compute='_compute_age')
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],default='male',required=True)
    image = fields.Binary(string="Teacher Image")
    phone = fields.Char(string="Phone Number", tracking=True)
    email = fields.Char(string="Email Id",compute='_compute_email')
    street = fields.Char()
    city = fields.Char(required=True,tracking=True)
    state_id = fields.Many2one('res.country.state',string='State',required=True, domain="[('country_id','=', country_id)]")
    country_id = fields.Many2one('res.country',string='Country',required=True)
    zip = fields.Char()
    active = fields.Boolean(default=True)
    department = fields.Char(required=True,tracking=True)
    designation = fields.Char(required=True,tracking=True)
    course_ids = fields.Many2many('school.course',string='Courses')
    subject_ids = fields.One2many('school.subject','subject_id',string='Subjects')


    @api.depends('date_of_birth')
    def _compute_age(self):
        today_date=date.today()
        if self.date_of_birth:
            date_of_birth = fields.Datetime.to_datetime(self.date_of_birth).date()
            total_age = str(int((today_date-date_of_birth).days/365))
            self.age = total_age

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for record in self:
            if self.date_of_birth >date.today():
                raise ValidationError("It is not possible to select future date")
    

    
    def _compute_email(self):
        for record in self:
            if record.name:
                record.email = record.name.replace(' ',".").lower()+'@school.com' 


    def action_activate(self):
        self.active = True
    
    def teacher_profile_method(self):
        template_id = self.env.ref('school.school_teacher_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    
    



    
   


