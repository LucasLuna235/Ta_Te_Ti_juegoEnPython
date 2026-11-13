import pygame

pygame.init()
screem = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Ta-Te-Ti")

fondo = pygame.image.load("static/tictactoe_background.png")
circulo = pygame.image.load("static/circle.png")
cruz = pygame.image.load("static/cruz.png")

fondo = pygame.transform.scale(fondo, (450, 450))
circulo = pygame.transform.scale(circulo, (125, 125))
cruz = pygame.transform.scale(cruz, (125, 125))

coordenadas = [
    [(40, 50), (165, 50), (290, 50)],
    [(40, 175), (165, 175), (290, 175)],
    [(40, 300), (165, 300), (290, 300)]
]

tablero = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

turno = 'X'
game_over = False
ganador = None
clock = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 72)
fuente_peq = pygame.font.SysFont(None, 36)

def graficar_board():
    screem.blit(fondo, (0, 0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'X':
                dibujar_x(fila, col)
            elif tablero[fila][col] == 'O':
                dibujar_o(fila, col)

def dibujar_x(fila, col):
    screem.blit(cruz, coordenadas[fila][col])

def dibujar_o(fila, col):
    screem.blit(circulo, coordenadas[fila][col])

def mostrar_ganador(nombre):
    overlay = pygame.Surface((450, 450))
    overlay.set_alpha(180)
    overlay.fill((20, 20, 30))
    screem.blit(overlay, (0, 0))

    texto = fuente.render(f"¡Ganó {nombre}!", True, (0, 255, 255))
    rect = texto.get_rect(center=(225, 200))
    screem.blit(texto, rect)

    sub = fuente_peq.render("Cierra la ventana para salir", True, (200, 200, 200))
    sub_rect = sub.get_rect(center=(225, 260))
    screem.blit(sub, sub_rect)

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return True
    return False

mouseX = 0
mouseY = 0

while not game_over:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos

    if (mouseX >= 40 and mouseX < 415) and \
       (mouseY >= 50 and mouseY < 425):
        fila = (mouseY - 50) // 125
        col = (mouseX - 40) // 125
        if tablero[fila][col] == '':
            tablero[fila][col] = turno
            ganador = turno
            fin_juego = verificar_ganador()
            if fin_juego:
                print(f"El ganador es: {ganador}!!")
                game_over = True
            turno = 'O' if turno == 'X' else 'X'

    graficar_board()
    if game_over and ganador:
        mostrar_ganador(nombre=ganador)
    pygame.display.update()

pygame.quit()
