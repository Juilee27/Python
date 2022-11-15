# _________for loop with else--------------------
khana = ["roti", 'sabzi', 'chawal']

# for item in khana:
#     print(item, end=" ")
#     break #break se loop se bahar ayega sidha
#
# else:
#     print('\nthis for loop ended properly')

for item in khana:
    # if item == "paratha":
    if item == "roti":

        # pass
        break
else:
    print("item does not exist in list")