def add_time(start, duration, dates = "none"):
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  timeOfDay = ["AM", "PM"]
  startTime = start.split()
  startTime1 = startTime[0].split(":")
  startHour = int(startTime1[0])
  startMin = int(startTime1[1])
  startAMPM = startTime[1]
  if startAMPM == timeOfDay[0]:
    tODcounter = 0
  else:
    tODcounter = 1
  duration = duration.split(":")
  durationHour = int(duration[0])
  durationMin = int(duration[1])
  daysLater = 0
  mins = startMin + durationMin
  while mins > 59:
    durationHour += 1
    mins -= 60
  hours = startHour + durationHour
  stop = False
  while hours >= 12 and stop == False:
    if hours == 12:
      stop = True
    if hours != 12:
      hours -= 12
    tODcounter += 1
    if tODcounter == 2:
      daysLater += 1
      tODcounter = 0
  if dates == "none":
    if daysLater == 0:
      new_time = str(hours) + ":" + str("%02d" % mins) + " " + timeOfDay[tODcounter]
    elif daysLater == 1:
      new_time = str(hours) + ":" + str("%02d" % mins) + " " + timeOfDay[tODcounter] + " " + "(next day)"
    else:
      new_time = str(hours) + ":" + str("%02d" % mins) + " " + timeOfDay[tODcounter] + " " + "(" + str(daysLater) + " days later)"
  else:
    dates = dates
    dateCounter = 0
    counter = 0
    while counter < 7:
      if days[counter].lower() == dates.lower():
        dateCounter = counter
      counter += 1
    daysLater1 = daysLater
    while daysLater1 != 0:
      dateCounter += 1
      daysLater1 -= 1
      if dateCounter == 7:
        dateCounter = 0
    if daysLater == 0:
      new_time = str(hours) + ":" + str("%02d" % mins) + " " + timeOfDay[tODcounter] + ", " + days[dateCounter]
    elif daysLater == 1:
      new_time = str(hours) + ":" + str("%02d" % mins) + " " + timeOfDay[tODcounter] + ", " + days[dateCounter] + " " + "(next day)"
    else:
      new_time = str(hours) + ":" + str("%02d" % mins) + " " + timeOfDay[tODcounter] + ", " + days[dateCounter] + " " + "(" + str(daysLater) + " days later)"
  return new_time