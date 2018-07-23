# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields, api
import datetime


class RollNumber(models.Model):
    _name = 'op.roll.number'
    _inherit = 'op.roll.number'

    @api.one
    def is_contract_payment_up_to_date(self):
        collection_plan_id = self.env['collection_plan.collection_plan'].search(
            [('contract_id', '=', self.contract_id.id)])[:1]
        payment_term_ids = self.env['education_contract.payment_term'].search(
            [('collection_plan_id', '=', collection_plan_id.id), ('planned_date', '<', datetime.datetime.today()),
             ('account_voucher_id', 'in', [False, None])])
        if len(payment_term_ids) > 0:
            return False
        return True


class OpAttendanceSheet(models.Model):
    _name = 'op.attendance.sheet'
    _inherit = 'op.attendance.sheet'

    @api.one
    @api.onchange('register_id', 'register_id.division_id')
    def _compute_attendance_line(self):
        if self.register_id and self.register_id.division_id:
            roll_number_ids = self.env['op.roll.number'].search([('division_id', '=', self.register_id.division_id.id),
                                                                 ('state', '=',
                                                                  'active')])  # falta filtrar por activa (fecha fin no establecida)
            data_lines = []
            datas = []

            for rn in roll_number_ids:
                data_lines.append((0, 0, {
                    'attendance_id': self.id,
                    'student_id': rn.student_id.id,
                    'present': False,
                    'course_id': rn.course_id.id,
                    'standard_id': rn.standard_id.id,
                    'division_id': rn.division_id.id,
                    'attendance_date': self.attendance_date,
                    'contract_payment_up_to_date': rn.is_contract_payment_up_to_date(),
                }))
                datas.append({
                    'attendance_id': self.id,
                    'student_id': rn.student_id.id,
                    'present': False,
                    'course_id': rn.course_id.id,
                    'standard_id': rn.standard_id.id,
                    'division_id': rn.division_id.id,
                    'attendance_date': self.attendance_date,
                })

            self.attendance_line = data_lines

    attendance_line = fields.One2many(
        'op.attendance.line', 'attendance_id', 'Attendance Line',
        required=True)
