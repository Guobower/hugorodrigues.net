{
    'name': 'Hugo Rodrigues Install',
    'version': '10.0.0.1',
    'description': """
Dummy module to install all hugorodrigues.net modules
""",
    'author': 'Hugo Rodrigues',
    'website': 'https://hugorodrigues.net',
    'license': 'Other OSI approved licence',
    'depends': [
        'base',
        'hugorodrigues_website',
        'hugorodrigues_theme',
        'disable_odoo_online',
        'base_user_gravatar',
        'note_extended',
        'calendar',
        'url_shorter',
        'letsencrypt',
    ],
    'installable': True,
    'active': True,
    'auto_install': False
}
