# 📊 Modelo de Markov - Simulación del Clima

## 📌 Descripción
Este proyecto implementa una cadena de Markov para simular el comportamiento del clima. Se utilizan tres estados: Soleado, Nublado y Lluvioso.

El modelo permite observar cómo evoluciona el sistema a través del tiempo utilizando probabilidades de transición.

---

## 🧠 Modelo de Markov
Una cadena de Markov es un proceso donde el siguiente estado depende únicamente del estado actual.

Estados utilizados:
- ☀️ Soleado
- ☁️ Nublado
- 🌧️ Lluvioso

Matriz de transición:

| Actual → Futuro | Soleado | Nublado | Lluvioso |
|----------------|--------|--------|----------|
| Soleado        | 0.6    | 0.3    | 0.1      |
| Nublado        | 0.2    | 0.5    | 0.3      |
| Lluvioso       | 0.3    | 0.3    | 0.4      |

---

## 💻 Implementación
El modelo fue desarrollado en Python utilizando la librería NumPy para la generación de valores aleatorios.

---

## ▶️ Cómo ejecutar

1. Instalar dependencias:

pip install numpy