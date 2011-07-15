ATP_DISABLE = False
ATP_UDP_IP = "85.222.100.189"
ATP_UDP_PORT = 8888
ATP_API_KEY = "HEROKU_1"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'atp_performance_test',  # Or path to database file if using sqlite3.
        'USER': 'atp_performance_test',                      # Not used with sqlite3.
        'PASSWORD': 'atp_performance_test',                  # Not used with sqlite3.
        'HOST': 'ec2-184-73-142-75.compute-1.amazonaws.com',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '5433',                     # Default pgpool
        'PORT': '5432',                     # Default PostgreSQL
#        'PORT': '6432',                      # Default pgBouncer
#        'OPTIONS': {
#            'autocommit': True,			 # Uncomment if on PostgreSQL 9.0, even more performance boost! Beware, it will not wrap every request in transaction by default.
#        }
    }
}
