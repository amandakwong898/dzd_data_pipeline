import sys
from collections import Counter

kseq = sys.argv[1]
seq = sys.argv[2]
print('KSEQ:', kseq)
print('SEQ:', seq)

def match(string1, string2):
    string1_len = len(string1)
    possible_matches = []
    for start_index in range(0, string1_len):
        for end_index in range(start_index+1, string1_len+1):
            current_string = string1[start_index:end_index]
            if len(current_string) == len(string2):
                if hamming_distance(current_string, string2) <= 2:
                    possible_matches.append(string1[start_index:end_index])
    if len(possible_matches) > 0:
        possible_matches=list(set(possible_matches))
        for match in possible_matches:
            print(match)

def hamming_distance(string1, string2):
    dist = 0
    length = len(string1)
    for i in range(length):
        if string1[i] != string2[i]:
            dist += 1
    return dist

match(seq.rstrip(),kseq.rstrip())