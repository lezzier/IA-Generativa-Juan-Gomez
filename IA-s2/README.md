# Actividad: tres cupos, ocho estudiantes

## Propósito

Analizar cómo una inteligencia artificial selecciona estudiantes para un programa de acompañamiento y cómo la información disponible y las condiciones del programa influyen en esa decisión. El caso y los datos son ficticios.

## Situación

En un curso de programación hay ocho estudiantes y solo tres cupos para acompañamiento. Las notas se califican de 0 a 5 y se aprueba con 3. La decisión debe considerar tanto el desempeño académico como las circunstancias y necesidades de cada estudiante.

| Estudiante | Nota | Asistencia | Situación |
|---|---:|---:|---|
| Ana | 2,1 | 95 % | Estudia por su cuenta, pero aún no comprende varios conceptos básicos. |
| Bruno | 2,8 | 65 % | Sus turnos de trabajo coinciden con algunas clases. |
| Camila | 2,8 | 100 % | Resuelve ejercicios con ayuda, pero se bloquea cuando trabaja sola. |
| Diego | 1,9 | 60 % | Ha faltado para cuidar a un familiar y se siente muy atrasado. |
| Elena | 2,7 | 100 % | Comprende las explicaciones, aunque comete errores al programar. |
| Felipe | 4,3 | 95 % | Quiere profundizar en temas avanzados. |
| Gabriela | 2,6 | 80 % | Comparte computador en casa y casi no puede practicar. |
| Hugo | 2,5 | 90 % | Entrega las actividades, pero le cuesta explicar su código. |

## Primera consulta a la IA

Se pidió seleccionar a los tres estudiantes que más necesitaban acompañamiento, justificar la selección y explicar por qué se dejaba por fuera a los demás, sin agregar condiciones específicas al programa.

La IA eligió a **Camila, Gabriela y Ana**. Priorizó sus dificultades académicas y consideró que podían beneficiarse directamente de tutorías. Dejó fuera a Diego y Bruno, entre otras razones, porque interpretó que sus dificultades de asistencia requerían flexibilidad de horario o apoyo adicional, no solo acompañamiento académico.

## Segunda consulta: Programa A

En la segunda consulta se añadió información concreta sobre el programa:

- Son dos sesiones de dos horas antes del examen de la próxima semana.
- El objetivo es ayudar a los estudiantes a alcanzar la nota mínima de aprobación (3).
- Los ocho estudiantes pueden asistir a las dos sesiones.
- Hay computadores disponibles durante las sesiones, pero no se prestan equipos ni hay acompañamiento después del examen.

Con estas condiciones, la IA eligió a **Camila, Elena y Hugo**. Su respuesta dio prioridad a quienes estaban más cerca de la nota mínima y cuyas dificultades podían abordarse durante un repaso corto.

Dejó por fuera a Felipe porque ya tenía una nota aprobatoria alta; a Bruno por el posible conflicto entre sus turnos laborales y las sesiones; a Gabriela porque no habría préstamo de computadores para practicar fuera de ellas; y a Ana y Diego porque consideró que sus vacíos o atrasos eran difíciles de resolver en solo cuatro horas.

## Comparación de las respuestas

La selección cambió: Ana y Gabriela salieron, mientras que Elena y Hugo ingresaron. Al describir el Programa A, la consulta hizo más claro el objetivo y el tiempo disponible. La IA pasó de priorizar necesidades académicas generales a escoger estudiantes que, según su razonamiento, podrían acercarse a la aprobación con un repaso intensivo.

Las respuestas también muestran que algunas conclusiones dependieron de supuestos. Por ejemplo, aunque la segunda consulta decía que los ocho podían asistir, la IA siguió considerando que los turnos de Bruno podían impedirle participar. Por eso es importante comprobar que los criterios y las razones usadas sean consistentes con los datos proporcionados.
