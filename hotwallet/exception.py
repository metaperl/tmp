
class BalanceTooLarge(Exception):

    @staticmethod
    def error_msg(balance, allowed):
        return "Balance of {} exceeds allowable balance of {}".format(
            balance, allowed)

class BalanceTooSmall(Exception):

    @staticmethod
    def error_msg(balance, allowed):
        return "Balance of {} is below mininum allowable balance of {}".format(
            balance, allowed)
