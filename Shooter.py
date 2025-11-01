class Shooter:
    def __init__(self):
        self.guns = {
            "Submachine Gun": {"range": 100, "power": 10, "bullet_size": 0.5},
            "Assault Rifle": {"range": 200, "power": 20, "bullet_size": 1},
            "Pistol": {"range": 80, "power": 8, "bullet_size": 0.5},
            "Shotgun": {"range": 50, "power": 40, "bullet_size": 4},
            "Sniper Rifle": {"range": 1000, "power": 30, "bullet_size": 3}
        }

        self.bullets = {
            0.5: {"name": "A", "damage": 1},
            1: {"name": "B", "damage": 1.5},
            3: {"name": "C", "damage": 3},
            4: {"name": "D", "damage": 2}
        }

        self.selected_gun = None
        self.bullet_count = 0

    def set_gun_by_name(self, name: str) -> None:
        if name not in self.guns:
            raise Exception("Weapon does not exist!")
        self.selected_gun = self.guns[name]
        self.bullet_count = 0

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        if self.selected_gun is None:
            raise Exception("No weapon selected!")
        if count < 0:
            raise Exception("Bullet count cannot be negative!")
        if size not in self.bullets:
            raise Exception("Bullet size does not exist!")
        
        gun_bullet_size = self.selected_gun["bullet_size"]
        if size != gun_bullet_size:
            raise Exception("Bullet size does not match the weapon!")
        
        self.bullet_count += count

    def shoot_to_target(self, target_x: int, target_y: int, target_distance: int, aim_x: int, aim_y: int) -> float:
        # Weapon
        if self.selected_gun is None:
            raise Exception("No weapon selected!")
        
        # Bullet
        if self.bullet_count <= 0:
            raise Exception("No bullets left!")
        
        # Range
        gun_range = self.selected_gun["range"]
        if target_distance > gun_range:
            return 0.0
        
 
        # Targeting
        if not (target_x <= aim_x <= target_x + 10 and target_y <= aim_y <= target_y + 10):
            return 0.0
        
        self.bullet_count -= 1
        
        # Damage
        gun_power = self.selected_gun["power"]
        bullet_size = self.selected_gun["bullet_size"]
        bullet_damage = self.bullets[bullet_size]["damage"]
        
        return gun_power * bullet_damage