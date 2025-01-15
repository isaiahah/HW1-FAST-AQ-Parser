# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    if not all(nucleotide in ALLOWED_NUC for nucleotide in seq):
        raise Exception(f"Sequence {seq} contains non-nucleotide character")
    transcribed = "".join(map(lambda n: TRANSCRIPTION_MAPPING[n], seq))
    if reverse:
        transcribed = transcribed[::-1]
    return transcribed


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq, reverse=True)