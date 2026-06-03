import pygame

pygame.init()

janela = pygame.display.set_mode([1280, 720])
titulo = pygame.display.set_caption("Pong")

campo = pygame.image.load("assets/field.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = (720 / 2)
player1_moveUP = False
player1_moveDown = False

player2 = pygame.image.load("assets/player2.png")
player2_y = (720 / 2)
player2_moveup = False
player2_movedown = False

ball = pygame.image.load("assets/ball.png")
ball_x = (1280 / 2)
ball_y = (720 / 2)
ball_dir = - 2

def Desenho():
    janela.blit(campo,(0, 0))
    janela.blit(player1, (0, player1_y))
    janela.blit(player2, (1200, player2_y))
    janela.blit(ball, (ball_x, ball_y))


def MoverBolinha():

    global ball_x
    global ball_y
    global ball_dir

    ball_x = ball_x + ball_dir
    if ball_x < 74:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir = ball_dir * -1



def MoverPlayer():

    global player1_y
    global player2_y

    if player1_moveUP:

        player1_y = player1_y - 7
    
    else:

        player1_y = player1_y + 0
    
    if player1_moveDown:

        player1_y = player1_y + 7
    
    else:
        player1_y = player1_y + 0

    if player1_y <= 0:

        player1_y = 0
    
    elif player1_y >= 577:
        
        player1_y = 577
    
    if player2_moveup:

        player2_y = player2_y - 7
    
    else:
        player2_y = player2_y + 0
    
    if player2_movedown:

        player2_y = player2_y + 7

    else:

        player2_y = player2_y - 0
    







loop = True

while loop:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:

            loop = False
        
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                player1_moveUP = True
            
            if evento.key == pygame.K_s:
                player1_moveDown = True
            
            if evento.key == pygame.K_i:
                player2_moveup = True
            
            if evento.key == pygame.K_k:
                player2_movedown = True
                
             
        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                player1_moveUP = False
                
            if evento.key == pygame.K_s:
                player1_moveDown = False
            
            if evento.key == pygame.K_i:
                player2_moveup = False
            
            if evento.key == pygame.K_k:
                player2_movedown = False
        
        
            
        

    Desenho()  
    MoverBolinha()
    MoverPlayer()
     

    
    pygame.display.update()

