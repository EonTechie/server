from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def mesaj_al():
    data = request.form.get("mesaj")
    print("Gelen mesaj:", data)
    return f"Mesaj alındı: {data}"
