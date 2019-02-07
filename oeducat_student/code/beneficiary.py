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
from lxml import etree
from openerp import models, fields, api


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    @api.multi
    def load_contract_owner_data(self):
        print('okokok')

    def default_get(self, cr, uid, fields, context=None):
        res = super(Partner, self).default_get(cr, uid, fields, context=context)
        if 'contract_id' in context:
            contract_id = self.pool.get('education_contract.contract').browse(cr, uid,
                                                                              [context.get('contract_id')],
                                                                              context=context)
            if contract_id:
                owner = contract_id.owner
                try:
                    res['street'] = 'la calle'
                    res['street2'] = 'la calle 2'
                    res['property_account_position'] = owner.property_account_position.id
                    res['mobile'] = owner.mobile
                    res['email'] = owner.email
                except:
                    print('nou nou nou...')
        return res
