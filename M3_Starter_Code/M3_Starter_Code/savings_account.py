"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(savings_balance, savings_interest_rate, savings_months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    savings_account = Account(balance = 0, interest = 0)
       
    # Calculate interest earned
     # ADD YOUR CODE HERE
    savings_interest_earned = float(savings_balance * (savings_interest_rate/100) * (savings_months/12))
    return savings_interest_earned

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    new_savings_balance = (savings_balance + savings_interest_earned)
    return new_savings_balance

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_balance(new_savings_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(savings_interest_earned)

    # Return the updated balance and interest earned.
     # ADD YOUR CODE HERE
    return new_savings_balance, savings_interest_earned