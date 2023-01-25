import sys
import json
import constants


def get_files_names(index, word):
	result = []
	for filename in index:
		if word in index[filename]:
			result.append(filename)
	return result


if __name__ == "__main__":
	if (len(sys.argv) < 2):
		raise "Error, arguments should be provided. Please provide words in the arguments"

	try: 
		file = open(constants.FORWARD_INDEX_JSON, "r")
	except:
		raise "File is not found"

	index = json.loads(file.read())
	for searched_word in sys.argv[1:]:
		result = get_files_names(index, searched_word)
		if not result:
			print(f'{searched_word} : {"There are no files that contain this word"}')
			continue

		files_names = ", ".join(result)
		print(f'{searched_word} : {files_names}')