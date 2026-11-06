
score = 80
doc = True
att = 80
ass = True
print("check 1")
print("Input:", score, doc, att, ass)
if score >= 70 and doc and att >= 75 and ass:
    print("Expected: Pass")
    print("Actual: Pass")
    print("Reason: All rules are correct.")
sc = 80
doc = True
att = 60
ass = True
print("check 2")
print("Input:", score, doc, att, ass)

if att < 75:
    print("Expected: Fail")
    print("Actual: Fail")
    print("Reason: Attendance is low.")

score = 80
doc = True
att = 80
ass = False
print("check 3")
print("Input:", score, doc, att, ass)
if ass == False:
    print("Expected: Fail")
    print("Actual: Fail")
    print("Reason: Assignment is missing.")
score = 70
doc = True
att = 75
ass = True
print("check 4")
print("Input:", score, doc, att, ass)
if score >= 70 and doc and att >= 75 and ass:
    print("Expected: Pass")
    print("Actual: Pass")
    print("Reason: Minimum limits are met.")
