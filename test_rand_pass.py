import rand_pass
import unittest


class RandPassTestCase(unittest.TestCase):

    def test_rand_pass(self):
        for _ in range(10):
            self.assertRegex(rand_pass.rand_pass(), r"^[a-zA-Z]+([2-9]{4})$")



if __name__ == "__main__":
    unittest.main()