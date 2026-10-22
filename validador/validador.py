def validar_password(pwd):
    errores = []
    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")
    return {"valida": len(errores) == 0, "errores": errores}

def validar_password(pwd):
    errores = []
    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")
    if not any(c.isupper() for c in pwd):
        errores.append("Al menos una mayúscula")
    return {"valida": len(errores) == 0, "errores": errores}

def validar_password(pwd):
    errores = []
    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")
    if not any(c.isupper() for c in pwd):
        errores.append("Al menos una mayúscula")
    if not any(c.islower() for c in pwd):
        errores.append("Al menos una minúscula")
    return {"valida": len(errores) == 0, "errores": errores}

def validar_password(pwd):
    errores = []
    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")
    if not any(c.isupper() for c in pwd):
        errores.append("Al menos una mayúscula")
    if not any(c.islower() for c in pwd):
        errores.append("Al menos una minúscula")
    if not any(c.isdigit() for c in pwd):
        errores.append("Al menos un dígito")
    return {"valida": len(errores) == 0, "errores": errores}

def validar_password(pwd):
    errores = []
    if len(pwd) < 8:
        errores.append("Mínimo 8 caracteres")
    if not any(c.isupper() for c in pwd):
        errores.append("Al menos una mayúscula")
    if not any(c.islower() for c in pwd):
        errores.append("Al menos una minúscula")
    if not any(c.isdigit() for c in pwd):
        errores.append("Al menos un dígito")
    if not any(c in "!@#$%^&*" for c in pwd):
        errores.append("Al menos un carácter especial")
    return {"valida": len(errores) == 0, "errores": errores}

    def test_password_valida_completa(self):
        res = validar_password("Segura1!abc")
        self.assertTrue(res["valida"])
        self.assertEqual(res["errores"], [])

    def test_multiples_errores(self):
        res = validar_password("abc")
        self.assertFalse(res["valida"])
        self.assertTrue(len(res["errores"]) >= 3)

    def test_varios_passwords_con_subTest(self):
        casos = [
            ("Abc1!xyz", True),
            ("abc", False),
            ("ABCDEFGH", False),
            ("Abcdefgh1!", True),
        ]
        for pwd, esperado in casos:
            with self.subTest(pwd=pwd):
                res = validar_password(pwd)
                self.assertEqual(res["valida"], esperado)