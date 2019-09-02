from unittest import TestCase
from line_overlapper import are_line_segments_overlapping, InvalidCoordinateFormatError


class LineOverLapTest(TestCase):

    def test_line_segments_overlap_positive_axis(self):
        line_1 = [2, 6]
        line_2 = [5, 8]
        self.assertTrue(are_line_segments_overlapping(line_1, line_2))

    def test_line_segments_overlap_positive_axis_negative(self):
        line_1 = [2, 6]
        line_2 = [-10, 8]
        self.assertTrue(are_line_segments_overlapping(line_1, line_2))

    def test_line_segments_does_not_overlap_positive_axis(self):
        line_1 = [2, 6]
        line_2 = [7, 11]
        self.assertFalse(are_line_segments_overlapping(line_1, line_2))

    def test_line_segments_does_not_overlap_negative_axis(self):
        line_1 = [2, 6]
        line_2 = [-17, -11]
        self.assertFalse(are_line_segments_overlapping(line_1, line_2))

    def test_line_segments_does_not_overlap_all_negative_axis(self):
        line_1 = [-2, -6]
        line_2 = [-17, -11]
        self.assertFalse(are_line_segments_overlapping(line_1, line_2))

    def test_line_segments_raises_error(self):
        line_1 = [-2, 'a']
        line_2 = [-17, -11]

        with self.assertRaises(InvalidCoordinateFormatError):
            are_line_segments_overlapping(line_1, line_2)
