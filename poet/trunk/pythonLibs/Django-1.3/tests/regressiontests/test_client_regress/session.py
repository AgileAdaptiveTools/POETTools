from django.contrib.sessions.backends.base import SessionBase

class SessionStore(SessionBase):
    """
    A simple cookie-based session storage implemenation.

    The session key is actually the session data, pickled and encoded.
    This means that saving the session will change the session key.
    """
    def __init__(self, session_key=None):
        super(SessionStore, self).__init__(session_key)

    def exists(self, session_key):
        return False

    def create(self):
        self.session_key = self.encode({})

    def save(self, must_create=False):
        self.session_key = self.encode(self._session)

    def delete(self, session_key=None):
        self.session_key = self.encode({})

    def load(self):
        try:
            return self.decode(self.session_key)
        except:
            self.modified = True
            return {}