class Account:

    def __init__(self, name: str) -> None:
        """
        This function initializes variables account_name and account_balance
        :param name: The name of the account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        This function adds funds to account_balance
        :param amount: Amount of funds to add
        :return: True if successful and False if unsuccessful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        This function withdraws funds from account_balance
        :param amount: Amount of funds to withdraw
        :return: True if successful and False if unsuccessful
        """
        if 0 < amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        This function gets the account_balance
        :return: The balance of the account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        This function gets the name of the account
        :return: The name of the account
        """
        return self.__account_name
