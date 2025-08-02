from sys import argv

from calculators.subscription_calculator import SubscriptionCalculation
ARGUMENT_LENGTH = 2
def main():
    
    if len(argv) != ARGUMENT_LENGTH:
        raise Exception("File path not entered")
    file_path = argv[1]
    get_subscription_data(file_path)


def get_subscription_data(file_path):

    with open(file_path, 'r') as f:
        Lines = f.readlines()

        user_subscription = SubscriptionCalculation()
        user_subscription.subscription_start_date = user_subscription.get_subscription_start_date(Lines[0])
        user_subscription.process_commands(Lines)

        

if __name__ == "__main__":
    main()