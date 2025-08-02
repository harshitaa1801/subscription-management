from dateutil.relativedelta import relativedelta

PREMIUM_REMINDER_MONTHS = 3
OTHER_REMINDER_MONTHS = 1

class ReminderCalculator:
    REMINDER_DATE_DAYS = 10

    def _get_reminding_months(self, plan):
        if plan == 'PREMIUM':
            return PREMIUM_REMINDER_MONTHS
        else:
            return OTHER_REMINDER_MONTHS


    def get_reminder_date(self, subscription_start_date, plan):

        months = self._get_reminding_months(plan)        
        renewal_reminder = subscription_start_date + relativedelta(months=months) - relativedelta(days=self.REMINDER_DATE_DAYS)
        
        return renewal_reminder