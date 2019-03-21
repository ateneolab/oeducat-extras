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


class Student(models.Model):
    _name = 'op.student'
    _inherit = 'op.student'

    @api.one
    @api.depends('name', 'middle_name', 'last_name', 'partner_id')
    def _compute_display_name(self):
        names = [self.name, self.middle_name or '', self.last_name, self.secondlastname or '']
        display_name = ' '.join(filter(None, names))
        self.display_name = display_name

        if self.partner_id.full_name is False or self.partner_id.full_name is None or self.partner_id.full_name == '':
            print(self.name)
            print(self.middle_name)
            print(self.last_name)

    contract_ids = fields.Many2many('education_contract.contract', string='Contratos')
    display_name = fields.Char(string='Nombre', compute='_compute_display_name')
    partner_id = fields.Many2one('res.partner', 'Partner', ondelete="cascade")
    student_email = fields.Char(string=u'Correo electrónico')
    last_name = fields.Char(related='partner_id.lastname')
    middle_name = fields.Char(related='partner_id.secondname')
    name = fields.Char(related='partner_id.firstname')

    @api.depends('roll_number_line', 'roll_number_line.roll_number',
                 'roll_number_line.student_id', 'roll_number_line.standard_id',
                 'roll_number_line.standard_id.sequence')
    def _get_curr_roll_number(self):
        for student in self:
            roll_no = 0
            seq = 0
            for roll_number in student.roll_number_line:
                if roll_number.standard_id.sequence > seq:
                    roll_no = roll_number.roll_number
                    seq = roll_number.standard_id.sequence
            student.roll_number = roll_no

    @api.model
    def create(self, vals):
        if 'birth_date' in vals:
            vals.update({'birthdate_date': vals.get('birth_date')})
        if 'gender' in vals:
            vals.update({'sex': str(vals.get('gender')).upper()})
        res = super(Student, self).create(vals)
        if 'student_email' in vals:
            res.partner_id.write({'email': vals.get('student_email')})
        return res
