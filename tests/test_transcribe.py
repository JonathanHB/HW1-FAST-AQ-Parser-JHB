# write tests for transcribes
import seqparser
from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

def exception_assertion(test_input, function, expected_exception):

    empty_handled = True
    try:
        function(test_input)
        empty_handled = False
    except ValueError as e:
        if str(e) != expected_exception:
            empty_handled = False

    return empty_handled
        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """

    test_input  = "ACGGACCCCGGATTAACCACCATGAA"
    test_output = "UGCCUGGGGCCUAAUUGGUGGUACUU"

    #test normal operation
    assert seqparser.transcribe(test_input) == test_output, \
        "Transcription unit test 1 failed; did not correctly transcribe test sequence"
    print("Transcription unit test 1 passed: normal sequence was accurately transcribed.")

    assert exception_assertion("", seqparser.transcribe, "Seq can't be an empty string."), \
        "Transcription unit test 2 failed, did not detect and report empty input"
    print("Transcription unit test 2 passed: empty sequence was detected and reported.")

    assert exception_assertion(189567482, seqparser.transcribe, "Seq must be of type string."), \
        "Transcription unit test 3 failed, did not detect and report non-string input"
    print("Transcription unit test 3 passed: non-string sequence was detected and reported.")

    non_nucleotide = "B"
    non_nucleotide_index = 7
    wrong_test_input = test_input[0:non_nucleotide_index] + non_nucleotide + test_input[non_nucleotide_index+1:]
    assert exception_assertion(wrong_test_input, seqparser.transcribe,
                               f"Nucleotide {non_nucleotide} at position {non_nucleotide_index+1} for {wrong_test_input} was not an allowed DNA nucleotide."), \
        "Transcription unit test 4 failed, did not detect and report non-nucleotide in sequence"
    print("Transcription unit test 4 passed: non-nucleotide was detected and reported.")

test_transcribe()

def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    pass
