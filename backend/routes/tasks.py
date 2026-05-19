from flask import Blueprint, jsonify, request

tasks_bp = Blueprint("tasks", __name__)
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
]

@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "done": False
    }

    tasks.append(new_task)
    return jsonify(new_task), 201

# deleting an existing endpoint by id:
@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks

    tasks = [task for task in tasks if task["id"] != task_id]

    return jsonify({"message": "Task deleted"})