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


# class Partner(models.Model):
#     _name = 'education_contract.beneficiary'
#     _inherit = 'education_contract.beneficiary'
#
#     display_name = fields.Char(string='Nombre', compute='_compute_display_name', )
#
#     @api.one
#     @api.depends('student_id', 'partner_id')
#     def _compute_display_name(self):
#         names = [self.student_id.name, self.student_id.last_name or '']
#         self.display_name = ' '.join(filter(None, names))


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def default_get(self, cr, uid, fields, context=None):
        res = super(Partner, self).default_get(cr, uid, fields, context=context)
        if 'contract_id' in context:
            contract_id = self.pool.get('education_contract.contract').browse(cr, uid,
                                                                              [context.get('contract_id')],
                                                                              context=context)
            if contract_id:
                owner = contract_id.owner
                try:
                    res['street'] = owner.street
                    res['street2'] = owner.street2
                    res['property_account_position'] = owner.property_account_position.id
                    res['mobile'] = owner.mobile
                    res['student_email'] = owner.email
                except:
                    print('nou nou nou...')
        return res

    @api.one
    @api.depends('firstname', 'secondname', 'lastname', 'secondlastname', 'name', 'is_company')
    def _compute_full_name(self):
        names = []
        if not self.is_company:
            if self.firstname not in [None, '', False]:
                names.append(self.firstname)
            if self.secondname not in [None, '', False]:
                names.append(self.secondname)
            if self.lastname not in [None, '', False]:
                names.append(self.lastname)
            if self.secondlastname not in [None, '', False]:
                names.append(self.secondlastname)
            if len(names) == 0:
                names = [self.name]
        else:
            names = [self.name or '']
        full_name = ' '.join(filter(None, names))
        self.full_name = full_name
        self.name = full_name

        if self.full_name is False or self.full_name is None or self.full_name == '':
            print('ok')

        return full_name
