import sys
s='\xe6\xb4\x9e\xe8\xa7\x81'
# print(isinstance(s, unicode))

ss = s.encode('raw_unicode_escape')
print(ss)  

sss = ss.decode()    
print(sss)   

   
