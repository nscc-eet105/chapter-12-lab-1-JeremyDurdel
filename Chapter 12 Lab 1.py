#Jeremy Durdel
#Chapter 12 Lab 1
#07/12/2025

state_capitals = {"Ohio": "Columbus",
                  "Michigan": "Lansing",
                  "Indiana": "Indianapolis",
                  "Illinois": "Springfield",
                  "West Virginia": "Charleston"}
def main():
    print("\nState Capital's Game\n")

    right = 0
    wrong = 0

    for states in state_capitals:
        print(f"What is the capital of {states}?")
        capital = input("Type your answer: ")
        if capital == state_capitals[states]:
            print("\nGood Job!\n")
            right += 1
        else:
            print(f"\nSorry the answer is {state_capitals[states]}\n")
            wrong += 1

    print(f"You answered {right} correctly and {wrong} incorrectly.")


main()