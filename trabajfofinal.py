calificaciones = {}

def add_calification():
    name = input("Enter the name of the product or service: ")
    rating = input("Enter your rating (1-5): ")
    comment = input("Enter your comment: ")
    calificaciones[name] = {"rating": rating, "comment": comment}
    print("Calification added successfully!")

def show_califications():
    if not calificaciones:
        print("No califications registered.")
    else:
        for product, calification in calificaciones.items():
            print(f"Product: {product}")
            print(f"Rating: {calification['rating']}")
            print(f"Comment: {calification['comment']}\n")

def main():
    while True:
        print("Calification Menu")
        print("1. Add Calification")
        print("2. Show Califications")
        print("3. Exit")
        option = input("Enter your option: ")
        if option == "1":
            add_calification()
        elif option == "2":
            show_califications()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()