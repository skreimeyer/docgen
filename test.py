import unittest
import toml
import render

with open('project.toml', 'r') as config_file:
    config = toml.load(config_file)

class TestRender(unittest.TestCase):
    def test_content_or_blank(self):
        """We can retrieve nested data"""
        notfound = "<div class='blank-line'></div>"
        simple = render.content_or_blank(config,['description','project'])
        self.assertNotEqual(simple,notfound)
        nested = render.content_or_blank(config,['disturbed_area','erosion_control','project'])
        self.assertNotEqual(simple,notfound)

if __name__ == "__main__":
    unittest.main()
