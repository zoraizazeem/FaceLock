# FaceLock

This is my "facelock" application.
I use this myself to decrypt sensitive files with just face recognition. 
If there is a match to the .jpeg that is referenced in the code, the application will use the "encryption.fernet" module to decrypt the file you have already encrypted.

You will first have to form a key.key (will automatically store locally in the same directory as the python file). The code that will do this is # out in the encrypt.py file, for further information see: https://cryptography.io/en/latest/fernet.html

In the example uploaded, a picture of my face is provided and hence the name that is selected is "Zoraiz". Just add a .jpeg of yourself and add your name in the code.

The facerecog.py file imports the sendsms.py file. Here a message is sent to your mobile device saying that you were recently signed in, as a notification. Using a library called twilio. https://www.twilio.com/docs/libraries/python
Buy a number (relatively cheap) and add your actual mobile number and the program is ready to use.

NOTE: This is not completely secure and was made to be novel security app. So encrypt and decrypt files at your own risk.

I will add machine learning and some extra features in some way inorder to increase accuracy at some point so keep an eye out on this repository.
