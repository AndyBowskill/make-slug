import unittest
import makeslug


class TestMakeSlug(unittest.TestCase):
    def test_check_for_errors_regular_sentence(self):
        """
        Test check_for_errors function works successfully when a regular sentence provided.
        """

        error, error_text = makeslug.check_for_errors("Test SLUG vaLUEs 1")

        self.assertFalse(error, "Error should be False.")
        self.assertIsNone(error_text, "Error text should be None.")

    def test_check_for_errors_empty_sentence(self):
        """
        Test check_for_errors function raising an error when no sentence provided.
        """

        error, error_text = makeslug.check_for_errors("")

        self.assertTrue(error, "Error should be True.")
        self.assertIsNotNone(error_text, "Error text should be populated.")

    def test_generate_regular_sentence(self):
        """
        Test generate function works successfully when a regular sentence provided.
        """

        slug = makeslug.generate("Test SLUG vaLUEs 1")

        self.assertEqual(
            slug, "test-slug-values-1", "Slug should be populated correctly."
        )


if __name__ == "__main__":
    unittest.main()
