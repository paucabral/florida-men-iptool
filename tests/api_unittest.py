from unittest import TestCase, main
import sys
sys.path.append('../')
from api import getSpecificIP, getOwnIP, usedFields, errorFields, test

class apiUnittest(TestCase):
    #Validate API if returns exist for captuing specific IP
    def testGSIP_working(self):
        self.assertIsNotNone(getSpecificIP(validIP))        #Working IP (Specific)
        self.assertIsNotNone(getSpecificIP(invalidIP))      #Invalid IP (Specific)
    
    #Compare the used fields from return, and the keys as list of accepted IP
    def testGSIP_acceptIP(self):
        self.assertEqual(usedFields, list(getSpecificIP(validIP).keys()))

    #Compare the used fields from return, and the keys as list of invalid IP
    def testGSIP_invalidIP(self):
        self.assertEqual(errorFields, list(getSpecificIP(invalidIP).keys()))

    #Verify reason for invalid IP if true 
    def testGSIP_invalidIP_invalid(self):
        self.assertTrue('Invalid IP Address', getSpecificIP(invalidIP)['reason'])

    #Verify reason for invalid - reserved IP if true
    def testGSIP_invalidIP_reserved(self):
        self.assertTrue('Reserved IP Address', getSpecificIP(invalidIP_Reserved)['reason'])

    #Verify will raise error TypeError without input
    def testGSIP_noInput(self):
        def test():
            noInputIP = getSpecificIP()
        with self.assertRaises(TypeError):
            test()

    #Verify will raise error ValueError with multiple inputs    
    def testGSIP_multipleInput(self):
        def test():
            multInput = getSpecificIP(multIP)
        with self.assertRaises(ValueError):
            test()

    #Validate API if returns exist for capturing own IP
    def testGOIP_working(self):
        self.assertIsNotNone(getOwnIP()) #IP (Own)

if __name__ == '__main__':
    main()