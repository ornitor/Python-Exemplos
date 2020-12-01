import pygame 

gray = [50, 50, 50]
blue = [150, 150, 255]
red = [255,50,0]
yellow = [255,255,0]
pygame.init()

size = width, height = 500,300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simulador de Gamepad")
clock = pygame.time.Clock()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
joy0 = pygame.joystick.Joystick(0)  # supoe que ha pelo menos 1 gamepad conectado
joy0.init()
name = joy0.get_name()
print("Joystick name: {}".format(name))

#posicionamento dos controles do game pad no desenho
but = [False, False, False, False, False, False, False, False, False, False, False, False]
pos = [[261,55], [279,73], [261,93] , [246,73], [88,2], [238,4],
      [80,10], [238,10], [138,53] , [186,53], [119,114], [203,114]]
but = axis = ball = "00000000000000000000000000000000000000"
hat = "0,0,0,0"
axpos = [[119,115],[203,115]]
hpos = [60,73]
imgPos = [90,50]
for i in range(0,12):
    pos[i][0] += imgPos[0]
    pos[i][1] += imgPos[1]
for i in range(0,2):
    axpos[i][0] += imgPos[0]
    axpos[i][1] += imgPos[1]
hpos[0] += imgPos[0]
hpos[1] += imgPos[1]

joyImg = pygame.image.load("joy.png")

def encodeAxis(axis):
    if axis <0:
        s="-"
    else:
        s="+"
    if axis > 0.9: axis = 0.9 
    if axis < -0.9: axis = -0.9 
    return s + "{}".format(abs(int(axis*10)))

def axisMotion():
    s = ""
    print("Joystick axis moved.")
    for  j in range(joystick_count):
        joy = pygame.joystick.Joystick(j)
        joy.init()
        for i in range(joy.get_numaxes()):
            s = s + encodeAxis(joy.get_axis(i))
    print("joy/axis",s)
    return s

def hatMotion():
    s = ""
    print("Joystick hat moved.")
    for  j in range(joystick_count):
        joy = pygame.joystick.Joystick(j)
        joy.init()
        for i in range(joy.get_numhats(),):
            a,b = joy.get_hat(i)
            s = s + str(a) + "," + str(b) + ","
    print("joy/hat",s)
    return s

def ballMotion():
    print("Joystick ball moved.")
    return s

def buttonPressed():
    s = ""
    for  j in range(joystick_count):
        joy = pygame.joystick.Joystick(j)
        joy.init()
        for i in range(12):
            s = s + "{}".format(joy.get_button(i))
    print("buttom",s)
    return s

def buttonReleased():
    s = ""
    for  j in range(joystick_count):
        joy = pygame.joystick.Joystick(j)
        joy.init()
        for i in range(12):
            s = s + "{}".format(joy.get_button(i))
    print("buttom",s)
    return s


running = True
while running:
    screen.fill(blue)
    screen.blit(joyImg, imgPos)
    for event in pygame.event.get():   # trata eventos: gamepad, teclado, janela, etc
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            but = buttonPressed()
        elif event.type == pygame.JOYBUTTONUP:
            but = buttonReleased()
        elif event.type == pygame.JOYBALLMOTION:
            ballMotion()
        elif event.type == pygame.JOYHATMOTION:
            hat = hatMotion()
        elif event.type == pygame.JOYAXISMOTION:
            axis = axisMotion()
        elif event.type == pygame.JOYHATMOTION:
             hatMotion()
    for i in range(12):
        if but[i]=="1":   # desenha os botões apertados
            pygame.draw.circle(screen, red, pos[i] ,9)
    for i in range(2): # desenha alavanca na posiçao atual
         x = axpos[i][0] + int(axis[i*4:i*4+2])*2
         y = axpos[i][1] + int(axis[i*4+2:i*4+4])*2
         pygame.draw.circle(screen, gray, [x,y] ,12)        
    ss = hat.split(',')     # desenha os ocntrole do hat se apertados
    xhat = int(ss[0])
    yhat = int(ss[1])
    x = hpos[0] + xhat*18
    y = hpos[1] - yhat*18
    if xhat != 0 : pygame.draw.circle(screen, yellow, [x,hpos[1]] ,7)
    if yhat != 0 : pygame.draw.circle(screen, yellow, [hpos[0], y] ,7)
    pygame.display.flip()
    clock.tick(300)
    
pygame.quit()