from flask import Flask
from flask_restful import Api, Resource, request
from model import StudentModel

app = Flask("Student Management System")
api = Api(app)

student_obj = StudentModel()

@app.route('/student')
def get():
        return student_obj.getall_student()

@app.route('/create', methods=['POST'])
def create_student():
        data = request.form
        return student_obj.create_student(data)

@app.route('/edit', methods=['PUT'])
def edit_student():
        data = request.form
        return student_obj.update_student(data)

@app.route('/delete', methods=['DELETE'])
def delete_student():
        data = request.form
        return student_obj.delete_student(data)
