import json

# Display categories and get user choice
def display_categories(issues):
    categories = list(issues["categories"].keys())
    print("Select a category:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    choice = int(input("Enter choice number: "))
    return categories[choice - 1]

# Capture ticket details
def capture_ticket_details(category, issue_type,ticket_counter ):
    user_name = input("Enter your name: ")
    description = input("Describe your issue: ")
    return {
        "ticket_id": ticket_counter,
        "user_name": user_name,
        "category": category,
        "issue_type": issue_type,
        "description": description
    }

# Display issues in the selected category and get user choice
def display_issues(issues, category):
    issue_types = issues["categories"][category]
    print(f"Select an issue type in {category}:")
    for idx, issue in enumerate(issue_types, 1):
        print(f"{idx}. {issue}")
    choice = int(input("Enter choice number: "))
    return issue_types[choice - 1]

# Store ticket (in-memory for this example)
def store_ticket(tickets, ticket):
    tickets.append(ticket)

# Main function
def main():
    issues_file = 'issues.json'
    with open(issues_file, 'r') as f:
        data = json.load(f)
    issues = data
    tickets = []
    ticket_counter=1

    while True:
        category = display_categories(issues)
        issue_type = display_issues(issues, category)
        ticket = capture_ticket_details(category, issue_type,ticket_counter)
        tickets.append(ticket)
        ticket_counter=ticket_counter+1
        
        print(f"Ticket {ticket['ticket_id']} created successfully.")
        another = input("Do you want to create another ticket? (y/n): ")
        if another.lower() != 'y':
            break
    print("----------------------------------")
    print("All tickets:")
    for ticket in tickets:
        print(ticket)

if __name__ == "__main__":
    main()
