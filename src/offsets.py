from dataclasses import dataclass

@dataclass
class Offsets:
    base_address: int = 0x2A4B461
    hp_current: int = 0x239
    hp_max: int = 0x23D
    atk: int = 0x241
    def_: int = 0x245
    magic: int = 0x249
    gold: int = 0x261
    inventory_ptr: int = 0x281
    battle_flag: int = 0x2B9
    timer: int = 0x2D1
    items_base: int = 0x2A4B551

CURRENT_OFFSETS = Offsets()
