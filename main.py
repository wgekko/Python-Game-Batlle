from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# este juego se desarrolla siguiendo un tutorial de juegos
# de Udemy dictado por Joseph Delgadillo

print("\n\n ")
#print("NAME               MP                                   MP")
#
#print("NAME               MP                                   MP")
#print("                     _________________________          __________ ")
#print("Valor:   460/460  |                         |   65/65  |          |")
#print("NAME               MP                                   MP")
#print("                     _________________________          __________ ")
#print("Valor:   460/460  |                         |   65/65  |          |")

print("\n\n ")

# aqui se crea la magia negra
fire = Spell("Fire", 25 , 600, "black")
thunder = Spell("Thunder", 25 , 600, "black")
blizzard = Spell("Blizzard", 25 , 600, "black")
meteor = Spell("Meteor", 40 , 1200, "black")
quake = Spell("Quake", 14 , 140, "black")

# aqui creamos la magia blanca
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 35, 1200, "white")
curaga =Spell("Curaga", 50, 6000,"white")

# creando los items
pottion = Item("Potion", "potion", "Heals 50 HP", 50)
hipottion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpottion = Item("Super-Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9000)
megaelixer = Item("MegaElixer", "elixer", "Fully restores HP/MP of one party member", 9900)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


'''
# creado inicialmente para pre cargar los datos de magia de los jugadores
magic = [{"name" : "Fire", "cost": 10, "dmg": 100 },
         {"name" : "Thunder", "cost": 10, "dmg": 124},
         {"name" : "Blizzard", "cost": 10, "dmg": 100}]
'''
# se instancia a personas 
player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells= [fire, meteor, curaga]
player_items = [{"item": pottion,"quantity": 15},
                {"item": hipottion,"quantity": 5},
                {"item": superpottion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": megaelixer, "quantity": 2},
                {"item": grenade, "quantity": 5}]


player1 = Person("Juan  :", 3260, 135, 300, 34, player_spells, player_items)
player2 = Person("Pedro :", 4160, 185, 320, 34, player_spells, player_items)
player3 = Person("Jose  :", 3089, 175, 340, 34, player_spells, player_items)


enemy1 = Person("Enemigo#1", 18200, 225, 525, 25, enemy_spells, [])
enemy2 = Person("Enemigo#2", 11200, 180, 560, 325, enemy_spells, [])
enemy3 = Person("Enemigo#3", 11200, 180, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACK" + bcolors.ENDC)

while running:
    
    print("================================")
    
    print("\n\n")   
    print("Name                  HP                                   MP")    
    for player in players: 
        player.get_stats()
    
    print("\n")
    
    for enemy in enemies:
        enemy.get_enemy_stats()
    
        
    for player in players:
         
        player.choose_accion()
        #player.choose_magic()
        choice = input("   choose action : ")
        index = int(choice)-1    
        #print("you chose ,", choice)
        #print("you chose ;", player.get_spell_name(int(choice)))
        if index ==0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            
            enemies[enemy].take_damage(dmg)
            print("You attacked "+ enemies[enemy].name.replace("   ", "") +" for", dmg, "points of damage") # Enemy HP:" , enemy.get_hp())
            if enemies[enemy].get_hp() ==0:
                print(enemies[enemy].name.replace("   ","") + " has died.")
                del enemies[enemy]
                     
            
        elif index ==1:
            player.choose_magic()
            magic_choice = int(input("   Choose magic : "))-1
            
            if magic_choice == -1:
                continue            
            '''
            magic_dmg = player.generate_spell_damage(magic_choice)
            spell = player.generate_spell_damage(magic_choice)
            cost = player.get_spell_mp_cost(magic_choice)
            '''
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
    
            
            current_mp = player.get_mp
            
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\n Not enough MP\n" + bcolors.ENDC)
                continue
            
            player.reduce_mp(spell.cost)
            
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n"+ spell.name + "heals for", str(magic_dmg), "HP. "+ bcolors.ENDC)
                
            elif spell.type == "black":  
                enemy = player.choose_target(enemies)
            
                enemies[enemy].take_damage(magic_dmg)
                
                # enemy.take_damage(magic_dmg)
                
                print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage to "+enemies[enemy].name.replace("   ","") + bcolors.ENDC)
                
                if enemies[enemy].get_hp() ==0:
                    print(enemies[enemy].name.replace("   ","") + " has died.")
                    del enemies[enemy]
        
        
        elif index==2:
            player.choose_item()
            item_choice = int(input("   Choose item : "))-1
            
            if item_choice == -1:
                continue
            
            item = player.items[item_choice]["item"]        
           
            if player.items[item.choice]["quantity"] ==0:
               print(bcolors.FAIL + "\n" + "None left.... " + bcolors.ENDC)     
               continue
           
            player.items[item_choice]["quantity"] -= 1 
            
            if item.type == "pottion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "deals for ", str(item.prop), "HP " + bcolors.ENDC)
            elif item.type == "elixer":
                
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:    
                    player.hp = player.maxhp
                    player.mp= player.maxmp
                    
                print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP " + bcolors.ENDC)
            elif item.type == "attack":
                
                enemy = player.choose_target(enemies)
            
                enemies[enemy].take_damage(item.prop)
                
                #enemy.take_damage(item.prop)
                
                print(bcolors.FAIL + "\n" + item.name + "deals ", str(item.prop), "points of damage to"+ enemies[enemy].name + bcolors.ENDC)
               
                if enemies[enemy].get_hp() ==0:
                    print(enemies[enemy].name.replace("  ", "") + " has died.")
                    del enemies[enemy]
     
    # verificamos si la batalla no terminó     
    defeated_enemies = 0
    defeated_players = 0
    for enemy in enemies:
        if enemy.get_hp() ==0:
            defeated_enemies +=1
    
    for player in players:
        if player.get_hp() ==0:
            defeated_players +=1
    
    if defeated_enemies ==2:
        print(bcolors.OKGREEN + "You win (Ganaste) !!!", bcolors.ENDC)
        running = False
   
    # verificamos si el jugador gano    
    if enemy.get_hp() ==0:
        print(bcolors.OKGREEN + "You win (Ganaste) !!!", bcolors.ENDC)
        running = False
        
        
    # verificamos si el enemigo gano   
    elif defeated_players == 2:
        print(bcolors.FAIL + "Your enemies have defeated you (tus enemigos te ha derrotado)!!!"+ bcolors.ENDC)
        running= False
             
    # aqui tenemos el enemigo en face de ataque
    for enemy in enemies:         
        
        enemy_choice = random.randrange(0,2)
        if enemy_choice == 0:
            # eleccion de ataque 
            target = random.randrange(0,3)
            
            enemy_dmg = enemy.generate_damage()
            
            players[target].take_damage(enemy_dmg)
            
            print(enemy.name.replace("  ", "")+ " attacks"+ players[target].name.replace("   ","")+ "for", enemy_dmg) #,"Player HP: ", player.get_hp())
        
        elif enemy_choice == 1:
           spell, magic_dmg = enemy.choose_enemy_spell()
           enemy.reduce_mp(spell.cost)
           if spell.type == "white":
               enemy.heal(magic_dmg)
               print(bcolors.OKBLUE  + spell.name + "heals "+enemy.name + "for", str(magic_dmg), "HP." + bcolors.ENDC)
           elif spell.type =="black":
               #enemy=player.choose_target(enemies)
               target = random.randrange(0,3)
               
               players[target].take_damage(magic_dmg)
               
               print(bcolors.OKBLUE + "\n"+ enemy.name.replace("   ","")+" 's "+ spell.name +"deals", str(magic_dmg), "points of damage to "+ players[target].name.replace("   ","") + bcolors.ENDC)
               if players[target].get_hp ==0:
                   print(players[target].name.replace("   ","") + " has died")
                   del players[player]
           
           print("Enemy chose ", spell, "damage is ", magic_dmg)
                

#    print("-----------------------------------")
#    print("Enemy HP :", bcolors.FAIL + str(enemy.get_hp())+ "/" + str(enemy.get_max_hp())+ bcolors.ENDC + "\n")
    
#    print("Your HP: "+ bcolors.OKGREEN + str(player.get_hp())+ "/" + str(player.get_max_hp())+ bcolors.ENDC)
#    print("Your MP: "+ bcolors.OKBLUE + str(player.get_hp()) + "/"+ str(player.get_max_mp())+ bcolors.ENDC + "\n")
    
    
        
    
   
    


