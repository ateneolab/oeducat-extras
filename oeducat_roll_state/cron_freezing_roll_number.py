# -*- coding: utf-8 -*-
##############################################################################
#
#    E-Invoice Module - Ecuador
#    Copyright (C) 2014 VIRTUALSAMI CIA. LTDA. All Rights Reserved
#    alcides@virtualsami.com.ec
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api
import datetime


class CronFreezingRollNumber(models.Model):
    _name = 'oeducat.cron.freezing.state'

    def update_freezing_state(self, cr, uid, context=None):
        roll_number_ids = self.pool.get('op.roll.number').search(cr, uid, [('state', 'in', ['active', 'inactive'])],
                                                                 context=context)
        roll_number_obj = self.pool.get('op.roll.number').browse(cr, uid, roll_number_ids, context=context)
        for rn in roll_number_obj:
            if rn.freezing_ids:
                today = datetime.datetime.today()
                if rn.state == 'active':
                    for fi in rn.freezing_ids:
                        start_date = datetime.datetime.strptime(fi.start_date, '%Y-%m-%d')
                        end_date = datetime.datetime.strptime(fi.end_date, '%Y-%m-%d')
                        if today >= start_date and today < end_date:
                            self.pool.get('op.roll.number').write(cr, uid, [rn.id],
                                                                  {'frozen': True, 'state': 'inactive'})
                elif rn.state == 'inactive':
                    for fi in rn.freezing_ids:
                        start_date = datetime.strptime(fi.start_date, '%Y-%m-%d')
                        end_date = datetime.strptime(fi.end_date, '%Y-%m-%d')
                        if today < start_date and today >= end_date:
                            change_state = True
                        else:
                            change_state = False
                    if change_state:
                        rn.state = 'active'
