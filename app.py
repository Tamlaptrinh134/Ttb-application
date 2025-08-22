import pygame, json
pygame.init()
with open('./resource/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
screen = pygame.display.set_mode((config["screen"]["width"], config["screen"]["height"]))
pygame.display.set_caption("Ttb TRẢ BÀI, V2.0")
bgcolor = config["style"][config["style"]["select"]]["bg"]

if __name__ == '__main__':
    running = True
    while running:
        screen.fill(bgcolor)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()