#   codingbat code practice
#   We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
#   We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

#   parrot_trouble(True, 6) -> True
#   parrot_trouble(True, 7) -> False
#   parrot_trouble(False, 6) -> False

def parrot_trouble(talking, hour):
    if talking and hour < 7:
        return True
    if talking and hour > 20:
        return True
    return False

if parrot_trouble(True, 6):
    print "We are in trouble"
else:
    print "We are not in trouble"

if parrot_trouble(True, 7):
    print "We are in trouble"
else:
    print "We are not in trouble"

if parrot_trouble(False, 6):
    print "We are in trouble"
else:
    print "We are not in trouble"

