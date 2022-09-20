from entities.base_entity import BaseEntity


class Spike(BaseEntity):
    def __init__(self, damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.damage = damage
