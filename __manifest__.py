{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage your library books and members',
    'description': """
        This module allows you to manage books, members, and book loans in your library.
    """,
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'category': 'Services/Library',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_member_views.xml',
        'views/library_loan_views.xml',
         'data/library_cron.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}