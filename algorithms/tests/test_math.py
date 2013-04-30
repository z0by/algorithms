import unittest
from ..math.extended_gcd import extended_gcd
from ..math.sieve_atkin import atkin


class TestExtendedGCD(unittest.TestCase):

    def test_extended_gcd(self):
        # Find extended_gcd of 35 and 77
        (a, b) = extended_gcd(35, 77)
        self.assertIs(35 * a + 77 * b, 7)

        # Find extended_gcd of 15 and 19
        (a, b) = extended_gcd(15, 19)
        self.assertIs(15 * a + 19 * b, 1)

        # Find extended_gcd of 18 and 9
        (a, b) = extended_gcd(18, 9)
        self.assertIs(18 * a + 9 * b, 9)

        # Find extended_gcd of 99 and 81
        (a, b) = extended_gcd(99, 81)
        self.assertIs(99 * a + 81 * b, 9)

        # Find extended_gcd of 50 and 15
        (a, b) = extended_gcd(50, 15)
        self.assertIs(50 * a + 15 * b, 5)

class TestSieveOfAtkin(unittest.TestCase):

    def test_atkin(self):
        rv1 = atkin(10)
        rv2 = atkin(100)
        rv3 = atkin(1000)
        rv4 = atkin(-10)
        self.assertEqual(rv1,[2, 3, 5, 7])
        self.assertEqual(rv2,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(rv3,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
                              101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
                              211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 
                              337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 
                              461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 
                              601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 
                              739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 
                              881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])
        self.assertEqual(rv4,[])
