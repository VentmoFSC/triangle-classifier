# triangle-classifier

An equilateral triangle can never also be a right triangle, as a right triangle must have a 90 degree angle. This would indicate an impossibility for an equilateral triangle, as it requires 3 sides to have equal angles, unless it wants to be a 180 degree line. 

## Review log

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