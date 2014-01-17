name = 'Zed A. Shaw'
age = 35
height = 56
height_in_cm = 2.56
weight = 180
weight_in_kg = weight * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches tall (%r cm)." % (height, height_in_cm)
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffe." % teeth

# this line is tricky, try to to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height, weight, age + height + weight)