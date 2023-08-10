from account import Account
import pytest


def test_init():
    account1 = Account('Checking')
    account2 = Account('Savings')

    assert account1.get_name() == 'Checking'
    assert account1.get_balance() == pytest.approx(0)
    assert account2.get_name() == 'Savings'
    assert account2.get_balance() == pytest.approx(0)


def test_deposit():
    account1 = Account('Checking')
    account2 = Account('Savings')

    assert account1.deposit(100.0) is True
    assert account1.get_balance() == pytest.approx(100.0)
    assert account2.deposit(0) is False
    assert account2.get_balance() == pytest.approx(0)
    assert account1.deposit(-25.0) is False
    assert account1.get_balance() == pytest.approx(100.0)


def test_withdraw():
    account1 = Account('Checking')
    account2 = Account('Savings')

    account1.deposit(100.0)
    assert account1.withdraw(25.0) is True
    assert account1.get_balance() == pytest.approx(75.0)
    assert account1.withdraw(100.0) is False
    assert account1.get_balance() == pytest.approx(75.0)
    assert account1.withdraw(75.0) is True
    assert account1.get_balance() == pytest.approx(0)
    assert account2.withdraw(-100) is False
    assert account2.get_balance() == pytest.approx(0)
