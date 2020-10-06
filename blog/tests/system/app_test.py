from unittest import TestCase
from unittest.mock import patch
from blog import appl
from blog.blog import Blog

class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            appl.menu()
            mocked_input.assert_called_with(appl.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                appl.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        appl.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            appl.print_blogs()
            mocked_print.assert_called_with('-Test by Test Author (0 posts)')