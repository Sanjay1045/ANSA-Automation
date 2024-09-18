# PYTHON script
import os
import ansa
from ansa import base, constants,mesh
from ansa import guitk
def main():
	faces= base.CollectEntities(constants.ABAQUS,None,"FACE", filter_visible=True)
	options=[
	"CRACKS",
	"OVERLAPS",
	'NEEDLE FACES',
	'COLLAPSED CONS',
	"NEEDLE FACES",
	"TRIPLE CONS",
	'UNCHECKED FACES',
	]
	fix=[1,1,1,1,1,1,1]
	ret=base.CheckAndFixGeometry(faces,options,fix,True,True)
	if ret!=None:
		print("total remaining errors: ",len(ret[" failed"]))
		print("total remaining errors: ",len(ret["remaining errors"]))
		print("geometry clean is done")
def setLength():
	length=guitk.UserInput("Enter the CAD length: ")
	mesh.ApplyNewLengthToMacros(length)
	base.DeleteVisibleHotPoints()
def removeLogo():
	heightInStr=guitk.UserInput("Enter height for remove logo: ")
	height= float(heightInStr)
	sizeInStr=guitk.UserInput("Enter size for remove logo: ")
	size=float(sizeInStr)
	revLogo=base.CollectEntities(constants.ABAQUS,None,"FACE")
	base.RemoveLogosAutomatic(height,size, source_faces=revLogo)
	###########################################
def getMessage():
    messageWindow = guitk.BCMessageWindowCreate(
        guitk.constants.BCMessageBoxWarning,
        "Process is  <b>Completed</b> ",
        True,
    )
    answer = guitk.BCMessageWindowExecute(messageWindow)

if __name__ == '__main__':
	setLength()
	removeLogo()
	main()
	getMessage()


