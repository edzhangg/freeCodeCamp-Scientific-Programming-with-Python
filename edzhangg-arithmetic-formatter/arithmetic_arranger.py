def arithmetic_arranger(problems, answers = False):
  if len(problems) > 5:
    return("Error: Too many problems.")
  else:
    counter = 0
    firstLine = ""
    secondLine = ""
    dashes = ""
    fourthLine = ""
    while counter < len(problems):
      aProblem = problems[counter]
      aProblem = aProblem.split()
      if aProblem[1] == "*" or aProblem[1] == "/":
        return("Error: Operator must be '+' or '-'.")
      if aProblem[0].isnumeric() == False or aProblem[2].isnumeric() == False:
        return("Error: Numbers must only contain digits.")
      if int(aProblem[0]) > 9999 or int(aProblem[2]) > 9999:
        return("Error: Numbers cannot be more than four digits.")
      num1 = int(aProblem[0])
      num2 = int(aProblem[2])
      length = len(aProblem[0])
      if len(aProblem[2]) > length:
        length = len(aProblem[2]) + 2
        counter2 = 0
        firstLineNumber = ""
        while counter2 < length-len(aProblem[0]):
          firstLineNumber += " "
          counter2 += 1
        firstLineNumber += str(num1)
        firstLine += firstLineNumber
        secondLineNumber = aProblem[1]
        secondLineNumber += " "
        secondLineNumber += str(num2)
        secondLine += secondLineNumber
      else:
        length += 2
        firstLineNumber = "  "
        firstLineNumber += str(num1)
        firstLine += firstLineNumber
        counter2 = 0
        secondLineNumber = aProblem[1]
        while counter2 < (length-len(aProblem[2])-1):
          secondLineNumber += " "
          counter2 += 1
        secondLineNumber += str(num2)
        secondLine += secondLineNumber
      dashes += ("-"*length)
      if aProblem[1] == "+":
        ans = num1 + num2
      else:
        ans = num1 - num2
      strans = str(ans)
      if len(strans) < length:
        diff = length - len(strans)
        fourthLine += " " * diff
      fourthLine += strans
      counter += 1
      if counter < len(problems):
        firstLine += "    "
        secondLine += "    "
        dashes += "    "
        fourthLine += "    "
    arranged_problems = ""
    if answers == False:
      arranged_problems = firstLine + "\n" + secondLine + "\n" + dashes
    else:
      arranged_problems = firstLine + "\n" + secondLine + "\n" + dashes + "\n" + fourthLine
    return arranged_problems