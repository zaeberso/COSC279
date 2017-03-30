import uuid
from decimal import*
from random import randint
from json import*



cust_id =(uuid.uuid4().get_hex().upper()[0:16])
r1=(uuid.uuid4().get_hex().upper()[0:16])
r2=(uuid.uuid4().get_hex().upper()[0:16])
r3=(uuid.uuid4().get_hex().upper()[0:16])
BIT = (uuid.uuid4().get_hex().upper()[0:16])

order_id1 = randint(0,100)
order_id2 = randint(0,100)
order_id3 = randint(0,100)

amount1 =round(float(input("please enter the amount of the first money order.")),2)
amount2 =round(float(input ("please enter the amount of the second money order.")),2)
amount3 =round(float(input ("please enter the amount of the third money order.")),2)





i111 = (uuid.uuid4().get_hex().upper()[0:16])
i112=(uuid.uuid4().get_hex().upper()[0:16])
i121=(uuid.uuid4().get_hex().upper()[0:16])
i122=(uuid.uuid4().get_hex().upper()[0:16])

i211=(uuid.uuid4().get_hex().upper()[0:16])
i212=(uuid.uuid4().get_hex().upper()[0:16])
i221=(uuid.uuid4().get_hex().upper()[0:16])
i222=(uuid.uuid4().get_hex().upper()[0:16])

i311=(uuid.uuid4().get_hex().upper()[0:16])
i312=(uuid.uuid4().get_hex().upper()[0:16])
i321=(uuid.uuid4().get_hex().upper()[0:16])
i322=(uuid.uuid4().get_hex().upper()[0:16])



def  split(x,y):
    #xor_result = hex(int(x, 16)) ^ hex(int(y, 16))
    
    xor_result ="".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(x, y)])
    
    
    return xor_result

def bit_com():
   
    #i11=r1
   # i12=split(cust_id,r1)

    #i21=r2
    #i22=split(cust_id,r2)

   
    #i31=r3
    #i32=split(cust_id,r3)


    #assign values to part 2 of bit commitment
    

    
    mes1 =  (int(i111,16)^int(i112,16)^int(i11,16)% int(BIT,16))
    mes2 =  (int(i121, 16)^int(i122, 16)^int(i12, 16)% int(BIT,16))

    mes3 =  (int(i211, 16)^int(i212, 16)^int(i21, 16)% int(BIT,16))
    mes4 =  (int(i221, 16)^int(i222, 16)^int(i22, 16)% int(BIT,16))

    mes5 =  (int(i311,16)^int(i312,16)^int(i31,16) % int(BIT,16))
    mes6 =  (int(i321, 16)^int(i322, 16)^int(i32, 16)% int(BIT,16))

    print "message1: ",mes1
    print "message2: ",mes2
    print "message3: ",mes3
    print "message4: ",mes4
    print "message5: ",mes5
    print "message6: ",mes6



def blind_orders():
    global order_id1
    global order_id2
    global order_id3
    global mes1
    global mes2
    global mes3
    global mes4
    global mes5
    global mes6
    
    global i111 
    global i112
    global i121
    global i122

    global i211
    global i212
    global i221
    global i222

    global i311
    global i312
    global i321
    global i322


    rand_mult=randint(1,1000000)*randint(1,1000000)

    order_id1 = order_id1*rand_mult
    order_id2 *= rand_mult
    order_id3 *= rand_mult

    mes1 = ((int(i111, 16)^int(i112, 16)^int(i11, 16))*int(rand_mult))
    mes2 = ((int(i121, 16)^int(i122, 16)^int(i12, 16))* int(rand_mult))

    mes3 = ((int(i211, 16)^int(i212, 16)^int(i21, 16))* int(rand_mult))
    mes4 = ((int(i221, 16)^int(i222, 16)^int(i22, 16))* int(rand_mult))

    mes5 =  ((int(i311,16)^int(i312,16)^int(i31,16)) * int(rand_mult))
    mes6 =  ((int(i321, 16)^int(i322, 16)^int(i32, 16))* (rand_mult))
    print "m1:",mes1
    print "m1:",mes2
    print "m1:",mes3
    print "m1:",mes4
    print "m1:",mes5
    print "m1:",mes6


i11=r1
i12=split(cust_id,r1)

i21=r2
i22=split(cust_id,r2)

i31=r3
i32=split(cust_id,r3)

#output to terminal

print("{0:.2f}".format(amount1))
print order_id1
print "{0:.2f}".format(amount2)
print order_id2
print "{0:.2f}".format(amount3)
print order_id3
print""
print"check if r1,2 and 3 xor."
print "cID"
print cust_id
print"r1"
print r1
r1=split(cust_id,r1)
print r1
print"r2"
print r2
r2=split(cust_id,r2)
print r2
print r3
r3=split(cust_id,r3)
print r3
bit_com()
blind_orders()

# add file output
text_file=open("customer_order1.txt",'a')
text_file.write(cust_id)
text_file.write("\n")
text_file.write(str(amount1))
text_file.write("\n")
#second money order
text_file=open("customer_order2.txt",'a')
text_file.write(cust_id)
text_file.write("\n")
text_file.write(str(amount2))
text_file.write("\n")
#third money order
text_file=open("customer_order3.txt",'a')
text_file.write(cust_id)
text_file.write("\n")
text_file.write(str(amount3))
text_file.write("\n")

#close file
text_file.close()
