class Student:

    def __init__(self,name,age,tracks,score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        

    def change_name(self,change_name):
        self.change_name = change_name
        print("The new student name is:",change_name)


    def change_age(self,change_age):
        self.change_age = change_age
        print("The new student age is:",change_age)

    def add_track(self,add_track):
        self.add_track = list(add_track)
        self.add_track.append(add_track)
        print("The added track is:",add_track)

    def get_score(self,get_score):
        self.get_score = get_score
        print("The retrieved score is:",get_score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(Bob.score)


#Extra Example
#Bola = Student(name="Jerry",age=31, tracks=["FW","YT"],score=25.29)

#Bola.change_name("Jane")
#Bola.change_age(15)
#Bola.add_track("Product")
#Bola.get_score(Bola.score)
