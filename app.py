from flask import Flask, jsonify, request
from flask_cors import CORS
import taskdata

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/',methods = ['GET','POST'])
def index():
    return {
        'status': 200,
        'message':"App is running "
    }

@app.route('/timepass',methods=['GET'])
def darukutta():
    return {
        'message':'mausambi k juiceeee piilaaa dooo'
    }
# 1. Get all tasks
@app.route('/gettasks', methods=['GET','POST'])
def get_tasks():
    return jsonify(taskdata.tasks)

# 2. Add a task
@app.route('/addtasks', methods=['POST'])
def add_task():
    new_task = request.json
    taskdata.tasks.append(new_task)
    return jsonify({"message": "Task added successfully", "task": new_task}), 201

# 3. Update a task
@app.route('/updatetasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.json
    for task in taskdata.tasks:
        if task['id'] == task_id:
            task.update(updated_task)
            return jsonify({"message": "Task updated successfully", "task": task}), 200
    return jsonify({"message": "Task not found"}), 404

# 4. Delete a task
@app.route('/deletetask/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in taskdata.tasks:
        if task['id'] == task_id:
            taskdata.tasks.remove(task)
            return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"message": "Task not found"}), 404

# 5. Get a task by name
@app.route('/gettaskbyname/<string:name>', methods=['GET'])
def get_task_by_name(name):
    result = [task for task in taskdata.tasks if task['name'] == name]
    if result:
        return jsonify(result), 200
    return jsonify({"message": "Task not found"}), 404

# 6. Get a task by id
@app.route('/gettaskbyid/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for task in taskdata.tasks:
        if task['id'] == task_id:
            return jsonify(task), 200
    return jsonify({"message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
