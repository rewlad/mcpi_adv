
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

## house
wall=1
mc.setBlocks(0, 0, 0, 10, 12, 21, wall) #main
mc.setBlocks(1,1,1,9,11,20,0) #main
mc.setBlocks(3, 12, 10, 7, 12, 14, 0) #люк
door = 0 #64
mc.setBlocks(10,1,2,10,5,5,door) #door
# for y in range(1,5):
#     mc.setBlock(10,y,2,64,8)
mc.setBlocks(10,10,17,10,2,16,0) #win
mc.setBlocks(10,10,12,10,2,13,0) #win
mc.setBlocks(10,10,8,10,2,9,0) #win
#bed
mc.setBlock(1,1,20,26,8)
mc.setBlock(1,1,19,26,0)
books=47
mc.setBlocks(8,1,19,9,11,20,books)
table=58
wood = 5
mc.setBlocks(8,1,16,9,1,17,table)


#mc.getBlockWithData(8,1,16)
#mc.player.getTilePos()
#mc.player.setTilePos(0,20,0)