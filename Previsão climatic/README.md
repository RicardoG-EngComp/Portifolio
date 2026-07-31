# 🛵 Weather Alert Pipeline for Delivery Drivers 
**(Pipeline de Alertas Climáticos para Entregadores)**

## 🎯 Summary / Resumo 
**[EN]** I built an automated data pipeline to monitor climate risks for delivery drivers, processing daily temperature, rain, and UV index data to generate safety alerts.
**[PT]** Construí um pipeline de dados automatizado para monitorar riscos climáticos para entregadores, processando dados de temperatura, chuva e índice UV diariamente para gerar alertas de segurança.

---

## 🚨 The Context & Problem
**[EN]** Gig economy delivery drivers are constantly exposed to climate hazards. The lack of predictability regarding sudden heavy rain or extreme UV radiation directly affects the worker's health, safety, and efficiency. 
**[PT]** Entregadores de aplicativo estão diariamente expostos a riscos climáticos. A falta de previsibilidade sobre chuvas intensas ou radiação UV extrema afeta diretamente a saúde e a segurança do trabalhador.

## 💡 The Solution (Data Architecture)
This project is an **ETL (Extract, Transform, Load)** pipeline built in Python to solve this business problem:

1. **Extract:** Fetches real-time weather forecast data (Temperatures, Rain Sum, and UV Index) for the next 3 days using the Open-Meteo API.
2. **Transform:** Cleans and structures the JSON payload into a tabular format using `pandas`. Applies business rules to generate actionable alerts:
   - *If Rain > 0:* "Levar capa de chuva!" (Take a raincoat!)
   - *If Temp > 25°C:* "Usar protetor solar e se hidratar" (Use sunscreen and hydrate!)
3. **Load:** Exports the processed and enriched data into a structured `CSV` file, ready to be consumed by a notification system or database.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** `requests` (API consumption), `pandas` (Data manipulation & cleaning)
- **Data Source:** Open-Meteo API

---

## 🚀 How to Run (Como Executar)

1. Clone this repository to your local machine.
2. Activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   ```
3. Install the required dependencies:
   ```bash
   pip install requests pandas
   ```
4. Run the extraction script:
   ```bash
   python extracao.py
   ```
5. Check the root folder for the generated `alertas_entregadores.csv` file!