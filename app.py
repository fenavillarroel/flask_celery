from celery import Celery
from celery.result import AsyncResult
from flask import Flask, jsonify
import time

app = Flask(__name__)

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
    task_serializer='json',
    result_serializer='json'
)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/tarea/x/<x1>/y/<x2>", methods=['POST'])
def tarea(x1, x2):
    result = divide.delay(int(x1),int(x2))
    return jsonify({"id":result.id}), 200

@app.route("/results/<task_id>", methods=["GET"])
def results(task_id):
    task_result = AsyncResult(task_id, backend=celery.backend)
    try:
        result=task_result.status
    except:
        result='Error check complete trace by id {} in Flower'.format(task_id)
    print(task_result.result, task_result.status)
    result = {
        "task_id": task_id,
        "task_status": str(task_result.status),
        "task_result": result
    }
    print(result)
    return jsonify(result), 200


@celery.task
def divide(x, y):
    time.sleep(30)
    return x / y