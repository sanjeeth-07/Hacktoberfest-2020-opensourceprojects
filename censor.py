blocklist = ['words','to','censor']

with open('messages.txt', 'r+', encoding='utf8') as f:
	with open('messages_censored.txt', 'w', encoding='utf8') as f2:
		replace_string = f.read()
		for word in blocklist:
			replace_string = replace_string.replace(word, '')
		f2.write(replace_string)
