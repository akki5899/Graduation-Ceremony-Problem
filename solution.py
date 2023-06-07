class Solution:
    def __init__(self, total_numbers_of_days, consecutive_days):
        # total_numbers_of_days: number of academic days
        # consecutive_days: cannot miss consecutive_days or more classes consecutively
        if (total_numbers_of_days < consecutive_days) or (total_numbers_of_days < 0) or (consecutive_days < 0):
            raise ValueError("Inputs are invalid")

        self.total_numbers_of_days = total_numbers_of_days
        self.consecutive_days = consecutive_days

    def graduation_probability(self):
        probability_matrix = [[0] * (self.consecutive_days + 1) for _ in range(self.total_numbers_of_days + 1)]
        for i in range(self.consecutive_days):
            probability_matrix[0][i] = 1

        for i in range(1, self.total_numbers_of_days + 1):
            for j in range(self.consecutive_days - 1, -1, -1):
                probability_matrix[i][j] = probability_matrix[i - 1][0] + probability_matrix[i - 1][j + 1]

        valid_way_to_attend_class = probability_matrix[self.total_numbers_of_days][0]
        number_of_way_to_miss_class = probability_matrix[self.total_numbers_of_days - 1][1]

        return f"{number_of_way_to_miss_class}/{valid_way_to_attend_class}"

    def output(self):
        print('total_numbers_of_days:', self.total_numbers_of_days, ', consecutive_days:', self.consecutive_days, '\n')
        print(self.graduation_probability())


total_numbers_of_days = input("Please enter number of ways to attend the class : ")
consecutive_days = 4  # You are not allowed to miss classes for four or more consecutive days.

obj = Solution(int(total_numbers_of_days), consecutive_days)
obj.output()
