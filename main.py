class Student:
    # [assignment] Skeleton class. Add your code here
    Detail='Student'

    def __init__(self,name,age,track,score):
        self.name = str(name)
        self.age = int(age)
        self.track = list(track)
        self.score = float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        print("New name is", change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print("New age is", change_age)

    def add_track(self, add_track):
        self.add_track = add_track
        print("New added track is", add_track)

    def get_score(self, get_score):
        self.get_score = get_score
        print("Score remains", get_score)




Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(20.90)
