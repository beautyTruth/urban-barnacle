# SLOT MACHINE by: Phil Hasenkamp via Tech With Tim 

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "🍑": 2,
    "🍒": 4,
    "🌺": 6,
    "🥤": 8
}

symbol_value = {
    "🍑": 5,
    "🍒": 4,
    "🌺": 3,
    "🥤": 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        
        print()

def deposit():
    while True:
        amount = input("Please deposit some fake money into your account. How much? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('The amount must be more than zero.')
        else:
            print('Enter an actual numerical value greater than zero')

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter how many lines you want to bet on: (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please follow the instructions and enter a valid number of lines (1-" + str(MAX_LINES) + "): ")
        else:
            print("Enter an actual numerical value (1-" + str(MAX_LINES) + "): ")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount must be more than ${MIN_BET} and less than ${MAX_BET}: $")
        else:
            print(f"Enter an actual numerical value more than ${MIN_BET} and less than ${MAX_BET}: $")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines   

        if total_bet > balance:
            print(f"Total bet is more than {balance}. Total bet must be less than {balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print("You won {} on {} lines.".format(winnings, winning_lines))
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        fate = input("Press enter to play . . . or q to quit")
        if fate.lower() == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()