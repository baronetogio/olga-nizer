from datetime import datetime

class Task:
    def __init__(self, name, due):
        self.name = name
        self.due = due
        self.createdOn = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    def add(self, handle):
        newtask = (self.name, self.due, self.createdOn)
        handle.append(newtask)
    
    def delete(self, handle):
        pass