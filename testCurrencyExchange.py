#!/bin/pithon

from currencyExchange import CurrencyExchange
from pytest import fixture, raises

@fixture
def currency():
  currency = CurrencyExchange()
  return currency

def test_is_valid_currency_with_valid_input(currency):
  assert currency.is_valid_currency("USD")
  assert currency.is_valid_currency("EGP")
  assert currency.is_valid_currency("RMB")
  assert currency.is_valid_currency("EUR")

def test_is_valid_currency_with_invalid_input(currency):
  assert not currency.is_valid_currency("usd")
  assert not currency.is_valid_currency("egp")
  assert not currency.is_valid_currency("UNE")

def test_exchange_one_currency_with_valid_input(currency):
  assert currency.exchange_one_currency("EGP", "USD") == (currency.currencies["USD"] * 1) / currency.currencies["EGP"]
  assert currency.exchange_one_currency("USD", "EGP") == (currency.currencies["EGP"] * 1) / currency.currencies["USD"]
  assert currency.exchange_one_currency("RMB", "EGP") == (currency.currencies["EGP"] * 1) / currency.currencies["RMB"]
  assert currency.exchange_one_currency("EGP", "EUR") == (currency.currencies["EUR"] * 1) / currency.currencies["EGP"]

def test_exchange_one_currency_with_invalid_input(currency):
  with raises(ValueError):
    assert currency.exchange_one_currency("egp", "usd")
  with raises(ValueError):
    assert currency.exchange_one_currency("USD", "egp")
  with raises(ValueError):
    assert currency.exchange_one_currency("EGP", "usd")
  with raises(ValueError):
    assert currency.exchange_one_currency("egp", "USD")
  with raises(ValueError):
    assert currency.exchange_one_currency("rmk", "usi")
  with raises(ValueError):
    assert currency.exchange_one_currency("RST", "JPU")

def test_exchange_with_valid_input(currency):
  assert currency.exchange("EGP", 1000, "USD") == (currency.currencies["USD"] * 1000) / currency.currencies["EGP"]
  assert currency.exchange("USD", 1000, "EGP") == (currency.currencies["EGP"] * 1000) / currency.currencies["USD"]
  assert currency.exchange("EGP", 1000, "EUR") == (currency.currencies["EUR"] * 1000) / currency.currencies["EGP"]
  assert currency.exchange("RMB", 1000, "EGP") == (currency.currencies["EGP"] * 1000) / currency.currencies["RMB"]

def test_exchange_with_invalid_input(currency):
  with raises(ValueError):
    assert currency.exchange("egp", 1000, "usd")
  with raises(ValueError):
    assert currency.exchange("EGP", 1000, "usd")
  with raises(ValueError):
    assert currency.exchange("egp", 1000, "USD")
  with raises(ValueError):
    assert currency.exchange("EGY", 1000, "USD")
  with raises(ValueError):
    assert currency.exchange("EGP", 1000, "USB")
  with raises(ValueError):
    assert currency.exchange("usi", 1000, "rmk")
