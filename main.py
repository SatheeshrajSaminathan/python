#pokemon game
#objectives
#create a pokemon
#letting user to pick his pokemon and opponent pokemon
#fight
#getting the winner based on its type
#feed the lost pokemon
import random
class pokemon: #creating a pokemon with its type and hp
    def __init__(self,name,p_type,hp):
        self.name=name
        self.p_type=p_type
        self.hp=hp
    def __str__(self): #this one will execute whenever we use print on object
        return f"\n{self.name}({self.p_type})({self.hp})"
    def feed(self): #feeding the pokemon which lost the fight
        self.hp+='100'
        print(f'{self.name} hp is 100 now and ready for next fight')
    def battle(self,other):
        print(f'\nBattle gonna start between  {self.name} and {other.name}')
        result1=self.fight(self.p_type,other.p_type) #calling the static method to get the winner
        if result1=='lose':
            print(f' your pokemon lost the fight \n{self.name} hp is zero now')
            self.hp='0'
            print(f'feeding {self.name} for the next fight')
            self.feed()
        elif result1=='win':
            print(f' your pokemon won the fight \n {other.name} hp is zero now')
            other.hp='0'
            print(f'feeding {other.name} for the next fight')
            other.feed()
        else:
            print('its a tie')


    @staticmethod
    def fight(a,b):
        points = {0: 'lose', 1: 'win', -1: 'tie'}
        val={'water':0,'grass':1,'fire':2,'electric':3} #
        winlosematrix=[[-1,0,1,0],[1,-1,0,1],[0,1,-1,1],[1,0,0,-1]]#defining win lose condition
        # water beats fire , grass beats water,
        result= winlosematrix[val[a]][val[b]]#using slicer method to get the winner
        return points[result]

print('welcome to pokemon battle')
print('\nThe pokemons which are available for battle are mentioned below with their power type and health')
print('\nplease select one for your side')
bulboser=pokemon('bulboser','grass','100')
charmander=pokemon('charmander','fire','100')
squirtle=pokemon('squirtle','water','100')
pikachu=pokemon('pikachu','electric','100')
print(bulboser)
print(charmander)
print(squirtle)
print(pikachu)
print('\npress 1 for bulboser')
print('\npress 2 for charmeander')
print('\npress 3 for squirtle')
print('\npress 4 for pikachu')
x=int(input('\nplease select one for your side'))
y={1:'bulboser',2:'charmendar',3:'squirtle',4:'pikachu'}
print(f'\nyou have selected:{y[x]}')
o=random.randrange(1,5)
print(f'\nyour opponent is {y[o]}  ')
if x==1:
    f=bulboser
elif x==2:
    f=charmander
elif x==3:
    f=squirtle
else:
    f=pikachu
if o==1:
    g=bulboser
elif o==2:
    g=charmander
elif o==3:
    g=squirtle
else:
    g=pikachu
f.battle(g)







