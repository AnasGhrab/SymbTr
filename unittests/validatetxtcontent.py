from symbtrdataextractor.SymbTrDataExtractor import SymbTrDataExtractor
from fileoperations.fileoperations import get_filenames_in_dir


def test_txt_data():
    [txtfilepaths, txtfolders, txtnames] = get_txt_filenames()

    is_all_txt_data_valid = True
    for tf, tn in zip(txtfilepaths, txtnames):
        try:
            extractor = SymbTrDataExtractor(print_warnings=False)
            txtdata, is_txt_data_valid = extractor.extract(tf)
            is_all_txt_data_valid = is_txt_data_valid \
                if is_all_txt_data_valid else False
        except (RuntimeError, ValueError, KeyError):
            print "Unspecified error in " + tn
            is_all_txt_data_valid = False

    assert is_all_txt_data_valid


def get_txt_filenames():
    symbtr_txt_folder = './txt/'
    return get_filenames_in_dir(symbtr_txt_folder, keyword='*.txt')
