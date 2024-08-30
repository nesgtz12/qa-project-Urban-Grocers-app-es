# Proyecto Urban Grocers
Hola buenas tardes auditor, en esta se esta comprobando el funcionamiento del formulario para la creación de un usuario/a.
Mi nombre es Nestor Gutierrez y pertenezco al grupo 12.
Antes de iniciar es necesario instala los siguientes programa (paquetes) para que funcione el código: -Pytes   - Coverage

# Herramientas tecnológicas utilizadas:
En este caso utilice mucho con chatgpt para realizar consultas para la corrección de cierta partes del código y como optimizarlo de una manera mas "limpia".

# Entorno de pruebas:
 Pycharm 2024.1.4 Python versión 3.12.4 Pytest 8.3.2, Coverage 7.6.1

# Pruebas para el parámetro firstName al crear un/a usuario/a en []
- Necesitas tener instalados los siguientes paquetes pytest y request para ejecutar las pruebas.
- Ejecuta todas las pruebas con el comando pytest.
Este proyecto contiene pruebas para la API de Urban Grocers, específicamente para la creación de kits.

### Pasos a seguir
- Instalación

1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Actualizar la URL

- Ejecución de Pruebas

Para ejecutar las pruebas, utiliza el siguiente comando:

```bash
pytest create_kit_name_kit_test.py

#Pruebas a realizar
Prueba 1. Numero permitido de caracteres (1):kit_body = { "name": "a"}
Prueba 2. Numero permitido de caracteres (511):kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
Prueba 3. Numero de caracteres debe ser inferior que la cantidad permitida(0): kit_body = { "name": "" }
Prueba 4. Numero de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
Prueba 5. Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
Prueba 6. Se permiten espacios:  kit_body = { "name": " A Aaa " }
Prueba 7. Se permiten números:  kit_body = { "name": "123" }
Prueba 8. El parámetro no se pasa en la solicitud: kit_body = { }
Prueba 9. Se ha pasado un tipo de parámetro diferente (numero): kit_body = { "name": 123 }


