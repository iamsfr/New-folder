print("Welcome to My computer Quiz!")

playing = input("Do you want to Play? ")

if playing.lower() != "yes":
    quit()

print("okay lets Play: ")
score = 0

    
answer = input("What does cpu stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer = input("what does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4) * 100) + "%.")


