# IAN JAY P. ESTUBIO 
# Week 04 - Conditional Statements
# Laboratory # 11 - Guided Coding Exercise: Nested if...else Statements in Python

def main():
    """Main function to determine the age."""
    
    try:
        age_str = input("Enter your age: ")
        membership_str = input("Are you a member? (Yes/No): ")
        
        age = int(age_str)
        membership = membership_str.strip().lower()
        
        # Determine the age 
        if age >= 18:
            if membership == "yes":
                print("Access granted.")
            else:
                print("Membership required for access.")
        else:
            print("Access denied. Must be at least 18 years old.")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
