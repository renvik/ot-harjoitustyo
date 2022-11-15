import unittest
from kassapaate import Kassapaate

class Kassapaate(unittest.TestCase):
    def setUp(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def test_saldot_on_alussa_oikein(self):
        self.assertEqual(str(self.kassassa_rahaa), "100000")
        self.assertEqual(str(self.edulliset), "0")
        self.assertEqual(str(self.maukkaat), "0")

    def kateisosto_toimii_edullisten_osalta(self):
        self.assertEqual(str(self.kassassa_rahaa), self.kassassa_rahaa + 240)
        #self.assertEqual(str(self.edulliset), self.edulliset += 1)       
    
    def kateisosto_toimii_maukkaiden_osalta(self):
        self.assertEqual(str(self.kassassa_rahaa), self.kassassa_rahaa + 400)

    #def riittava_maksu_kasvattaa_kassaa(self):


