#If char is an "A" or char is an "a", print "X", instead of char

phrase = "A bird in the hand..."
for char in phrase:
  if char == "A" or char == "a":
    print "X",
  else: 
    print char,
