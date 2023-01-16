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

def exception_assertion(test_input, expected_exception):

    empty_handled = True
    try:
        seqparser.transcribe(test_input)
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
    assert seqparser.transcribe(test_input) == test_output, "Transcription unit test 1 failed; did not correctly transcribe test sequence"
    print("Transcription unit test 1 passed: normal sequence was accurately transcribed.")

    #test empty string detection
    test_empty = ""

    empty_handled = True
    try:
        seqparser.transcribe(test_empty)
        empty_handled = False
    except ValueError as e:
        if str(e) != "Seq can't be an empty string.":
            empty_handled = False

    assert empty_handled, "Transcription unit test 2 failed, did not detect and report empty input"
    print("Transcription unit test 2 passed: empty sequence was detected and reported.")


    #test non-string handling
    test_nonstring = 189567482

    nonstr_handled = True
    try:
        seqparser.transcribe(test_nonstring)
        nonstr_handled = False
    except ValueError as e:
        if str(e) != "Seq must be of type string.":
            nonstr_handled = False

    assert nonstr_handled, "Transcription unit test 3 failed, did not detect and report non-string input"
    print("Transcription unit test 3 passed: non-string sequence was detected and reported.")


test_transcribe()

def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    pass
