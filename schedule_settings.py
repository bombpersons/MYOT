# -*- coding: utf-8 -*-
# This file contains settings for a week's schedule
from block import Block
from series import Series

# EXAMPLE BLOCK
testBlock = Block()
testBlock.picker = 'default'
testBlock.ad_picker = 'default'
testBlock.autoAd("test")
testBlock.use_ads = True
testBlock.old_episodes = True
testBlock.series = [
	Series("test2"),
]

# ANOTHER BLOCK
anotherBlock = Block()
anotherBlock.picker = 'latest'
anotherBlock.series = [
	Series(auto="test"),
]


# ACTIVE BLOCKS
BLOCKS = (
	(testBlock, "Monday 11:10", "Monday 14:36"),
	(anotherBlock, "Monday 11:36", "Monday 17:10"),
)
