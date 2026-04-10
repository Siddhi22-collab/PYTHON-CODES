class Employee:
    def setData(self,empno,name):
        self.empno=empno
        self.name=name
    def getData(self):
        print(self.empno)
        print(self.name)
e=Employee()
e.setData(1,'Siddhi')
e.getData()