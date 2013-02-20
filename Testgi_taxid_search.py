#!/usr/bin/python
import sys
import os
import unittest
import gi_taxid_search

class TestGiTaxIDFinder(unittest.TestCase):
    def create_testfile(self):
        outfile = open(self.filename, "w")
	outfile.write("0\ta\n")
	outfile.write("1\tb\n")
	outfile.write("2\tc\n")
	outfile.write("3\td\n")
	outfile.write("4\te\n")
	outfile.write("5\tf\n")
	outfile.write("6\tg\n")
	outfile.write("7\th\n")
	outfile.write("8\ti\n")
	outfile.write("9\tj\n")
	outfile.close()

    def setUp(self):
	if not os.path.exists("./fixture"):
	    os.mkdir("./fixture")
        self.filename = "./fixture/giNrtest.txt"
        self.create_testfile()

    def tearDown(self):
        os.remove(self.filename)

    def test_searchFile0(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "0\ta"
	self.assertEqual(finder.searchFile(0), expectedLine)

    def test_searchFile1(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "1\tb"
	self.assertEqual(finder.searchFile(1), expectedLine)

    def test_searchFile2(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "2\tc"
	self.assertEqual(finder.searchFile(2), expectedLine)

    def test_searchFile3(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "3\td"
	self.assertEqual(finder.searchFile(3), expectedLine)

    def test_searchFile4(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "4\te"
	self.assertEqual(finder.searchFile(4), expectedLine)

    def test_searchFile5(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "5\tf"
	self.assertEqual(finder.searchFile(5), expectedLine)

    def test_searchFile6(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "6\tg"
	self.assertEqual(finder.searchFile(6), expectedLine)

    def test_searchFile7(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "7\th"
	self.assertEqual(finder.searchFile(7), expectedLine)

    def test_searchFile8(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "8\ti"
	self.assertEqual(finder.searchFile(8), expectedLine)

    def test_searchFile9(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = "9\tj"
	self.assertEqual(finder.searchFile(9), expectedLine)

    def test_searchFile10(self):
	finder = gi_taxid_search.GItaxidFinder(self.filename)
	expectedLine = ""
	self.assertEqual(finder.searchFile(10), expectedLine)

def suite():
    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromTestCase(TestGiTaxIDFinder)
    return testsuite

def main():
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testsuite)

main()
