from datetime import datetime, timedelta

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        session_id = self._generate_session_id(user_id)
        self.sessions[session_id] = {
            'user_id': user_id,
            'created_at': datetime.utcnow(),
            'expires_at': datetime.utcnow() + timedelta(hours=1)
        }
        return session_id

    def _generate_session_id(self, user_id):
        return f'session_{user_id}_{int(datetime.utcnow().timestamp())}'

    def get_session(self, session_id):
        return self.sessions.get(session_id)

    def is_session_valid(self, session_id):
        session = self.sessions.get(session_id)
        if session:
            return datetime.utcnow() < session['expires_at']
        return False

    def delete_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def cleanup_sessions(self):
        expired_sessions = [session_id for session_id, session in self.sessions.items() if datetime.utcnow() >= session['expires_at']]
        for session_id in expired_sessions:
            self.delete_session(session_id)
