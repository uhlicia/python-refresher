import unittest
import hello


class TestHello(unittest.TestCase):
        
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "i miss my dog")

    def test_add(self):
        self.assertEqual(hello.add(1, 4), 5)
        self.assertNotEqual(hello.add(1, 4), 6)
        self.assertEqual(hello.add(1, -4), -3)
    
    def test_sub(self):
        self.assertEqual(hello.sub(1, 4), -3)
        self.assertNotEqual(hello.sub(1, 4), 5)
        self.assertEqual(hello.sub(1,-4), 5)

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertNotEqual(hello.sin(0), 1)
        self.assertEqual(hello.sin(1), 0.8414709848078965)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertNotEqual(hello.cos(0), 0)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertNotEqual(hello.tan(0), 1)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertNotEqual(hello.cot(0), 0)
        self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
