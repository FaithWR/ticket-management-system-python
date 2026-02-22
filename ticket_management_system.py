# support_ticket_system.py

import json
import os

FILE_NAME = "tickets.json"

def load_tickets():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tickets(tickets):
    with open(FILE_NAME, "w") as file:
        json.dump(tickets, file, indent=4)

def create_ticket():
    tickets = load_tickets()
    title = input("Enter issue title: ")
    description = input("Enter issue description: ")
    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "description": description,
        "status": "Open"
    }
    tickets.append(ticket)
    save_tickets(tickets)
    print("Ticket created successfully!")

def view_tickets():
    tickets = load_tickets()
    if not tickets:
        print("No tickets found.")
        return
    for ticket in tickets:
        print(f"\nID: {ticket['id']}")
        print(f"Title: {ticket['title']}")
        print(f"Description: {ticket['description']}")
        print(f"Status: {ticket['status']}")

def update_ticket():
    tickets = load_tickets()
    ticket_id = int(input("Enter ticket ID to close: "))
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "Closed"
            save_tickets(tickets)
            print("Ticket closed successfully!")
            return
    print("Ticket not found.")

def main():
    while True:
        print("\n--- SUPPORT TICKET SYSTEM ---")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Close Ticket")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()