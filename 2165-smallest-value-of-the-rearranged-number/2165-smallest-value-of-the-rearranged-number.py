class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            numbers = str(num)[1:]
            numbers_list = list(numbers)
            numbers_list.sort(reverse = True)
            sorted_number_str = ''.join(numbers_list)
            result = int(sorted_number_str) * -1
        else:
            number = str(num)
            number_list = list(number)
            number_list.sort()
            if number_list[0] == '0':
                for i in range(1, len(number_list)):
                    if number_list[i] != '0':
                        number_list[0], number_list[i] = number_list[i], number_list[0]
                        break  
            sorted_number_str = ''.join(number_list)
            result = int(sorted_number_str)
        return result    