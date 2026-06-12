import random

print("=== MathGenius AI ===")

score = 0

for i in range(5):
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    print(f"\nQuestion {i+1}")
    answer = int(input(f"{a} + {b} = "))

    if answer == a + b:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", a + b)

print("\n===== RESULT =====")
print("Score:", score, "/ 5")

percentage = (score / 5) * 100

print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: F")