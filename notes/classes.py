# syntax
# class ClassName:
#   code here

# name = 'Megan' is a default method if nothing gets passed in
class Person:
    def __init__(self, name = 'Megan'):
        self.name = name
        self.skills = []
    def person_info(self):
        return f'{self.name}'
    def add_skill(self,skill):
        self.skills.append(skill)

class Student(Person):
    # when we add a new init it overrides the parents init
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        super().__init__(name) # you do not need this if you do not write a custom __init__ method in the child class.

    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{gender} is {self.name}.'


p = Person('Megan')
a = Person()
print(p.name)
print(p)
print(a.name)

print(p.person_info())
p.add_skill('HTML')
p.add_skill('CSS')
p.add_skill('JavaScript')
print(p.skills)

s = Student('Eyob', 'male')
print(s.person_info())
s.add_skill('Reading')
print(s.skills)

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics():
    def __init__(self, data):
        self.data = data
    def count(self):
        return len(self.data)
    def sum(self):
        sum = 0
        for item in self.data:
            sum += item
        return sum
    def min(self):
        return sorted(ages)[0]
    def max(self):
        return sorted(ages, reverse= True)[0]
    def range(self):
        return self.max() - self.min()
    def mean(self):
        return self.sum() / self.count()
    def median(self):
        sorted_data = sorted(self.data)
        mid = self.count() // 2

        if self.count() % 2 != 0:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    def mode(self):
        frequencies = {}
        for item in self.data:
            frequencies[item] = frequencies.get(item, 0) + 1

        mode_val = max(frequencies, key=frequencies.get)
        return {'mode': mode_val, 'count': frequencies[mode_val]}
    def var(self):
        avg = self.mean()
        squared_diff_sum = sum((x - avg) ** 2 for x in self.data)
        return round(squared_diff_sum / self.count(), 1)
    def std(self):
        return round(self.var() ** 0.5, 1)
    def freq_dist(self):
        frequencies = {}
        for item in self.data:
            frequencies[item] = frequencies.get(item, 0) + 1
            
        return sorted(frequencies.items())

data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist())