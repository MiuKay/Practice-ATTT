import string
import matplotlib.pyplot as plt 
import numpy as np 


# CIPHER_FIX = """THVVWCZTQ! CZ WECQ YIAQQ, LFN JCII IVAHZ WEV DCPPVHVZYV MVWJVVZ VZYHLOWCFZ AZD ANWEVZWCYAWCFZ. WECQ RVQQATV CQ VZYHLOWVD JCWE A BVHL CZQVYNHV VZYHLOWCFZ QYEVRV. CDVAIIL, AZ VZYHLOWCFZ QYEVRV QEFNID AIIFJ FZIL ANWEFHCGVD OAHWCVQ, JEF XZFJ WEV XVL, WF HVAD WEV RVQQATV. EFJVBVH, LFN SNQW HVAD WEV RVQQATV JCWEFNW XZFJCZT WEV XVL. EVZYV, WEV VZYHLOWCFZ QYEVRV CQ CZQVYNHV."""  
# CIPHER = "".join(CIPHER_FIX.split()) 
# CIPHER = CIPHER.translate(str.maketrans('', '', string.punctuation))

# print(CIPHER)

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
ALPHABET_ARRAY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
CIPHER = 'THVVWCZTQCZWECQYIAQQLFNJCIIIVAHZWEVDCPPVHVZYVMVWJVVZVZYHLOWCFZAZDANWEVZWCYAWCFZWECQRVQQATVCQVZYHLOWVDJCWEABVHLCZQVYNHVVZYHLOWCFZQYEVRVCDVAIILAZVZYHLOWCFZQYEVRVQEFNIDAIIFJFZILANWEFHCGVDOAHWCVQJEFXZFJWEVXVLWFHVADWEVRVQQATVEFJVBVHLFNSNQWHVADWEVRVQQATVJCWEFNWXZFJCZTWEVXVLEVZYVWEVVZYHLOWCFZQYEVRVCQCZQVYNHV'



#sử dụng biểu đồ cột để vẽ đồ thị bằng thư viện matplot
mono_freq_cipher = [0]*26 
for char in CIPHER:   
    x = ALPHABET.index(char)   
    mono_freq_cipher[x] += 1  

dict_monogram_cipher = dict(zip(ALPHABET_ARRAY, mono_freq_cipher)) 
dict_monogram_cipher = dict(sorted(dict_monogram_cipher.items(), key=lambda item: item[1], reverse=True)) 

plt.figure(figsize=(20,5)) 
plt.bar(dict_monogram_cipher.keys(), dict_monogram_cipher.values(), color=(0.97, 0.73, 0.77, 0.8), edgecolor=(0.86, 0.44, 0.50)) 
plt.suptitle('Monogram frequencies for Cipher') 
plt.show()


#sử dụng mảng 1 chiều để đại diện cho mảng 2 chiều trong python
bi_freq_cipher = [0]*26*26 
BI_CHARACTERS_ALL = [0]*26*26 
for i in range(len(CIPHER) - 1):     
    x = (ALPHABET.index(CIPHER[i])*26 +          
        ALPHABET.index(CIPHER[i+1]))     
    BI_CHARACTERS_ALL[x] = CIPHER[i] + CIPHER[i+1]     
    bi_freq_cipher[x] += 1      

dict_bigram_cipher = dict(zip(BI_CHARACTERS_ALL, bi_freq_cipher)) 
dict_bigram_cipher = dict(sorted(dict_bigram_cipher.items(), key=lambda item: item[1], reverse=True))

plt.figure(figsize=(20,5)) 
plt.bar(list(dict_bigram_cipher.keys())[0:20], list(dict_bigram_cipher.values())[0:20], color=(0.97, 0.73, 0.77, 0.8), edgecolor=(0.86, 0.44, 0.50)) 
plt.suptitle('Bigram frequencies for Cipher') 
plt.show()


#sử dụng mảng 1 chiều để đại diện cho mảng 3 chiều trong python
tri_freq_cipher = [0]*26*26*26 
TRI_CHARACTERS_ALL = [0]*26*26*26 
for i in range(len(CIPHER) - 2):     
    x = (ALPHABET.index(CIPHER[i])*26*26 +         
        ALPHABET.index(CIPHER[i+1])*26 +         
        ALPHABET.index(CIPHER[i+2]))     
    TRI_CHARACTERS_ALL[x] = CIPHER[i] + CIPHER[i+1] + CIPHER[i+2]     
    tri_freq_cipher[x] += 1  
    
dict_trigram_cipher = dict(zip(TRI_CHARACTERS_ALL, tri_freq_cipher)) 
dict_trigram_cipher = dict(sorted(dict_trigram_cipher.items(), key=lambda item: item[1], reverse=True))  

plt.figure(figsize=(20,5)) 
plt.bar(list(dict_trigram_cipher.keys())[0:20], list(dict_trigram_cipher.values())[0:20], color=(0.97, 0.73, 0.77, 0.8), edgecolor=(0.86, 0.44, 0.50)) 
plt.suptitle('Trigram frequencies for Cipher') 
plt.show()




# các số liệu tham khao tại: https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html

#Monogram frequencies trong ngôn ngữ tiếng Anh
MONO_CHARACTERS = ALPHABET_ARRAY 
mono_freq_en = [8.000395, 1.535701, 2.575785, 4.317924, 12.57564, 2.350463, 1.982677, 6.236609, 6.920007, 0.145188, 0.739906, 4.057231, 2.560994, 6.903785, 7.59127, 1.795742, 0.117571, 5.959034, 6.34088, 9.085226, 2.841783, 0.981717, 2.224893, 0.179556, 1.900888, 0.07913]  

dict_monogram_en = dict(zip(MONO_CHARACTERS, mono_freq_en)) 
dict_monogram_en = dict(sorted(dict_monogram_en.items(), key=lambda item: item[1], reverse=True))  

plt.figure(figsize=(20,5)) 
plt.bar(dict_monogram_en.keys(), dict_monogram_en.values(), color=(0.40, 0.64, 0.80, 0.8), edgecolor=(0.09, 0.45, 0.71)) 
plt.suptitle('Monogram frequencies for English') 
plt.show()


#Bigram frequencies trong ngôn ngữ tiếng Anh
BI_CHARACTERS = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ND', 'ON','EN', 'AT', 'OU', 'ED', 'HA', 'TO', 'OR', 'IT', 'IS', 'HI', 'ES', 'NG'] 
bi_freq_en = [3.882543, 3.681391, 2.283899, 2.178042, 2.14046, 1.749394, 1.571977, 1.418244, 1.383239, 1.335523, 1.285484, 1.275779, 1.274742, 1.169655, 1.151094, 1.134891, 1.109877, 1.092302, 1.092301, 1.053385]  

plt.figure(figsize=(20,5)) 
plt.bar(BI_CHARACTERS, bi_freq_en, color=(0.40, 0.64, 0.80, 0.8), edgecolor=(0.09, 0.45, 0.71)) 
plt.suptitle('Bigram frequencies for English') 
plt.show()


#Trigram frequencies trong ngôn ngữ tiếng Anh
TRI_CHARACTERS = ['THE', 'AND', 'ING', 'HER', 'HAT', 'HIS', 'THA', 'ERE', 'FOR', 'ENT', 'ION', 'TER', 'WAS', 'YOU', 'ITH', 'VER', 'ALL', 'WIT', 'THI', 'TIO'] 
tri_freq_en = [3.508232, 1.593878, 1.147042, 0.822444, 0.650715, 0.596748, 0.593593, 0.560594, 0.555372, 0.530771, 0.506454, 0.461099, 0.460487, 0.437213, 0.43125, 0.430732, 0.422758, 0.39729, 0.394796, 0.378058]  

plt.figure(figsize=(20,5)) 
plt.bar(TRI_CHARACTERS, tri_freq_en, color=(0.40, 0.64, 0.80, 0.8), edgecolor=(0.09, 0.45, 0.71)) 
plt.suptitle('Trigram frequencies for English') 
plt.show()

