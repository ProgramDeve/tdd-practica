# TDD Práctica — FizzBuzz y Validador de Contraseñas

## ¿Qué es TDD?

TDD (Test-Driven Development) es una técnica donde **se escribe el test ANTES del código de producción**. Sigue el ciclo **Red → Green → Refactor**:

- **Red**: Escribir un test que falla (el código aún no existe).
- **Green**: Escribir el código mínimo necesario para que el test pase.
- **Refactor**: Mejorar la estructura del código sin cambiar su comportamiento.

## Proceso aplicado

### FizzBuzz (5 ciclos)
1. Números normales.
2. Fizz (múltiplos de 3).
3. Buzz (múltiplos de 5).
4. FizzBuzz (múltiplos de 15).
5. Refactor con `subTest`.

### Validador de contraseñas (6 ciclos)
1. Longitud mínima (8 caracteres).
2. Al menos una mayúscula.
3. Al menos una minúscula.
4. Al menos un dígito.
5. Al menos un carácter especial.
6. Refactor + tests integrales con `subTest`.

## Ejecutar los tests
```bash
python -m unittest discover