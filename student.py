class Student():

    social_status = 'student'
    
    def __init__(self, name, marks=[]):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    def print_info(self):
        print('%s: marks: %s, score: %s' % (self.name, self.marks, self.average_marks()))

    def __str__(self):
        return '%s: marks: %s, score: %s' % (self.name, self.marks, self.average_marks())



