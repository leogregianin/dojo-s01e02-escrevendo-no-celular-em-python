
import unittest
import celular

class TestCase(unittest.TestCase):

    def test_padrao(self):
    	test1 = celular.Escrever('77773367_7773302_222337777_777766606660366656667889999_9999555337777')
    	self.assertEqual(test1.escrever_no_celular(), 'SEMPRE ACESSO O DOJOPUZZLES')

    def test_cookies(self):
    	test2 = celular.Escrever('222666_666554443377770446665330222666_666554443377770262664420222666_666554443377770727772077773367_77733')
    	self.assertEqual(test2.escrever_no_celular(), 'COOKIES HOJE COOKIES AMANHA COOKIES PARA SEMPRE')

if __name__ == '__main__':
    unittest.main()

