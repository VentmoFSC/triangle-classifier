from triangle import classify_triangle

def test_customer_acceptance():

    #test to confirm a valid triangle, and confirming the triangle type. In this case, it is an equilateral.
    assert classify_triangle(5,5,5) == "Equilateral"

    #test to confirm numbers given from customer is invalid, and a message is returned to the customer
    assert classify_triangle(1,2,3) == "Invalid"

    #ttest to confirm a right triangle per customer input
    assert classify_triangle(3,4,5) == "Right Scalene"