{
    'name': "Era Dyn Periods",
    'version': '15.0.0',
    'author': 'Era',
    'summary': """Era Accounting Dynamic Report Periods""",
    'description': "Era Accounting Dynamic Report Periods",
    "category": "Account",
    'depends': ['account_dynamic_reports'],
    'data': [
        'views/account_move_view.xml',
    ],
    'assets': {
        'web.assets_backend': [          
            'era_dyn_periods/static/src/scss/dynamic_common_style.scss',    
        ],
            'web.assets_qweb': [
                'era_dyn_periods/static/src/xml/partner_ageing_view.xml',],},
    'application': False,
    'installable': True,
    'price': 15,
    'currency': 'EUR',
    "images": ['static/description/banner.jpg'],
    'live_test_url': 'https://preciseways.com',
    'license': 'OPL-1',
}

