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


class OpStudent(models.Model):
    _name = 'op.student'
    _inherit = 'op.student'
    
    """@api.one
    @api.depends('roll_number_line')
    def _compute_divisions(self):
        div_ids = []
        for rn in self.roll_number_line:
            div_ids.append(rn.division_id.id)
        self.division_ids = [(6, 0, div_ids)]"""
        
    @api.one
    @api.depends('roll_number_line')
    def _compute_operating_units(self):
        div_ids = []
        op_ids = []
        for rn in self.roll_number_line:
            div_ids.append(rn.division_id)
            
        for div in div_ids:
            if div.operating_unit_id:
                op_ids.append(div.operating_unit_id.id)
        
        self.operating_unit_ids = [(6, 0, op_ids)]
    
    """division_ids = fields.Many2many('op.division', compute='_compute_divisions')"""
    operating_unit_ids = fields.Many2many('operating.unit', compute='_compute_operating_units', store=True)