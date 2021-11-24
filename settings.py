from pygame.mouse import set_visible


class Settings:
    """储存游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化屏幕"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #飞船设置
        self.ship_limit = 3

        #子弹设
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        #外星人设置
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5

    def increase_dynamic_settings(self):
        """初始化随着游戏变化而变化的值"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #fleet_direction 1为右
        self.fleet_direction = 1

        #记分
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)



