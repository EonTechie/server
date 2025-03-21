from flask import Flask, request, render_template_string

app = Flask(__name__)

mesajlar = []

@app.route("/", methods=["GET", "POST"])
def mesaj_al():
    if request.method == "POST":
        mesaj = request.form.get("mesaj")
        mesajlar.append(mesaj)
        return "Mesaj alındı"
    

    html = """
    <h1>Gelen Mesajlar</h1>
    <ul>
        {% for m in mesajlar %}
            <li>{{ m }}</li>
        {% endfor %}
    </ul>
    """
    return render_template_string(html, mesajlar=mesajlar)
