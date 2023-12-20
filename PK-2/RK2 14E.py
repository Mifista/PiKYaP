import unittest
import PK1


class testPK1(unittest.TestCase):
    def setUp(self):
        self.test1 = (['Металл', 'Хардстайл'], ['MetallicA', 'Bladee Mixtape', 'SOAD Mezmerize'])
        self.test2 = [['Металл', 2193], ['Рок-Н-Ролл', 2188], ['Хардстайл', 1488]]
        self.test3 = [['MetallicA', ['Металл']], ['Mашина времени', ['Рок-Н-Ролл']]]

    def test1_rk(self):
        self.assertEqual(PK1.task1(PK1.OneToMany), self.test1)

    def test2_rk(self):
        self.assertEqual(PK1.task2(PK1.OneToMany), self.test2)

    def test3_rk(self):
        self.assertEqual(PK1.task3(PK1.ManyToMany), self.test3)


if __name__ == '__main__':
    unittest.main()
