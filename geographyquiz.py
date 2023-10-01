print("Welcome to the geography quiz")

answer = input("Are you ready to start? (yes/no): ")
score = 0

if answer.lower() == "yes":
    answer = input("1. What is the capital of France? ")
    if answer == 'Paris':
        score += 1
        print("Well done")
    else:
        print("Incorrect")

    answer = input("2. What is the capital of Indonesia? ")
    if answer == "Jakarta":
        score += 1
        print("Well done")
    else:
        print("Incorrect")

    answer = input("3. What is the capital of Peru? ")
    if answer == "Lima":
        score += 1
        print("Well done")
    else:
        print("Incorrect")

    answer = input("4. What is the capital of Botswana? ")
    if answer == "Gaborone":
        score += 1
        print("Well done")
    else:
        print("Incorrect")

    answer = input("5. What is the capital of Spain? ")
    if answer == "Madrid":
        score += 1
        print("Well done")
    else:
        print("Incorrect")

print("Your total score is", score)
