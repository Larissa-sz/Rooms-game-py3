from room import Room
from character import Enemy
from character import Friend
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on every wall")

ballroom = Room ("Ballroom")
ballroom.set_description("A vast room with shiny decorations")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there.")
ballroom.set_character(catrina)

candle = Item("Candle")
candle.set_description("A candle to see your way through dark passages")
kitchen.set_item(candle)

current_room = kitchen
backpack = []

dead = False

while dead == False:
  
  print("\n")
  current_room.get_details()
  
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
    
  stuff = current_room.get_item()
  if stuff is not None:
    stuff.describe()
  
  command = input("> ")
  
  if command in ["north", "south", "east", "west"]:
    # Move in the given direction
    current_room = current_room.move(command)
  elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
      inhabitant.talk()
    else:
      print "There's no one in here"
  elif command == "fight":
    # You can check whether an object is an instance of a particular
    # class with isinstance() - useful! This code means
    # "If the character is a Friend"
    if inhabitant == None or isinstance(inhabitant, Friend):
      print("There is no one here to fight with")
    else:
      # Fight with the inhabitant, if there is one
      print("What will you fight with?")
      fight_with = input()
      if fight_with in backpack: 
        if inhabitant.fight(fight_with) == True:
          # What happens if you win?
          print("Hooray, you won the fight!")
          current_room.character = None
        else:
          # What happens if you lose?
          print("Oh dear, you lost the fight.")
          print("That's the end of the game")
          dead = True
      else:
        print "You don't have that item in your backpack!"
  elif command == "hug":
    if isinstance(inhabitant, Enemy):
      print("I wouldn't do that if I were you...")
    else:
      inhabitant.hug()
      
  elif command == "take":
    new_item = stuff.name
    backpack.append(new_item.lower())
    current_room.item = None
