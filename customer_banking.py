# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    while True:
        try:
            savings_balance = float(input('Please enter your Savings Account Balance: '))
        
            savings_interest = float(input('Please enter the Savings Interest Rate: '))
        
            savings_maturity = int(input('Please enter the Number of Months to be Matured in Savings: '))
            break
        except ValueError:
            print('-' * 60)
            print('Invalid Input! Restarting Savings Account Interest Calculation!')
            print('-' * 60)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('-' * 60)
    print(f'Your Savings Account Interest will earn ${interest_earned: ,.2f} from a {savings_interest: ,.2f}% rate over {savings_maturity} months. With a new Savings Account balance of: ${updated_savings_balance: ,.2f}')
    print('-' * 60)
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    while True:
        try:
            cd_balance = float(input('Please enter your CD Account Balance: '))

            cd_interest = float(input('Please enter the CD Interest Rate: '))

            cd_maturity = int(input('Please enter the Number of Months to be Matured in CD: '))
            break
        except ValueError:
            print('-' * 60)
            print('Invalid Input! Restarting CD Account Interest Calculation!')
            print('-' * 60)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('-' * 60)
    print(f'Your CD Account Interest will earn ${interest_earned: ,.2f} from a {cd_interest: ,.2f}% rate over {cd_maturity} months. With a new CD Account balance of: ${updated_cd_balance: ,.2f}')
    print('-' * 60)
if __name__ == "__main__":
    # Call the main function.
    main()