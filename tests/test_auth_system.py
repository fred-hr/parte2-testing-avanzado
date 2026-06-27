from src.auth_system import authenticate_user


def test_authentication_success():
    result = authenticate_user("admin", "Admin123", "admin", "known", "private")
    assert result["success"] is True
    assert result["message"] == "Acceso permitido"


def test_authentication_incomplete_credentials():
    result = authenticate_user("", "", "admin", "known", "private")
    assert result["success"] is False
    assert result["message"] == "Credenciales incompletas"


def test_authentication_user_not_found():
    result = authenticate_user("unknown", "Admin123", "admin", "known", "private")
    assert result["success"] is False
    assert result["message"] == "Usuario no encontrado"


def test_authentication_invalid_password():
    result = authenticate_user("admin", "wrong", "admin", "known", "private")
    assert result["success"] is False
    assert result["message"] == "Contraseña incorrecta"


def test_authentication_invalid_role():
    result = authenticate_user("admin", "Admin123", "student", "known", "private")
    assert result["success"] is False
    assert result["message"] == "Rol incorrecto"


def test_authentication_access_with_warning():
    result = authenticate_user("admin", "Admin123", "admin", "unknown", "public")
    assert result["success"] is True
    assert result["message"] == "Acceso permitido con advertencia"
