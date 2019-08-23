
#characters available, letters to numbers
def avail():
  a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890,.?!^*()-~\/:;'|#+= \n"

  b=[]
  i=0
  for letter in a:
    b.append(i)
    i+=1
  return [a , b]

#encoding
def encode(textfilein,textfileout):  
  
  from random import randint
  print("Encoding File")
  [a,b] = avail()
  #codein
  #K1=a0(t+a1)+a2
  #K2=b0(t+b1)^3+b2
  codein = ""
  for x in range(0,8):
    codein += str(randint(1,9))
  #print(codein)

  T = int(codein[0])*10 + int(codein[1])
  cA=[]
  
  for n in range(2,5):
    cA.append(int(codein[n]))
  cB=[]
  for n in range(5,8):
    cB.append(int(codein[n]))
  
  #textfile = "extext.txt"
  
  fhand = open(textfilein)
  
  
  numin = []
  
  #letters to numbers
  for line in fhand:
    for let in line:
      
      for i in range(0,len(a)):
        if let == a[i]:
          numin.append(b[i])
  fhand.close()

  
  print("Input Processed")
    

  #print(numin[81])
  #K1X+K2
  numout=[]
  for num in numin:
    K1 = cA[0]*(T+cA[1])+cA[2]
    K2 = cB[0]*(T+cB[1])**3+cB[2]
    while K1 % 83 == 0 or K2 % 83 == 0:
      T+=1
      K1 = cA[0]*(T+cA[1])+cA[2]
      K2 = cB[0]*(T+cB[1])**3+cB[2]

    numout.append((K1*num+K2) % 83)
    T+=1
  #print(numout[81])

  
  print("File Encoded")
  

  numoutlet = ""
  for num in numout:
    for c in b:
      if num == c:
        numoutlet=numoutlet+a[c]
  numoutlet+=" "
  numoutlet+=codein

  #print(numoutlet)
  fhand2=open(textfileout,"w")
  fhand2.write(numoutlet)
  
  print("File written")
  fhand2.close()
  print("Encoding Successful\n")

########################

def decode(textfilein,textfileout):
  print("Decoding File")
  #codein
  #K1=a0(t+a1)+a2
  #K2=b0(t+b1)^3+b2  

  

  [a,b] = avail()
  
  fhin = open(textfilein)
  [textin, codein] = fhin.read().rsplit(" ",1) 
  #print(textin)
  #print(codein)
  numin = []
  for line in textin:
    for let in line:
      for i in range(0,len(a)):
        if let == a[i]:
          numin.append(b[i])
  #print(numin)
  fhin.close()

  T = int(codein[0])*10 + int(codein[1])
  cA=[]
  for n in range(2,5):
    cA.append(int(codein[n]))
  cB=[]
  for n in range(5,8):
    cB.append(int(codein[n]))
    
  print("Input Processed")
  #print(numin[10])
  #num = K1X+K2
  numout=[]
  for num in numin:
    
    K1 = cA[0]*(T+cA[1])+cA[2]
    K2 = cB[0]*(T+cB[1])**3+cB[2]

    while K1 % 83 == 0 or K2 % 83 == 0:
      T+=1
      K1 = cA[0]*(T+cA[1])+cA[2]
      K2 = cB[0]*(T+cB[1])**3+cB[2]
      

    Xt = (num-cB[0]*(T+cB[1])**3-cB[2])
    Xb = (cA[0]*(T+cA[1])+cA[2])
    while Xt % Xb != 0:
      num+=83
      #print(num)
      Xt = (num-cB[0]*(T+cB[1])**3-cB[2])
    
    numout.append(int((Xt/Xb) % 83))
    #print(T,num,numout[-1])
    T+=1
    
  print("Decoding Completed")
  #print(numout[10])
      
  numoutlet = ""
  for num in numout:
    for c in b:
      if num == c:
        numoutlet=numoutlet+a[c]
 
  #print(numoutlet)
  fhand2=open(textfileout,"w")
  fhand2.write(numoutlet)
  fhand2.close()    
  
  print("File Written")
  print("Decoding Successful")


def UIstart():
  a=0
  while a == 0:
    print("Would you like to [encode] or [decode] a clocktower cipher?\nType [exit] to quit or [clear] to reset the text docs")
    answer1 = input()
    if answer1=="encode":
      UIencode()
      UIclear(1)
      return
    elif answer1 == "decode":
      UIdecode()
      UIclear(2)
      return
    elif answer1 == "exit":
      a=1
    elif answer1 == "clear":
      UIclear(3)
      a=1
    else:
      print("The input was not recognizable.  Please try again.\n")


def UIclear(num):
  if num>=1:
    fhand = open("clocktower1.txt","w")
    fhand.write("Data to be encoded")
    fhand.close()
  if num>=2:
    fhand2 = open("clocktower2.txt","w")
    fhand2.write("Encoded Data")
    fhand2.close()
  if num >=3:
    fhand3 = open("clocktower3.txt","w")
    fhand3.write("Decoded Data")
    fhand3.close()
  print("Docs cleared\n")

def UIencode():
  print("You have chosen to encode.\nPlease type or copy and paste text into the [clocktower1.txt] file found to the left.\n  When finished, type [ready]\nTo cancel type [exit]\n")
  answer1 = input()
  if answer1 == "ready":
    
    enfilein = "clocktower1.txt"
    enfileout = "clocktower2.txt"
    encode(enfilein,enfileout)
    print("The encoded file can be found in the file to the left named [clocktower2.txt].\n")
    
  elif answer1=="exit":
    return
  else:
    print("Input not recognized, try again\n")
    UIencode()
  return


def UIdecode():
  print("You have chosen to decode.\nPlease copy and paste encoded text into the [clocktower2.txt] file found to the left.\n  When finished, type [ready]\nTo cancel type [exit]\n")
  answer1 = input()
  if answer1 == "ready":
    
    defilein = "clocktower2.txt"
    defileout = "clocktower3.txt"
    decode(defilein,defileout)
    print("The decoded file can be found in the file to the left named [clocktower3.txt].\n")
  elif answer1=="exit":
    return
  else:
    print("Input not recognized, try again\n")
    UIdecode()
  
  return  