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


class OpExam(models.Model):
    _name = 'op.exam'
    _inherit = 'op.exam'

    @api.one
    @api.onchange('division_id')
    def _compute_attendance_line(self):
        if self.division_id:
            roll_number_ids = self.env['op.roll.number'].search(
                [('division_id', '=', self.division_id.id), ('state', '=', 'active')])  # filtrar por activo
            data_lines = []

            for rn in roll_number_ids:
                data_lines.append((0, 0, {
                    'student_id': rn.student_id.id,
                    'exam_id': self._context.get('active_id', False),
                    'status': 'a'
                }))

            self.attendees_line = data_lines

    attendees_line = fields.One2many(
        'op.exam.attendees', 'exam_id', 'Attendees', required=True)
    # attendance_line = fields.One2many(
    #    'op.attendance.line', 'attendance_id', 'Attendance Line',
    #    required=True)


class OpStudent(models.Model):
    _inherit = 'op.student'

    exam_attendance_ids = fields.One2many('op.exam.attendees', 'student_id', u'Exámenes')
