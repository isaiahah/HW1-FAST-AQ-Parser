# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # Test case where no sequence data (bad.fa)
    badfa_parser = FastaParser("./tests/bad.fa")
    with pytest.raises(ValueError):
        badfa_records = [record for record in badfa_parser]

    # Test case where empty data file (blank.fa)
    blankfa_parser = FastaParser("./tests/blank.fa")
    with pytest.raises(ValueError):
        blankfa_records = [record for record in blankfa_parser]

    # Test case that test.fa reads in and has correct number of records
    testfa_parser = FastaParser("./data/test.fa")
    testfa_records = [record for record in testfa_parser]
    assert len(testfa_records) == 100

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # Test case on test.fa
    testfa_parser = FastaParser("./data/test.fa")
    testfa_records = [record for record in testfa_parser]
    # Check first, last, and an entry in the middle
    assert testfa_records[0] == ("seq0", "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA")
    assert testfa_records[99] == ("seq99", "CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA")
    assert testfa_records[42] == ("seq42", "GCGCCGGCGCTGTATTCTGCAGATGGAGGGTAGCCCCTGAGTCTGATATAACACGGCCTTTGTAATAGAGCCCCATAGAAGCCCTGGATCTGGAAGCCTG")

    # Omitted test on fastq files, as the parser is not intended to read those


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # Test case on test.fq: check it loads the records without error and
    # returns the correct number of records
    testfq_parser = FastqParser("./data/test.fq")
    testfq_records = [record for record in testfq_parser]
    assert len(testfq_records) == 100

    # Test case where empty data file (blank.fa)
    blankfq_parser = FastqParser("./tests/blank.fa")
    with pytest.raises(ValueError):
        blankfq_records = [record for record in blankfq_parser]

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Test case on test.fq: check first, last, and middle entry
    testfq_parser = FastqParser("./data/test.fq")
    testfq_records = [record for record in testfq_parser]
    assert len(testfq_records) == 100
    assert testfq_records[0] == ("seq0", "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG", "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32=")
    assert testfq_records[99] == ("seq99", "CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG", "2$7)*5:\"=+++!:.=>!5>79)8!566$!3*/4$=4.%=//;900$9)!%)4%$=0\":02\"0=!0#/>+*1$1$39!.8+9<'1$*1$321&<'&9,)2")
    assert testfq_records[42] == ("seq42", "GATAAGTCGTTGGAAACGTGTCGTTACGACAGTGCGCACTTTACAGGGGTCTCCAGCGGGTGCTGAGGTCGTTCTCAGTATTATTATCTGTGGTACCTAA", ">%79;86'9>;61$8703*#;#<1*16>>15$57&,969411*'=0=-#\"0>&&-'%8'\"1->95<;5<0:4\"%2<'+99+610-6%40<6600.&\".07")
