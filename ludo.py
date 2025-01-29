import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BOARD_COLOR = (255, 223, 186)
DICE_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo Game")

# Dice function
def roll_dice():
    return random.randint(1, 6)

def draw_board():
    screen.fill(BOARD_COLOR)
    text = FONT.render("Press SPACE to roll the dice", True, TEXT_COLOR)
    screen.blit(text, (150, 50))

def draw_dice(number):
    pygame.draw.rect(screen, DICE_COLOR, (250, 250, 100, 100))
    text = FONT.render(str(number), True, TEXT_COLOR)
    screen.blit(text, (290, 290))

def main():
    running = True
    dice_value = 1
    
    while running:
        screen.fill(BOARD_COLOR)
        draw_board()
        draw_dice(dice_value)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dice_value = roll_dice()
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
