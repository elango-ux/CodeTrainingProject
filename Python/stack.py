# empty list
browsing_seaion = []
#add item in the list using append functin
browsing_seaion.append(1)
browsing_seaion.append(2)
browsing_seaion.append(3)
browsing_seaion.append(4)
print(browsing_seaion)
#remove last item in the list (back button)
browsing_seaion.pop()
print(browsing_seaion)
browsing_seaion.pop()
print("redirect to previous page",browsing_seaion)
browsing_seaion.pop()
browsing_seaion.pop()
if not browsing_seaion:
    print("disable")