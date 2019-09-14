from dbapi_opentracing import ConnectionTracing, Cursor
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
        cursor = super(DatabaseWrapperMixin, self).create_cursor(name)
        return Cursor(cursor, self.tracing._self_tracer, self.tracing._self_span_tags,
                      trace_execute=False, trace_executemany=False)
