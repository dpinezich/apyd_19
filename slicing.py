


line = "David:Pinezich"
colon_pos = line.find(':')


entry_key = line[:colon_pos]
entry_content = line[colon_pos + 1:]

print(entry_key)
print(entry_content)