# This file contains settings for MYOT
from pickers import * # Import all the default pickers.
from players import * # Import all the default players.

# A list of all pickers that you want to be loaded.
PICKERS = {
	'default': DummyPicker,
	'random': RandomPicker,
	'latest': LatestEpisodePicker,
}
PICKER = 'random'

# A list of players to choose from
PLAYERS = {
	'mplayer': mPlayer,
}
PLAYER = 'mplayer'

# Extensions for the Series class to use when auto finding files.
SERIES_AUTOFIND_EXTENSIONS = [
	'mp4', 'mpg', 'flv', 'mpeg', 'avi', 'mkv',
]

# TIMER SLEEP
TIMER_SLEEP = 0.5

# SCHEDULE SLEEP
SCHEDULE_SLEEP = 0.5

# MANAGER SLEEP (How often the manager reloads the schedule)
MANAGER_SLEEP = 60

# DAYS OF THE WEEK SETTINGS
DAYS = {
	'Monday': 0,
	'Tuesday': 1,
	'Wednesday': 2,
	'Thursday': 3,
	'Friday': 4,
	'Saturday': 5,
	'Sunday': 6,
}
