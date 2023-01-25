import os
import re
import json
import constants


def get_forward_index_words(text):
	forward_index_words = []
	regex = r'\b\w+\b'
	words = re.findall(regex, text)
	for word in words:
		lowercase_word = word.lower()
		if lowercase_word not in forward_index_words:
			forward_index_words.append(lowercase_word)

	forward_index_words.sort()

	return forward_index_words


if __name__ == "__main__":

	forward_index_result = {}
	for filename in os.listdir(constants.DATA_DIR):
		path = os.path.join(constants.DATA_DIR, filename)
		f = open(path, "r")
		forward_index_result[filename] = get_forward_index_words(f.read())

	output = open(constants.FORWARD_INDEX_JSON, "w")
	output.write(json.dumps(forward_index_result, indent=4))