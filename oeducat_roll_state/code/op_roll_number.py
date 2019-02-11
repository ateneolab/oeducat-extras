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
from dateutil.relativedelta import relativedelta


class OpRollNumber(models.Model):
    _name = 'op.roll.number'
    _inherit = 'op.roll.number'

    # state = fields.Selection(
    #     [('active', u'Asistiendo'), ('inactive', u'Congelado'), ('done', u'Incorporado'), ('gone', u'Retirado'), ('relocated', u'Trasladado')],
    #     default='active', string=u'Estado')
    state = fields.Selection(
        [('active', u'Asistiendo'), ('inactive', u'Congelado'), ('done', u'Incorporado'), ('gone', u'Retirado'),
         ('relocated', u'Cambio de escuela'), ('bochanged', u'Cambio de sucursal'),
         ('bchange', u'Cambio de beneficiario')],
        default='active', string=u'Estado')
    date_state = fields.Datetime(u'Fecha de cambio de estado')
    is_active = fields.Boolean(u'Activo', default=True)
    previous_roll_number_id = fields.Many2one('op.roll.number', string=u'Matrícula anterior')
    next_roll_number_id = fields.Many2one('op.roll.number', string=u'Matrícula nueva')

    @api.onchange('freezing_ids')
    def _onchange_freezing_ids(self):
        if self.freezing_ids:
            today = datetime.datetime.today()
            for fi in self.freezing_ids:
                start_date = datetime.datetime.strptime(fi.start_date, '%Y-%m-%d')
                end_date = datetime.datetime.strptime(fi.end_date, '%Y-%m-%d')
                if today >= start_date and today < end_date:
                    self.frozen = True
                    self.state = 'inactive'
                    self.date_state = datetime.datetime.today()

    @api.multi
    def open_relocate_wizard(self):
        wizard_form = self.env.ref('oeducat_roll_state.view_wizard_relocate_student_form', False)
        view_id = self.env['op.wizard_relocate']
        new = view_id.create({})

        return {
            'name': "Trasladar estudiante",
            'type': 'ir.actions.act_window',
            'res_model': 'op.wizard_relocate',
            'res_id': new.id,
            'view_id': wizard_form.id,
            'view_mode': 'form',
            'view_type': 'form',
            'nodestroy': True,
            'target': 'new',
            'context': {'default_current_roll_number_id': self.id}
        }

    @api.model
    def update(self, data):
        id = data['id']
        # vals = data['vals']
        # print(id)
        # print(vals['roll_number'])
        rn = self.env['op.roll.number'].browse([id])
        # if rn:
        #     rn.write(vals)
        # print('ok')

        seq = self.env['ir.sequence'].search([('code', '=', 'seq.roll.number')])
        number = self.env['ir.sequence'].get(seq.code)
        rn.write({'roll_number': number})

        return True
