
## Problem Description
Implement a weapon system for a first-person shooter game that manages guns, bullets, and shooting mechanics with proper validation and exception handling.

## Class Specification
```python
class Shooter:
    def set_gun_by_name(self, name: str) -> None
    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None  
    def shoot_to_target(self, target_x: int, target_y: int, target_distance: int, 
                       aim_x: int, aim_y: int) -> float

Weapons:
    - Submachine Gun: range=100, power=10, bullet_size=0.5
    - Assault Rifle: range=200, power=20, bullet_size=1  
    - Pistol: range=80, power=8, bullet_size=0.5
    - Shotgun: range=50, power=40, bullet_size=4
    - Sniper Rifle: range=1000, power=30, bullet_size=3

Bullets:
    - Size 0.5: damage=1
    - Size 1: damage=1.5
    - Size 3: damage=3
    - Size 4: damage=2

Methods:
    set_gun_by_name(name): Select weapon (case-sensitive)
    add_bullet_of_given_size_to_gun(size, count): Add bullets with validation
    shoot_to_target(target_x, target_y, distance, aim_x, aim_y): Shoot at target

Exceptions:
    - Weapon does not exist!
    - No weapon selected!
    - Bullet count cannot be negative!
    - Bullet size does not exist!
    - Bullet size does not match the weapon!
    - No bullets left!

Example:
    >>> shooter = Shooter()
    >>> shooter.set_gun_by_name('Submachine Gun')
    >>> shooter.add_bullet_of_given_size_to_gun(0.5, 1)
    >>> shooter.shoot_to_target(1, 1, 20, 5, 4)
    10.0
"""
