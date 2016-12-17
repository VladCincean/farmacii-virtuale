'''
Created on 5 dec. 2015

@author: Vlad Cincean
'''
from domain.operations import add, sub, mul, div
from domain.rapid_conversions import to_base_2, from_base_2, rapid_convert
from domain.conversions import substitution_method, successive_divisions_method

def test_all():
    
    def test_add():
        assert add("1010", "110", 2) == "10000"
        assert add('222', '7', 10) == '229'
        assert add('7', '222', 10) == '229'
        assert add('23', '14', 5) == '42'
        assert add('2AF6', '12C', 16) == '2C22'
        assert add('45', '0', 7) == '45'
        assert add('0', '45', 7) == '45'
    test_add()
    
    def test_sub():
        assert sub('10101011', '11001', 2) == '10010010'
        assert sub('84', '9', 10) == '75'
        assert sub('2AFFD', 'C8', 16) == '2AF35'
        assert sub('3C8', '0', 16) == '3C8'
        assert sub('24', '24' , 7) == '0'
    test_sub()
    
    def test_mul():
        assert mul('19', 'B', 16) == '113'
        assert mul('ABC', 'D', 16) == '8B8C'
        assert mul('256', '3', 10) == '768'
        assert mul('10111', '1', 2) == '10111'
        assert mul('10111', '0', 2) == '0'
    test_mul()
    
    def test_div():
        assert div('9420', '7', 10) == ('1345', '5')
        assert div('2AB4F', 'B', 16) == ('3E1E', '5')
        assert div('10110', '1', 2) == ('10110', '0')
        try:
            div('858', '0', 9)
            assert False
        except ValueError:
            assert True
    test_div()
    
    def test_to_base_2():
        assert to_base_2('FA27', 16) == '1111101000100111'
        assert to_base_2('24701', 8) == '10100111000001'
        assert to_base_2('1230', 4) == '1101100'
        assert to_base_2('0', 8) == '0'
        assert to_base_2('1', 8) == '1'
    test_to_base_2()
    
    def test_from_base_2():
        assert from_base_2('1111101000100111', 16) == 'FA27'
        assert from_base_2('10100111000001', 8) == '24701'
        assert from_base_2('1101100', 4) == '1230'
        assert from_base_2('0', 8) == '0'
        assert from_base_2('1', 8) == '1'
    test_from_base_2()
    
    def test_rapid_convert():
        assert rapid_convert('1101100', 2, 4) == '1230'
        assert rapid_convert('10100111000001', 2, 8) == '24701'
        assert rapid_convert('1111101000100111', 2, 16) == 'FA27'
        assert rapid_convert('1230', 4, 2) == '1101100'
        assert rapid_convert('1230', 4, 8) == '154'
        assert rapid_convert('33220213', 4, 16) == 'FA27'
    test_rapid_convert()
    
    def test_substitution_method():
        assert substitution_method('354', 6, 8) == '216'
        assert substitution_method('11011', 2, 4) == '123'
        assert substitution_method('322244', 5, 10) == '10949'
        assert substitution_method('1111101000100111', 2, 16) == 'FA27'
        try:
            assert substitution_method('162', 8, 4) == '........' #assert False
        except ValueError:
            assert True
    test_substitution_method()
    
    def test_successive_divisions_method():
        assert successive_divisions_method('24', 10, 2) == '11000'
        assert successive_divisions_method('A5B', 16, 8) == '5133'
        assert successive_divisions_method('123', 4, 2) == '11011'
        assert successive_divisions_method('2E23D', 16, 7) == '1414663'
        try:
            assert successive_divisions_method('1552225', 6, 9) == '........' #assert False
        except ValueError:
            assert True
    test_successive_divisions_method()
    
test_all()

print("All tests succeded!")