# -*- coding: utf-8 -*-
##############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2017-Today Trey, Kilobytes de Soluciones <www.trey.es>
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
##############################################################################
{
    'name': 'Sale cost simulator',
    'summary': 'Sale cost simulator',
    'description': 'Sale cost simulator',
    'author': 'Trey Kilobytes de Soluciones (www.trey.es)',
    'website': 'https://www.trey.es',
    'category': 'Sale',
    'version': '8.0.0.1.0',
    'depends': [
        'print_formats_base',
        'sale',
        'mail',
        'web_one2many_list_action'
    ],
    'data': [
        'wizards/import_line.xml',
        'wizards/apply_pricelist.xml',
        'views/sale_cost_line.xml',
        'views/sale_cost_simulator.xml',
        'views/menu.xml',
        'report/report_sale_cost_simulation.xml',
        'security/ir.model.access.csv',
        'security/multicompany.xml',
    ],
    'installable': True,
}
