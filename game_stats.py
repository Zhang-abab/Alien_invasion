
from pygame.sprite import spritecollideany


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        #游戏启动标志位
        self.game_active = True

    def reset_stats(self):
        """初始化在游戏运行期间可能产生变化的值"""
        self.ships_left = self.settings.ship_limit