import sys
from collections import Counter
import re
import pprint

pattern = re.compile("[^\w'-]|_")
with open(sys.argv[1], 'r') as content_file:
	content = content_file.read().strip().lower()
	stripped_content = pattern.sub(' ', content)
	arr = stripped_content.split()
	counter = Counter()
	for word in arr:
		counter[word] += 1

	pprint.pprint(counter)

