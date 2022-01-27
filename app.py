from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        username = request.form.get("username")
        print(username)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)