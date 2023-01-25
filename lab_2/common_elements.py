import os
import re
import constants


def __remove_duplicates(l):
	return list(dict.fromkeys(l))

def __inverted_index(text, inverted_index, filename):
	regex = r'\b\w+\b'
	words = re.findall(regex, text)
	for word in words:
		lowercase_word = word.lower()
		if lowercase_word not in inverted_index:
			inverted_index[lowercase_word] = []

		if filename not in inverted_index[lowercase_word]:
			inverted_index[lowercase_word].append(filename)

	return

def __get_headline(text):
	return text.split('\n')[0]

def common(list1, list2):
	return __remove_duplicates([i for i in list1 if i in list2])

def create_index(filenames, index, file_titles):
	for filename in filenames:
		path = os.path.join(constants.DATA_DIR, filename)
		f = open(path, "r")
		text = f.read()
		file_titles[filename] = __get_headline(text)
		__inverted_index(text, index, filename)

def search(index, query):
	filenames = os.listdir(constants.DATA_DIR)
	words = query.split(" ")
	for word in words:
		if word not in index:
			return []
		
		filenames = common(filenames, index[word])

	return filenames

if __name__ == "__main__":
	index = {}
	file_titles = {}
	create_index(os.listdir(constants.DATA_DIR), index, file_titles)
	
	query = ""
	while True:
		query = input('Query (empty query to stop) : ').strip()
		if not query:
			print('Stop')
			break

		print('Results for query : ' + query)
		filenames = search(index, query)
		if not filenames:
			print('No results match that query.')
			continue

		for i, filename in enumerate(filenames):
			print("{}. Title : {}. File : {}".format(i + 1, file_titles[filename], filename))