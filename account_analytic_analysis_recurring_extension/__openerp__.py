# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2014-Today Trey, Kilobytes de Soluciones <www.trey.es>
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

{
    "name": "Trey Account Analytic Contract",
    'version': '8.0.0.1',
    'category': 'Accounting',
    'sequence': 14,
    'summary': 'Trey customize contract',
    'description': """
Account Analytic Contract Todo
=========================================
* On creating invoice fill "reference" with contract name
* On creating invoice compute tax for total
* On creating invoice take only tax of contract company
* Use #MONTH_INT#, #MONTH_STR# and #YEAR_INT# in the contract line to
automatically insert the dates of the invoiced
    """,
    'author': 'Trey Kilobytes de Soluciones (www.trey.es)',
    'website': 'https://www.trey.es',
    'depends': [
        'account_analytic_analysis',
    ],
    'data': [
        'views/account_analytic_analysis_view.xml'
    ],
    'demo': [
    ],
    'test': [
    ],
    'images': [
    ],

    'installable': True,
}
