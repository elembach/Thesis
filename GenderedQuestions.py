import random

# Create the paired question labels
pairedQuestions = [[f"{i}F", f"{i}M"] for i in range(1, 11)]

# Randomize the order of F and M(female versus male) within each pair
for question in pairedQuestions:
    random.shuffle(question)

# Shuffle the list of paired questions themselves (order of M and F within each number)
random.shuffle(pairedQuestions)

# Flatten the list but keep the pairs together
results = [question for pair in pairedQuestions for question in pair]

# Print the result
print(results)

for question in results:
    if question == "1F":
        print("")
    elif question == "1M":
        print("")
    elif question == "2F":
        print("")
    elif question == "2M":
        print("")
    elif question == "3F":
        print("")
    elif question == "3M":
        print("")
    elif question == "4F":
        print("")
    elif question == "4M":
        print("")
    elif question == "5F":
        print("")
    elif question == "5M":
        print("")
    elif question == "6F":
        print("")
    elif question == "6M":
        print("")
    elif question == "7F":
        print("")
    elif question == "7M":
        print("")
    elif question == "8F":
        print("")
    elif question == "8M":
        print("")
    elif question == "9F":
        print("")
    elif question == "9M":
        print("")
    elif question == "10F":
        print("")
    elif question == "10M":
        print("")
    elif question == "11F":
        print("")
    elif question == "11M":
        print("")
    elif question == "12F":
        print("")
    elif question == "12M":
        print("")
    elif question == "13F":
        print("")
    elif question == "13M":
        print("")
    elif question == "14F":
        print("")
    elif question == "14M":
        print("")
    elif question == "15F":
        print("")
    elif question == "15M":
        print("")
    elif question == "16F":
        print("")
    elif question == "16M":
        print("")
    elif question == "17F":
        print("")
    elif question == "17M":
        print("")
    elif question == "18F":
        print("")
    elif question == "18M":
        print("")
    elif question == "19F":
        print("")
    elif question == "19M":
        print("")
    elif question == "20F":
        print("")
    elif question == "20M":
        print("")


