from myot.timer import Timer

def ring():
	print "RINGING"
	
def running():
	print "..."

def over():
	print "TIME UP"

if __name__ == "__main__":
	timer = Timer()
	timer.ring = ring
	timer.running = running
	timer.over = over
	
	timer.activate("2009 10 3 11:45", "2009 10 3 11:46", "%Y %m %d %H:%M")
	
	while 1:
		pass
