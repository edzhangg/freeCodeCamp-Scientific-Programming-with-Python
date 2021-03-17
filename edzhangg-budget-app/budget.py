class Category:
  def __init__(self, name, ledger=[]):
    self.name = name
    self.ledger = []
    self.withdrawals = 0
  def deposit(self, amount, description=""):
    amount = amount
    description = description
    self.ledger.append({"amount": amount, "description": description})
    return(self.ledger)
  def withdraw(self, amount, description=""):
    amount = amount
    description = description
    check = self.check_funds(amount)
    if check == True:
      self.withdrawals += amount
      amount *= -1
      self.ledger.append({"amount": amount, "description": description})
      return(True)
    else:
      return(False)
  def get_balance(self):
    lenLedger = len(self.ledger)
    counter = 0
    cashAvailable = 0
    while counter < lenLedger:
      cashAvailable += self.ledger[counter]["amount"]
      counter += 1
    return(cashAvailable)
  def transfer(self, amount, name):
    amount = amount
    check = self.check_funds(amount)
    if check == False:
      return(False)
    else:
      name = name
      self.withdraw(amount, "Transfer to " + name.name)
      name.deposit(amount, "Transfer from " + self.name)
      return(True)
  def check_funds(self, amount):
    lenLedger = len(self.ledger)
    counter = 0
    cashAvailable = 0
    while counter < lenLedger:
      cashAvailable += self.ledger[counter]["amount"]
      counter += 1
    amount = amount
    if amount > cashAvailable:
      return(False)
    else:
      return(True)
  def __str__(self):
    output = ""
    name = self.name
    lenName = len(name)
    starTotal = 30 - lenName
    rightStar = int(starTotal / 2)
    leftStar = 30 - lenName - rightStar
    output += ("*" * leftStar) + name + ("*" * rightStar) + "\n"
    lenLedger = len(self.ledger)
    counter = 0
    total = 0
    while counter < lenLedger:
      amount = self.ledger[counter]["amount"]
      total += amount
      description = self.ledger[counter]["description"]
      if len(description) > 23:
        counter1 = 0
        temp = ""
        while counter1 < 23:
          temp += description[counter1]
          counter1 += 1
        description = temp
      else:
        while len(description) < 23:
          description += " "
      counter2 = 0
      while (len(str("%.2f" % amount)) + counter2) < 7:
        description += " "
        counter2 += 1
      output += (description + "%.2f" % amount + "\n")
      counter += 1
    output += ("Total: " + str(total))
    return(output)

def create_spend_chart(categories):
  output = "Percentage spent by category\n"
  categories = categories
  lenList = len(categories)
  totalSpent = 0
  counter = 0
  while counter < lenList:
    name = categories[counter]
    totalSpent += name.withdrawals
    counter += 1
  counter1 = 0
  percent = []
  while counter1 < lenList:
    name = categories[counter1]
    fraction = name.withdrawals / totalSpent
    fraction *= 100
    percent.append(fraction - (fraction % 10))
    counter1 += 1
  counter2 = 100
  while counter2 != -10:
    if len(str(counter2)) < 3:
      output += " "
      if len(str(counter2)) < 2:
        output += " "
    output += str(counter2) + "| "
    counter3 = 0
    while counter3 < lenList:
      if counter2 <= percent[counter3]:
        output += "o  "
      else:
        output += "   "
      counter3 += 1
    output += "\n"
    counter2 -= 10
  output += ("    -" + ("---"*lenList) + "\n")
  counter3 = 0
  longestString = 0
  while counter3 < lenList:
    if len(categories[counter3].name) > longestString:
      longestString = len(categories[counter3].name)
    counter3 += 1
  counter4 = 0
  while counter4 < longestString:
    output += " " * 5
    counter5 = 0
    while counter5 < lenList:
      if counter4 < len(categories[counter5].name):
        output += (categories[counter5].name[counter4] + "  ")
      else:
        output += "   "
      counter5 += 1
    counter4 += 1
    if counter4 < longestString:
      output += "\n"
  return(output)
