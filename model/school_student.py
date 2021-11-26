from odoo import models,fields,api
from datetime import date, datetime
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student Data"
    _inherit = ['mail.thread','mail.activity.mixin']




    name = fields.Char('Student Name',required=True,tracking=True)
    date_of_birth = fields.Date(required=True,tracking=True,default=fields.Date.today())
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],
                                 default='male', required=True)
    image = fields.Binary(string='Student Image')
    street = fields.Char(string="Street")
    zip = fields.Char(string="Zip")
    age = fields.Integer(compute='_compute_age')
    email = fields.Char('Email')
    phone = fields.Char(string='Phone No',tracking=True)
    state_id = fields.Many2one('res.country.state',string='State',required=True, domain="[('country_id','=', country_id)]",tracking=True)
    country_id = fields.Many2one('res.country',string='Country',required=True)
    state = fields.Selection([('new','New'), ('current','Current'),('pass_out','Pass Out')],
                            default='new',string='status')
    city = fields.Char(tracking=True)
    course_id = fields.Many2one('school.course',string='Course',help="Courses in which student to be enrolled",required=True)
    subject_ids = fields.Many2many('school.subject',related='course_id.subject_ids', string='Subjects',help="Subjects for this Course")
    active = fields.Boolean(default=True)
    registration_number = fields.Char(required=True)
    date_registration = fields.Date(string="Registration Date",required=True,default=fields.Date.today())
    fee_line_ids = fields.One2many('school.student.fee.line','student_id',string="Student Fee",help="Student Fee Record")
    fee_id = fields.Many2one('school.student.fee',string="Fee")
    
    

    @api.depends('date_of_birth')
    def _compute_age(self):
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
        student_fee = self.env['school.student.fee'].create({
            'student_id':self.id,
            'course_id':self.course_id.id
        })
        self.fee_id=student_fee.id
        
       


    def pass_out_method(self):
        self.state = 'pass_out'
        self.active = False

    # @api.model
    # def create(self,vals_list):
    #     name = vals_list.get('name')
    #     vals_list.update({'name':"Bharat yadav",'phone':9990612354,'email':name+'@gmail.com'})
    #     _logger.info(f'\n Student is being created by following details:{vals_list} \n')
    #     record = super(SchoolStudent,self).create(vals_list)       
    #     return record
        
    def unlink(self):
        _logger.info(f'\n deleting {self.name} \n')
        return super(SchoolStudent,self).unlink()
    
    def write(self,vals):
        _logger.info(f'\n Name {self.name} \n')


        return super(SchoolStudent,self).write(vals)

    def copy(self):
        copied = super(SchoolStudent,self).copy()
        _logger.info(f'\n copied = {self.name} \n ')
        return copied
        
    def student_profile_method(self):
        template_id = self.env.ref('school.school_student_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)


        
        

    




    


   


