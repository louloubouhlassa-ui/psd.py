
for i in range (3):
   psd1 = input ('enter the password')
if len (psd1)<6:
    print("invlid password!the length must be over 6")
else:
    psd2= input('confirm your password')
if psd1!=psd2:
    print("invalid password !the password and it's confirmation must be identical ")
else:
    print('valid password')
