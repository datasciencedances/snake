import pygame
import random

# Khởi tạo pygame
pygame.init()

# Cài đặt màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Tạo cửa sổ game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rắn Săn Mồi')

class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)]
        self.direction = "RIGHT"
        self.change_to = self.direction

    def move(self):
        if self.change_to == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        if self.change_to == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if self.change_to == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if self.change_to == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"

        # Di chuyển rắn
        x, y = self.body[0]
        if self.direction == "RIGHT":
            x += BLOCK_SIZE
        elif self.direction == "LEFT":
            x -= BLOCK_SIZE
        elif self.direction == "UP":
            y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            y += BLOCK_SIZE

        # Thêm phần đầu mới
        self.body.insert(0, (x, y))

    def grow(self):
        # Giữ lại phần đuôi khi ăn mồi
        pass

    def check_collision(self):
        x, y = self.body[0]
        # Kiểm tra va chạm với tường
        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            return True
        # Kiểm tra va chạm với thân
        if (x, y) in self.body[1:]:
            return True
        return False

class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
        return (x, y)

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.change_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    snake.change_to = "LEFT"
                elif event.key == pygame.K_UP:
                    snake.change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    snake.change_to = "DOWN"

        # Di chuyển rắn
        snake.move()

        # Kiểm tra ăn mồi
        if snake.body[0] == food.position:
            score += 1
            food.position = food.generate_position()
        else:
            snake.body.pop()

        # Kiểm tra va chạm
        if snake.check_collision():
            game_over = True

        # Vẽ màn hình
        screen.fill(BLACK)
        
        # Vẽ rắn
        for pos in snake.body:
            pygame.draw.rect(screen, GREEN, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        
        # Vẽ mồi
        pygame.draw.rect(screen, RED, (food.position[0], food.position[1], BLOCK_SIZE, BLOCK_SIZE))
        
        pygame.display.update()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()