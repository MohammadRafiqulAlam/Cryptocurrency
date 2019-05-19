import hashlib
sh256 = hashlib.sha256("100".encode()).hexdigest()
#sh256 = '001'
bin_sh256 = bin(int(sh256,16))[2:]
leading_zeros = len(bin_sh256.split('1',1)[0])
print(bin_sh256)
print(leading_zeros)


#print(bin_sh256.index('1'))





#print(bin(int(sh256,16))[2:])#