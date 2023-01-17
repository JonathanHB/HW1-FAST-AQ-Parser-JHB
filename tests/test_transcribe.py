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

#convert a specific value error to a boolean to be fed into an assert statement
def exception_assertion(test_input, tr_func, expected_exception):

    err_handled = True
    try:
        tr_func(test_input)
        err_handled = False
    except ValueError as e:
        if str(e) != expected_exception:
            err_handled = False

    return err_handled

def transcription_rt_error_handling(tr_func, forward, test_input):

    funcnameroot = "Transcription unit test part "

    if forward:
        funcname = "    " + funcnameroot
    else:
        funcname = "    Reverse t" + funcnameroot[1:]

    # test empty string handling
    assert exception_assertion("", tr_func, "Seq can't be an empty string."), \
        funcname + "2 failed, did not detect and report empty input"
    print(funcname + "2 passed: empty sequence was detected and reported.")

    # test non-string handling
    assert exception_assertion(189567482, tr_func, "Seq must be of type string."), \
        funcname + "3 failed, did not detect and report non-string input"
    print(funcname + "3 passed: non-string sequence was detected and reported.")

    # test non-nucleotide handling
    non_nucleotide = "B"
    non_nucleotide_index = 7
    wrong_test_input = test_input[0:non_nucleotide_index] + non_nucleotide + test_input[non_nucleotide_index + 1:]

    # invert sequence as necessary since the sequence is reversed before the exceptions are reached, so the text thereof
    # includes the reversed forms
    if forward:
        err_nuc_index = non_nucleotide_index + 1
        wrong_test_input_2 = wrong_test_input
    else:
        err_nuc_index = len(wrong_test_input) - non_nucleotide_index
        wrong_test_input_2 = wrong_test_input[::-1]

    assert exception_assertion(wrong_test_input, tr_func,
                               f"Nucleotide {non_nucleotide} at position {err_nuc_index} for {wrong_test_input_2} was not an allowed DNA nucleotide."), \
        funcname + "4 failed, did not detect and report non-nucleotide in sequence"
    print(funcname + "4 passed: non-nucleotide in sequence was detected and reported.")
        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """

    test_input  = "ACGGACCCCGGATTAACCACCATGAA"
    test_output = "UGCCUGGGGCCUAAUUGGUGGUACUU"

    #test normal operation
    assert transcribe(test_input) == test_output, \
        "Transcription unit test 1 failed; did not correctly transcribe test sequence"
    print("Transcription unit test 1 passed: normal sequence was accurately transcribed.")

    transcription_rt_error_handling(transcribe, True, test_input)


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """

    test_input  = "ACGGACCCCGGATTAACCACCATGAA"
    test_output = "UUCAUGGUGGUUAAUCCGGGGUCCGU"

    # test normal operation
    assert reverse_transcribe(test_input) == test_output, \
        "Reverse transcription unit test 1 failed; did not correctly reverse-transcribe test sequence"
    print("Reverse transcription unit test 1 passed: normal sequence was accurately reverse-transcribed.")

    transcription_rt_error_handling(reverse_transcribe, False, test_input)

test_transcribe()
test_reverse_transcribe()
