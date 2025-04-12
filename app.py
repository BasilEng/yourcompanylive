import csv
from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

# Function to write leads to a CSV file
def save_to_csv(data):
    with open("leads.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([data["name"], data["business"], data["number"]])

# Example route for your app
@app.route('/')
def home():
    return "Welcome to your business live!"

# API route to handle customer order form submission
@app.route('/customer', methods=['POST'])
def handle_customer():
    data = request.get_json()
    name = data.get("name")
    business = data.get("business")
    number = data.get("number")

    # Save the lead to the CSV file
    save_to_csv(data)

    # Respond back to the customer
    return jsonify({
        "message": "Customer details received successfully",
        "data": {
            "name": name,
            "business": business,
            "number": number
        }
    })

# Run the app using Waitress for Windows compatibility
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
