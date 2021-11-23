import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人"""

    def __init__(self, ai_game):
        """初始化外星人"""
        super().__init__()
        self.screen = ai_game.screen

        #加载外星人的图像并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初位置都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #储存外星人的水平位置
        self.x = float(self.rect.x)