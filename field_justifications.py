"""
Field Type Justifications - Quiz Application

Model: Exam
"""

# EXAM MODEL JUSTIFICATIONS

"""
1. title = CharField(max_length=200)
   Justification: Se usa CharField porque el título del examen es un texto corto
   de longitud limitada. CharField está optimizado para textos de tamaño conocido
   y max_length=200 es suficiente para un título descriptivo. CharField requiere
   índice de base de datos por defecto y garantiza que el texto no exceda 200
   caracteres, previniendo datos inválidos.

2. description = TextField()
   Justification: TextField se usa porque la descripción puede ser extensa y no
   tiene un límite predecible de caracteres. TextField no seIndexa automáticamente
   y está diseñado para contenido largo como explicaciones detalladas del examen.
   SQLite lo mapea al tipo TEXT, que puede almacenar hasta 2^31-1 bytes.

3. created_at = DateTimeField(auto_now_add=True)
   Justification: DateTimeField es el tipo correcto para registrar timestamps.
   auto_now_add=True asegura que la fecha se registre automáticamente al crear
   el registro, sin necesidad de intervención manual. Permite ordenar exámenes
   cronológicamente y proporciona metadatos útiles sobre cuándo se creó cada
   examen. El formato UTC (USE_TZ=True) garantiza consistencia temporal.

4. __str__ = return self.title
   Justification: Devolver el título en __str__ proporciona una representación
   legible en el admin de Django y en el shell, identificando rápidamente cada
   instancia de Exam por su nombre principal.
"""

"""
Model: Question
"""

"""
1. exam = ForeignKey(Exam, on_delete=CASCADE)
   Justification: ForeignKey establece la relación de muchos-a-uno entre Question
   y Exam, ya que una pregunta pertenece a un solo examen pero un examen tiene
   muchas preguntas. CASCADE asegura que al eliminar un examen se eliminen
   también sus preguntas, manteniendo la integridad referencial. related_name
   'questions' permite acceder inversamente desde Exam.questions.all().

2. text = TextField()
   Justification: TextField se elige porque el enunciado de una pregunta puede
   variar significativamente en longitud, desde preguntas cortas hasta
   problemas matemáticos complejos con múltiples líneas. TextField no tiene
   límite de caracteres impuesto y almacena el contenido completo sin truncar.

3. score = IntegerField(default=1)
   Justification: IntegerField es el tipo apropiado para un puntaje porque los
   puntos son valores numéricos enteros. El default=1 asigna un puntaje estándar
   de 1 punto por pregunta. IntegerField es eficiente en almacenamiento (4 bytes
   en SQLite) y permite operaciones aritméticas directas para calcular puntajes
   totales de exámenes.

4. __str__ = return f"Q{self.id}: {self.text[:50]}..."
   Justification: La representación incluye el ID para identificación única y
   un fragmento del texto para contexto visual. El truncamiento a 50 caracteres
   mantiene el output legible en listas del admin sin perder la información
   esencial de identificación.
"""

"""
Model: Choice
"""

"""
1. question = ForeignKey(Question, on_delete=CASCADE)
   Justification: ForeignKey establece que cada choice pertenece a una sola
   question (relación muchos-a-uno). CASCADE garantiza que al eliminar una
   pregunta se eliminen también todas sus opciones, preservando la integridad
   de los datos. related_name='choices' permite iterar sobre las opciones desde
   una pregunta con question.choices.all().

2. text = CharField(max_length=500)
   Justification: CharField con max_length=500 limita la longitud de cada opción
   a un tamaño razonable. Una opción de respuesta rara vez excede 500 caracteres;
   si fuera más largo, debería ser una pregunta, no una opción. CharField permite
   índices de base de datos y validación automática del límite.

3. is_correct = BooleanField(default=False)
   Justification: BooleanField es el tipo semánticamente correcto para indicar
   una respuesta verdadera o falsa. default=False asegura que ninguna opción se
   marque como correcta accidentalmente. BooleanField se almacena como tinyint
   en SQLite (1 byte), siendo el tipo más eficiente para valores binarios. La
   validación de que exactamente una opción sea True se implementa a nivel de
   vista para mantener reglas de negocio complejas.
"""
