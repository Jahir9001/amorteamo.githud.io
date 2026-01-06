import pygame
import random
import math
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lluvia de Corazones Amarillos para Mi Amor 💕")

# Colores
YELLOW = (255, 215, 0)  # Amarillo dorado
GOLD = (255, 223, 0)    # Dorado brillante
PINK = (255, 182, 193)   # Rosa suave
RED = (255, 105, 180)    # Rosa intenso
WHITE = (255, 255, 255)  # Blanco
BLACK = (0, 0, 0)        # Negro

class Corazon:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-100, -50)
        self.size = random.randint(15, 40)
        self.speed = random.uniform(1, 4)
        self.sway_speed = random.uniform(0.01, 0.03)
        self.sway_amount = random.uniform(20, 50)
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-2, 2)
        self.color = random.choice([YELLOW, GOLD, PINK, RED])
        self.opacity = random.randint(150, 255)
        self.time = random.uniform(0, math.pi * 2)
        
    def update(self):
        # Movimiento hacia abajo con balanceo suave
        self.y += self.speed
        self.time += self.sway_speed
        self.x += math.sin(self.time) * self.sway_amount * 0.02
        self.rotation += self.rotation_speed
        
        # Reiniciar si sale de la pantalla
        if self.y > HEIGHT + 50:
            self.y = random.randint(-100, -50)
            self.x = random.randint(0, WIDTH)
    
    def draw(self, surface):
        # Crear superficie para el corazón con transparencia
        heart_surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        
        # Dibujar corazón usando círculos y polígonos
        heart_color = (*self.color, self.opacity)
        
        # Círculos principales del corazón
        pygame.draw.circle(heart_surface, heart_color, 
                        (self.size // 2, self.size // 2), self.size // 2)
        pygame.draw.circle(heart_surface, heart_color, 
                        (self.size + self.size // 2, self.size // 2), self.size // 2)
        
        # Triángulo inferior del corazón
        points = [
            (self.size // 4, self.size // 2),
            (self.size * 2 - self.size // 4, self.size // 2),
            (self.size, self.size * 2 - self.size // 4)
        ]
        pygame.draw.polygon(heart_surface, heart_color, points)
        
        # Rotar el corazón
        rotated = pygame.transform.rotate(heart_surface, self.rotation)
        
        # Dibujar en la pantalla principal
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(rotated, rect)

class MensajeAmor:
    def __init__(self):
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 32)
        self.textos = [
            "Para Mi Amor Eterno 💕",
            "Cada corazón es por ti",
            "Te amo más cada día",
            "Eres mi todo, mi amor",
            "Corazones que vuelan hacia ti"
        ]
        self.current_text = 0
        self.text_timer = 0
        self.text_duration = 180  # 3 segundos a 60 FPS
        
    def update(self):
        self.text_timer += 1
        if self.text_timer >= self.text_duration:
            self.text_timer = 0
            self.current_text = (self.current_text + 1) % len(self.textos)
    
    def draw(self, surface):
        # Texto principal
        text = self.font.render(self.textos[self.current_text], True, GOLD)
        text_rect = text.get_rect(center=(WIDTH // 2, 100))
        
        # Fondo del texto
        padding = 20
        bg_rect = text_rect.inflate(padding * 2, padding)
        pygame.draw.rect(surface, (0, 0, 0, 128), bg_rect, border_radius=15)
        pygame.draw.rect(surface, GOLD, bg_rect, 3, border_radius=15)
        
        surface.blit(text, text_rect)
        
        # Texto secundario
        small_text = self.small_font.render("Lluvia de Amor para Ti 🌹", True, WHITE)
        small_rect = small_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        surface.blit(small_text, small_rect)

def main():
    clock = pygame.time.Clock()
    corazones = [Corazon() for _ in range(50)]  # 50 corazones cayendo
    mensaje = MensajeAmor()
    
    # Fondo con gradiente
    def draw_background(surface):
        for y in range(HEIGHT):
            color_value = int(20 + (y / HEIGHT) * 30)
            color = (color_value, 0, color_value // 2)
            pygame.draw.line(surface, color, (0, y), (WIDTH, y))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Añadir más corazones al presionar espacio
                    for _ in range(20):
                        corazones.append(Corazon())
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        # Dibujar fondo
        draw_background(screen)
        
        # Actualizar y dibujar corazones
        for corazon in corazones:
            corazon.update()
            corazon.draw(screen)
        
        # Actualizar y dibujar mensaje
        mensaje.update()
        mensaje.draw(screen)
        
        # Instrucciones
        font_small = pygame.font.Font(None, 24)
        instructions = font_small.render("Presiona ESPACIO para más corazones | ESC para salir", True, WHITE)
        screen.blit(instructions, (10, 10))
        
        # Contador de corazones
        counter_text = font_small.render(f"Corazones: {len(corazones)}", True, GOLD)
        screen.blit(counter_text, (10, 40))
        
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
