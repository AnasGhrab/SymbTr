from symbtrdataextractor import extractor
from fileoperations.fileoperations import get_filenames_in_dir

import os

def test_txt_data():
	[txtfilepaths, txtfolders, txtnames] = get_txt_filenames()

	isAllDataValid = True
	for tf, tn in zip(txtfilepaths, txtnames):
		try:
			txtdata, isDataValid = extractor.extract(tf, print_warnings=False)
			isAllDataValid = isDataValid if isAllDataValid else False
		except (RuntimeError, ValueError, KeyError):
			print "Unspecified error in " + tn
			isAllDataValid = False

	assert(isAllDataValid)

def get_txt_filenames():
	symbTrTxtfolder = './txt/'
	return get_filenames_in_dir(symbTrTxtfolder, keyword = '*.txt')