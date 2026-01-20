from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/admission")
def admission():
    return render_template("admission.html")

@app.route("/department")
def department():
    return render_template("department.html")

@app.route("/hostel")
def hostel():
    return render_template("hostel.html")

@app.route("/sports")
def sports():
    return render_template("sports.html")

@app.route("/placement")
def placement():
    return render_template("placement.html")
@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"].lower()

    if "admission" in msg:
        return jsonify({"reply": "Opening Admission page… <script>window.location='/admission'</script>"})

    if "department" in msg or "course" in msg:
        return jsonify({"reply": "Opening Departments page… <script>window.location='/department'</script>"})

    if "hostel" in msg:
        return jsonify({"reply": "Opening Hostel page… <script>window.location='/hostel'</script>"})

    if "sports" in msg:
        return jsonify({"reply": "Opening Sports page… <script>window.location='/sports'</script>"})

    if "placement" in msg:
        return jsonify({"reply": "Opening Placement page… <script>window.location='/placement'</script>"})

    if "gallery" in msg or "photos" in msg:
        return jsonify({"reply": "Opening Gallery… <script>window.location='/gallery'</script>"})

    return jsonify({"reply": "Please use the menu above to explore KNCET."})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
