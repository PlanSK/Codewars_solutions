import pytest

from PaginationHelper import PaginationHelper

helper = PaginationHelper(range(1,25), 10)

def test_page_index():
    assert helper.page_index(23) == 2
    assert helper.page_index(1) == 0
    assert helper.page_index(40) == -1
    assert helper.page_index(0) == 0

def test_page_item_count():
    assert helper.page_item_count(0) == 10
    assert helper.page_item_count(2) == 4

def test_page_count():
    assert helper.page_count() == 3

def test_item_count():
    assert helper.item_count() == 24