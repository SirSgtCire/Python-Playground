# Main file for running test strategies
# make sure to do imports here
import os

def test_file2_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	assert x == y,"test failed because x=" + str(x) + " y=" + str(y)
