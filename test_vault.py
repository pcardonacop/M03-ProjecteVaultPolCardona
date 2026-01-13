import unittest
from vault_security import check_password

class TestVaultSecurity(unittest.TestCase):
    def test_password_length(self):
        """Requisit 1: Mínim 8 caràcters"""
        self.assertFalse(check_password("abc"))      # Massa curta
        self.assertTrue(check_password("abcdefgh"))   # Exactament 8
        self.assertTrue(check_password("abcdefghi"))  # Més de 8
    
    def test_contains_number(self):
        """Requisit 2: Ha de contenir almenys un número"""
        self.assertFalse(check_password("abcdefgh"))  # Sense números
        self.assertTrue(check_password("abcdefg1"))   # Amb número
    
    def test_contains_uppercase(self):
        """Requisit 3: Ha de contenir almenys una majúscula"""
        self.assertFalse(check_password("abcdefg1"))  # Sense majúscules
        self.assertTrue(check_password("Abcdefg1"))   # Amb majúscula
    
    def test_no_admin_word(self):
        """Requisit 4: No pot contenir la paraula 'admin'"""
        self.assertFalse(check_password("admin123"))     # Conté 'admin'
        self.assertFalse(check_password("myadminpass"))  # Conté 'admin'
        self.assertTrue(check_password("Adm1nPass"))     # No conté exacte 'admin'

if __name__ == "__main__":
    unittest.main()
