from footprints import Footprints

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
        for i in spawnAmt:
            self.objs.insert(self.objToSpawn.clone())

    #get an inactive obj
    def getInactiveObj(self):
        for obj in self.objs:
            if not obj.active:
                return obj
        
        self.spawnMoreObj(ObjectPooler.SPAWN_AMT)
        return self.InactiveObj()

    #set obj pos and activate it
    def setObjPos(self, pos):
        obj = self.getInactiveObj()
        obj.startObj(pos)
