from datetime import datetime

from data.subscriptions import SubscriptionFactory, TopupFactory
from .reminder_calculator import ReminderCalculator

FIRST_ELEMENT_INDEX = 0


class SubscriptionCalculation:
    def __init__(self):
        self.subscription_start_date = None
        self.subscription_data = {}
        self.topup_added = False
        self.total_price = 0

    def get_subscription_start_date(self, subscription_start_date):
        subscription = subscription_start_date.split()

        if subscription[0] == 'START_SUBSCRIPTION':
            try:
                start_date_obj = datetime.strptime(subscription[1], '%d-%m-%Y')
                self.subscription_start_date = start_date_obj
                return start_date_obj
            except Exception:
                print("INVALID_DATE")

        return None


    def _add_subscription_and_save_price(self, sub_name, plan_name):
        subscription = SubscriptionFactory.get_subscription(sub_name)
        if not subscription:
            print("ADD_SUBSCRIPTION_FAILED INVALID_SUBSCRIPTION_TYPE")
            return
        
        price = subscription.get_price(plan_name)
        self.total_price += price

        self.subscription_data[sub_name] = plan_name


    def _add_subscription(self, command_list):
        if not self.subscription_start_date:
            print("ADD_SUBSCRIPTION_FAILED INVALID_DATE")
            return

        if command_list[1] in self.subscription_data:
            print("ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY")
            return

        self._add_subscription_and_save_price(command_list[1], command_list[2])




    def _add_topup_and_save_price(self, topup_category, num_of_months):
        topup = TopupFactory.get_topup(topup_category)
        if not topup:
            print("ADD_TOPUP_FAILED INVALID_TOPUP_TYPE")
            return
        
        price_per_month = topup.get_price(topup_category)
        self.total_price += price_per_month*num_of_months
        self.topup_added = True


    def _add_topup(self, command_list):
        if not self.subscription_start_date:
            print("ADD_TOPUP_FAILED INVALID_DATE")
            return

        if self.topup_added:
            print("ADD_TOPUP_FAILED DUPLICATE_TOPUP")
            return
        
        if not self.subscription_data:
            print("ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND")
            return

        self._add_topup_and_save_price(command_list[1], int(command_list[2]))


    def process_commands(self, lines):

        for command in lines:
            command_list = command.split()
            command_type = command_list[FIRST_ELEMENT_INDEX]
            self.process_each_command(command_type, command_list)


    def process_each_command(self, command_type, command_list):
        command_handlers = {
            'ADD_SUBSCRIPTION': self._add_subscription,
            'ADD_TOPUP': self._add_topup,
            'PRINT_RENEWAL_DETAILS': self.print_renewal_details
        }

        handler = command_handlers.get(command_type)
        if handler:
            if command_type == 'PRINT_RENEWAL_DETAILS':
                handler()
            else:
                handler(command_list)


    def print_renewal_details(self):
        if not self.subscription_data:
            print("SUBSCRIPTIONS_NOT_FOUND")
            return

        for subscription, plan in self.subscription_data.items():
            renewal_reminder = ReminderCalculator().get_reminder_date(self.subscription_start_date, plan)
            print(f"RENEWAL_REMINDER {subscription} {renewal_reminder.strftime('%d-%m-%Y')}")
        
        print(f"RENEWAL_AMOUNT {self.total_price}")
