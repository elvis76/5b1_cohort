# class Student():
#     instructor = "Elvis"


#     def __init__(self, name, grade, stu_num):
#         self.name = name
#         self.grade = grade
#         self.stu_num = stu_num

# student = Student(name ="Tunde", grade="c", stu_num="308")
# student1 = Student(name ="chuks", grade="A", stu_num="456")
# print(student.name)    
# print(student1.name) 

# class Square():
#     num_side = 4


#     def __init__(self, side_len):
#         self.side_len = side_len
#         self.area = side_len**2
#         self.perimeter = side_len*4

#     def get_area(self):
#         return self.area  

# square = Square(side_len=4)         
# square1 = Square(side_len=10)         

# print(square.side_len)
# print(square.area)
# print(square.perimeter)

# print(square1.side_len)
# print(square1.area)
# print(square1.perimeter)

# class Employee():
#     def __init__(self, name, salary, years):
#         self.name = name
#         self.salary = salary
#         self.years = years
        
#         @property
#         def bonus(self):
#             if self.years >= 5:
#                 return self.salary*0.1
#             return 0

# class Supervisor(Employee):
#     def __init__(self, name, salary, years, branch):
#         self.branch = branch
#         super().__init__(name, salary, years)            

# emp1 = Employee("Chidi", 250, 2)        
# emp1 = Employee("Adeola", 500, 5)        
# sup1 = Supervisor("Charles", 2500, 15, "Yaba")       

# print(sup1.years, sup1.branch)

# class Question:
#     def __init__(self, correct_ans, user_ans):
#         self.correct_ans = correct_ans
#         self.user_ans = user_ans



# quest = [
#     "Who won 2019's Sports Personality of the Year?\n"
#     "(a) james\n"
#     "(b) king\n"
#     "(c) ben stokes\n"
#     "(d) robert\n",
#     "How many goals did England score (excluding penalty shoot-outs) at the Mens' 2018 FIFA World Cup?\n(a) 10\n(b) 12\n(c) 11\n(d) 13\n",
#     "Which European city hosted the 1936 Summer Olympics?\n(a) berlin\n(b) demark\n(c) spain\n(d) russian\n",
#     "How many horses are on each team in a polo match?\n(a) five\n(b) two\n(c) four\n(d) six\n",
#     "How many permanent teeth does a dog have?\n(a) 32\n(b) 40\n(c) 35\n(d) 42\n"
# ]

# questions = [
#     Question(quest[0], "c"),
#     Question(quest[1], "b"),
#     Question(quest[2], "a"),
#     Question(quest[3], "c"),
#     Question(quest[4], "d")
# ]


# def run_quiz(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.correct_ans)
#         if answer == question.user_ans:
#             score +=1     
#     print("You got" + str(score) + '/' + str(len(questions)) + "correct") 
       

# run_quiz(questions)        


# class QuizQuestion():
#     num_questions = 0
#     num_correct = 0
#     question = ""
#     correct_answer = ""

#     def __init__(self, quest, options:list, answer):
#         QuizQuestion.question = quest
#         for ans in options:
#             QuizQuestion.question+=f"\n{ans}"


#         QuizQuestion.correct_answer = answer.upper()

#     def __ask(self):

#         while True:
#             print(self.question)
#             answer = input(">").upper()
#             if answer in ["A","B", "C","D", "E"]:
#                 return answer
#             print("\nInvalid answer. Please enter A, B, C, D, or E.\n")

#     def check(self):
#         QuizQuestion.num_questions+=1
#         ans = self.__ask()
#         if QuizQuestion.correct_answer == ans:
#             QuizQuestion.num_correct+=1
#             print("Correct")
#         else:
#             print("Incorrect")


#     def result(self):
#         print(f"{QuizQuestion.num_correct} correct our of {QuizQuestion.num_questions} question(s)")


# q1 = QuizQuestion("What year was java created?", 
#                   [
#                     "A. 1982", 
#                     "B. 1996",
#                     "C. 1991",
#                     "D. 1891",
#                     "E. 1981",
# ],
#                   "B")
# q1.check()

# q2 = QuizQuestion("Who invented Java?", 
#                   [
#                     "A. James Gosling", 
#                     "B. Dennis Ritchie",
#                     "C. Raj Reddy",
#                     "D. Guido van Ross",
#                     "E. Bill Joy"
# ],
#                   "A")
# q2.check()


# q2.result()