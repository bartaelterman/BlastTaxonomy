#!/usr/bin/python

import unittest
import sys
import blasthittaxonomy

class TestTaxonomyFetcher(unittest.TestCase):
    def createFixture(self):
	if not os.path.exists("./fixture"):
	    os.mkdir("./fixture")
        outfile = open("./fixture/wrongKnownTaxonomy.txt", "w")
	outfile.write(pickle.dumps({"9913": [{u'Lineage': 'cellular organisms; Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Embryophyta; Tracheophyta; Euphyllophyta; Spermatophyta; Magnoliophyta; eudicotyledons; core eudicotyledons; Caryophyllales; Caryophyllaceae; Silene', u'Division': 'Plants', u'ParentTaxId': '3573', u'PubDate': '1995/05/09 15:59:00', u'LineageEx': [{u'ScientificName': 'cellular organisms', u'TaxId': '131567', u'Rank': 'no rank'}, {u'ScientificName': 'Eukaryota', u'TaxId': '2759', u'Rank': 'superkingdom'}, {u'ScientificName': 'Viridiplantae', u'TaxId': '33090', u'Rank': 'kingdom'}, {u'ScientificName': 'Streptophyta', u'TaxId': '35493', u'Rank': 'phylum'}, {u'ScientificName': 'Streptophytina', u'TaxId': '131221', u'Rank': 'no rank'}, {u'ScientificName': 'Embryophyta', u'TaxId': '3193', u'Rank': 'no rank'}, {u'ScientificName': 'Tracheophyta', u'TaxId': '58023', u'Rank': 'no rank'}, {u'ScientificName': 'Euphyllophyta', u'TaxId': '78536', u'Rank': 'no rank'}, {u'ScientificName': 'Spermatophyta', u'TaxId': '58024', u'Rank': 'no rank'}, {u'ScientificName': 'Magnoliophyta', u'TaxId': '3398', u'Rank': 'no rank'}, {u'ScientificName': 'eudicotyledons', u'TaxId': '71240', u'Rank': 'no rank'}, {u'ScientificName': 'core eudicotyledons', u'TaxId': '91827', u'Rank': 'no rank'}, {u'ScientificName': 'Caryophyllales', u'TaxId': '3524', u'Rank': 'order'}, {u'ScientificName': 'Caryophyllaceae', u'TaxId': '3568', u'Rank': 'family'}, {u'ScientificName': 'Silene', u'TaxId': '3573', u'Rank': 'genus'}], u'CreateDate': '1995/05/09 15:59:00', u'TaxId': '39875', u'Rank': 'species', u'GeneticCode': {u'GCId': '1', u'GCName': 'Standard'}, u'ScientificName': 'Silene conica', u'MitoGeneticCode': {u'MGCId': '1', u'MGCName': 'Standard'}, u'UpdateDate': '2005/01/19 14:59:40'}]}))
	outfile.close()

    def test_getTaxonomyfromFile(self):
        tf = blasthittaxonomy.TaxonomyFetcher()
	giNr = 2
	tf.setKnownTaxaFile("./fixture/wrongKnownTaxonomy.txt")
	taxonomy = tf.getTaxonomy(giNr)
	self.assertEqual(taxonomy[0]["Division"], "Plants")

    def test_retrieveTaxonomy(self):
        tf = blasthittaxonomy.TaxonomyFetcher()
	taxonID = "9913"
	scientName = "Bos taurus"
	taxonomy = tf.retrieveTaxonomy(taxonID)
	self.assertEqual(scientName, taxonomy[0]["ScientificName"])

    def test_getTaxonID(self):
        tf = blasthittaxonomy.TaxonomyFetcher()
	giNr = 2
	expectedTaxonID = "9913"
	print "searching for giNr: ", giNr
	self.assertEqual(expectedTaxonID, tf.getTaxonID(giNr))

def suite():
    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromTestCase(TestTaxonomyFetcher)
    return testsuite

def main():
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testsuite)

main()
