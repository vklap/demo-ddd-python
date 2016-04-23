import unittest

from app.domain.services import extract_most_descriptive_words

class ServicesTestCase(unittest.TestCase):
    def test_extract_most_descriptive_words(self):
        text = """
        Domain-driven design (DDD) is an approach to software development for complex needs by connecting the implementation to an evolving model.[1] The premise of domain-driven design is the following:
        placing the project's primary focus on the core domain and domain logic;
        basing complex designs on a model of the domain;
        initiating a creative collaboration between technical and domain experts to iteratively refine a conceptual model that addresses particular domain problems.
        """

        result = extract_most_descriptive_words(text)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 'domain')
        self.assertEqual(result[1], 'model')
