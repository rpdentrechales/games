import pygame

def main():

    LARGURA, ALTURA = 700, 700
    JANELA = pygame.display.set_mode((LARGURA, ALTURA))
    FPS = 2
    clock = pygame.time.Clock()
    pygame.display.set_caption("primeiro jogo!")

    quadrado = pygame.Rect((0,0),(70,70))
    andar =  False
    indo = True

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

            if indo == True:
                quadrado.x += 70

            else:

                quadrado.x -= 70

            if quadrado.x >= LARGURA-70:

                indo = False

            if quadrado.x <= 0:
                indo = True

        JANELA.fill("black")

        pygame.draw.rect(JANELA, "red", quadrado)
        pygame.display.flip()
        clock.tick(FPS)
        
main()


if __name__ == "__main__":
    main()