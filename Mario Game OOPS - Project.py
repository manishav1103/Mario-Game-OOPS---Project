class Charater:
  
    def __init__(self,name):
        self.name=name
        self.__score=0
        self.__life=3
        
        
    def kicked(self):
        self.__score = self.__score + 10
            
    def punched(self):
        self.__score = self.__score + 5
          
    def stabbed(self):
       self.__life = self.__life -1
        
    
    def displaylife(self):
        return self.__life

    def displayscore(self):
        return self.__score

    def intro(self):
        print(f'Name:{self.name}')
        print(f'Score:{self.__score}')
        print(f'Life:{self.__life}')
    
Mario=Charater('Mario')
Mario.kicked()
Mario.punched()
Mario.stabbed()
Mario.stabbed()
Mario.intro()

v = Mario.displaylife()
if(v==0):
    print('Game Over....!')
else:
    print('Welcome to level 2')

