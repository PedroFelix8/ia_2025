from iaLib import agent, joc

class Aspirador(joc.JocNoGrafic):

    def __init__(self, agents: list[agent.Agent] | None = None):
        if agents is None:
            agents = []
        super(Aspirador, self).__init__(agents=agents)
        self.habitacions = [False, False] # False = bruta, True = neta
        self.posAsp = 0
        self.fiJoc = False


    def _draw(self):
        print(f"Aspirador a la habitació {'esquerra' if self.posAsp == 0 else 'dreta'}")
        print(f"Habitació esquerra {'neta' if self.habitacions[0] == True else 'bruta'}")
        print(f"Habitació dreta {'neta' if self.habitacions[0] == True else 'bruta'}")


    def percepcio(self):
        return (self.posAsp, self.habitacions[self.posAsp])


    def _aplica(self, accio, params=None, agent_actual=None):

        match accio:
            case 'E':
                self.posAsp = 0
            case 'D':
                self.posAsp = 1
            case 'A':
                self.habitacions[self.posAsp] = True
            case _:
                pass

        if self.habitacions[0] and self.habitacions[1]:
            self.fiJoc = True
            print("Fi del joc")