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
    
@app.get('/stats')
async def get_count():

    # Initialize counters
    stats = {}
    
    # Iterate through all students in the data
    for student in data:
        # Count meal preferences (pref field)
        pref = student.get('pref')
        if pref:
            stats[pref] = stats.get(pref, 0) + 1
        
        # Count programmes (programme field)
        programme = student.get('programme')
        if programme:
            stats[programme] = stats.get(programme, 0) + 1
    
    # Return the statistics (return outside the loop)
    return stats

@app.get('/add/a/b')
async def add(a: float, b: float):
   return a + b

@app.get('/subtract/a/b')
async def subtract(a: float, b: float):
   return a - b

@app.get('/multiply/a/b')
async def multiply(a: float, b: float):
   return a * b

@app.get('/divide/a/b')
async def divide(a: float, b: float):
   return a / b
