#!/usr/bin/env python
# coding: utf-8

# In[8]:


# !/usr/bin/env python
# coding: utf-8

import random


def criaPlayer():
    player = ['name', 'lp', 'strength', 'potion']

    print('Tela de criação do Player :\n')

    # name = input('Digite o Nome : ')
    player[0] = 'gustavo'
    # [0] = vida atual // [1] = Max Vida 
    player[1] = [100,100]

    player[2] = random.randrange(20, 90)

    # Posição 0(Quantas possui) , posição 1 (minimo), posição 2 (maximo)
    player[3] = [1, 0, 5]

    # print('\nName : ',player[0],'\nLife Points : ',player[1],'\nStrength :', player[2], '\nLife potion :', player[3])

    return player


def enemy():
    enemy = ['name', 'life', 'stregth', 'drop']

    name = ('skeleton', 'gosth', 'thief', 'man lizard', 'werewolf', 'goblin')
    enemy[0] = random.choice(name)
    enemy[1] = random.randrange(50, 100)
    enemy[2] = random.randrange(10, 90)
    enemy[3] = random.randrange(8, 10)

    # print('\nname: ',enemy[0],'\nlife : ',enemy[1],'\ndrop chance: ',enemy[2])

    return enemy


def continuePlay(option):
    while True:
        option = int(input('\n Deseja Continuar ? : \nDigite 1 para SIM(True) ou 2 para NAO(False) \n'))

        if option == 1:
            print('op 1')
            return False
            break
        elif option == 2:
            print('op 2')
            return True
            break
        else:
            print('porra meu irmão')
            continue


def atack(stregntSelf):
    damage = 0

    damage = stregntSelf

    return damage


def dropPotion(equip,maxi,dropChance):
    
    print('\nTeste de drop\n Max=',maxi,'\n quantidade atual = ',equip,'\n Chance de drop = ' ,dropChance)
    
    if maxi>equip:
        if random.randrange(9,10) <= dropChance:
            print('O inimigo Dropou uma poção')
            return 1
        else:
            print('flopw')
            return 0
    else:
        return 0
    
def usePotion(playerSelf):
    
    print('\n******Poção usada*********')
    cure = random.randrange(30,100)
    playerSelf[1][0] = playerSelf[1][0]+cure
    print('\nBonus :',cure)
    if playerSelf[1][0]>playerSelf[1][1]:
        print('Player Life: ',playerSelf[1][1])
        return playerSelf[1][1]
    else:
        print('Player Life: ',playerSelf[1][0])
        return playerSelf[1][0]
    print('****************************')


def batlle():
    turno = 0
    control = False
    rodada = 0
    playerSelf = ['null']
    enemySelf = ['null']

    playerSelf = criaPlayer()
    enemySelf = enemy()

    print('\nLets the battle Beguin : \n*************************************************\n')
    print('\nPlayer \n\nName : ', playerSelf[0], '\nLife Points :', playerSelf[1][0], '\nStrength :', playerSelf[2],
          '\nLife potion :', playerSelf[3])
    print('\nEnemy \n\nName: ', enemySelf[0], '\nLife : ', enemySelf[1], '\nStrength: ', enemySelf[2],
          '\nDrop Chance: ', enemySelf[3])
    print('*************************************************')

    while control == False:

        rodada = rodada + 1

        print('\nRodada :', rodada, ':\nVida ', playerSelf[0], ' :', playerSelf[1][0], '\nVida ', enemySelf[0], ' :',
              enemySelf[1])

        if playerSelf[1][0] <= 0:
            print('\nYou Die')
            break
        elif enemySelf[1] <= 0:
            print('\nYou has Defeated the ', enemySelf[0])
            playerSelf[3][0]=dropPotion(playerSelf[3][0],playerSelf[3][2],enemySelf[3])
            break

        else:
            print('\n')
            # control = True

        if turno == 0:
            print('Turno Player')
            turno = turno + 1
            if playerSelf[1][0]<50&playerSelf[3][0]>0:
                playerSelf[3][0]= playerSelf[3][0]-1
                playerSelf[1][0] = usePotion(playerSelf)
                
            enemySelf[1] = enemySelf[1] - int(atack(playerSelf[2]))
            print('Voce atacou o ', enemySelf[0], ' ! \nVida :', enemySelf[1])
            
        elif turno == 1:
            print('Turno Enemy')
            turno = turno - 1
            playerSelf[1][0] = playerSelf[1][0] - int(atack(enemySelf[2]))
            print('Voce foi atacado pelo o ', enemySelf[0], ' ! \nVida :', playerSelf[1])

    print('\nfim do laço')
    print('*************************************************')
    print('\nPlayer \n\nName : ', playerSelf[0], '\nLife Points :', playerSelf[1][0], '\nStrength :', playerSelf[2],
          '\nLife potion :', playerSelf[3])
    print('\nEnemy \n\nName: ', enemySelf[0], '\nLife : ', enemySelf[1], '\nStrength: ', enemySelf[2],
          '\nDrop Chance: ', enemySelf[3])


def play():
    print('jogando')

    control = False
    op = 2

    num = 0

    while control == False:
        
        num = num + 1
        
        print('interação : ', num, 'op', op)
        
        batlle()
        
        control = continuePlay(op)

    print('\nfim do laço')


if __name__ == "__main__":
    print('Dungeon World')
    print('\n')
    # criaPlayer()
    # print('\n')
    # print('\n')
    # enemy()
    # print('\n')
    play()
    # batlle()


# In[ ]:




