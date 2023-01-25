import unittest

import forwardIndex
import invertedIndex
import forwardSearch
import invertedSearch


class TestForwardIndex(unittest.TestCase):
	def test_should_returnWords(self):
		text = 'One TWO thrEE four'
		result = forwardIndex.get_forward_index_words(text)
		self.assertEqual(result, ['four', 'one', 'three', 'two'])

	def test_should_returnOneWord_when_oneWordInText(self):
		text = 'One'
		result = forwardIndex.get_forward_index_words(text)
		self.assertEqual(result, ['one'])

	def test_should_returnEmpty_when(self):
		text = ''
		result = forwardIndex.get_forward_index_words(text)
		self.assertEqual(True, not result)


class TestInvertedIndex(unittest.TestCase):
	def test_should_invertWords(self):
		text = 'One TWO thrEE four'
		dict = {
			'two': ['file1']
		}
		invertedIndex.inverted_index(text, dict, 'file2')
		self.assertDictEqual(dict, {
			'two': ['file1', 'file2'],
			'one': ['file2'],
			'three': ['file2'],
			'four': ['file2']
		})

	def test_should_invertOneWord_when_oneWordInText(self):
		text = 'One'
		dict = {
			'one': ['file1']
		}
		invertedIndex.inverted_index(text, dict, 'file2')
		self.assertDictEqual(dict, {
			'one': ['file1', 'file2']
		})

	def test_should_notInvert_when_emptyText(self):
		text = ''
		dict = {
			'one': ['file1']
		}
		invertedIndex.inverted_index(text, dict, 'file2')
		self.assertEqual(dict, {
			'one': ['file1']
		})


class TestSearchForward(unittest.TestCase):
	def test_should_returnMultipleFilesNames_when_presentInMultiplesFiles(self):
		forward_index = {
			'file1': ['one', 'two', 'three'],
			'file2': ['three'],
		}
		result = forwardSearch.get_files_names(forward_index, 'three')
		self.assertEqual(result, ['file1', 'file2'])

	def test_should_returnOneFileName_when_presentInOneFile(self):
		forward_index = {
			'file1': ['one', 'two', 'three'],
			'file2': ['four'],
		}
		result = forwardSearch.get_files_names(forward_index, 'two')
		self.assertEqual(result, ['file1'])

	def test_should_returnEmpty_when_notPresentInAnyFile(self):
		forward_index = {
			'file1': ['one', 'two', 'three'],
			'file2': ['four'],
		}
		result = forwardSearch.get_files_names(forward_index, 'five')
		self.assertEqual(result, [])


class TestSearchInverted(unittest.TestCase):
	def test_should_returnMultipleFilesNames_when_presentInMultiplesFiles(self):
		inverted_index = {
			'one': ['file1', 'file3'],
			'two': ['file2'],
		}
		result = invertedSearch.get_files_names(inverted_index, 'one')
		self.assertEqual(result, ['file1', 'file3'])
		
	def test_should_returnOneFileName_when_presentInOneFile(self):
		inverted_index = {
			'one': ['file1'],
			'two': ['file2'],
		}
		result = invertedSearch.get_files_names(inverted_index, 'one')
		self.assertEqual(result, ['file1'])

	def test_should_returnEmpty_when_notPresentInAnyFile(self):
		inverted_index = {
			'one': ['file2'],
		}
		result = invertedSearch.get_files_names(inverted_index, 'two')
		self.assertEqual(result, [])


if __name__ == '__main__':
	unittest.main()