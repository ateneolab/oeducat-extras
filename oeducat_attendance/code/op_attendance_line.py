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


class OpAttendanceLine(models.Model):
    _name = 'op.attendance.line'
    _inherit = 'op.attendance.line'

    contract_payment_up_to_date = fields.Boolean(u'Al día con los pagos')
    attendance_id = fields.Many2one('op.attendance.sheet', 'Hoja de asistencia', required=True)
    course_id = fields.Many2one('op.course', 'Curso', related='attendance_id.register_id.course_id', store=False,
                                readonly=True)
    standard_id = fields.Many2one('op.standard', u'Módulo', related='attendance_id.register_id.standard_id',
                                  store=False, readonly=True)
    division_id = fields.Many2one('op.division', 'Grupo', related='attendance_id.register_id.division_id', store=False,
                                  readonly=True)


class OpAttendanceSheet(models.Model):
    _inherit = 'op.attendance.sheet'
    _rec_name = 'name'


class OpStudent(models.Model):
    _inherit = 'op.student'

    attendance_ids = fields.One2many('op.attendance.line', 'student_id', 'Asistencias')
