# AURA – Asistente Universitario con Recomendaciones y Autonomía

**AURA** es un asistente inteligente diseñado para estudiantes universitarios. Su objetivo es ayudarlos a planificar sus tareas, acceder a recursos relevantes y cuidar su bienestar académico mediante el uso de agentes inteligentes.

---

## 🎯 Objetivo

Desarrollar un asistente basado en inteligencia artificial que organice, recomiende y acompañe al estudiante en su vida académica, combinando tecnología, empatía y adaptabilidad.

---

## 🚨 Problema

Los estudiantes enfrentan una carga académica creciente, dificultades para encontrar recursos adecuados y escasa conciencia de su bienestar. AURA busca resolver estos problemas mediante:

- Planificación automatizada de tareas y estudios
- Recomendaciones personalizadas de materiales de aprendizaje
- Sugerencias para cuidar la salud mental y física del estudiante

---

## 🧩 Arquitectura basada en agentes inteligentes

AURA está compuesto por los siguientes módulos:

| Agente         | Rol |
|----------------|-----|
| 🧠 **Planificador** | Organiza tareas y sesiones de estudio según tiempo, prioridad y deadlines |
| 📚 **Recomendador** | Sugiere recursos educativos según tema, estilo de aprendizaje y tiempo disponible |
| 🧘 **Bienestar** | Monitorea sobrecarga y propone descansos o pausas activas |
| 💬 **Chatbot** | Permite interacción natural con el estudiante, traduciendo mensajes a acciones |

---

## 🖥️ Interfaz gráfica

La interfaz está compuesta por tres vistas:

1. **📆 Calendario**: muestra sesiones de estudio, entregas, descansos y otros eventos.
2. **🗂️ Lista de Tareas**: tabla editable con actividades académicas, fechas límite, prioridad y estado.
3. **💬 Chat AURA**: entrada conversacional donde el estudiante puede dar órdenes como “agrega descanso mañana” o “qué tengo pendiente”.

---

## ⚙️ Tecnologías utilizadas

- **Python**
- **Streamlit** para la interfaz
- **Pandas / SQLite** para almacenamiento local de tareas y eventos
- **spaCy / NLTK** para procesamiento de lenguaje natural
- **Scikit-learn** para lógica de recomendación y bienestar
- **Licencia MIT**

---

## 💬 Ejemplos de uso

> 🗣️ “Tengo parcial de cálculo el jueves”  
✔️ AURA asigna sesiones de estudio martes y miércoles, con pausas sugeridas.

> 🗣️ “Estoy cansado”  
✔️ El agente de bienestar propone una pausa activa de 10 minutos y motiva con un mensaje amable.

> 🗣️ “Recomiéndame algo fácil para álgebra lineal”  
✔️ El recomendador sugiere dos videos y un PDF con resúmenes.

---

## 🔐 Consideraciones éticas

- No se almacenan datos sensibles
- Todo el código es open source con licencia MIT
- Se explican las recomendaciones
- Se detectan señales de sobrecarga emocional con responsabilidad

---

## 📦 Estado del proyecto

| Componente           | Estado     |
|----------------------|------------|
| Calendario visual    | 🟡 En desarrollo |
| Lista de tareas      | ✅ Funcional básica |
| Chatbot              | 🟡 En pruebas |
| Lógica planificador  | 🟡 Prototipo |
| Recomendaciones      | 🟡 Base inicial |
| Bienestar            | 🔲 Por implementar |

---

## 🧪 Cómo contribuir

1. Haz fork del repositorio
2. Crea una rama `feature/nombre`
3. Haz tus cambios y prueba localmente
4. Haz un pull request explicando claramente tu contribución

---

## 👨‍🔬 Créditos

Este proyecto es desarrollado por estudiantes de la Universidad Nacional de Colombia – Sede Medellín como parte de la **Hackatón Deeppunk 2025**.

---

## 📝 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Puedes usarlo, modificarlo y distribuirlo libremente.
