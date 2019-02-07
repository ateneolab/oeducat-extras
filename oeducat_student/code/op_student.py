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
        names = [self.partner_id.name]
        self.display_name = ' / '.join(filter(None, names))

        # if (not self.name or not self.middle_name or not self.last_name) and self.partner_id:
        #     self.name = self.partner_id.firstname
        #     if self.partner_id.lastname:
        #         lastnames = self.partner_id.lastname.split(' ')
        #         if len(lastnames) > 0:
        #             self.middle_name = lastnames[0]
        #         if len(lastnames) > 1:
        #             self.last_name = lastnames[1]

    contract_ids = fields.Many2many('education_contract.contract', string='Contratos')
    display_name = fields.Char(string='Nombre', compute='_compute_display_name', )
    partner_id = fields.Many2one('res.partner', 'Partner', ondelete="cascade")

    # name = fields.Char(related='partner_id.firstname')
    # last_name = fields.Char(compute='_compute_names')
    # middle_name = fields.Char(compute='_compute_names')

    # @api.one
    # @api.depends('partner_id')
    # def _compute_names(self):
    #     if self.partner_id is not None:
    #         if self.partner_id.firstname:
    #             self.name = self.partner_id.firstname
    #         if self.partner_id.lastname:
    #             lastnames = self.partner_id.lastname.split(' ')
    #             if len(lastnames) > 0:
    #                 self.middle_name = lastnames[0]
    #             if len(lastnames) > 1:
    #                 self.last_name = lastnames[1]

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
