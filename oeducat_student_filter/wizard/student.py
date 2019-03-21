# -*- coding: iso-8859-1 -*-

from openerp import models, fields, api
from datetime import datetime, timedelta
from dateutil import parser
from openerp.exceptions import ValidationError
from openerp.exceptions import except_orm, Warning, RedirectWarning
import json

import logging
_logger = logging.getLogger(__name__)

#### RPM
class StudentReport(models.TransientModel):
    _name = 'openeducat_erp.student_wizard'
    
    operating_unit_id = fields.Many2one('operating.unit')
    division_ids = fields.Many2many('op.division')
    division_ids = fields.Many2many('op.division')
    batch_id = fields.Many2one('op.batch')
    standard_id = fields.Many2one('op.standard')
    course_id = fields.Many2one('op.course')
    sdutend_ids = fields.Many2many('op.student')
    all_divisions = fields.Boolean('All divisions')
    
    """manager_id = fields.Many2many('res.users', relation='education_contract_rpm_wizard_manager_user_rel', string='Gerenete de Marketing')
    user_id = fields.Many2many('res.users', string='Vendedor')
    campus_id = fields.Many2many('operating.unit', string='Sucursal')
    date_start = fields.Date('Fecha inicio')
    date_end = fields.Date('Fecha fin')
    contract_ids = fields.Many2many('education_contract.contract', relation='education_contract_rpm_wizard_rel', string='Contratos')"""
            
    @api.multi
    def print_report(self):
        domain = []
        divisions = []
        roll_numbers = False
        students = []
        
        if self.operating_unit_id:
            domain = [('operating_unit_id', '=', self.operating_unit_id.id)]
            if self.division_ids:
                domain.append(('id', 'in', self.division_ids.ids))
            else:
                self.all_divisions = True
            divisions = self.env['op.division'].search(domain).ids
            
        domain = [('division_id', 'in', divisions)]
        if self.batch_id:
            domain.append(('batch_id', '=', self.batch_id.id))
        if self.standard_id:
            domain.append(('standard_id', '=', self.standard_id.id))
        if self.course_id:
            domain.append(('course_id', '=', self.course_id.id))
        roll_numbers = self.env['op.roll.number'].search(domain)
        
        for rn in roll_numbers:
            students.append(rn.student_id.id)
            
        #self.student_ids = [(6, False, students)]
        self.division_ids = [(6, False, divisions)]
        
        datas = {
            #'ids': students,
            'ids': divisions,
            'model': 'op.division',
            #'form': contract_ids,
        }
        
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'oeducat_student_filter.report_students',
            'datas': datas,
        }
        
        """return {
            "type": "ir.actions.do_nothing",
        }"""
        
            
    """def _get_beneficiary_data(self, contract):
        data = []
        
        beneficiary_ids = contract.beneficiary_ids
        
        for b in beneficiary_ids:
            data.append({
                'name': '%s %s %s' % (b.student_id.name, b.student_id.middle_name or '', b.student_id.last_name or '')
            })
            
        return data"""
        
        
"""class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        
        return json.JSONEncoder.default(self, obj)"""
        
        
"""class report_rpm(models.Model):
    _name = 'education_contract.rpm'
    
    user_id = fields.Char('Vendedor')
    date_start = fields.Char('Fecha inicio')
    date_end = fields.Char('Fecha fin')
    code = fields.Char('Code')"""