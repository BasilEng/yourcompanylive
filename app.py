from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/customer", methods=["POST"])
def collect_lead():
	name = request.form.get("name")
	business = request.form.get("business")
	number = request.form.get("number")

	if not name or not business or not number:
		return "Missing data", 400

	# Save to CSV
	with open("leads.csv", "a", newline="") as file:
		writer = csv.writer(file)
		writer.writerow([datetime.now().isoformat(), name, business, number])

	return "Thanks! We'll contact you soon.", 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
