from flask import Flask, request, jsonify

app = Flask(__name__)

# Contoh rules diagnosa sederhana
def diagnose(symptoms):
    if "demam" in symptoms and "batuk" in symptoms:
        return "Kemungkinan Anda terkena flu."
    elif "pusing" in symptoms and "mual" in symptoms:
        return "Kemungkinan Anda mengalami vertigo."
    else:
        return "Gejala tidak cukup untuk diagnosis."

@app.route("/diagnosa", methods=["POST"])
def diagnosa():
    data = request.json
    symptoms = data.get("symptoms", [])
    result = diagnose(symptoms)
    return jsonify({"diagnosis": result})

@app.route("/", methods=["GET"])
def index():
    return "Aplikasi Diagnosa AI aktif."

if __name__ == "__main__":
    app.run(debug=True)
