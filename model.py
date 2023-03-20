from mysql import connector

class StudentModel():

    def __init__(self):
        try:
            self.con = connector.connect(host="localhost", user="root", password="", database="StudentDB")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
        except:
            print("Connection Error..")

    def getall_student(self):
        self.cur.execute("SELECT * FROM students")
        result = self.cur.fetchall()    
        return result
    
    def create_student(self, data):
        name = data['name']
        rollno = data['rollno']
        self.cur.execute(f"INSERT INTO students(name,rollno) VALUES('{name}', '{rollno}')")
        return "Student Created Successfully!"
    
    def update_student(self, data):
        name = data['name']
        rollno = data['rollno']
        self.cur.execute(f"UPDATE students SET name='{name}' WHERE rollno LIKE '{rollno}'")
        return "Data Successfully Updated!"
    
    def delete_student(self, data):
        rollno = data['rollno']
        self.cur.execute(f"DELETE FROM students WHERE rollno LIKE '{rollno}'")
        return "Student Data Deleted"