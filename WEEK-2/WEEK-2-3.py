first = "kaleidoscope"
second = ""
for i in range(len(first)-1,-1,-2):
  second = first[i]+second

"""

Here len(first) returns size of first which is 12 therefore len(first)-1 is 11
till i value is greater than -1 the loop should run
everytime i value must decreament by 2
so the code works like this
i value will be set to 11 which is greater than -1 so it comes inside for loop
initially we have set secound value empty
now secound value will be first[11] which is 'e' will be added with ""
somewhat like this secound='e'+""; ==> which will be like secound=e
i value will be decremented by 2 now i value will be 9
we have secound value as e
now secound value will be first[9] which is 'o' will be added with "e"
somewhat like this secound='o'+"e"; ==> which will be like secound=oe
i value will be decremented by 2 now i value will be 7
we have secound value as oe
now secound value will be first[7] which is 's' will be added with "oe"
somewhat like this secound='s'+"oe"; ==> which will be like secound=soe
i value will be decremented by 2 now i value will be 5
we have secound value as d
now secound value will be first[5] which is 'd' will be added with "soe"
somewhat like this secound='d'+"soe"; ==> which will be like secound=dsoe
i value will be decremented by 2 now i value will be 3
we have secound value as e
now secound value will be first[3] which is 'e' will be added with "dsoe"
somewhat like this secound='e'+"dsoe"; ==> which will be like secound=edsoe
i value will be decremented by 2 now i value will be 1
we have secound value as a
now secound value will be first[1] which is 'a' will be added with "edsoe"
somewhat like this secound='a'+"edsoe"; ==> which will be like secound=aedsoe
i value will be decremented by 2 now i value will be -1
condition will be false and the program will terminate

"""