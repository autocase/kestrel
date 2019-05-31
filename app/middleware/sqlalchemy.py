class SQLAlchemySessionManager:
    """
    Close scoped session when the a request ends.
    """

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, "db"):
            resource.db.disconnect()
