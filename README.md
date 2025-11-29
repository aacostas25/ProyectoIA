# 🧠 Proyecto: Edición de Conocimiento en LLMs con ROME + Groq

Este repositorio contiene el código, datos y notebooks utilizados para el estudio experimental sobre **edición de conocimiento en modelos de lenguaje** aplicado a mitos y leyendas de Chile, Colombia y Europa. El objetivo principal es evaluar cómo el método **ROME (Rank-One Model Editing)** modifica hechos específicos dentro de un modelo **LLaMA 3–8B**, preservando estabilidad y coherencia en el resto del conocimiento.

---

## 📂 ¿Qué encontrarás en este repositorio?

### ✔️ 1. **Notebook de Google Colab: Implementación de ROME**

Un notebook completo que incluye:

* Carga del modelo **LLaMA 3–8B** con EasyEdit.
* Configuración del editor ROME.
* Construcción de instancias de edición.
* Evaluación pre y post edición:

  * *Reliability (rewrite accuracy)*
  * *Locality accuracy*
* Estudio de ablación variando la **capa de edición** del modelo.
* Ejemplos reales de edición sobre hechos mitológicos.

Este notebook reproduce exactamente los experimentos presentados en el informe del proyecto.

---

### ✔️ 2. **Conjuntos de edición generados con Groq**

El repositorio incluye los archivos generados mediante un modelo LLaMA 3.3–70B desplegado en **Groq**, utilizados para construir las instancias de edición.

Cada registro contiene:

* Pregunta natural generada automáticamente.
* Respuesta objetivo clara y autocontenida.
* Metadatos del mito: entidad, relación, país o tradición.
* Formato estructurado JSON listo para EasyEdit.

Los conjuntos fueron creados a partir de tripletas del tipo:
**(entidad, relación, objeto)** → *por ejemplo:*
`("alicanto", "alas brillan", "según el metal que come")`

---

### ✔️ 3. **Código del pipeline completo**

Incluye scripts para:

* Procesamiento de tripletas.
* Enriquecimiento semántico vía Groq (limpieza y naturalización de preguntas).
* Construcción del dataset final de edición.
* Ejecución de ediciones con EasyEdit (ROME).
* Evaluación automática de fiabilidad y localidad.

---

### ✔️ 4. **Ejemplos de Prompts y Resultados**

El repositorio contiene ejemplos reales de resultados antes y después de aplicar ROME:

* Mito chileno: *El Alicanto*
* Mito colombiano: *Los animales que anuncian*
* Mito europeo: *Cidipe y Aconcio*

Cada ejemplo incluye:

* Prompt aplicado
* Respuesta esperada
* Respuesta original del modelo
* Respuesta del modelo después de la edición

---

## 🔧 Tecnologías utilizadas

* **GroqCloud** (LLaMA 3.3–70B) — Para la generación de preguntas y respuestas limpias.
* **EasyEdit** — Framework principal de edición.
* **ROME** — Método de edición puntual en modelos transformer.
* **LLaMA 3–8B** — Modelo objetivo para aplicar las ediciones.
* Python, PyTorch, HuggingFace, JSON.

---

## 🧪 Experimentos reproducibles

El repositorio permite replicar todos los resultados:

* Evaluación antes/después de las ediciones.
* Comparaciones por región (Chile, Colombia, Europa).
* Ablaciones por capa: de 1 a 31.
* Experimentos con y sin regularización de localidad.

---

## 📘 Estructura del repositorio

```
/
├── notebooks/
│   └── ROME_Implementation_Colab.ipynb
├── data/
│   ├── tripletas_originales.json
│   ├── preguntas_groq_generadas.json
│   └── conjuntos_edicion_final.json
├── src/
│   ├── pipeline_groq.py
│   ├── build_edit_dataset.py
│   ├── run_rome_edit.py
│   └── evaluation.py
└── README.md
```

---

## 🧩 Objetivo del proyecto

Este proyecto forma parte de un estudio sobre **edición controlada de conocimiento en LLMs**, donde se busca:

1. Determinar qué tan bien ROME puede insertar o corregir hechos mitológicos específicos.
2. Analizar la estabilidad del modelo tras la edición (locality).
3. Evaluar cómo afecta la capa donde se aplica la edición.
4. Comparar comportamientos entre diferentes tradiciones mitológicas.




