import os.path
from os import path
from gtts import gTTS #google text to speech

#Checking if file exists or not
def fileExists(fileName):
	if not path.exists(fileName):
		print("We can not find the file,check the filename you entered or check if file is in same directory?")
		return False
	else:
		return True


#getting user input for file name
rawFileName=input(str("Please enter the name of file you want to make mp3 and press enter:"))
print('\n')
extension=os.path.splitext(rawFileName)[1] #getting extension for user input
# print(extension)
if extension=='.txt': #if extension is txt
	fileName=rawFileName 
	if fileExists(fileName)==False:
		exit()

elif extension=='.': #if extension is not txt, but something else
	print("Sorry to say but right now we can only convert text files.Please try again with text file.")
	exit()

elif extension!=' ': #if there is no extension at all
	fileName=rawFileName+'.txt'
	if fileExists(fileName)==False:
		exit()


#opening and reading the file into one string veriable
f=open(fileName)
text_val = f.read()

language = 'gu' #you can change the speeching accent ..... IT WILL NOT TRANSLATE... JUST ACCENT OF SPEECH WILL CHANGE

obj = gTTS(text=text_val, lang=language, slow=False)

mp3File=input(str("Please enter the name you want to give to mp3 file:- "))
print('\n')
print("Please Wait we are brewing spell on your text file to make it mp3")
print('\n')
extension=os.path.splitext(mp3File)[1]
if extension=='.mp3':
	mp3FileExt=mp3File
else:
	initial=os.path.splitext(mp3File)[0]
	mp3FileExt=initial+".mp3"

# obj.save(mp3FileExt)
print("We Finished the work your mp3 file is ready-",mp3FileExt)
print('\n')