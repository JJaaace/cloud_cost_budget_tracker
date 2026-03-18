def calculate_total_cost(num_servers):
    total = 0
    for i in range(num_servers):
        while True:
            try:
                cost = float(input(f"Enter monthly cost for Server {i+1}: $"))
                if cost < 0:
                    print("Cost cannot be negative. Try again.")
                    continue
                total += cost
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return total


def analyze_budget(budget, total_cost):
    difference = round(abs(budget - total_cost), 2)

    if total_cost > budget:
        print(f"\n Budget exceeded by ${difference}")
        print("Consider reducing server costs or optimizing usage.")
    elif total_cost == budget:
        print("\n You are exactly on budget.")
    else:
        print(f"\n Total cost: ${total_cost}")
        print(f"You have ${difference} remaining in your budget.")


def main():
    print("=== Cloud Cost Budget Tracker ===")

    while True:
        try:
            num_servers = int(input("How many servers do you have? "))
            if num_servers <= 0:
                print("Enter at least 1 server.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            budget = float(input("Enter your monthly budget: $"))
            if budget < 0:
                print("Budget cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    total_cost = calculate_total_cost(num_servers)
    analyze_budget(budget, total_cost)

main()
