class Student:
    name = 'A'
    age = 0
    tracks = ['AA', 'BB']
    score = 0.0

    def __init__(self):
        pass

    def change_name(self, name2):
        self.name = name2
        return name2

    def change_age(self, age2):
        self.age = age2
        return age2

    def add_track(self, track2):
        self.tracks = track2
        return track2

    def get_score(self, score2):
        self.score = score2
        return score2


Bob = Student()

Expected methods
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)
Bob.change_name("Peter")
print(Bob.name)
(Bob.change_age(34))
print(Bob.age)
Bob.add_track("UI/UX")
print(Bob.add_track)
Bob.get_score(34.5)
print(Bob.get_score)
