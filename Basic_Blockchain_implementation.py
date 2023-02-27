import hashlib as h
from datetime import datetime
from datetime import datetime as t
import random as r
import hashlib as h

difficulty=4
time=str(datetime.now())
genisis_block=['0',["paid 50BTC"],'0000c06de17f394fecdcfdfbfd761bfd73b875e150c26761831e677136670baa',4,57079,time]
max_=10000000000000000000000000000000000000000

sendr_keys=['12345678','1235678','345678']
tran_done=[]
chain=[]
chain.append(genisis_block)
def data_merger(data1):
	 data=0
	 for i in data1:
        	if data==0:
       			data=str(i)
       		else:
       			data=str(data)+str(i)
	 return data
###############################################################	 	
def hash_value(text):
	H=h.sha256(text.encode('utf-8')).hexdigest()
	return H	
	
	
###############################################################	
def create_hash(p,t):#function to create hash
    data=str(p)+str(t)
    hash1=h.sha256(data.encode('utf-8'))
    return hash1.hexdigest()  
################################################################   
def block_creation(p,t,new_hash,n):#function to create block
        lblock=[]
        lblock.append(p)
        lblock.append(tran_done[-1])
        lblock.append(new_hash)
        lblock.append(difficulty)
        lblock.append(n)
        time=str(datetime.now())
        lblock.append(time)
        chain.append(lblock)
################################################################
def reciever(skey):#reciever side validation
	if str(skey) in sendr_keys:
		return 1
	else:
		return 2 
################################################################
def consensus(c,n,t,p):#consensus mechanism
	text=t+str(p)+str(difficulty)+str(n)
	new_hash= hash_value(text)
	if new_hash==c:
		block_creation(p,t,new_hash,n)
		
	
     
################################################################
def miner():#function to mine
	print("A transaction found")
	input('press enter key to enter mining')
	prefix_str= '0'* difficulty
	trans=data_merger(tran_done[-1])
	prev_hash=chain[-1][2]
	for nonce in range(max_):
		text= trans+str(prev_hash)+str(difficulty)+str(nonce)
		new_hash= hash_value(text)
		if new_hash.startswith(prefix_str):
			return (new_hash,nonce,trans,prev_hash)
####################################################################
def send_funct(y,skey,):#sender side validation
	ttran=[]
	while True:
		rec=input("enter reciever key----->")
		if str(rec) not in sendr_keys or str(rec)==skey:
			print("reciever not valid")
			continue
		h=reciever(skey)
		print("waiting for reciever to accept your request")
		if h==1:
			print("reciever accepted your request proceeding transactions")
		else:
			print('reciever rejected your request')
			return
			
		if y==1:
			amount=int(input('enter amount--->'))
			d=amount
		if y==2:
			fil=input('attach file---->')
			d=fil
		if y==3:
			mess=input('enter message--->')
			d=mess
		flag=0
		while(True):
			rbit=int(r.getrandbits(10))
			print(rbit)
			r1bit=int(input('enter above CAPTCHA number--->'))
			if rbit==r1bit:
				ttran.append(skey)
				ttran.append(rec)
				ttran.append(d)
				ttran.append(str(datetime.now()))
				tran_done.append(ttran)
				print("proceeding to consensus")
				flag=1
				break
				
			else:
				print("CAPTCHA not matched,Try again")
			
		if flag==1:
			current_hash,nonce,t,p=miner()
			consensus(current_hash,nonce,t,p)
			break

#############################################################################
def sender():#to make transaction
	sender_key='12345678'
	if sender_key in sendr_keys:
		print("1) send money\n",'2) send files\n','3) send message\n')
		y=int(input("enter option------>"))
		send_funct(y,sender_key)
		return
##############################################################################  
def sec_check(phash):#security checkup of blockchain
	flag=0
	data=0
	for i in range(len(chain)-1,-1,-1):
		data=data_merger(chain[i][1])
		text= data+str(chain[i][0])+str(difficulty)+str(chain[i][-2])
		n=hash_value(text)
		if n!=chain[i][2]:
			if flag==0:
				print("************someone tried to alter block number",i,'******************\n')
				for l,m in enumerate(chain):
                    			print("block ",l,'\n',m)
				
                    
			flag=1
			print('\n\n*****************But recovered instantly****************\n')
			chain[i][1]=phash
			for l,m in enumerate(chain):
                    			print("block ",l,'\n',m)
	if flag==1:
		return flag
		
################################################################################

def main():#main function
    phash=chain[-1][1]
    f=0
    while(True):
        print("Welcome to blockchain",'\nenter\n1) Show blockchain\n2) make transactions\n3) alter a block')
        f=sec_check(phash)
        if f==1:
       		continue
        d=int(input('---->'))
       
        if d==1:
                for l,i in enumerate(chain):
                	print("block ",l,'\n',i)
        elif d==2:
            	sender()
            	print("\nblock added succesfully\n")
            
        elif d==3:
        	phash=chain[-1][1]
        	chain[-1][1]=['i hacked you']
        	

main() 
