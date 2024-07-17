#!/bin/python

logo =          """
   ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
             \n"""

class CurrencyExchange:
  currencies = {"USD":1.0, "EUR":0.85, "EGP":30.9, "RMB":6.5}

  def print_logo(self):
    print(logo)

  def print_currencies(self):
    for key in self.currencies:
      print(f" {key}: {self.currencies[key]}")

  def is_valid_currency(self, currency):
    return True if currency in self.currencies else False

  def exchange_one_currency(self, user_currency, target_currency):
    if self.is_valid_currency(user_currency):
      if self.is_valid_currency(target_currency):
        return (self.currencies[target_currency] * 1) / self.currencies[user_currency]
      else:
        raise ValueError(f" ValueError: '{target_currency}' is invalid currency")
    else:
      raise ValueError(f" ValueError: '{user_currency}' is invalid currency")

  def exchange(self, user_currency, user_amount, target_currency):
    if self.is_valid_currency(user_currency):
      if self.is_valid_currency(target_currency):
        return (self.currencies[target_currency] * user_amount) / self.currencies[user_currency]
      else:
        raise ValueError(f" ValueError: '{target_currency}' is invalid currency")
    else:
      raise ValueError(f" ValueError: '{user_currency}' is invalid currency")
