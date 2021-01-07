from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def get():
    emp = {"first_name": "Vikram",
           "last_name": "Shinde"}

    return jsonify({"emp": emp}), 200


@app.route('/<employee_id>')
def get_employee(employee_id):

    emp = _get_by_employee_id(employee_id)

    return jsonify({"emp": emp}), 200


def _get_by_employee_id(employee_id):
    return employee_id
