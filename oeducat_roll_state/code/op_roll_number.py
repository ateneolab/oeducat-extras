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

    state = fields.Selection(
        [('active', u'Asistiendo'), ('inactive', u'Congelado'), ('done', u'Incorporado'), ('gone', u'Retirado')],
        default='active', string=u'Estado')
    date_state = fields.Datetime(u'Fecha de cambio de estado')

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


