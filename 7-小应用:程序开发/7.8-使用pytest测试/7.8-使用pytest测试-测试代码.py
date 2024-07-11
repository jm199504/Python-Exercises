import pytest
from solution import UserManager


def test_create_user():
    manager = UserManager()
    manager.create_user("alice", "password123")
    assert "alice" in manager.users
    assert manager.users["alice"]["password"] == "password123"
    assert manager.users["alice"]["email"] is None


def test_create_existing_user():
    manager = UserManager()
    manager.create_user("bob", "bobpass")
    with pytest.raises(ValueError):
        manager.create_user("bob", "newpass")


def test_authenticate_user():
    manager = UserManager()
    manager.create_user("charlie", "secret")
    assert manager.authenticate_user("charlie", "secret")
    assert not manager.authenticate_user("charlie", "wrongpass")
    assert not manager.authenticate_user("nonexistent", "anypass")


def test_update_user_email():
    manager = UserManager()
    manager.create_user("dave", "davepass")
    manager.update_user_email("dave", "dave@example.com")
    assert manager.get_user_email("dave") == "dave@example.com"


def test_update_nonexistent_user_email():
    manager = UserManager()
    with pytest.raises(ValueError):
        manager.update_user_email("nonexistent", "email@example.com")


def test_get_user_email():
    manager = UserManager()
    manager.create_user("eve", "evepass")
    manager.update_user_email("eve", "eve@example.com")
    assert manager.get_user_email("eve") == "eve@example.com"


def test_get_nonexistent_user_email():
    manager = UserManager()
    with pytest.raises(ValueError):
        manager.get_user_email("nonexistent")


def main():
    test_functions = [
        test_create_user,
        test_create_existing_user,
        test_authenticate_user,
        test_update_user_email,
        test_update_nonexistent_user_email,
        test_get_user_email,
        test_get_nonexistent_user_email
    ]

    for test_function in test_functions:
        try:
            test_function()
            print(f"{test_function.__name__} passed.")
        except AssertionError:
            print(f"{test_function.__name__} failed.")


if __name__ == "__main__":
    main()
