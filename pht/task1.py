#1-ci daxil edilen ededlerin siralamsi

# a=[]
# say=1
# while say<6:
#     b=int(input("eded daxil edin:"))
#     say+=1
#     a.append(b)

# a.sort()
# print(a)

#2-ci sozu elifba sirasi ile duzmek

# soz = (input("cumleni daxil edin:"))
# sozler = soz.split() 

# sirali_sozler = []  
# for a in sozler:
#     siralanmis_soz = ''.join(sorted(a))
#     sirali_sozler.append(siralanmis_soz)

# sirali_soz = ' '.join(sirali_sozler)
# print(sirali_soz)

#3-cu nece cehde tapildi

# eded=13
# cehd=0

# while True:
#     b=int(input("Texmininizi yazin:"))
#     cehd+=1
#     if b==eded:
#         print(f"Tebrikler {cehd} sayida cehde tapdiniz")
#         break

#4-cu sade ededler

# for i in range(2, 100):  
#     for j in range(2, i):  
#         if i % j == 0:
#             break
#     else: 
#         print(f"Sade eded: {i}")
        