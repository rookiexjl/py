# coding: utf-8
# 对比dir1与dir2的目录差异
import filecmp

a = "/home/test/filecmp/dir1"
b = "/home/test/filecmp/dir2"
dirobj = filecmp.dircno(a,b,['test.py']) #目录比较忽略test.py文件

dirobj.report()
dirobj.report_partial_closure()
dirobj.report_full_closure()
print "left_list:" + str(dirobj.left_list)
print "right_list:" + str(dirobj.right_list)
print "common:" + str(dirobj.common)
print "lift_only:" + str(dirobj.lift_only)
print "right_only:" + str(dirobj.right_only)
print "common_dirs:" + str(dirobj,common_dirs)
print "common_files:" + str(dirobj.common_files)
print "common_funny:" + str(dirobj.common_funny)
print "same_file:" + str(dirobj.same_file)
print "funny_files:" + str(dirobj.funny_files)




