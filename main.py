import os

from flask import Flask, request, jsonify, make_response, send_file
from functions import simulate_population_continuous

app = Flask(__name__)

	
@app.get("/") 
def index():
	return send_file("src/index.html")

@app.post("/api/predict") 
def api_predict(): 
	data = request.get_json(force=True)
	
	# Extract and validate inputs with defaults
	P0 = float(data.get("P0", 0))
	years = float(data.get("years", 1))
	b = float(data.get("b", 0.0))
	d = float(data.get("d", 0.0))
	I = float(data.get("I", 0.0))
	E = float(data.get("E", 0.0))
	K = data.get("K", None)
	K = None if K is None or K == "" else float(K)
	steps = int(data.get("steps", 1000))
	
	t, P = simulate_population_continuous(P0, years, b, d, I, E, K, steps)
	return jsonify({
		"t": t,
		"P": P,
		"P_final": P[-1],
		"model": "logistic" if K is not None else "exponential"
	})
	


def main():
    app.run(port=int(os.environ.get('PORT', 80)))




