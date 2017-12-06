
#!/usr/bin/env python
################################################################################
#
#   Filename:           test_zigzag_conversion.py
#
#   Author:             Arnaud Ongenae
#
################################################################################
from ..zigzag_conversion import Solution
from .leetcode_test import LeetcodeTest


class _Mixin(object):

    def validate(self, string, num_rows, expected):
        self.assertEqual(
            Solution().convert(string, num_rows),
            expected,
            '\n -> considering the input "{}", nb rows "{}"'.format(
                string,
                num_rows
            )
        )


class TestAddStrings(LeetcodeTest, _Mixin):

    def test_example(self):
        self.validate('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')
