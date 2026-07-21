# Build a student grade classifier

name = input("Enter the student's name: ")
mark1 = float(input("Enter the first mark: "))
mark2 = float(input("Enter the second mark: "))
mark3 = float(input("Enter the third mark: "))

average = (mark1 + mark2 + mark3) / 3

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
    
if average >= 60:
    status = "Pass"
else:
    status = "Fail"
    
intervention = []
if mark1 < 60:
    intervention.append("Mark 1")
if mark2 < 60:
    intervention.append("Mark 2")
if mark3 < 60:
    intervention.append("Mark 3")
    
print("\n" +  "="*30)
print("          STUDENT REPORT CARD")
print("="*30)
print(f"Learner Name : {name}")
print(f"Subject 1     : {mark1}")
print(f"Subject 2     : {mark2}")
print(f"Subject 3     : {mark3}")
print(f"Grade         : {grade}")
print(f"Status        : {status}")
if intervention:
    print("Intervention : Needs intervention in " + ", ".join(intervention))
else:
    print("Intervention : None - All subjects above 50")