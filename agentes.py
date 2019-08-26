# https://docs.google.com/document/d/1eP3aCyTWuTCbYMwf3inNHd7AIIpYHyb_PEj-aXYc1xU/edit


from classMain import Agent,Environment
import time
from random import randrange


class AgentConMeoria(Agent):
    def __init__(self, env):  # recibe como parámetro un objeto de la clase Environment
        Agent.__init__(self,env)

    def think(self, env):  # implementa las acciones a seguir por el agente
        if (self.prespective(env)):
            self.suck(env)
        while True:
            if (env.accept_action("up")):
                self.up(env)
            else:
                if (env.accept_action("L")):
                    self.left(env)
                else:
                    while True:
                        while True:
                            if (env.accept_action("R")):
                                self.right(env)
                            else:
                                break
                            if (self.thinkAux(env)):
                                break
                        if (env.accept_action("down")):
                            self.down(env)
                        else:
                            break
                        if (self.thinkAux(env)):
                            break
                        while True:
                            if (env.accept_action("L")):
                                self.left(env)
                            else:
                                break
                            if (self.thinkAux(env)):
                                break                    
                        if (env.accept_action("down")):
                            self.down(env)
                        else:
                            break
                        if (self.thinkAux(env)):
                            break
                    break
            if (self.thinkAux(env)):
                break
        return True
      
    def think2(self, env):  # implementa las acciones a seguir por el agente
        if (self.prespective(env)):
            self.suck(env)
        while True:
            if (self.prespectivePosX(env) >= 1):
                self.up(env)
            else:
                if (self.prespectivePosY(env) >= 1):
                    self.left(env)
                else:
                    while True:
                        while True:
                            if (self.prespectivePosY(env) != self.prespectiveSizeY(env)-1):
                                self.right(env)
                            else:
                                break
                            if (self.thinkAux(env)):
                                break
                        if (self.prespectivePosX(env) != self.prespectiveSizeX(env)-1):
                            self.down(env)
                        else:
                            break
                        if (self.thinkAux(env)):
                            break
                        while True:
                            if (self.prespectivePosY(env) != 0):
                                self.left(env)
                            else:
                                break
                            if (self.thinkAux(env)):
                                break                    
                        if (self.prespectivePosX(env) != self.prespectiveSizeX(env)-1):
                            self.down(env)
                        else:
                            break
                        if (self.thinkAux(env)):
                            break
                    break
            if (self.thinkAux(env)):
                break
        return True

class AgentAleatorio(Agent):
    def __init__(self, env):  # recibe como parámetro un objeto de la clase Environment
        Agent.__init__(self,env)
    def thinkAleatorio(self, env):
        aux = randrange(4)
        if (aux == 0):
            if (env.accept_action("up")):
                self.up(env)
        if (aux == 1):
            if (env.accept_action("down")):
                self.down(env)
        if (aux == 2):
            if (env.accept_action("R")):
                self.right(env)
        if (aux == 3):
            if (env.accept_action("L")):
                self.left(env)
        return self.thinkAux(env)
 
            
class AgentSinEstado(Agent):
    def __init__(self, env):  # recibe como parámetro un objeto de la clase Environment
        Agent.__init__(self,env)
    #Sin estados ni memoria 
    def thinkSinMem(self, env):  
            if (self.prespective(env)):
                self.suck(env)
            if (self.prespectivePosY(env) != self.prespectiveSizeY(env)-1 and (self.prespectivePosX(env) % 2) == 1) :
                self.right(env)
            elif ((self.prespectivePosX(env) == self.prespectiveSizeX(env)-1) and (self.prespectivePosY(env) == self.prespectiveSizeY(env)-1)):
                self.idle()
            elif ((self.prespectivePosX(env) % 2) == 1 ):
                self.down(env)
            elif (self.prespectivePosY(env) != 0):
                self.left(env)
            elif (self.prespectivePosX(env) != self.prespectiveSizeX(env)-1):
                self.down(env)
            env.print_environment()
            time.sleep(self.sleepTime)
            if (self.periodo < 0):
                return True 
            else:
                return False
            

