from vector2 import Vector2

class ObjectPooler():
    SPAWN_AMT = 5

    def __init__(self, objToSpawn):
        self.objs = []
        self.objToSpawn = objToSpawn
        
        self.spawnMoreObj(ObjectPooler.SPAWN_AMT)
    
    #update all of them
    def update(self):
        for obj in self.objs:
            if obj.active:
                obj.update()

    #add more obj into the obj pooler
    def spawnMoreObj(self, spawnAmt):
        for i in range(spawnAmt):
            self.objs.append(self.objToSpawn.clone())

    #get an inactive obj
    def getInactiveObj(self):
        for obj in self.objs:
            if not obj.active:
                return obj
        
        self.spawnMoreObj(ObjectPooler.SPAWN_AMT)
        return self.getInactiveObj()

    #set obj pos and activate it
    def setObjPos(self, pos):
        obj = self.getInactiveObj()
        obj.startObj(Vector2(round(pos.x), round(pos.y)))
