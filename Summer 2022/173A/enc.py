


def caesar_enc(m, k, fmt=False):
	m_lower = m.lower()

	c = ""
	l = 0

	for ch in m_lower:
		if ch != ' ':
			if fmt and l > 0 and l%5 == 0:
				c += ' '
			c += chr( ((ord(ch) + k-97) % 26) + 97)
			l += 1

	return c



k = 1
while k < 26:
	print caesar_enc('XPPEE ZXZCC ZH', (-1)*k, fmt=True)
	if k%5 ==0:
		print ""
	k +=1 