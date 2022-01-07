import enum
  
class PetState(enum.Enum):
    DEFAULT = 0
    IDLE = 1
    CATCH_MOUSE = 2
    GOT_MOUSE = 3