# sha1Cracker

## 🔨 Sha1Cracker 

This is a program that cracks SHA1 hashes as well as salted word hashes. 

## 💯 Project facts
* It was written in Python 2.7.
* Developed by Alexander Mitchell for Blockchain assignment 2.

## 🏎 Getting up and Running

> You can access this program by cloning the repo to your local machine via SSH.
<!-- -->
❗️**IMPORTANT:**
> Your sysargv[1] is the input hash and your sysargv[2] is your salt term.

### 🤔How to run
You run the code by either:
1. Typing python, the file name and the hash that you want to solve in your terminal.
```bash
$ python amitchell_assignment2.py <YOUR INPUT HASH>
```

Or

2. Typing python, the file name and the hash that you want to solve and your hash in your terminal.
```bash
$ python amitchell_assignment2.py <YOUR INPUT HASH> <YOUR SALT TERM>
```

## 📝 Homework outputs

1. Solution to a
![A Solution](./solutions/prob1.png)

2. Solution to b
![A Solution](./solutions/prob2.png)

3. Solution to c
![A Solution](./solutions/prob3.png)

## 🔑 Project components

### 📚 Libraries used (and how to import them)

This program uses three libraries...
1. hashlib: For all of our hash functions
2. sys: For command line arguments
3. time: To time the program

Install them by doing the following at the top of your program if you aren't copying the repo:
```python
import hashlib
import sys
import time
```

### 🔩 Breaking down the code
1. Establish variables that track the time and amount of times it takes to find the solved hash.

```python
# Time tracking variables
counter = 0
start_time = time.time()

# for args in sys.argv
# inputhash = sys.argv[1]
# salt = sys.argv[2]
```

2. Open the file and put each word in their own index, removing beginning and trailing characters.
```python
# Opening the files
with open("./pwdlist.txt", 'r') as f:
    pwdlist = [eachline.strip() for eachline in f]
```

3. If there are only two system args, filename and input hash, then run this code.
```python
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
```

4. If there are three system args, filename, input hash, and salt, then run this code.
```python
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
```

