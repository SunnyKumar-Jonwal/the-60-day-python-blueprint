class Grade:
    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100


print(Grade.is_valid_score(85))
print(Grade.is_valid_score(150))
