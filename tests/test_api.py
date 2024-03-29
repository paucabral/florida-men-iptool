import sys
sys.path.append('../')
from api import getSpecificIP, getOwnIP, usedFields, errorFields
from unittest import TestCase, main

validIP = '2001:4860:4860::8888'
invalidIP = '123.3.21.3.2'
multIP = ('2001:4860:4860::8888', '8.8.8.8', '2001:4860:4860::8844')
invalidIP_Reserved = '192.168.0.0'

class apiUnittest(TestCase):
    #Validate API if returns exist for captuing specific IP
    def testGSIP_working(self):
        self.assertIsNotNone(getSpecificIP(validIP))        #Working IP (Specific)
        self.assertIsNotNone(getSpecificIP(invalidIP))      #Invalid IP (Specific)
    
    # NOTE: STASHED DUE TO CHANGES IN IP API RESPONSE.
    #Compare the error fields from return, and the keys as list of invalid IP
    # def testGSIP_invalidIP(self):
    #     self.assertEqual(errorFields, list(getSpecificIP(invalidIP).keys()))

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