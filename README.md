# Popu Cast (Population Predictor)

A simple **Flask-based web app** to simulate and predict population growth using both **exponential** and **logistic models**.

The app provides a **one-page UI** with clean minimal design where users can input:

- Initial population (**P0**)
- Time horizon (**years**)
- Birth rate (**b**, per capita per year)
- Death rate (**d**, per capita per year)
- Immigration (**I**, absolute per year)
- Emigration (**E**, absolute per year)
- Carrying capacity (**K**, optional â†’ logistic model if provided)

---

## Features
- One-page responsive UI (HTML + CSS + JS embedded in Flask)
- REST API endpoint (`/api/predict`) returning JSON result
- Two growth models: **Exponential** (default) & **Logistic** (when K provided)
- Results displayed in numeric format (with locale thousands separator) and Chart

---

## Tech Stack
- **Backend**: Python + Flask
- **Frontend**: HTML, CSS, Vanilla JS (single-page embedded)

---

## Installation & Usage

Clone the repository:
```bash
git clone https://github.com/arjunahmads20/popu-cast.git
cd popu-cast
```

Install dependencies:
```bash
pip install flask
```

Run the server:
```bash
python app.py
```

Open your browser at [http://localhost:5000](http://localhost:5000).

---

## API Usage

Endpoint: `POST /api/predict`

Request body (JSON):
```json
{
  "P0": 1000000,
  "years": 20,
  "b": 0.03,
  "d": 0.01,
  "I": 1200,
  "E": 500,
  "K": 5000000,
  "steps": 1000
}
```

Response body (JSON):
```json
{
  "t": [0, 0.02, 0.04, ...],
  "P": [1000000.0, 1003200.0, ...],
  "P_final": 1345200.55,
  "model": "logistic"
}
```
