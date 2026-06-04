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
ball_dir =  5
ball_dir_y = 1

win = pygame.image.load("assets/win.png")


pontoPlayer1 = 7
pontoPlayer1_img = pygame.image.load("assets/score/0.png")

pontoPlayer2 = 7
pontoPlayer2_img = pygame.image.load("assets/score/0.png")

def Desenho():
    if pontoPlayer1 or pontoPlayer2 < 9:
    
        janela.blit(campo,(0, 0))
        janela.blit(player1, (0, player1_y))
        janela.blit(player2, (1200, player2_y))
        janela.blit(ball, (ball_x, ball_y))
        janela.blit(pontoPlayer1_img, (500, 50))
        janela.blit(pontoPlayer2_img, (710, 50))
        MoverBolinha()
        MoverPlayer()

    else:
        janela.blit(win, (330, 300))



def MoverBolinha():

    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global pontoPlayer1
    global pontoPlayer2
    global pontoPlayer1_img
    global pontoPlayer2_img

    ball_y = ball_y + ball_dir_y
    ball_x = ball_x + ball_dir
    
    if ball_x < 74:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir = ball_dir * -1
    
    if ball_x > 1158:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir = ball_dir * -1
    
    if ball_y < 700:
        ball_dir_y = ball_dir_y * -1
    
    if ball_y > 0:

        ball_dir_y = ball_dir_y * -1
    
    if ball_x < -50:
        
        ball_x = (1280 / 2)
        ball_y = (720 / 2)
        ball_dir_y = ball_dir_y * -1
        ball_dir = ball_dir * -1
        
        pontoPlayer2 = pontoPlayer2 + 1
        pontoPlayer2_img = pygame.image.load("assets/score/" + str(pontoPlayer2) + ".png")
        
    
    if ball_x > 1300:

        ball_x = (1280 / 2)
        ball_y = (720 / 2)
        ball_dir_y = ball_dir_y * -1
        ball_dir = ball_dir * -1

        pontoPlayer1 = pontoPlayer1 + 1
        pontoPlayer1_img = pygame.image.load("assets/score/" + str(pontoPlayer1) + ".png")
        




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
    
    if player2_y >= 577:

        player2_y = 577
    
    elif player2_y <= 0:

        player2_y = 0
    

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
    
     

    
    pygame.display.update()

