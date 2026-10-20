"""Task Tracker - a tiny Flask app used for the DevOps mini project."""
from flask import Flask, jsonify, request, render_template, abort

VERSION = "1.0.0"


def create_app():
    app = Flask(__name__)
    app.config["TASKS"] = []
    app.config["NEXT_ID"] = 1

    @app.get("/")
    def index():
        return render_template("index.html", version=VERSION)

    @app.get("/health")
    def health():
        return jsonify(status="ok", version=VERSION)

    @app.get("/api/tasks")
    def list_tasks():
        return jsonify(app.config["TASKS"])

    @app.post("/api/tasks")
    def add_task():
        data = request.get_json(silent=True) or {}
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify(error="title is required"), 400
        task = {"id": app.config["NEXT_ID"], "title": title, "done": False}
        app.config["NEXT_ID"] += 1
        app.config["TASKS"].append(task)
        return jsonify(task), 201

    def _find(task_id):
        for t in app.config["TASKS"]:
            if t["id"] == task_id:
                return t
        abort(404)

    @app.patch("/api/tasks/<int:task_id>")
    def toggle_task(task_id):
        task = _find(task_id)
        task["done"] = not task["done"]
        return jsonify(task)

    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id):
        task = _find(task_id)
        app.config["TASKS"].remove(task)
        return "", 204

    return app
