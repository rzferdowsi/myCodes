"""Gradebook
You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores."""

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects=["physics","calculus","poetry","history"]
grades=[98, 97, 85, 88]
gradebook= [[subjects[0],grades[0]],
[subjects[1],grades[1]],
[subjects[2],grades[2]],
[subjects[-1],grades[-1]]]
print(gradebook)
print("_______________")
gradebook.append(["computer science", 100])
print(gradebook)
print("_______________")
new_mark=["visual arts", 93]
gradebook.append(new_mark)
print(gradebook)
print("_______________")
gradebook[-1][-1]+=5
print(gradebook)
print("_______________")
gradebook[2].remove(gradebook[2][-1])
print(gradebook)
print("_______________")
gradebook[2].append("Pass")
print(gradebook)
print("_______________")
full_gradebook=last_semester_gradebook+gradebook
print(full_gradebook)
print("_______________")
