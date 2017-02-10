# coding:utf-8
# 两个字符串的差异比较
import difflib

text1 = """ text1:
This module provice classes and functions for comparing squences.
including HTML and context and unified diffs.
diflib document v7.4
add string
"""

text1_lines = text1.splitlines()
text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""
text2_lines = text2.splitlines()
#d = difflib.Differ()
#diff = d.compare(text1_lines, text2_lines)
#print '\n'.join(list(diff))
d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)

a
