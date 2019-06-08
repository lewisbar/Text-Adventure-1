from time import sleep

def narrate(text, delay=0.03):
	if not text:
		return
	for char in text:
		print(char, end='', flush=True)
		sleep(delay)
	print('')

def list_up(*args, char_delay=0.01, line_delay=0.3):
	for text in args:
		if not text:
			continue
		narrate(text, char_delay)
		sleep(line_delay)
