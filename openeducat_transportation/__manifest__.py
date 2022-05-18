# -*- coding: utf-8 -*-
{
    'name': 'OpenEduCat Trasportation',
    'version': '14.0.1.0',
    'license': 'LGPL-3',
    'category': 'Trasportation',
    "sequence": 4,
    'summary': 'Manage Trasportation',
    'complexity': "easy",
    'author': 'Dharmesh Chudasama',
    'depends': ['openeducat_core','fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/transportation_view.xml',
        # 'views/facility_task_view.xml',
        # 'views/facility_line_view.xml',
        'menus/op_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
