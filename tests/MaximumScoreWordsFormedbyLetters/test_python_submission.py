import itertools

from src.MaximumScoreWordsFormedbyLetters.python_submission import Solution, score_word


def test_solution():
    solution = Solution()
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5,
             0, 0, 3, 0,
             0, 0, 0, 0,
             0, 0, 2, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0]
    expected_result = 23
    actual_result = solution.maxScoreWords(words=words, letters=letters, score=score)
    assert actual_result == expected_result


def test_solution2():
    solution = Solution()
    words = ["xxxz", "ax", "bx", "cx"]
    letters = ["z", "a", "b", "c", "x", "x", "x"]
    score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
    expected_result = 27
    actual_result = solution.maxScoreWords(words=words, letters=letters, score=score)
    assert actual_result == expected_result


def test_permutation():
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5,
             0, 0, 3, 0,
             0, 0, 0, 0,
             0, 0, 2, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0]

    def score_list_of_words(list_of_words):
        return sum([score_word(word, score) for word in list_of_words])

    def possible_combo(list_of_words):
        remaining_letter = [item for item in letters]
        try:
            all_chars = [char for word in list_of_words for char in word]
            for char in all_chars:
                remaining_letter.remove(char)
            return True
        except ValueError:
            return False

    def display(list_of_words):
        print(f"{list_of_words} -> {score_list_of_words(list_of_words)}")

    all_combinations = [list_of_words for i in range(len(words)) for list_of_words in itertools.combinations(words, i)]
    all_possible_words = [list_of_words for list_of_words in all_combinations if possible_combo(list_of_words)]
    [display(list_of_words) for list_of_words in all_possible_words]
