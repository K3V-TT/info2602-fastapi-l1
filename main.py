from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

### New Function
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: # select only the students with a given meal preference
              filtered_students.append(student) # add match student to the result
        return filtered_students
    return data
### End of new function

@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: # Only return the student if the ID matches
      return student