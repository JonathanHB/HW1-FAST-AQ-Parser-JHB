# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import data
from data import make_seq #note that 'import data.make_seq' does not work


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """

    #need to set this dynamically
    path_to_install = '/Users/jonathanborowsky/PycharmProjects/HW1-FAST-AQ-Parser-JHB'

    test_fa_truth = make_seq.main()[0]
    test_fastaparser_1 = FastaParser(path_to_install + '/data/test.fa')

    for idx, ri in enumerate(test_fastaparser_1):

        assert list(ri) == test_fa_truth[idx], f"Fasta parser unit test failed: parsed record {idx} of fasta file ( {list(ri)} ) does not match true record {test_fa_truth[idx]}."

    print("Fasta parser unit test 1 passed; parser output matched true file contents.")

    #I can't get assertRaises() to work, so I'm using a try/except statement to check empty file handling

    try:
        test_fastaparser_2 = FastaParser(path_to_install + '/data/test_empty.fa')
        # this line is just to call test_fastparser_2's __iter__ method and throw an empty file error
        b = [i for i in test_fastaparser_2]
        empty_passed = False
    except ValueError as e:
        if str(e) == f"File ({path_to_install}/data/test_empty.fa) had 0 lines.":
            empty_passed = True
        else:
            empty_passed = False

    assert empty_passed, "Fasta parser unit test 2 failed; parser failed to throw correct exception for empty file."

    print("Fasta parser unit test 2 passed; parser recognized empty file.")


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """

    path_to_install = '/Users/jonathanborowsky/PycharmProjects/HW1-FAST-AQ-Parser-JHB'

    test_fq_truth = make_seq.main()[1]
    test_fastqparser = FastqParser(path_to_install + '/data/test.fq')

    #this is potentially more informative than trying to compare lists of lists directly because it tells the user
    #where in the fastq file the mismatch occurs
    for idx, ri in enumerate(test_fastqparser):

        assert list(ri) == test_fq_truth[idx], f"Fastq parser unit test failed: parsed record {idx} of fastq file ( {list(ri)} ) does not match true record {test_fq_truth[idx]}."

    print("Fastq parser unit test 1 passed; parser output matched true file contents.")

    #I can't get assertRaises() to work, so I'm using a try/except statement to check empty file handling

    try:
        test_fastqparser_2 = FastqParser(path_to_install + '/data/test_empty.fq')
        # this line is just to call test_fastparser_2's __iter__ method and throw an empty file error
        b = [i for i in test_fastqparser_2]
        empty_passed = False
    except ValueError as e:
        if str(e) == f"File ({path_to_install}/data/test_empty.fq) had 0 lines.":
            empty_passed = True
        else:
            empty_passed = False

    assert empty_passed, "Fastq parser unit test 2 failed; parser failed to throw correct exception for empty file."

    print("Fastq parser unit test 2 passed; parser recognized empty file.")


test_FastaParser()
test_FastqParser()