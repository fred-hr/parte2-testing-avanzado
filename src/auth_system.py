def authenticate_user(username, password, role, device, network):
    """
    Simula un sistema sencillo de autenticación.
    """

    valid_users = {
        "admin": {
            "password": "Admin123",
            "role": "admin"
        },
        "student": {
            "password": "Student123",
            "role": "student"
        },
        "guest": {
            "password": "Guest123",
            "role": "guest"
        }
    }

    # Verificar que no existan campos vacíos
    if not username or not password:
        return {
            "success": False,
            "message": "Credenciales incompletas"
        }

    # Verificar si el usuario existe
    if username not in valid_users:
        return {
            "success": False,
            "message": "Usuario no encontrado"
        }

    # Verificar contraseña
    if valid_users[username]["password"] != password:
        return {
            "success": False,
            "message": "Contraseña incorrecta"
        }

    # Verificar rol
    if valid_users[username]["role"] != role:
        return {
            "success": False,
            "message": "Rol incorrecto"
        }

    # Advertencia por dispositivo desconocido o red pública
    if device == "unknown" or network == "public":
        return {
            "success": True,
            "message": "Acceso permitido con advertencia"
        }

    # Acceso correcto
    return {
        "success": True,
        "message": "Acceso permitido"
    }
