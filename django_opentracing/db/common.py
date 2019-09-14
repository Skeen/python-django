from dbapi_opentracing import ConnectionTracing
import opentracing


class DatabaseWrapperMixin(object):
    """Extends the DatabaseWrapper to count connections and cursors."""

    def get_new_connection(self, *args, **kwargs):
        new_connection = super(DatabaseWrapperMixin, self).get_new_connection(
            *args, **kwargs
        )
        self.tracing = ConnectionTracing(new_connection)
        return new_connection

    def create_cursor(self, name=None):
        return self.tracing.cursor(self.CURSOR_CLASS, self.alias, self.vendor)
