from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
CONFIG_PATH = "config.json"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mapping = {}
        for i in range(1, 513):
            dev = request.form.get(f"device_{i}")
            act = request.form.get(f"action_{i}")
            if dev and act:
                mapping[str(i)] = {"device": dev, "action": act}
        with open(CONFIG_PATH, "w") as f:
            json.dump(mapping, f, indent=2)
        return redirect("/")

    try:
        with open(CONFIG_PATH) as f:
            mapping = json.load(f)
    except:
        mapping = {}

    return render_template("index.html", mapping=mapping)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
