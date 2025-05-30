import pygame
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

def main():

    LARGURA, ALTURA = 700, 700
    JANELA = pygame.display.set_mode((LARGURA, ALTURA))
    FPS = 2
    clock = pygame.time.Clock()
    pygame.display.set_caption("primeiro jogo!")

    quadrado = pygame.Rect((0,0),(70,70))
    andar =  False

    ir_para_direita = True
    ir_para_esquerda = False
    ir_para_cima = False
    ir_para_baixo = False


    rodar = True


    while rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
                pygame.quit()


            
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:
            andar =  True
         
        if andar:

            if ir_para_direita == True:
                quadrado.x += 70

            if ir_para_esquerda == True:
                quadrado.x -= 70
            
            if ir_para_cima == True:
                quadrado.y -= 70
            
            if ir_para_baixo == True:
                quadrado.y += 70

            if quadrado.x >= LARGURA-70:
                
                print("bateu na parede direita")
                ir_para_direita = False
                ir_para_esquerda = False
                ir_para_cima = False
                ir_para_baixo = True
            
            if quadrado.y >= ALTURA-70:
                
                print("bateu na parede de baixo")
                ir_para_direita = False
                ir_para_esquerda = True
                ir_para_cima = False
                ir_para_baixo = False

            if quadrado.x <= 0:

                print("bateu na parede da esquerda")
                ir_para_direita = False
                ir_para_esquerda = False
                ir_para_cima = True
                ir_para_baixo = False
            
            if quadrado.y <= 0 and quadrado.x == 0:

                print("bateu na parede de cima")
                ir_para_direita = True
                ir_para_esquerda = False
                ir_para_cima = False
                ir_para_baixo = False

        posicao = (quadrado.x, quadrado.y)
        posicao_texto = my_font.render(f'{posicao}', False, "white")

        JANELA.fill("black")
        JANELA.blit(posicao_texto, (LARGURA//2,ALTURA//2))
        pygame.draw.rect(JANELA, "red", quadrado)
        pygame.display.flip()
        clock.tick(FPS)
        
main()


if __name__ == "__main__":
    main()