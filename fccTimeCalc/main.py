def add_time(current_time, duration, day=None):
  days_message = ""
  day_of_week = ""
  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  changing_format = {"AM":"PM", "PM":"AM"}

  # get time (hour, minute, and format) for the start time and time adjust arguments
  current_time_hour = int(current_time.split(" ")[0].split(":")[0])
    # split at " " to split the time from the am pm, ei 11:45 pm -> [0] = 11:45 [1] = pm
    # then split at : to get the hour and minute.
    # We only keep hour here [0] = 11 [1] = 45
  current_time_format = current_time.split(" ")[1].upper()
  duration_hour = int(duration.split(":")[0])
    # split adjustment time to separate hour from minute
  minutes_calculated = int(current_time.split(" ")[0].split(":")[1]) + int(duration.split(":")[1])
    # get the minutes from the start time and add that to the minutes from the time to adjust

  # check if added minutes are greater than 60 and convert to hour if so
  if minutes_calculated > 60:
    minutes_calculated -= 60
    duration_hour += 1

  # calculate next time hour, format and total days
  count_hours = (current_time_hour + duration_hour) % 12
  count_days = (current_time_hour + duration_hour) // 24
  count_format = (current_time_hour + duration_hour) % 24

  if (current_time_hour + duration_hour) >= 12 and current_time_format == "PM":
      days_later = count_days + 1
  else:
      days_later = count_days

# assigns count_hours to next_time_hours, unless it's 0. If it is 0, then 12 is used instead (since in 12-hour time, 0 is represented as 12).
  if count_hours != 0:
      next_time_hours = count_hours
  else:
      next_time_hours = 12

# switches AM to PM, or PM to AM, using the dictionary changing_format, if count_format >= 12. Otherwise, keeps the same time format.
  if count_format >= 12:
      next_time_format = changing_format[current_time_format]
  else:
      next_time_format = current_time_format

  # if the sum of the current hour and duration is exactly 12 and the time format is "PM", then set next_time_hours to 0. Otherwise, keep next_time_hours as it is.
  if (current_time_hour + duration_hour) == 12 and current_time_format == "PM":
        next_time_hours = 0

  # set days later message
  if days_later > 0:
    days_message = " (next day)" if days_later == 1 else f" ({days_later} days later)"

  # determine what day of the week it will be after a given number of days, starting from a provided current day.
  if day:
    current_day_index = week.index(day.capitalize()) # converts 'day' argument to title case ei "wednesday" to "Wednesday", and then finds the index of that day in the week list var ei Wednesday will be 2
    reset_week = week[current_day_index:] + week[:current_day_index]
        # this manipulates the week list so that it starts from the current_day_index ei week = ["Wednesday", "Thursday", "Friday", ...]
        # this is done to make it easier to index from the current day when we add days
    next_day_index = days_later % 7 # make sure the next_day_index gives a valid index for a 7 day week
    day_of_week = f", {reset_week[next_day_index]}"
        # building part of the string that will show the new day of the week
        # ei if today is "Wednesday" and days_later is 3, then next_day_index is 3, and reset_week[3] is "Saturday". day_of_week = ", Saturday"

  return f"{next_time_hours}:{str(minutes_calculated).zfill(2)} {next_time_format}{day_of_week}{days_message}"

def main():
    print('Welcome to the Freecodecamp challange: Time Calculator \n\n This python file accepts input in the form of ["start time", "time to change by", "start day"]. Start day is optional \nei add_time("11:43 PM", "24:20", "tueSday")')
    start_time = input('Enter your start time: ')
    time_change = input('Enter your time to adjust by: ')
    add_start = input("Enter start day (press Enter to skip): ") or False
    user_input = add_time(start_time, time_change, add_start)
    print(user_input)

main()