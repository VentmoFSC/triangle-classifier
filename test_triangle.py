import math
import pytest
from triangle import is_valid_triangle, classify_triangle

#Test to confirm triangle with 3 equal sides is classified as Equilateral
def test_equilateral_triangle(): 
    assert classify_triangle(3, 3, 3) == "Equilateral"

#Test to confirm triangle with 2 equal sides is classified as Isosceles
def test_isosceles_triangle(): 
    assert classify_triangle(3, 3, 4) == "Isosceles"

#Test to confirm triangle with no equal sides is classified as Scalene
def test_scalene_triangle(): 
    assert classify_triangle(4, 5, 6) == "Scalene"

#Test to confirm triangle with sides that do not form a valid triangle is classified as Invalid
def test_invalid_triangle(): 
    assert classify_triangle(1, 2, 3) == "Invalid"

#test that a 3-4-5 triangle is classified as Right Scalene
def test_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"

    #test that zero or negative sides are classified as Invalid
def test_zero_or_negative_sides():
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(-3, 4, 5) == "Invalid"

    #test that a right triangle using non-integer sides is classified as Right Scalene
def test_right_triangle_non_integer_sides():
    assert classify_triangle(1.5, 2.0, 2.5) == "Right Scalene"

    #test that a triangle is invalid when the sum of two sides is equal to the third side
def test_invalid_triangle_sum_of_sides():
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(5, 10, 15) == "Invalid"
    assert classify_triangle(50, 100, 150) == "Invalid"