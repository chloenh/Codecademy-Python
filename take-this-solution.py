#Add a key to inventory called 'pocket'

#Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'

#.sort() the items in the list stored under the 'backpack' key

#Then .remove('dagger') from the list of items stored under the 'backpack' key

#Add 50 to the number stored under the 'gold' key

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

inventory['pouch'].sort() 

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50
