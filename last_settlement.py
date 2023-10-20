
def tutorial():
    with open("tutorial.txt", "r") as file:
        print("")


def cycle():
    print("_")

print("Welcome to The Last Settlement. Please start off by inputting your nam.e \n(Type into the space underneath and press \"Enter\")")
input("")
print("Welcome, Angel. Would you like to re-take the tutorial or get right in? (T for Tutorial, P for Play)")
active_choice = input("")

if active_choice.lower() == "t" or active_choice.lower() == "tutorial":
    tutorial()
elif active_choice.lower() == "p" or active_choice.lower() == "play":
    cycle()