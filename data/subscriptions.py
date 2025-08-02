from abc import ABC, abstractmethod

class Subscription(ABC):
    @abstractmethod
    def get_price(self, subscription_type):
        pass


class Music_Subscription(Subscription):
    def get_price(self, subscription_type):
        prices = {
            'FREE': 0,
            'PERSONAL': 100,
            'PREMIUM': 250
        }
        return prices.get(subscription_type, 0)
    

class Video_Subscription(Subscription):
    def get_price(self, subscription_type):
        prices = {
            'FREE': 0,
            'PERSONAL': 200,
            'PREMIUM': 500
        }
        return prices.get(subscription_type, 0)

class Podcast_Subscription(Subscription):
    def get_price(self, subscription_type):
        prices = {
            'FREE': 0,
            'PERSONAL': 100,
            'PREMIUM': 300
        }
        return prices.get(subscription_type, 0)
    

class SubscriptionFactory:
    @staticmethod
    def get_subscription(subscription_type):
        if subscription_type == 'MUSIC':
            return Music_Subscription()
        elif subscription_type == 'VIDEO':
            return Video_Subscription()
        elif subscription_type == 'PODCAST':
            return Podcast_Subscription()
        else:
            raise ValueError("Invalid subscription type")


class Topup(ABC):
    @abstractmethod
    def get_price(self, topup_type):
        pass


class Four_Device_Topup(Topup):
    def get_price(self, topup_type):
        prices = {
            'FOUR_DEVICE': 50
        }
        return prices.get(topup_type, 0)
    
class Ten_Device_Topup(Topup):
    def get_price(self, topup_type):
        prices = {
            'TEN_DEVICE': 100
        }
        return prices.get(topup_type, 0)
    
class TopupFactory:
    @staticmethod
    def get_topup(topup_type):
        if topup_type == 'FOUR_DEVICE':
            return Four_Device_Topup()
        elif topup_type == 'TEN_DEVICE':
            return Ten_Device_Topup()
        else:
            raise ValueError("Invalid topup type")