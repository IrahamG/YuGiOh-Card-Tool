import yugioh
import textwrap

def getCard(query):
    print("\n")

    try:
        cards = yugioh.get_cards_by_name(keyword = query)
        cardquery = cards.list[0]
        card = yugioh.get_card(card_name = cardquery)
        
        print("-----------------------------------------------------")
        print("ID:", card.id)
        print(card.name)
        print(card.type)
        print(card.race)

        print("\n")
        cardDesc = textwrap.dedent(card.description).strip()
        print(textwrap.fill(cardDesc, width=60))
        print("\n")

        if "Monster" in card.type:
            print("ATK:", card.attack)
            print("DEF:", card.defense)
            print("Archetype:", card.archetype)
            print(card.attribute)
            if "Link" in card.type:
                print("Link Rating:", card.linkval)
                print("Link Markers:", card.linkmarkers)
            else:
                print("LVL:", card.level)

        print("-----------------------------------------------------")
        print("\n")
        
    except:
        print("Carta no encontrada")
        print("\n")

# Funciont to get banlist depending on the user input. The only avbailable options are
# 'ocg', 'tcg', 'goat'
def getBanlist(blist):
    banlist = yugioh.get_banlist(banlist=blist)
    searchString = 'ban_' + blist

    semiList = []
    limitedList = []
    forbiddenList = []

    for element in banlist.list:
        if element[1][searchString] == 'Limited':
            limitedList.append(element[0])
        elif element[1][searchString] == 'Semi-Limited':
            semiList.append(element[0])
        elif element[1][searchString] == 'Banned':
            forbiddenList.append(element[0])

    print('\n') 
    print("---------------------- FORBIDDEN -------------------------")
    for element in forbiddenList:
        print(element)
    print("---------------------- LIMITED -------------------------")
    for element in limitedList:
        print(element)
    print("---------------------- SEMI-LIMITED -------------------------")
    for element in semiList:
        print(element)
    print('\n')

# ------------------------------- Main loop ------------------------------
while(True):
    print("""Bienvenido, elija una opción:
    1. Busqueda de carta
    2. Obtener banlist
    3. Salir
    """)
    option = int(input("Ingrese la opción: "))

    if option == 1:
        query = input("Ingrese nombre de la carta: ")
        getCard(query)
    
    if option == 2:
        listType = input("""Type the banlist to get: (tcg, ocg, goat) """)
        getBanlist(listType)
        
    if option == 3:
        break


