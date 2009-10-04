# -*- coding: utf-8 -*-
# This file contains settings for a week's schedule
from block import Block
from series import Series

# EXAMPLE BLOCK
testBlock = Block()
testBlock.picker = 'random'
testBlock.auto(".")
testBlock.old_episodes = True

# ANOTHER BLOCK
anotherBlock = Block()
anotherBlock.picker = 'latest'
anotherBlock.series = [
	Series(auto="test"),
]


# ACTIVE BLOCKS
BLOCKS = (
	(testBlock, "Sunday 10:10", "Sunday 13:25"),
	(anotherBlock, "Sunday 13:25", "Sunday 17:10"),
)
