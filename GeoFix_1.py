# PYTHON script
import os
import ansa
from ansa import base, constants,mesh
from ansa import guitk
def main():
		def askUserPermission():
			messageWindow = guitk.BCMessageWindowCreate(
	        guitk.constants.BCMessageBoxWarning,
    	    "Do you want to  <b>Completed</b> Geometry clean up?",
        	True,
	   		 )	
    		guitk.BCMessageWindowSetAcceptButtonText(messageWindow, "Yes")
 	 	 	 guitk.BCMessageWindowSetRejectButtonText(messageWindow, "No")
 		   guitk.BCMessageWindowSetTextAlignment(
 	       messageWindow, guitk.constants.BCAlignTop | guitk.constants.BCAlignHCenter
 		   )
 	  	 	answer = guitk.BCMessageWindowExecute(messageWindow)
   		 	if answer == guitk.constants.BCRetKey:
        def geoFix()
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
	def removeLogo():
		heightInStr,sizeInStr=guitk.UserInput("Enter height and size to remove logo : ").split()
		height= float(heightInStr)
	#	sizeInStr=guitk.UserInput("Enter size for remove logo: ")
		size=float(sizeInStr)
		revLogo=base.CollectEntities(constants.ABAQUS,None,"FACE")
		base.RemoveLogosAutomatic(height,size, source_faces=revLogo)
	###########################################
	def getMessage():
    	messageWindow = guitk.BCMessageWindowCreate(
        	guitk.constants.BCMessageBoxWarning,
        	"Process is <b>Completed</b> <br>Do you want to proceed?",
        	True,
    	)
    	guitk.BCMessageWindowSetAcceptButtonText(messageWindow, "Yes")
    	guitk.BCMessageWindowSetRejectButtonText(messageWindow, "No")
    	guitk.BCMessageWindowSetTextAlignment(
        	messageWindow, guitk.constants.BCAlignTop | guitk.constants.BCAlignHCenter
    	)
    	answer = guitk.BCMessageWindowExecute(messageWindow)
   	 else answer == guitk.constants.BCEscKey:
    	    print("Sorry Process is stop")
#    	elif answer == guitk.constants.BCQuitAll:
#        	print("Quit all")
#
#    if answer == guitk.constants.BCRetKey:
#        print("Accept")
#    elif answer == guitk.constants.BCEscKey:
#        print("Reject")
#    elif answer == guitk.constants.BCQuitAll:
#        print("Quitall")	
if __name__ == '__main__':
	setLength()
	removeLogo()
	main()
	getMessage()


