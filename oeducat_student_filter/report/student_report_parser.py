# -*- coding: iso-8859-1 -*-=

from openerp.report import report_sxw
from openerp import api, models
from openerp.osv import osv

class StudentReportPartser(report_sxw.rml_parse):
    
    def __init__(self, cr, uid, name, context=None):
        
        super(StudentReportPartser, self).__init__(cr, uid, name, context=context)
        
        wizard_pool = self.pool.get('openeducat_erp.student_wizard')
        wizard_obj = wizard_pool.browse(self.cr, self.uid, self.localcontext.get('active_id'))
        division_ids = wizard_obj.division_ids
        
        """roll_lines = self._get_roll_lines(division_ids, wizard_obj)"""
        
        self.localcontext.update({
            'get_roll_numbers': self._get_roll_numbers,
        })
        
    def _get_roll_numbers(self, division):
        if division:
            wizard_pool = self.pool.get('openeducat_erp.student_wizard')
            wizard_obj = wizard_pool.browse(self.cr, self.uid, self.localcontext.get('active_id'))
            
            domain = [('division_id', '=', division.id)]
            if wizard_obj.batch_id:
                domain.append(('batch_id', '=', wizard_obj.batch_id.id))
            if wizard_obj.standard_id:
                domain.append(('standard_id', '=', wizard_obj.standard_id.id))
            if wizard_obj.course_id:
                domain.append(('course_id', '=', wizard_obj.course_id.id))
            roll_numbers = self.pool.get('op.roll.number').search(self.cr, self.uid, domain)
            roll_numbers = self.pool.get('op.roll.number').browse(self.cr, self.uid, roll_numbers)
            
            return roll_numbers
        
        return False
    
    
    def _get_roll_lines(self, divs, wiz):
        divisions = [(x.id, x.name) for x in divs]
        
        div_data = []
        
        for div, name in divisions:
            domain = [('division_id', '=', div)]
            if wiz.batch_id:
                domain.append(('batch_id', '=', wiz.batch_id.id))
            if wiz.standard_id:
                domain.append(('standard_id', '=', wiz.standard_id.id))
            if wiz.course_id:
                domain.append(('course_id', '=', wiz.course_id.id))
            roll_numbers = self.pool.get('op.roll.number').search(self.cr, self.uid, domain)
            roll_numbers = self.pool.get('op.roll.number').browse(self.cr, self.uid, roll_numbers)
            
            roll_data = []
            for rd in roll_numbers:
                roll_data.append({
                    'roll_number': rd.roll_number,
                    'student': '%s %s' % (rd.student_id.middle_name, rd.student_id.last_name),
                    'course_id': rd.course_id.name,
                    'batch_id': rd.batch_id.name,
                    'standard_id': rd.standard_id.name
                })
            
            div_data.append({
                'data': roll_data,
                'name': name
            })
            
        import pdb
        pdb.set_trace()
        return div_data
        

class report_rpm_parser(osv.AbstractModel):
    
    _name = 'report.oeducat_student_filter.report_students'
    _inherit = 'report.abstract_report'
    _template = 'oeducat_student_filter.report_students'
    _wrapped_report_class = StudentReportPartser
    
