from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks (can be replaced with a database for production)
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        if task:
            tasks.append(task)
        return redirect(url_for("index"))
    return render_template("todo.html", tasks=tasks)

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
