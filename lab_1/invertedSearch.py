import sys
import json
import constants


def get_files_names(index, word):
	return index[word] if word in index else []


if __name__ == "__main__":
	if (len(sys.argv) < 2):
		raise "Error, arguments should be provided. Please provide words in the arguments"

	try:
		index_file = open(constants.INVERTED_INDEX_JSON, "r")
	except:
		raise "File is not found"

	index = json.loads(index_file.read())
	for searched_word in sys.argv[1:]:
		result = get_files_names(index, searched_word)
		if not result:
			print(f'{searched_word} : {"There are no files that contain this word"}')
			continue

		result_str = ", ".join(result)
		print(f'{searched_word} : {result_str}')