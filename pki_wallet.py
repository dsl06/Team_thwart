
import os
import random
from twilio.rest import Client 

mypub_key = '765d4ac67eff46571d1fd0f6bec9ab2e3c78703ffeabfd2fbff8e6d82dc1b229'
base= { "31f61035daf5a48422b7b53b3388832f88eb2e8809976ccf6617a16e046dc1ee": ['Darshan'], "734a6e7c513d7f6caf90706f764bfb42ac935eb35691b23cd4ac5d924c87d831" : ['Preethu'] ,"1416a0edcaf9c57a38fd0170389d06872336dfb6ec8ba5946b0edf931953a9e7": ['Reshma'] ,"b8d7e97c103b46beeb1ce543c964fe563fb835a35548ef21cb784c66838bd2a6" : ['Arshad'] }


def verify(key1):
	for key in base:
		if str(key)==str(key1):
			print("verified....")
			flag = 1
			return True
		else:
			flag = 0
	if flag==0:
		print("inavalid address provided.....")
		return False

print("your public address----> ",mypub_key)

rec_pub_key = input("enter recipeint public address----> ")
print("verifying provided recipeint address.........")

value = verify(rec_pub_key)

if value:

	account_sid = 'AC58785c7b66aec4f949ec34e19be86f8b'
	auth_token = '3e2132ab8a05c2f03ea1afcf56d8d523'
	client = Client(account_sid,auth_token)
	flag=0
	while True:
		OTP=""
		for i in range(6):
			otp=random.getrandbits(3)
			OTP+=str(otp)
		
		msg=" This is your otp " + str(OTP)

		message = client.messages.create(
				body = msg,
				from_='+12055435065',
				to= '+919535274394'
				)
		while True:		
			otp1= input("enter otp sent--->  ")
			if otp1==OTP:
				print("@@@@@@Proceeding to transaction@@@@@@ ")
						
				flag=1	
				break
			else:
				print("*****enter valid otp******")
		if flag==1:
			break				
				
						
			

