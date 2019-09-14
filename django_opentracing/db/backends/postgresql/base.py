import django

from django_opentracing.db.common import DatabaseWrapperMixin

import psycopg2.extensions

if django.VERSION >= (1, 9):
    from django.db.backends.postgresql import base
else:
    from django.db.backends.postgresql_psycopg2 import base


class DatabaseFeatures(base.DatabaseFeatures):
    """Our database has the exact same features as the base one."""
    pass


class DatabaseWrapper(DatabaseWrapperMixin, base.DatabaseWrapper):
    pass
