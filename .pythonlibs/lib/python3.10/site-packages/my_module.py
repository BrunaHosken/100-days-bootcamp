"""simple comment for module"""
import sys


def print_list(list_sequence, indented=False, tab_count=0):
    for list_item in list_sequence:
        if isinstance(list_item, list):
            if not isinstance(tab_count, int):
                tab_count = 0
            print_list(list_item, indented, tab_count + 1)
        else:
            if isinstance(tab_count, int):
                if indented:
                    sys.stdout.write('\t' * tab_count)
            sys.stdout.write(str(list_item) + '\n')
