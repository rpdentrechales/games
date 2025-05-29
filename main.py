import pygame

def main():

    LARGURA, ALTURA = 700, 700
    JANELA = pygame.display.set_mode((LARGURA, ALTURA))
    FPS = 60
    clock = pygame.time.Clock()
    pygame.display.set_caption("primeiro jogo!")

    quadrado = pygame.Rect((35,35),(1,1)).inflate(70,70)
    posicoes_x = [35,105,175,245,315,385,455,525,595,665]
    andar =  False
    index_x = 0
    rodar = True

    while rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
                pygame.quit()


            
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:
            andar =  True
         
        if andar :
            index_x += 1
            if (index_x > len(posicoes_x)-1):
                index_x = 0
            quadrado.x = posicoes_x[index_x]
        JANELA.fill("black")

        pygame.draw.rect(JANELA, "red", quadrado)
        pygame.display.flip()
        clock.tick(FPS)
        
main()


if __name__ == "__main__":
    main()