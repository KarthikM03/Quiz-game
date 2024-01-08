import random
def start():
    print("\n\n")
    g= input("Click (ENTER) to start the game: ")
    return Game(g)
    
def Game(a): 
    if  a == '':
        qtn=[['what is the capital of INDIA ?','Mumbai','Hyderabad','Delhi','Goa','C'],
             ['3 + 5 = ___', '8','9','7','35','A'],
             ['Taj mahal is located at ?','Hyderabad','Mysore','Chennai','Agra','D'],
             ['What country drinks the most coffee per capita?','England','Hyderabad','Finland','Goa','C'],
             ['How many bones do we have in an ear?', '4','3','6','2','B'],
             ['Which planet has the most moons ?','Mars','Saturn','Venus','Jupiter','B'],
             ['who set a new record for most number of sixes by an individual in an odi innings ?','Eoin Morgan','Rohit sharma','AB de Villiers','Shahid Afridi','A'],
             ['who was the first indian ruler who had territory outside india', 'Kanishka','Bimbisara','Chandragupta Maurya','Raja Raja Chola','A'],
             ['Upanishads are books on ___ ?','Religion','Philosophy','Yoga','Law','B']
            ]
        random.shuffle(qtn)    
        PM=[0,100,200,500,1000,2000,5000,10000,20000,50000] 
        m=0
        amt = 0
        for i in range(0,len(qtn)):
            qt= qtn[i]
            print()
            print()
            print('*'*40)
            print(f" Question for rs.{PM[i+1]}")
            print(f"{i+1}. {qt[0]}")
            print(f"A. {qt[1]}                            B. {qt[2]}")
            print(f"C. {qt[3]}                            D. {qt[4]}")
            k= input("Enter your answer (A-D) or Q to quit: ").upper()
            if k== 'Q':
                m= PM[i]
                print("You QUIT the game !")
                print("You got rs.",m)
                return start()
            elif k == qt[-1]:
                print('CORRECT! :)')
                if i == 4 :
                    m =PM[5]
                    print("__________LEVEL3__________")
                elif i == 6 :
                    m =PM[7]
                    print("__________LEVEL4__________")
                elif i == 2 :
                    m =PM[3]
                    print("__________LEVEL2__________")
                elif i == 8 :
                    m =PM[9]
                    print("Congratulations you completed all levels :)")
                    print("You got rs.",m)
                    return start()
            else : 
                print("WRONG! :(")
                print(f"You answered {i} Questions Correctly!")
                print("you got rs.",m)
                return start()
               
start()