# This module contains functions to help figure out the full date from,
# just a week day and a time.

import time
import settings

# GET DATE -------------------------------------------------------------
# Returns the day of the year
def getDate(day):
	# Get the current day of the year
	today_year = int(time.strftime("%j"))
	
	# And get the day
	today = time.strftime("%A")
	
	# Get the start of the week
	start_of_week = today_year - settings.DAYS[today]
	
	# If the number is negative, we need to sort that out
	if start_of_week < 0:
		# So this week must be on the boundary of new years day.
		# So we can just add this number to 365
		start_of_week = 365 + start_of_week
		
	# Okay, now we have the start of the week, so we can start to calculate
	# when the week days are
	# Day should be this:
	final_day = start_of_week + settings.DAYS[day]
	
	# However if we are at the boundary of a year, this will mess up.
	# It will be more than 365
	# So calculate the proper day
	if final_day > 365:
		final_day = final_day - 365
		
	# Now we should have a proper day
	return final_day
