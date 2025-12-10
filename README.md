# Minimax en Python 🐭🐱

Este proyecto implementa un **laberinto simple en Python** donde un **gato (G)** intenta atrapar a un **ratón (R)**.  
El ratón o el gato pueden ser controlados por el usuario o por la **IA Minimax**, dependiendo del modo de juego elegido.

El programa genera un tablero vacío, coloca los personajes en posiciones aleatorias y luego simula los movimientos turno a turno.

---

# 🧠 ¿Qué es Minimax?
El algoritmo **Minimax** se utiliza para que la IA evalúe posibles movimientos y decida el mejor según un puntaje.  
En este juego:

- **El Gato es el jugador MAX** → intenta obtener el valor **más alto** (acercarse al ratón).  
- **El Ratón es el jugador MIN** → intenta obtener el valor **más bajo** (alejarse del gato y acercarse a la salida).

La evaluación usa **distancia Manhattan** para medir qué tan favorables son las posiciones.

---

# 🎮 Modos de juego

El usuario puede elegir entre:

1. **Gato-IA vs Ratón (usuario)**  
2. **Ratón-IA vs Gato (usuario)**  
3. **Gato (usuario) vs Ratón (usuario)**

Además, se puede elegir la **profundidad** del Minimax:

- 1 → Fácil  
- 2 → Medio  
- 3 → Difícil  

A mayor profundidad, más inteligente se vuelve la IA (pero también más lento el cálculo).

---

# 📦 Contenido del proyecto

El archivo principal incluye:

- Generación del tablero (`crear_tabla`)
- Posicionamiento aleatorio de personajes (`insertar_raton_gato`)
- Movimiento válido dentro del tablero (`movimientos_posibles`)
- Distancia Manhattan (`distancia_manhattan`)
- Función de evaluación para Minimax (`evaluar_posicion`)
- Algoritmo Minimax completo (`minimax`)
- Lógica de turnos y condiciones de fin de juego (`ganar_perder`)

---

# ▶️ Cómo ejecutar

1. Clona el repositorio:

```bash
git clone https://github.com/IvanOcampos/Minimax.git
cd Minimax
