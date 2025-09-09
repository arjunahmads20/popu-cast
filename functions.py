def simulate_population_continuous(
	P0: int, 
	years: float, 
	b: float, 
	d: float, 
	I: float = 0.0, 
	E: float = 0.0, 
	K: float | None = None, 
	steps: int = 1000
): 
	""" 
	Continuous population model integrated with forward Euler.

	Differential equations
	----------------------
	- Exponential (default, when K is None):
	   dP/dt = r * P + (I - E)
	- Logistic (when K is provided):
	   dP/dt = r * P * (1 - P/K) + (I - E)
	
	Parameter semantics
	-------------------
	b, d : float
	   Per-capita rates per year (e.g., b=0.03 means ~3 births per 100 people per year).
	I, E : float
	   Absolute numbers of immigrants and emigrants per year (constant inflow/outflow, not multiplied by P). Example: I=120 means +120 people per year.
	K : float or None
	   Carrying capacity. If provided, the model becomes logistic; otherwise exponential.
	steps : int
	   Number of Euler steps over the `years` horizon.
	
	Returns
	-------
	t : list[float]
	   Time points in years (length steps+1).
	P : list[int]
	   Predicted population at each time in `t`.
	"""
	r = b - d
	dt = years / steps
	t = [i * dt for i in range(steps + 1)]
	P = [int(P0)]

	for _ in range(steps):
	    if K is None:
	        dPdt = r * P[-1] + (I - E)
	    else:
	        dPdt = r * P[-1] * (1 - P[-1] / K) + (I - E)
	    P.append(int(P[-1] + dPdt * dt))
	
	return t, P
