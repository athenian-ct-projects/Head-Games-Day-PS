# Football player simulator and adventure game
# this is a choose your own path game

#beginning of the game/ enter a name
print("This is a choose your own path game. You will be a football player, and you will have to make decisions that will influence your career: ")

x = input(str("to begin the game enter your football player's name: "))
print("Alright you are ready to begin, " + x)

#functions 

def catch():
  for x in range (random.randint(4,8)):
    print("you caught a ball!")

def catch2():
  for x in range (random.randint(1,5)):
    print("you caught a ball!")



#NFL or college
y = input("YOUR FIRST BIG DECISION! Do you want to go straight to the NFL or finish college and risk an injury? for NFL type football, for college type college: ")

while y != "football" and y != "college":
  y = input("please type football or college! ")


if y == "football":
  print("your talents have been recognized by the NFL and you have been recruited!")
else:
  print("your academic commitment is recognized for being special! After your year in college you have been recruited")


#draft or undrafted
z = input("BIG DECISION! Do you want to participate in the draft or be undrafted? For draft type draft, for undrafted type undrafted: ")

if z == "draft":
  print("You have been drafted by the Miami Dolphins! Don't worry they are in rebuild")
elif z == "undrafted":
  print("You have been picked up off the waver wire by the GREEN BAY PACKERS! You have a shot at getting a ring in your first season!")
else:
  print("please enter a valid name, You have been drafted the ATLANTA FALCONS! Solid middle of the pack team")



#leader or follower
a = input("BIG DECISION! Do you want to become a leader or take a secondary role on your new team? Type leader for leader or follower for secondary role: ")

while a != "leader" and a != "follower":
  a = input("please type leader or follower! ")

if a == "leader":
  print("your coach and teamates have noticed your leadership, but they blame you for their most recent loss. Try and get back on their good side")
else:
  print("your talent goes unoticed by your coaches and teammates, try putting yourself out there for more playing time")


#money or better team
b = input("BIG DECISION! After a few years in the league your contract is up, do you want a bigger contract or play for a better team for less money? Type money or team: ")

while b != "money" and b != "team":
  b = input("please type money or team! ")

if b == "money":
  print("you have been picked up in free agency by the ARIZONA CARDINALS, but you got your big money")
else:
  print("you have taken less money, but secured a spot on a really good San Fransisco 49ers team")


#stats or wins
c = input("BIG DECISION! Would you rather chase stats and become a legendary player or get wins by being a team player? Type stats or wins: ")

while c != "stats" and c != "wins":
  c = input("please type stats or wins! ")

if c == "stats":
  print("you have broken the yards record for a single season, but your team didn't make the playoffs")
else: 
  print("you have had an average year, but your team won their division and you might be on your way to a ring")


print("PLEASE GO TO NEXT BLOCK")

