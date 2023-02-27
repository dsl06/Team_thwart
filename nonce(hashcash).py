from hashlib import sha256

difficulty=4
max_=10000000000000000000000000000000000000000

def hash_value(text):
	h=sha256(text.encode('utf-8')).hexdigest()
	return h
#############################################################

def mine(trans,prev_hash,difficulty):
	prefix_str= '0'* difficulty
	for nonce in range(max_):
		text= trans+prev_hash+str(difficulty)+str(nonce)
		new_hash= hash_value(text)
		if new_hash.startswith(prefix_str):
			print("mined bitcoin with a nonce = ",nonce)
			return new_hash
	
	

def data_merger(data1):
	 data=0
	 for i in data1:
        	if data==0:
       			data=str(i)
       		else:
       			data=str(data)+str(i)
	 return data
	 
def main():
	trans='paid 50BTC'
	data=data_merger(trans)
	new_hash=mine(data,'0',difficulty)
	print("the hash is",new_hash)
main()
