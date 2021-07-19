import pytest

from StringsMix import mix

def test_camel_case():
    assert mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"
    assert mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp") == '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'

def test_all_lowers():
    assert mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"

def test_non_equally():
    assert mix(" In many languages", " there's a pair of functions") == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"

def test_one_only():
    assert mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"

def test_empty():
    assert mix("codewars", "codewars") == ""

def test_one_equally():
    assert mix("A generation must confront the looming ", "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"