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

    test_fa_truth = make_seq.main()[0]
    test_fastaparser = FastaParser('/Users/jonathanborowsky/PycharmProjects/HW1-FAST-AQ-Parser-JHB/data/test.fa')

    for idx, ri in enumerate(test_fastaparser):

        assert list(ri) == test_fa_truth[idx], f"Fasta parser unit test failed: parsed record {idx} of fasta file ( {list(ri)} ) does not match true record {test_fa_truth[idx]}."

    print("Fasta parser unit test passed; parser output matched true file contents.")
    return True


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """

    test_fq_truth = make_seq.main()[1]
    test_fastqparser = FastqParser('/Users/jonathanborowsky/PycharmProjects/HW1-FAST-AQ-Parser-JHB/data/test.fq')

    #this is potentially more informative than trying to compare lists of lists directly because it tells the user
    #where in the fastq file the mismatch occurs
    for idx, ri in enumerate(test_fastqparser):

        assert list(ri) == test_fq_truth[idx], f"Fastq parser unit test failed: parsed record {idx} of fastq file ( {list(ri)} ) does not match true record {test_fq_truth[idx]}."

    print("Fastq parser unit test passed; parser output matched true file contents.")
    return True


test_FastaParser() #works for the standard case
test_FastqParser()

# if ri[0] != test_fa_truth[idx][0]:
#     print(f"Fasta parser unit test failed; label entry {idx} of test file ({ri[0]}) does not "
#           f"yield correct value of {test_fa_truth[idx][0]}.")
#     return False
#
# if ri[1] != test_fa_truth[idx][1]:
#     print(f"Fasta parser unit test failed; data entry {idx} of test file ({ri[1]}) does not "
#           f"yield correct value of {test_fa_truth[idx][1]}.")
#     return False
