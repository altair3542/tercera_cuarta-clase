# Encapsulamiento y abstraccion

# Explicar el concepto de encapsulación y por qué es clave proteger los atributos internos de una clase.

# Usar convenciones de Python (_ y __) para declarar atributos “protegidos” o “privados”.

# Implementar propiedades (@property y @X.setter) para controlar el acceso y validación de atributos.

# Definir abstracción, distinguiendo qué detalles ocultar y qué interfaz pública ofrecer.

# Aplicar ejemplos prácticos que muestren cómo un objeto puede simplificar su uso escondiendo su complejidad interna.


# Encapsulación
# Definición: Mecanismo que restringe el acceso directo a ciertos componentes de un objeto, obligando a pasar por métodos controlados.

# Convenciones en Python:

# _atributo: convención de “protegido” (interno, pero no estrictamente inaccesible).

# __atributo: nombre “mangleado” para simular privacidad real, evitando colisiones en subclases.

# 3.2 Propiedades en Python
# @property: convierte un método en atributo de solo lectura, permitiendo calcular o validar antes de devolver un valor.

# @X.setter: define un método que se ejecuta al asignar a la propiedad, ofreciendo validación y lógica adicional.


# 3.3 Abstracción
# Definición: Seleccionar y exponer solo aquello que el usuario del objeto necesita, escondiendo detalles de implementación.

# Beneficios:

# Interfaces claras y fáciles de usar.

# Posibilidad de cambiar la implementación interna sin afectar a quien usa la clase.
