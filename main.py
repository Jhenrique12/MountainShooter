import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode((600, 480))
print('Setup end')

while True:
#     Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
