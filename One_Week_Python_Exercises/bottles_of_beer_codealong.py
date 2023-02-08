# # num=99

# # while num>0:
# #     print(f'{num} bottles of beer on the wall.')
# #     print(f'{num} bottles of beer.')
# #     print(f'Take one down, pass it around, {num-1} bottles of beer on the wall')
# #     print("*"*40)
# #     num-=1
# # print("There are no bottles on the wall!")

# for bottles in range(99,0,-1):
#     print(f'{bottles} bottles of beer on the walll!')
#     print(f'{bottles} bottles of beer!')

#     if bottles == 1:
#         print(f"Take one down, pass it around, no more bottles of beer on the wall!")
#     else:
#         print(f"Take one down, pass it around {bottles-1} bottles of beer on the wall!")
#     print("*"*40)

bottles=99

while bottles >=2:
    if bottles >2:
        print(f'{bottles} bottles of beer on the wall!')
        print(f'{bottles} bottles of beer!')
        print(f"Take one down, pass it around, {bottles-1} bottles of beer on the wall!")
        print("*"*40)
        bottles-=1
    else:
        print(f'{bottles} bottles of beer on the wall!')
        print(f'{bottles} bottles of beer!')
        print(f"Take one down, pass it around, {bottles-1} bottle of beer on the wall!")
        print("*"*40)
        bottles-=1 

print(f"{bottles} bottle of beer on the wall!")
print(f"{bottles} bottle of beer!")
print("Take it down, pass it around, no more bottles of beer on the wall!")