# My solution
def open_or_senior(data):
    handicap_limit = [z for z in range(-2,26+1)]
    score = 0
    for x in data:
        years = x[0]
        handicap = x[1]
        if (handicap in handicap_limit)==True:
            if years >= 55 and handicap > 7:
                data[score] = "Senior"
            else:
                data[score] = "Open"
        else:
            if years > 55 and handicap > 7:
                data[score] = "Senior"
            else:
                data[score] = "Open"
        score += 1
    return data
lista = [(45, 12),(55,21),(19, -2),(104, 20)]
print(open_or_senior(lista))

#Solution num_py
import numpy as np
def open_or_senior(data):
    arr = np.array(data)
    arr = np.bitwise_and(arr[:,0] >= 55, arr[:,1] > 7)
    applicants = np.where(arr, 'Senior', 'Open')
    return applicants.tolist()
lista = [(45, 12),(55,21),(19, -2),(104, 20)]
print(open_or_senior(lista))

#solution someone
def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

#solution next
def openOrSenior(data):
    def categorize(age, handicap):
        if age >= 55 and handicap > 7:
            return 'Senior'
        return 'Open'

    return [ categorize(*item) for item in data ]

#solution next
def openOrSenior(data):
    # Hmmm.. Where to start?
    ret = []
    for datum in data:
        age, handicap = datum
        if age >= 55 and handicap > 7:
            ret.append('Senior')
        else:
            ret.append('Open')
    return ret