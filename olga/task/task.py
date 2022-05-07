from datetime import datetime

class Task:
    def __init__(self, name, due):
        self.name = name
        self.due = due
        self.createdOn = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    def add(self, handle):
        newtask = {"task" : self.name, "due" : self.due, "created" :self.createdOn}
        handle.append(newtask)
    
    def delete(self, handle):
        pass