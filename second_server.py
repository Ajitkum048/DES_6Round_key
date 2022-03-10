import pexpect

child = pexpect.spawn('/usr/bin/ssh students@172.27.26.188')
child.expect('students@172.27.26.188\'s password:')
child.sendline('cs641a')
child.expect('.*', timeout=50) 
child.sendline("cipher101")
child.expect('Enter password: ', timeout=50)
child.sendline("thisispassword")
child.expect('.*', timeout=50)
child.sendline("4")
child.expect('.*')
child.sendline("read")
child.expect('.*')

f = open("plaintexts2.txt", 'r')
f1= open("ciphertexts2.txt",'w')

for line in f.readlines():
	child.sendline(line)
	print(child.before)
	f1.writelines(str(child.before)[48:64]+"\n")
	child.expect("Slowly, a new text starts*")
	child.sendline("c")
	child.expect('The text in the screen vanishes!')
data = child.read()
print(data)
child.close()
print(child.before, child.after)
f.close()
f1.close()


