list_1 = [x for x in range(16)]
header = ["|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")]
list_2 = []

for i in list_1:

    list_2.append("|{0:<10d}|{0:^10x}|{0:>10b}|".format(i))
header.extend(list_2)
return header
# for j in header:
#     print(j, sep="\n")
# # print(header, list_2)