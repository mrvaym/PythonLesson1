from divisor_master import simple, devisors, simple_devisor, max, min, prime_factorization, devisor_not_num, \
    greatest_common_divisor

def test_1_devisors():
    assert devisors(383) == [1, 383]

def test_2_prime_factorization():
    assert prime_factorization(15465) == [3, 5, 1031]

def test_3_simple():
    num = [48, 3, 4, 577, 18, 578, 2, 206, 27, 378, 2310, 289]
    for i in num:
        result = simple_devisor(i)
        for j in result:
            assert simple(j) == 1

def test_4_greatest_common_divisor():
    assert greatest_common_divisor([108, 72, 432, 972]) == 36
    assert greatest_common_divisor([108, 72, 432, 973]) != 36

def test_5_devisor_not_num():
    simp_num = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for k in simp_num:
        devisor_not_num(k)
        assert devisor_not_num(k) == [1]
        
