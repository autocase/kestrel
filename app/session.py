from contextlib import contextmanager


@contextmanager
def session_scope(session=None):
    """Provide a transactional scope around a series of operations."""\

    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
