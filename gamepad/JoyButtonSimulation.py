import pygame 

blue = [150, 150, 255]
red = [255,50,0]
pygame.init()

size = width, height = 500,300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simulador de Gamepad - Botões")
clock = pygame.time.Clock()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
joy0 = pygame.joystick.Joystick(0)  # supoe que ha pelo menos 1 gamepad conectado
joy0.init()
name = joy0.get_name()
print("Nome do Joystick: {}".format(name))

but = [False, False, False, False, False, False, False, False, False, False, False, False]
pos = [[261,55], [279,73], [261,93] , [246,73], [88,2], [238,4],
      [80,10], [238,10], [138,53] , [186,53], [119,114], [203,114]]
imgPos = [90,50]
for i in range(0,12):
    pos[i][0] += imgPos[0]
    pos[i][1] += imgPos[1]
joyImg = pygame.image.load("joy.png")

running = True
while running:
    screen.fill(blue)
    screen.blit(joyImg, imgPos)
    for event in pygame.event.get():   # trata eventos: gamepad, teclado, janela, etc
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
            for i in range(0,12):
                if joy0.get_button(i): # apertou botao i
                    but[i] = 1
                    print("but",i,pos[i])  ## pygame.mouse.get_pos())
                else: but[i] = 0    # soltou botao i
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(pygame.mouse.get_pos())
    for i in range(0,12):
        if but[i]:pygame.draw.circle(screen, red, pos[i] ,10)
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()