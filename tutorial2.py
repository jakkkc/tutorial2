class Student:

    num_of_students = 0
    fee_increament = 1.4

    def __init__(self, first, last, fee_balance):
        self.first = first
        self.last = last
        self.pay = fee_balance
        self.email = first + "." + last + "@school.com"

        Student.num_of_students +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def fee_increament(self):
        self.fee_balance = int(self.fee_balance * self.fee_increament)

stud_1 = Student("Jackson", "Munene", 500)
stud_2 = Student("John", "Doe", 6000)

# print(stud_1.email, stud_2.email) 
# print(stud_1.fullname())
# print(Student.fullname(stud_2))

stud_1.fee_increament=1.5
print(stud_1.fee_increament)
print(Student.num_of_students)