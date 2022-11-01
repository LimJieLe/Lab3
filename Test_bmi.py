import Lab2.calculate_bmi as bmi

def Test_bmi_normal_weight():
    result = bmi.calculate_bmi(weight=57, height=1.73)
    test_bmi = 0
    assert (result == test_bmi)

def Test_bmi_over_weight():
    result = bmi.calculate_bmi(weight=80, height=1.50)
    test_bmi = 1
    assert (result == test_bmi)

def Test_bmi_under_weight():
    result = bmi.calculate_bmi(weight=45, height=1.87)
    test_bmi = -1
    assert (result == test_bmi)