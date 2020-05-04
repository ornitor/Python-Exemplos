# faz o diagnósticos dos Joystick ligados ao computador

import pygame 

pygame.init()
pygame.joystick.quit()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
print("\n\n\nBom dia! Há ",joystick_count, " joysticks conectados.")
for i in range(0, joystick_count):
    j = pygame.joystick.Joystick(i)
    j.init()
    name = j.get_name()
    print("\nJoystick ",i,": {}".format(name))
    print (j.get_numaxes()," eixos"  )
    print (j.get_numballs() , " balls" )
    print (j.get_numbuttons(), " botoes"  )
    print (j.get_numhats(), " hats"  )

