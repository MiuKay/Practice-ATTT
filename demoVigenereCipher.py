import string
import matplotlib.pyplot as plt 
import numpy as np 


# CIPHER_FIX = """TWT CMGWI ZJTWT AIOEAP XO QT DICJGP MN IWPMR ETCWOCH, SSUHTD, TAETCW, ACS PJFTREW, AVPTRSI JYVEPHZRAQAP WEPGNLEH PYH STXKYRTH, DLAAA YST QT GMOAPEID, PCO RO LPCVACID WHPAW MSHJP, FUI JASN EGZFAQAP GAJHP, WUEEZVTTS MC OPIS SR PUQMRBPEMOC, PYH PPGEMCJALVLN SPWCGXMMNV ISI PAPNI TD QP WEPGNLES, PYH TWT AIRHDYW OG ISMNVH ES BT HPMZTS."""  
# CIPHER = "".join(CIPHER_FIX.split()) 
# CIPHER = CIPHER.translate(str.maketrans('', '', string.punctuation))

# print(CIPHER)

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
ALPHABET_ARRAY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 



key_length = 5 
CIPHER = 'TWTCMGWIZJTWTAIOEAPXOQTDICJGPMNIWPMRETCWOCHSSUHTDTAETCWACSPJFTREWAVPTRSIJYVEPHZRAQAPWEPGNLEHPYHSTXKYRTHDLAAAYSTQTGMOAPEIDPCOROLPCVACIDWHPAWMSHJPFUIJASNEGZFAQAPGAJHPWUEEZVTTSMCOPISSRPUQMRBPEMOCPYHPPGEMCJALVLNSPWCGXMMNVISIPAPNITDQPWEPGNLESPYHTWTAIRHDYWOGISMNVHESBTHPMZTS' 
CIPHER_BY_KEY = ['']*key_length 
for i in range(len(CIPHER)):   
    CIPHER_BY_KEY[i%key_length] += CIPHER[i]  

# print(CIPHER_BY_KEY)
# CIPHER_BY_KEY = ['TGTOOCNROUAAFASEAEESRATODOAHSUNAAUTORROPCLCNPTEETRONBZ', 
#                  'WWWEQJIECHECTVIPQPHTTAQAPLCPHIEQJETPPBCPJNGVADPSWHGVTT', 
#                  'TITATGWTHTTSRPJHAGPXHATPCPIAJJGAHESIUPPGASXIPQGPTDIHHS', 
#                  'CZAPDPPCSDCPETYZPNYKDYGEOCDWPAZPPZMSQEYELPMSNPNYAYSEP', 
#                  'MJIXIMMWSTWJWRVRWLHYLSMIRVWMFSFGWVCSMMHMVWMIIWLHIWMSM'] 




#Monogram frequencies trong ngôn ngữ tiếng Anh
MONO_CHARACTERS = ALPHABET_ARRAY 
mono_freq_en = [8.000395, 1.535701, 2.575785, 4.317924, 12.57564, 2.350463, 1.982677, 6.236609, 6.920007, 0.145188, 0.739906, 4.057231, 2.560994, 6.903785, 7.59127, 1.795742, 0.117571, 5.959034, 6.34088, 9.085226, 2.841783, 0.981717, 2.224893, 0.179556, 1.900888, 0.07913] 

def Shift(l, n):   
    return l[n:] + l[:n]


    
mono_freq_cipher_by_key_1 = [0]*26 
for char in CIPHER_BY_KEY[0]:   
    x = ALPHABET.index(char)   
    mono_freq_cipher_by_key_1[x] += 1  
    
plt.figure(figsize=(15,3)) 
plt.plot( ALPHABET_ARRAY, mono_freq_cipher_by_key_1, color=(0.86, 0.44, 0.50)) 
plt.suptitle('Monogram frequencies for Cipher by key 1') 
plt.show()


#độ dịch chuyển 0 thì hai biểu đồ có độ tương đồng nhau nhất ( chữ A )
shift_length = 0 
mono_freq_cipher_by_key_1_shift = Shift(mono_freq_cipher_by_key_1, shift_length) 
ALPHABET_ARRAY_SHIFT = Shift(ALPHABET_ARRAY, shift_length)  

fig, ax = plt.subplots(1, 1, figsize=(15, 3)) 
ax.plot(ALPHABET_ARRAY_SHIFT, mono_freq_cipher_by_key_1_shift, label="frequencies cipher by key 1", color=(0.86, 0.44, 0.50)) 
ax.plot(ALPHABET_ARRAY_SHIFT,  mono_freq_en, label="frequencies english", color=(0.09, 0.45, 0.71)) 
ax.legend() 
plt.show()


#tần suất của nhóm mật mã theo chữ cái thứ hai trong khóa
mono_freq_cipher_by_key_2 = [0]*26 
for char in CIPHER_BY_KEY[1]:   
    x = ALPHABET.index(char)   
    mono_freq_cipher_by_key_2[x] += 1  
    
plt.figure(figsize=(15,3)) 
plt.plot( ALPHABET_ARRAY, mono_freq_cipher_by_key_2, color=(0.86, 0.44, 0.50)) 
plt.suptitle('Monogram frequencies by key 2') 
plt.show()

#độ dịch chuyển 15 thì hai biểu đồ có độ tương đồng nhau nhất ( chữ P )
shift_length = 15 
mono_freq_cipher_by_key_2_shift = Shift(mono_freq_cipher_by_key_2, shift_length) 
ALPHABET_ARRAY_SHIFT = Shift(ALPHABET_ARRAY, shift_length)  

fig, ax = plt.subplots(1, 1, figsize=(15, 3)) 
ax.plot(ALPHABET_ARRAY_SHIFT, mono_freq_cipher_by_key_2_shift, label="frequencies cipher by key 2", color=(0.86, 0.44, 0.50)) 
ax.plot(ALPHABET_ARRAY_SHIFT,  mono_freq_en, label="frequencies english", color=(0.09, 0.45, 0.71)) 
ax.legend() 
plt.show()


#tần suất của nhóm mật mã theo chữ cái thứ ba trong khóa
mono_freq_cipher_by_key_3 = [0]*26 
for char in CIPHER_BY_KEY[2]:   
    x = ALPHABET.index(char)   
    mono_freq_cipher_by_key_3[x] += 1  
    
plt.figure(figsize=(15 ,3)) 
plt.plot( ALPHABET_ARRAY, mono_freq_cipher_by_key_3, color=(0.86, 0.44, 0.50)) 
plt.suptitle('Monogram frequencies by key 3') 
plt.show()

#độ dịch chuyển 15 thì hai biểu đồ có độ tương đồng nhau nhất ( chữ P )
shift_length = 15 
mono_freq_cipher_by_key_3_shift = Shift(mono_freq_cipher_by_key_3, shift_length) 
ALPHABET_ARRAY_SHIFT = Shift(ALPHABET_ARRAY, shift_length)  

fig, ax = plt.subplots(1, 1, figsize=(15, 3)) 
ax.plot(ALPHABET_ARRAY_SHIFT, mono_freq_cipher_by_key_3_shift, label="frequencies cipher by key 3", color=(0.86, 0.44, 0.50)) 
ax.plot(ALPHABET_ARRAY_SHIFT,  mono_freq_en, label="frequencies english", color=(0.09, 0.45, 0.71)) 
ax.legend() 
plt.show()


#tần suất của nhóm mật mã theo chữ cái thứ tư trong khóa
mono_freq_cipher_by_key_4 = [0]*26 
for char in CIPHER_BY_KEY[3]:   
    x = ALPHABET.index(char)   
    mono_freq_cipher_by_key_4[x] += 1  
    
plt.figure(figsize=(15,3)) 
plt.plot( ALPHABET_ARRAY, mono_freq_cipher_by_key_4, color=(0.86, 0.44, 0.50)) 
plt.suptitle('Monogram frequencies by key 4') 
plt.show()

#độ dịch chuyển 11 thì hai biểu đồ có độ tương đồng nhau nhất ( chữ L )
shift_length = 11 
mono_freq_cipher_by_key_4_shift = Shift(mono_freq_cipher_by_key_4, shift_length) 
ALPHABET_ARRAY_SHIFT = Shift(ALPHABET_ARRAY, shift_length)  

fig, ax = plt.subplots(1, 1, figsize=(15, 3)) 
ax.plot(ALPHABET_ARRAY_SHIFT, mono_freq_cipher_by_key_4_shift, label="frequencies cipher by key 4", color=(0.86, 0.44, 0.50)) 
ax.plot(ALPHABET_ARRAY_SHIFT,  mono_freq_en, label="frequencies english", color=(0.09, 0.45, 0.71)) 
ax.legend() 
plt.show()


#tần suất của nhóm mật mã theo chữ cái thứ năm trong khóa
mono_freq_cipher_by_key_5 = [0]*26 
for char in CIPHER_BY_KEY[4]:   
    x = ALPHABET.index(char)   
    mono_freq_cipher_by_key_5[x] += 1  
    
plt.figure(figsize=(15,3)) 
plt.plot( ALPHABET_ARRAY, mono_freq_cipher_by_key_5, color=(0.86, 0.44, 0.50)) 
plt.suptitle('Monogram frequencies by key 5') 
plt.show()

#độ dịch chuyển 4 thì hai biểu đồ có độ tương đồng nhau nhất ( chữ E )
shift_length = 4 
mono_freq_cipher_by_key_5_shift = Shift(mono_freq_cipher_by_key_5, shift_length) 
ALPHABET_ARRAY_SHIFT = Shift(ALPHABET_ARRAY, shift_length)  

fig, ax = plt.subplots(1, 1, figsize=(15, 3)) 
ax.plot(ALPHABET_ARRAY_SHIFT, mono_freq_cipher_by_key_5_shift, label="frequencies cipher by key 5", color=(0.86, 0.44, 0.50)) 
ax.plot(ALPHABET_ARRAY_SHIFT,  mono_freq_en, label="frequencies english", color=(0.09, 0.45, 0.71)) 
ax.legend() 
plt.show()


















'''
#decrypt GIẢI MÃ

def decrypt(cipher_text, key):   
    plain_text = ''   
    for i in range(len(cipher_text)):     
        p = ALPHABET.index(cipher_text[i])     
        k = ALPHABET.index(key[i%len(key)])     
        c = (p - k) % 26     
        plain_text += ALPHABET[c]   
    return plain_text  

KEY = "APPLE" 
result = decrypt(cipher_text=CIPHER, key=KEY) 
print(result)
'''

