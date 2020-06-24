import pygame 

my=[193,189,182]
pygame.init()
size = width, height = 720, 720
screen = pygame.display.set_mode(size)

print(".")
pygame.joystick.quit()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
print(joystick_count)
j = pygame.joystick.Joystick(pygame.joystick.get_count()-1)
j.init()
name = j.get_name()
print("Joystick name: {}".format(name))

cores()
screen.fill(my)
pygame.display.flip()

driveLeft = False
driveRight = False

while True:
    if joystick_count < 1:
        SetupPygameAndController()
    else:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(0) : print("but 0")
                if j.get_button(1) : print("but 1")
                if j.get_button(2) : print("but 2")
                if j.get_button(3) : print("but 3")
                if j.get_button(4) : print("but 4")
                if j.get_button(5) : print("but 5")
                if j.get_button(6) : print("but 6")
                if j.get_button(7) : print("but 7")
                if j.get_button(8) : print("but 8")
                if j.get_button(9) : print("but 9")
                if j.get_button(10) : print("but 10")
                if j.get_button(11) : print("but 11")
                if j.get_button(0) : 
                    print("sag")
                    quit()

