#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random

def criaPlayer():
    
    player = ['name','lp','strength','potion']
    
    print('Tela de criação do Player :\n')
    
    #name = input('Digite o Nome : ')
    player[0] = 'gustavo'
    
    player[1] = 100
    
    player[2] = random.randrange(20,80)
    
    #Posição 0(Quantas possui) , posição 1 (minimo), posição 2 (maximo)
    player[3] = [0,0,5]
    
    #print('\nName : ',player[0],'\nLife Points : ',player[1],'\nStrength :', player[2], '\nLife potion :', player[3])
    
    return player
    
def enemy():
    
    enemy = ['name','life','drop']
    
    name = ('skeleton','gosth','thief','man lizard','werewolf','goblin')
    enemy[0] = random.choice(name)
    enemy[1] = random.randrange(50, 100)
    enemy[2] = random.randrange(0,10)
    
    
    #print('\nname: ',enemy[0],'\nlife : ',enemy[1],'\ndrop chance: ',enemy[2])
    
    return enemy

def continuePlay(option):
    
    
    while True:
        option = int(input('\n Deseja Continuar ? : \nDigite 1 para Não(True) ou 2 para Sim(False) \n'))
        
        if option==1 :
            print('op 1')
            return True
            break
        elif option == 2: 
            print('op 2')
            return False
            break
        else :
            print('porra meu irmão')
            continue
            
def batlle():
    control =  False
    num = 0
    playerSelf = ['null']
    enemySelf = ['null']
    
    playerSelf=criaPlayer()
    enemySelf=enemy()
    
    print ('\nLets the battle Beguin : \n*************\n')
    print('\nPlayer \n\nName : ',playerSelf[0],'\nLife Points :',playerSelf[1],'\nStrength :',playerSelf[2], '\nLife potion :',playerSelf[3])
    print('\nEnemy \n\nName: ',enemySelf[0],'\nLife : ',enemySelf[1],'\nDrop Chance: ',enemySelf[2])
    
    while control == False: 
        
        num = num+1
        
        print('\nRodada :',num,':')
        if playerSelf[1] <= 0:
            print('\nYou Die')
            break
        elif enemySelf[1]<=0:
            print('\nYou has Defet the ',enemySelf[0])
            break
        else:
            print('\nKeep Figthing')
            
            control = True
        
        
    
    print('\nfim do laço')
    

def play():
    
    print('jogando')

    control =  False
    op = 2
    
    num=0
    
    while control == False: 
        
        num = num+1
        print('interação : ',num,'op',op)
        
        batlle()
        control = continuePlay(op)
        
        
    
    print('\nfim do laço')
        
    
if __name__ == "__main__":   
    
    print('Dangeon Works')
    print('\n')
    #criaPlayer()
    #print('\n')
    #print('\n')
    #enemy()
    #print('\n')
    play()
    #batlle()




# In[80]:


import random 

foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))


# In[63]:


control = False 

#op = 1
op = int(input('Digite 1 para true ou 2 para false \n'))
print(op) 
if op == 1 :
    print('op 1')
    control = True
elif op == 2: 
    control = False
    print('op 2')
else :
    
    print('porra meu irmão')
    
print(control)


# In[17]:


def teste(tt):
    
    print(tt)
    
return True

print('teste de alguma coisa')
tt= 1
ctr = False
print(ctr)

ctr = teste(tt)
print(ctr)



# In[ ]:




