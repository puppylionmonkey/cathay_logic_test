str1 = "Hello welcome to Cathay 60th year anniversary"
str1 = str1.upper()
ch_count_dict = dict()
for ch in str1:
    if ch == ' ':
        continue
    if ch not in ch_count_dict.keys():
        ch_count_dict[ch] = 1
    else:
        ch_count_dict[ch] += 1
# print(ch_count_dict)
ch_count_dict = dict(sorted(ch_count_dict.items()))
for ch, count in ch_count_dict.items():
    print(ch, count)
