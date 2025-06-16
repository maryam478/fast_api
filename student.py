from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {
    1:{
        'name':'Maryam',
        'age':24,
        'course':'MCA'
    }
}

class Student(BaseModel):
    name:str
    age:int
    course:str

class UpdateStudent(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    course:Optional[str] = None



@app.get('/')
def index():
    return{'data':'Hi this is studen API'}

@app.get('/student/{student_id}')
def get_student(student_id:int):
    return students [student_id]

@app.get('/student_by_name/{student_id}')
def get_student(student_id,name:str = None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
        return {'data':'Student not found'}
    
@app.post('/create_student/{student_id}')
def create_student(student_id:int,student:Student):
    if student_id in students:
        return {'Error':'Student exists'}
    students[student_id] = student
    return students[student_id]

@app.put('/update_student/{student_id}')
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {'Error':'Student does not exist'}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.course != None:
        students[student_id].course = student.course

@app.delete('/delete_student/{student_id}')
def delete_student(student_id:int):
    if student_id not in students:
        return {'Error':'Student does not exist'}
    del students[student_id]
    return {'Message':'Student deleted successfully'}