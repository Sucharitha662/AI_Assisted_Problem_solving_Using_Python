import pytest
from task3 import is_sentence_palindrome

class TestIsSentencePalindrome:
    """Test cases for is_sentence_palindrome function"""
    
    def test_classic_palindrome(self):
        assert is_sentence_palindrome("A man, a plan, a canal: Panama") is True
    
    def test_no_x_in_nixon(self):
        assert is_sentence_palindrome("No 'x' in Nixon") is True
    
    def test_car_or_cat(self):
        assert is_sentence_palindrome("Was it a car or a cat I saw?") is True
    
    def test_bees_in_cave(self):
        assert is_sentence_palindrome("Eva, can I see bees in a cave?") is True
    
    def test_able_was_i(self):
        assert is_sentence_palindrome("Able was I, I saw Elba") is True
    
    def test_not_palindrome(self):
        assert is_sentence_palindrome("Hello, World!") is False
    
    def test_not_a_palindrome_text(self):
        assert is_sentence_palindrome("Not a palindrome") is False
    
    def test_numeric_palindrome(self):
        assert is_sentence_palindrome("12321") is True
    
    def test_numeric_not_palindrome(self):
        assert is_sentence_palindrome("12345") is False
    
    def test_empty_string(self):
        assert is_sentence_palindrome("") is True
    
    def test_single_character(self):
        assert is_sentence_palindrome("a") is True
    
    def test_single_character_with_punctuation(self):
        assert is_sentence_palindrome("a!") is True
    
    def test_spaces_only(self):
        assert is_sentence_palindrome("   ") is True
    
    def test_mixed_case_simple(self):
        assert is_sentence_palindrome("AaBbAa") is True
    
    def test_punctuation_heavy(self):
        assert is_sentence_palindrome("A1b2B1a") is True