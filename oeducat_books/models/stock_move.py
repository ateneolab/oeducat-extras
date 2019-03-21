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

from openerp import models, fields, api, _


class StockMove(models.Model):
    _name = 'stock.move'
    _inherit = 'stock.move'

    def default_get(self, cr, uid, fields, context=None):
        res = super(StockMove, self).default_get(cr, uid, fields, context=context)
        stock_picking_type_id = self.pool.get('stock.picking.type').search(cr, uid,
                                                                           [('name', '=', 'Delivery Orders'),
                                                                            ('code', '=', 'outgoing')])[:1]
        if stock_picking_type_id is not None and len(stock_picking_type_id):
            stock_picking_type_obj = self.pool.get('stock.picking.type').browse(cr, uid, stock_picking_type_id)[:1]

            if stock_picking_type_obj is not None and len(stock_picking_type_obj):
                default_location_src_id = stock_picking_type_obj[0].default_location_src_id
                default_location_dest_id = stock_picking_type_obj[0].default_location_dest_id

                res['picking_type_id'] = stock_picking_type_obj[0].id
                res['location_id'] = default_location_src_id.id
                res['location_dest_id'] = default_location_dest_id.id

        return res
