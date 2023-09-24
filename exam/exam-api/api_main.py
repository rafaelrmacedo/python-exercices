from flask import Flask, request, jsonify
from db_functions import *

app = Flask(__name__)

@app.route("/task", methods=['GET'])
def getAllTasks():
    tasks = select_all_task()
    return jsonify(tasks)

@app.route('/task', methods=['POST'])
def add_task():
    new_task = request.json
    insert_task(new_task)
    return jsonify({'message': 'Task added!'}), 201

@app.route('/produto/<int:task_id>', methods=['PUT'])
def update_product(task_id):
    updated_task = request.json
    update_task(updated_task, task_id)
    return jsonify({'message': 'Task updated!'}), 200

@app.route('/task/<int:task_id>', methods=['DELETE'])
def destroy_task(task_id):
    delete_task(task_id)
    return jsonify({'message': 'Task destroyed!'}), 200

# End basic CRUD

@app.route('/task/lowPriority', methods=['GET'])
def get_task_by_id(priority):
    task = select_task_low_priority(priority)
    return jsonify(task)

@app.route('/task/highPriority', methods=['GET'])
def get_tasks_by_priority():
    tasks = select_task_high_priority()
    return jsonify(tasks)

@app.route('/task/priority/<int:priority>', methods=['GET'])
def get_tasks_by_priority(priority):
    tasks = select_task_priority(priority)
    return jsonify(tasks)

@app.route('/task/todo', methods=['GET'])
def get_tasks_by_state(state):
    tasks = select_task_todo_state(state)
    return jsonify(tasks)

@app.route('/task/doing', methods=['GET'])
def get_tasks_by_state(state):
    tasks = select_task_doing_state(state)
    return jsonify(tasks)

@app.route('/task/done', methods=['GET'])
def get_tasks_by_state(state):
    tasks = select_task_done_state(state)
    return jsonify(tasks)

@app.route('/task/<string:state>/<int:priority>', methods=['GET'])
def get_tasks_by_description_priority():
    state = request.args.get('state')
    priority = request.args.get('priority')
    tasks = select_task_state_priority(state, priority)
    return jsonify(tasks)

app.run()