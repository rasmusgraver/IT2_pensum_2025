x = 1

class Ball:
    def __init__(self):
        # ikke global: Oppretter en NY variabel (lokal) x
        x = 2
        self.x = x
    
    def setx(self):
        # ikke global: Oppretter en NY variabel (lokal) x
        x = 7

def increase():
    # ikke global: Oppretter en NY variabel (lokal) x
    x = 6

ball = Ball()
ball.setx()
increase()
print(x, ball.x)
# printer 1,2
