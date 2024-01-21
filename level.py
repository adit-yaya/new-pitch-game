from level_dict import level_dict
import random
class Level(object):
    currentLevel = 1
    level_success = None
    kill_list = []
    ammo = None
    def __init__(self, version):
        if self.currentLevel==1 or self.currentLevel==2:
            self.ammo = 60
        elif self.currentLevel==3 or self.currentLevel==4:
            self.ammo = 50
        elif self.currentLevel==5:
            self.ammo = 40
        elif self.currentLevel==6:
            self.ammo = 45
            # Enemy.y_speed = 1
            # Game.stick_sensitivity = 5
        elif self.currentLevel >= 7 and self.currentLevel < 9:
            self.ammo = 35
        else:
            self.ammo = 30
        
    def check_success(self):
        if len(self.kill_list)<=6:
            self.level_success = False #failed the level
        else:
            self.level_success = True
            self.increase_level()
    
    def increase_level(self):
        self.currentLevel+=1
        # Enemy.speed += 1
        # Bullet.bullet_speed += 1
        # Game.stick_sensitivity += 0.1
        
    
    def load_level(self, version):
        self.__init__(version)
        
