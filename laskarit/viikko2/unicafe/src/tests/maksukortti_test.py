import unittest
from maksukortti import Maksukortti

# Rahan ottaminen toimii:
    # Saldo vähenee oikein, jos rahaa on tarpeeksi
    # Saldo ei muutu, jos rahaa ei ole tarpeeksi
    # Metodi palauttaa True, jos rahat riittivät ja muuten False

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")