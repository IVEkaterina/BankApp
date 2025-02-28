from src.processing import filter_by_state, sort_by_date

def test_filter_by_state_1(test_filter_1):
    for filter_1 in test_filter_1:
        ind1_1, ind1_2, ind1_3 = filter_1
        assert filter_by_state(ind1_1, ind1_2) == ind1_3


def test_filter_by_state_2(test_filter_2):
    for filter_2 in test_filter_2:
        ind2_1, ind2_2, ind2_3 = filter_2
        assert filter_by_state(ind2_1, ind2_2) == ind2_3

def test_filter_by_state_3(test_filter_3):
    for filter_3 in test_filter_3:
        ind3_1, ind3_2 = filter_3
        assert filter_by_state(ind3_1) == ind3_2


def test_sort_by_date_1(test_sorted_1):
    for sorted_1 in test_sorted_1:
        sor1_1, sor1_2 = sorted_1
        assert sort_by_date(sor1_1) == sor1_2

def test_sort_by_date_2(test_sorted_2):
    for sorted_2 in test_sorted_2:
        sor2_1, sor2_2, sor2_3 = sorted_2
        assert sort_by_date(sor2_1, sor2_2) == sor2_3

def test_sort_by_date_3(test_sorted_3):
    for sorted_3 in test_sorted_3:
        sor3_1, sor3_2 = sorted_3
        assert sort_by_date(sor3_1) == sor3_2