import database


def test_password_history(tmp_path, monkeypatch):
    test_db = tmp_path / "test_password_history.db"
    monkeypatch.setattr(database, "DB_PATH", test_db)

    database.init_db()

    password = "TestPassword!123"
    other_password = "DifferentPassword!456"

    assert database.password_was_used(password) is False

    database.hash_password(password)

    assert database.password_was_used(password) is True
    assert database.password_was_used(other_password) is False


def test_password_is_not_stored_as_plaintext(tmp_path, monkeypatch):
    test_db = tmp_path / "test_hash.db"
    monkeypatch.setattr(database, "DB_PATH", test_db)

    database.init_db()

    password = "SecretPassword!123"
    database.hash_password(password)

    with database.get_connection() as conn:
        stored_hash = conn.execute(
            "SELECT password_hash FROM password_history LIMIT 1"
        ).fetchone()[0]

    assert password.encode("utf-8") != stored_hash
    assert stored_hash.startswith(b"$2")
