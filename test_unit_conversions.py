import unittest
import unit_conversions as uc


class TestConversion(unittest.TestCase):
    
    def test_temp(self):
        self.assertEqual(uc.cel_to_K(0), 273.15)
        self.assertEqual(uc.K_to_cel(0), -273.15)

    def test_dosage(self):
        self.assertEqual(uc.rem_to_sv(100), 1)
        self.assertEqual(uc.sv_to_rem(1), 100)
        
    def test_activity(self):
        self.assertEqual(uc.curie_to_bq(1), 3.7E10)
        self.assertEqual(uc.bq_to_curie(3.7E10), 1)

    def test_time(self):
        self.assertEqual(uc.seconds_to_minutes(60), 1)
        self.assertEqual(uc.seconds_to_hours(3600), 1)
        self.assertEqual(uc.seconds_to_days(86400), 1)
        self.assertEqual(uc.seconds_to_years(31557600), 1)
        self.assertEqual(uc.years_to_days(1), 365.25)
        self.assertEqual(uc.years_to_hours(1), 8766)
        self.assertEqual(uc.years_to_minutes(1), 525960)
        self.assertEqual(uc.years_to_seconds(1), 31557600)


if __name__ == '__main__':
    unittest.main()