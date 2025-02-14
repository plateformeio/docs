from plateforme import Plateforme

# Create application
app = Plateforme(
    debug=True,  # (1)!
    logging={'level': 'DEBUG'},  # (2)!
    database_engines='plateforme.db',  # (3)!
    namespaces=[  # (4)!
        ('assets', {'alias': ''}),
        ('staff', {'alias': ''}),
    ],
    packages=[  # (5)!
        'packages.assets',
        'packages.ops',
        'packages.staff',
    ],
)
