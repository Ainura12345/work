def string_both_ends(str):
    if len(str)<2:
        return ''
    else:
        return str[0:2] + str[-2:]

print(string_both_ends("w3source"))
print(string_both_ends("w3"))
print(string_both_ends("w"))
