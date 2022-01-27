from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        username = request.form.get("username")
        return redirect(url_for("form", username=username))
    return render_template("index.html")

@app.route("/form/<username>", methods=["GET", "POST"])
def form(username):
    return render_template("form.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)