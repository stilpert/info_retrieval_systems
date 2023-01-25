import os
import re
import json
import constants
from collections import OrderedDict


def inverted_index(text, inverted_index, filename):
	regex = r'\b\w+\b'
	words = re.findall(regex, text)
	for word in words:
		lowercase_word = word.lower()
		if lowercase_word not in inverted_index:
			inverted_index[lowercase_word] = []

		if filename not in inverted_index[lowercase_word]:
			inverted_index[lowercase_word].append(filename)

	return


if __name__ == "__main__":

	inverted_index_result = {}
	for filename in os.listdir(constants.DATA_DIR):
		path = os.path.join(constants.DATA_DIR, filename)
		f = open(path, "r")
		inverted_index(f.read(), inverted_index_result, filename)

	inverted_index_result = OrderedDict(sorted(inverted_index_result.items()))
	output = open(constants.INVERTED_INDEX_JSON, "w")
	output.write(json.dumps(inverted_index_result, indent=4))