def Check(studentscore):
    for f in studentscore.items():
        if f[1] >= 50:
            print(f[0], f[1])

            
studentscore = {'prayut':10,'prawit':23,'praleena':20,'sommer':63,'handerson':53,'rungnapar':70,'tawan':60,'odin':78,'peter':72,'kinmaiaong':98,'arsenal':88}
Check(studentscore)

class School:
    def __init__(self, subject='student score'):
        print('ตรวจเกรด')
        self.subject = subject
    
class Student(School):
    def __init__(self, fullname, score, subject):
        super().__init__(subject)
        self.fullname = fullname
        self.score = score

    def checkGrade(self):
        if self.score >= 80:
            print(f' ได้เกรด 4')
        elif self.score >= 70:
            print(f' ได้เกรด 3')
        elif self.score >= 60:
            print(f' ได้เกรด 2')
        elif self.score >= 50:
            print(f' ได้เกรด 1')
        else:
            print(f'ได้เกรด 0')

print('==============')
student01 = Student('prayut', 10, 'japen')
print(f'ชื่อ {student01.fullname}')
print(f'คะแนน {student01.score}')
student01.checkGrade()
print('==============')
student02 = Student('prawit', 23, 'japen')
print(f'ชื่อ {student02.fullname}')
print(f'คะแนน {student02.score}')
student02.checkGrade()
print('==============')
student03 = Student('praleena', 20, 'japen')
print(f'ชื่อ {student03.fullname}')
print(f'คะแนน {student03.score}')
student03.checkGrade()
print('==============')
student04 = Student('sommer', 63, 'japen')
print(f'ชื่อ {student04.fullname}')
print(f'คะแนน {student04.score}')
student04.checkGrade()
print('==============')
student05 = Student('handerson', 53, 'japen')
print(f'ชื่อ {student05.fullname}')
print(f'คะแนน {student05.score}')
student05.checkGrade()
print('==============')
student06 = Student('rungnapar', 70, 'japen')
print(f'ชื่อ {student06.fullname}')
print(f'คะแนน {student06.score}')
student06.checkGrade()
print('==============')
student07 = Student('tawan', 60, 'japen')
print(f'ชื่อ {student07.fullname}')
print(f'คะแนน {student07.score}')
student07.checkGrade()
print('==============')
student08 = Student('odin', 78, 'japen')
print(f'ชื่อ {student08.fullname}')
print(f'คะแนน {student08.score}')
student08.checkGrade()
print('==============')
student09 = Student('peter', 72, 'japen')
print(f'ชื่อ {student09.fullname}')
print(f'คะแนน {student09.score}')
student09.checkGrade()
print('==============')
student010 = Student('kinmaiaong', 98, 'japen')
print(f'ชื่อ {student010.fullname}')
print(f'คะแนน {student010.score}')
student010.checkGrade()
print('==============')
student011 = Student('arsenal', 88, 'japen')
print(f'ชื่อ {student011.fullname}')
print(f'คะแนน {student011.score}')
student011.checkGrade()
