#!/bin/python

from currencyExchange import CurrencyExchange
import time
import os

def user_experience(user_currency:str, target_currency:str):
  print("\n Analyzing your request... please wait")
  time.sleep(3)
  print(f" Checking for {target_currency}'s best rates available..... please wait")
  time.sleep(3)
  print(f" Getting a discount price for {user_currency}..... please wait")
  time.sleep(3)
  print(f" Preparing the deal from {user_currency} to {target_currency}..... please wait")
  time.sleep(3)

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")

def user_continue(user_choice:str) -> bool:
  if user_choice == "N":
    return False
  elif user_choice == "Y":
    return True
  else:
    raise ValueError(f" ValueError: '{user_choice}' is invalid choice")

while True:
  try:
    clear_screen()
    print("\n Welcome to currency converter:")

    currency = CurrencyExchange()
    currency.print_logo()
    currency.print_currencies()
    user_currency = input("\n Enter a currency to convert from: ").upper()
    user_amount = float(input(" Enter the amount: "))
    target_currency = input(" Enter a currency to convert to: ").upper()
    confirm = input(f"\n You entered {user_amount} {user_currency} to convert into {target_currency}. comfirm? (Y/N): ").upper()

    if confirm == "N":
      user_continue_choice = input("\n Do you want to perform another conversion? (Y/N): ").upper()
      if user_continue(user_continue_choice) == False:
        break
      else:
        continue
    elif confirm != "Y":
      raise ValueError(f" ValueError: '{confirm}' is invalid input")

    user_experience(user_currency, target_currency)
    one_currency_result = currency.exchange_one_currency(user_currency, target_currency)
    clear_screen()
    print(f"\n Exchange rate: 1 {user_currency} = {one_currency_result} {target_currency}")
    user_currencies_result = currency.exchange(user_currency, user_amount, target_currency)
    print(f" {user_amount} {user_currency} is equal to {user_currencies_result} {target_currency}")
    user_accept = input("\n Do you accept this transaction? (Y/N): ").upper()

    if user_accept == "Y":
      print("\n The operation was completed successfully.")
    elif user_accept == "N":
      print("\n Transcation canceled.")
    else:
      raise ValueError(f" ValueError: '{user_accept}' is invalid choice")

    user_continue_choice = input(" Do you want to perform another conversion? (Y/N): ").upper()

    if user_continue(user_continue_choice) == False:
      break
  except ValueError as VE:
    print(VE)
    break
