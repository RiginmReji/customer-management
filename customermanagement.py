class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        if customer.customer_id in self.customers:
            print(f"Customer ID {customer.customer_id} already exists.")
        else:
            self.customers[customer.customer_id] = customer
            print(f"Customer {customer.name} added successfully.")

    def update_customer(self, customer_id, name=None, email=None, phone=None):
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            customer.name = name if name else customer.name
            customer.email = email if email else customer.email
            customer.phone = phone if phone else customer.phone
            print(f"Customer {customer_id} updated successfully.")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer {customer_id} deleted successfully.")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def view_customer(self, customer_id):
        if customer_id in self.customers:
            print(self.customers[customer_id])
        else:
            print(f"Customer with ID {customer_id} not found.")

    def list_customers(self):
        if not self.customers:
            print("No customers to display.")
        else:
            for customer in self.customers.values():
                print(customer)


# Main function to interact with the Customer Management Module
def main():
    cm = CustomerManagement()

    # Adding some customers
    cm.add_customer(Customer(1, "rigin", "john.doe@example.com", "1234567890"))
    cm.add_customer(Customer(2, "Jackson", "jack.smith@example.com", "9876543210"))
    
    # Listing all customers
    print("\nList of Customers:")
    cm.list_customers()

    # Viewing a specific customer
    print("\nView Customer ID 1:")
    cm.view_customer(1)

    # Updating a customer's details
    cm.update_customer(2, email="jack.newemail@example.com", phone="5551234567")

    # Deleting a customer
    cm.delete_customer(1)

    # Final list of customers
    print("\nUpdated List of Customers:")
    cm.list_customers()

if __name__ == "__main__":
    main()
