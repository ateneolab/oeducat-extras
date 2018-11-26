# -*- coding: utf-8 -*-

import datetime
import logging

from openerp import models, fields, api, _

_logger = logging.getLogger(__name__)


class WizardInvoice(models.TransientModel):
    _name = 'op.wizard_relocate'

    current_roll_number_id = fields.Many2one('op.roll.number')
    # next_roll_number_id = fields.Many2one('op.roll.number')

    roll_number = fields.Char('Roll Number', size=8, required=True)
    course_id = fields.Many2one('op.course', 'Course', required=True)
    batch_id = fields.Many2one('op.batch', 'Batch', required=True)
    standard_id = fields.Many2one('op.standard', 'Standard', required=True)
    division_id = fields.Many2one('op.division', 'Division')
    # student_id = fields.Many2one('op.student', 'Student', required=True)
    operating_unit_id = fields.Many2one('operating.unit', string=_(u'Branch Office'),
                                        related='division_id.operating_unit_id', store=True)

    @api.multi
    def relocate_student(self):
        # self.ensure_one()

        new_data = {
            'roll_number': self.roll_number,
            'course_id': self.course_id.id,
            'batch_id': self.batch_id.id,
            'standard_id': self.standard_id.id,
            'division_id': self.division_id.id,
            'operating_unit_id': self.operating_unit_id.id,
            'previous_roll_number_id': self.current_roll_number_id.id,
            'student_id': self.current_roll_number_id.student_id.id,
            'is_active': True
        }

        res = self.env['op.roll.number'].create(new_data)

        if res:
            self.current_roll_number_id.write({'is_active': False, 'state': 'relocated'})
