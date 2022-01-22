import random

def main():
    action = "y"
    seed = [1, 2, 3, 4, 5, 6]
    total = 0
    while action != "n":
        action = input('Roll dice? [y/n] ')
        if action == "n":
            break
        option1 = random.choice(seed)
        option2 = random.choice(seed)
        option3 = random.choice(seed)
        option4 = random.choice(seed)
        option5 = random.choice(seed)
        
        total = (get_score(option1, total) + get_score(option2, total) + get_score(option3, total) + get_score(option4, total) + get_score(option5, total))
        print(f'You rolled: {option1} {option2} {option3} {option4} {option5}')
        print (f'{total}')

def get_score(option, total):
    if option == 5:
        total += 50
    elif option == 1:
        total += 100
    return total

if __name__ == "__main__":
    main()