class Student:
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}


    def setGrade(self, cource, grade):
        self.grades[cource] = grade
    
    def getGrade(self, cource):
        return self.grades[cource]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)


sravan = Student("Sravan", 13, 'Male', 8, {"Maths": 100000,"English": 122333,"Chemistry": 664445454})

print(sravan.getGPA())
sravan.setGrade("Coding", 100)
print(sravan.grades)        
