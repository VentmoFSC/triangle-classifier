# Triangle

An equilateral triangle can never also be a right triangle, as a right triangle must have a 90 degree angle. This would indicate an impossibility for an equilateral triangle, as it requires 3 sides to have equal angles, unless it wants to be a 180 degree line. 

##Running Tests

In order to run the test, please install the following: 

py -m pip install -r requirements.txt

Upon installing the above, run the below: 

py -m pytest -v

##Review log

| Test | Copilot-suggested? | Kept/edited/rejected | Why |
|---|---|---|---|
| test_equilateral_triangle | No | Edited | self-added verification to confirm triangle equilateral |
| test_isosceles_triangle | No | Edited | self-added verification to confirm triangle isosceles |
| test_scalene_triangle | Yes | Edited | Changed the input from (3,4,5) to (4,5,6) as the former is a right triangle |
| test_invalid_triangle | Yes | Edited | Prior test returned invalid because triangle was a valid triangle, changed to (1,2,3) |
| test_right_scalene_triangle | No | Kept | Generated code was correct, changed numbers to confirm (3,5,2) to confirm failure, returned to (3,4,5) thereafter  |
| test_zero_or_negative_sides | Yes | Edited | Did not originallya account for 0, included 0 in code |
| test_right_triangle_non_integer_sides | Yes | Kept | Generated code was correct, verified by changing numbers to int variables confirmed failed test |
| test_invalid_triangle_sum_of_sides | Yes | Edited | added an additional test to account for multiple digit test cases |

##Customer Acceptance Test
Valid Triangle
1) Valid triangles - The system correctly identifies valid triangles as either Equilateral, Isosceles, or Scalene.
2) Invalid Triangles - The system returns an "Invalid" message to those who input measurements that cannot create a triangle, without crashing the entire system.
3) Right Triangles - The system can identify right triangles by including "Right" in their classifications. 

##Equivalent Classes and Boundaries

Equivalence classes
1) Equilateral: All 3 sides are equal, ex: (9,9,9)
2) Isosceles: 2 sides are equal, one side is different, ex: (5,5,8)
3) Scalene: All sides have a different number, ex: (2,6,9)
4) Right Triangle: The sides form a 90 degree angle, ex: (3,4,5)
5) Invalid Triangle: The lengths cannot create a triangle, ex: (1,2,3)

Boundaries
1) zero / Negative Sides: Lengths must be greater than 0.
2) The sum of 2 lengths must be bigger than the 3rd side. 
3) (2,3,5) is invalid because 2 + 3 = 5, whereas (2,3,4) is valid. 

##AI Use Disclosure

Github Copilot was used to generate unit tests for the triangle classifier. Copilot provided suggestions for several test cases, which were then reviewed and edited to confirm proper testing of the program's functionality. Some suggestions were modified for varrying reasons. For example, Copilot suggested using (3,4,5) to test a scalene triangle, but those measurements form a right triangle. I also edited and corrected an invalid triangle test as it was providing a correct triangle. 

I reviewed suggestions pertaining to the test for zero-length sides, and expanded the invalid triangle tests to account for additional measurements. I then verified the tests by reviewing their expected outputs, editing input values to confirm failures, and ran pytests to confirm results. I maintained a review log, and used copilot to organized said review log into readable collumns and rows for easier reading. 

As requested by the professor, I chose not to use Github Copilot for part 3, which included intepreting the stained glass studio's requirments, opting to define the acceptance criteria and creating the customer acceptance test. 