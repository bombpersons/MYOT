# -*- coding: utf-8 -*-

from myot.schedule import Schedule
from myot.block import Block
from myot.series import Series
from myot.timer import Timer
from myot import settings

if __name__ == "__main__":
	scheduler = Schedule()
	
	block = Block()
	block.picker = 'random'
	block.new_episodes = True
	
	series = Series()
	series.auto("test")
	series2 = Series()
	series2.auto("test2")
	
	block.series = [series, series2]
	
	timer = Timer()
	scheduler.add("3 19:50", "3 23:00", "%d %H:%M", block)
	
	scheduler.start()
	
	while True:
		pass
