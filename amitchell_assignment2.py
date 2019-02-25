import hashlib
import sys
import time

# Done by Alexander Mitchell for 
# Blockchain assignment 2

# Command line input guide

# for args in sys.argv
# inputhash = sys.argv[1]
# salt = sys.argv[2]

# Time tracking variables
counter = 0
start_time = time.time()

# Opening the files
with open("./pwdlist.txt", 'r') as f:
    pwdlist = [eachline.strip() for eachline in f]

# cracking the hashes
if len(sys.argv) == 2:
    for pwd in pwdlist:
        hashdpwd = hashlib.sha1(pwd).hexdigest()
        if sys.argv[1] == hashdpwd:
            print "The magic password is " + pwd
            break
        elif pwd != hashdpwd:
            counter += 1
            continue
    print "It took " + str(time.time()-start_time) + " seconds long and " +str(counter) + " many tries to find this.\n"
    quit()
elif len(sys.argv) == 3:
    for pwd in pwdlist:
        hashdpwd = hashlib.sha1(pwd).hexdigest()
        if sys.argv[2] == hashdpwd:
            saltsaver = pwd
with open("./pwdlist.txt", 'r') as f:
    pwdlist = [eachline.strip() for eachline in f]
    for pwd in pwdlist:
        hashdpwd = hashlib.sha1(saltsaver + pwd).hexdigest()
        if sys.argv[1] == hashdpwd:
            break
        elif pwd != hashdpwd:
            counter += 1
            continue
    print "It took " + str(time.time()-start_time) + " seconds long and " + str(counter) + " many tries to find the salted password " + pwd + "\n"