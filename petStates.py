import enum
  
class PetState(enum.Enum):
    IDLE = 1
    CHASE_MOUSE = 2
    GOT_MOUSE = 3