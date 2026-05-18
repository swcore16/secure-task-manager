from flask import Blueprint, jsonify

tasks_bp = Blueprint("tasks", __name__)
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build project", "done": False}
]

@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)