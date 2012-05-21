from amuse.test.amusetest import TestWithMPI

from amuse.community.seba.interface import SeBaInterface, SeBa

from amuse.units import units
from amuse.datamodel import Particle

class TestSeBaInterface(TestWithMPI):

    def test1(self):
        instance = self.new_instance_of_an_optional_code(SeBaInterface)
            
        endtime, mass, radius, luminosity, temperature, time_step, stellar_type, error = instance.evolve_star(1, 4600, 0.02)
        self.assertEquals(error, 0)
        self.assertTrue( endtime <= 4600.0)
        self.assertAlmostRelativeEqual(endtime, 4600.0, 4)
        self.assertAlmostRelativeEqual(mass, 1.0, 6)
        self.assertAlmostRelativeEqual(radius, 0.9856, 4)
        self.assertAlmostRelativeEqual(luminosity, 0.9585, 4)
        self.assertAlmostRelativeEqual(temperature, 5751, 4)
        self.assertAlmostRelativeEqual(time_step, 1089.3, 4)
        self.assertEqual(stellar_type, 1)
        
class TestSeBa(TestWithMPI):

    def test1(self):
        
        instance = self.new_instance_of_an_optional_code(SeBa)
            
        endtime, mass, radius, luminosity, temperature, time_step, stellar_type = instance.evolve_star(1 | units.MSun, 4600 | units.Myr, 0.02)
        
        self.assertTrue( endtime <= 4600 | units.Myr)
        self.assertAlmostRelativeEqual(mass, 1.0 | units.MSun, 4)
        self.assertAlmostRelativeEqual(radius, 0.9856 | units.RSun, 4)
        self.assertAlmostRelativeEqual(luminosity, 0.9585 | units.LSun, 4)
        self.assertAlmostRelativeEqual(temperature, 5751 | units.K, 4)
        self.assertAlmostRelativeEqual(time_step, 1089.3 | units.Myr, 4)
        self.assertEqual(stellar_type, 1 | units.stellar_type)

        
    def test2(self):
        instance = self.new_instance_of_an_optional_code(SeBa)
        
        p = Particle()
        p.mass = 5 | units.MSun
        p.metallicity = 0.02
        
        p = instance.particles.add_particle(p)
        instance.evolve_model(130 | units.Myr)

        self.assertAlmostRelativeEqual(p.mass, 0.9906 | units.MSun, 4)
        
