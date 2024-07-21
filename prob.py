import pygame

# параметры игрового окна
pygame.init()
WIDTH = 400
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # задаем окно
pygame.display.set_caption("крестики-нолики") # название окна
pygame.display.set_icon(pygame.image.load("f vs s.png"))  # иконка перед названием

# параметры для игры:
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#
BOARD_SIZE = 3
TILE_SIZE = int(WIDTH / BOARD_SIZE) #размер клетки

# Создаем игровое поле:
board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# функция отрисовки игрового поля:
def game():
    _SNOW = pygame.image.load('snejinka.png') #картинка для обозначения "0"
    snow = pygame.transform.scale(_SNOW, (TILE_SIZE, TILE_SIZE)) #размер картинки=размер клетки

    _FIRE = pygame.image.load('fire.png') #картинка для обозначения "Х"
    fire = pygame.transform.scale(_FIRE, (TILE_SIZE, TILE_SIZE)) #размер картинки=размер клетки

    SCREEN.fill(WHITE) #поле белое
    for i in range(1, BOARD_SIZE): # рисуем линии для клетки горизонтальные(red) и вертикальные(green)
        pygame.draw.line(SCREEN, RED, (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE), 3)
        pygame.draw.line(SCREEN, GREEN, (i * TILE_SIZE, 0), (i * TILE_SIZE, WIDTH), 3)

    for i in range(BOARD_SIZE): #размер клетки(рабочая область
        for j in range(BOARD_SIZE):
            a = (i * TILE_SIZE) + TILE_SIZE / 2
            b = (j * TILE_SIZE) + TILE_SIZE / 2

            if board[i][j] == 'X': # если Х то огонь
                fire_rect = fire.get_rect(center=(a, b))
                SCREEN.blit(fire, fire_rect)

            elif board[i][j] == 'O': #если 0 то снег
                snow_rect = snow.get_rect(center=(a, b))
                SCREEN.blit(snow, snow_rect)  #

def check_winner(): #функция проверки победителя
    for i in range(BOARD_SIZE):
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] is not None):
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] is not None):
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        return board[0][2]
    return None


def main():#основной цикл игры
    turn = 'X' #первые ходят х
    font = pygame.font.SysFont(None, 100)

    while True: #
        for event in pygame.event.get(): #
            if event.type == pygame.QUIT: #
                pygame.quit() #
                return

            elif event.type == pygame.MOUSEBUTTONDOWN: #нажатие клавиши мыши
                x, y = event.pos #
                tile_x = x // TILE_SIZE #
                tile_y = y // TILE_SIZE #
                if board[tile_x][tile_y] is None: #
                    board[tile_x][tile_y] = turn #

                    if turn == 'X': #если х сходили, дальше ходят 0
                        turn = 'O'
                    else:
                        turn = 'X'
        game()
        winner = check_winner() #функция победителя
        if winner is not None:
            SCREEN.blit(font.render("Победа!!!", True, RED, GREEN), (50, 100))
            pygame.display.update()
            pygame.time.wait(2000)
            return

        elif all([all(row) for row in board]) and (winner is None):
            SCREEN.blit(font.render("НИЧЬЯ!", True, BLUE), (50,100))
            pygame.display.update()
            pygame.time.wait(1000)
            return
        pygame.display.update()

#
if __name__ == "__main__":
    main()
