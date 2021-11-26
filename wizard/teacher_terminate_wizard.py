import logging
from odoo import models,fields
import logging

_logger = logging.getLogger(__name__)


class TeacherTerminate(models.TransientModel):
    _name = "teacher.terminate.wizard"
    _description = "Terminating the Teacher"


    reason = fields.Text(string="Reason")
    


    def teacher_terminate(self):
        active_teacher_id = self.env.context.get('active_id')
        active_teacher_record = self.env['school.teacher'].browse(active_teacher_id)
        active_teacher_record.write({
            'active':False
        })
        active_teacher_record.message_post(body=self.reason)      
        _logger.info(f'\n ')
     
        
        
        
        
      

        
