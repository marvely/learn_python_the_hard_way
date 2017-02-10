from nose.tools import *
from exer48.parser import *

'''
x = parse_sentence([('verb', 'run'), ('direction', 'north')])
print x.subject, x.verb, x.object

# the result should be player run north
'''

def test_Sentence():
    testing_s = Sentence(('noun', 'player'),
                           ('verb', 'hit'),
                           ('noun', 'bear'))
    assert_equal(testing_s.subject, 'player')
    assert_equal(testing_s.verb, 'hit')
    assert_equal(testing_s.object, 'bear')

def test_peek():
    assert_equal(peek([('verb', 'run')]), 'verb')
    result = peek([('verb', 'run'), ('direction', 'north')])
    assert_equal(result, 'verb')

def test_match():
    assert_equal(match([('verb', 'run')], 'verb'), ('verb', 'run'))
    result = match([('verb', 'run'), ('direction', 'north')], 'verb')
    assert_equal(result, ('verb', 'run'))

def test_skip():
    assert_equal(skip([('noun', 'bear'), ('aaa', 'bbb')], 'noun'), None)
# since the function skip() does not have a return, it will always return None... so should test return None....

def test_parse_verb():
    assert_equal( parse_verb([('verb', 'run')]), ('verb', 'run') )
    result = parse_verb([('stop', 'the'), ('verb', 'run'), ('direction', 'north')])
    assert_equal(result, ('verb', 'run'))

def test_parse_object():

    assert_raises(ParserError, parse_object, [('verb', 'run')])

    result = parse_object([('direction', 'north')])
    assert_equal(result, ('direction', 'north'))

def test_parse_subject():

    assert_raises(ParserError, parse_subject, [('direction', 'east')])
    result = parse_subject([('verb', 'hit'), ('noun', 'bear')])
    assert_equal(result, ('noun', 'player'))

def test_parse_sentence():

    result = parse_sentence([('verb', 'hit'), ('noun', 'bear')])

    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'hit')
    assert_equal(result.object, 'bear')
