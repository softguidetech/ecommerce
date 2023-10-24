# -*- coding: utf-8 -*-
{
    'name': "e-commerce sgt",

    'summary': """Shopping
    """,

    'description': """
    """,

    'author': "Jamsheena kc",
    'website': "http://www.sgt.com",

    'category': 'e-commerce',
    'assets': {
        'web.assets_frontend': [
            'ecommerce_sgt/static/scss/styles.scss',
        ]
    },
    'version': '0.1',

    'depends': ['base', 'portal', 'web', 'website', 'website_sale', 'website_blog'],
    'demo': [
        'demo/demo.xml',
    ],
    'data': [
        'views/header.xml',
        'views/footer.xml',
        'views/home.xml',
        'views/home_page.xml',
        'views/add_to_cart.xml',
    ],
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3'
}
