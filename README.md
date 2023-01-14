# PyEncrypt

You can use this code to encrypt password for invoking external service in your python application.  
You will encrypt string with AES cypher with a 128-bit or 256-bit key.  

Before run this code, please launch for windows
```
pip install pycryptodome
```
for Ubuntu
```
pip install crypto
```
Generate a 16 byte key and put it in place of the 'key' variable.
You can use this tool https://www.allkeysgenerator.com/Random/Security-Encryption-Key-Generator.aspx , set "Encryption Key" and choose 128-bit ( to get a key lenght of 128/8 = 16 byte) or 256-bit to have a 
