name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.000 # inches
weight = 180.0000000 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
metric_height = height * 2.14
metric_weight = weight * 0.4525925

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
# added for self study 
print "Here are %s. 's stats in the metric system." % name
print "He weighs", metric_weight, "Kilograms."
print "He is", metric_height, "Centimeters tall."

