class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def reverse_integer(n):
            reversed_n = 0
    
            while n != 0:
                digit = n % 10
                reversed_n = reversed_n * 10 + digit
                n //= 10
    
            return reversed_n
        
        nums = {0: ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'], 1:['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'], 2: ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']}

        suffix = {0:'Hundred', 1:'Thousand', 2: 'Million', 3: 'Billion'}

        # n  1 2 3 4 5
        # i  4 3 2 1 0
        

        # n 1 2 3    4 5 6
        # i 5 4 3    2 1 0
        #   H T D sf H T D
        # One Hundred twenty three thousand four hundred fifty six
        # six fifty hundred four thousnad three twenty hundred one
        
        i = 0
        sf = 1
        word = []
        sNum = str(reverse_integer(num))
        for i in range(len(sNum)):
            digit = int(sNum[i])
            try:
                next_digit = int(sNum[i+1])
            except IndexError:
                next_digit=None
            try:
                prev_digit = int(sNum[i-1])
            except IndexError:
                prev_digit = None

        
            if i in (2, 5, 8, 11): # erronous hundreds/thousands must stem from here as only time hundreds is called
                word.append(suffix[0])
                word.append(nums[0][digit])
            elif i in (0, 3, 6, 9):
                if i != 0:
                    # word.append(suffix[sf] +' '+ nums[0][digit])
                    word.append(suffix[sf])
                    if next_digit!=1:
                        word.append(nums[0][digit])
                    elif digit == 0 and next_digit:
                        word.append(nums[2][next_digit])
                    sf += 1

                elif next_digit != (None or 1):
                    word.append(nums[0][digit])
            elif i in (1, 4, 7, 10): # causing issue with test two
                if (digit == 1 and prev_digit != 0):
                    word.append(nums[1][prev_digit]) 
                else: 
                    word.append(nums[2][digit])

        return ' '.join(reversed(word))


            
wordnum = Solution()
test = wordnum.numberToWords(1234567891)
print('\nTest: ' + test)
print('Expt: One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One\n')

test = wordnum.numberToWords(10)
print('\nTest: ' + test)
print('Expt: Ten\n')







        
    

        # num_names = {0: ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'], 1:['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninty'], 2:'Hundred', 3:'Thousand', 4:'Thousand', 5:'Thousand', 6:'Million', 7:'Billion'}
        # num_names = {0: ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'], 1:['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'], 2:['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninty'], 3:' Hundred', 4:' Thousand', 7:' Million', 10:' Billion'}


#         count = 0
#         word = []
#         reversed_num = str(reverse_integer(num))
#         l = len(reversed_num)

#         # structure 
#         # digit, 10s (creating teens), 100s (adding suffix), thousand (adding suffix and maintaining previous)
#         i = len(str(num)) - 1
#         while i > 0:
#             digit, next_digit = int(num[i]), int(num[i+1])
#             l = len(str(num))











#         def binomial_expansion(n):
#             result = 1
#             if n == 0:
#                 return 1
#             else:
#                 for i in range(1, n+1):
#                     result *= i
#                 return result - 1

#         def get_teens(count, nums, digit, next_digit=None):
#             if next_digit:
#                 if next_digit != 1:
#                     return nums[1][0][digit]
#                 else:
#                     if digit == 0:
#                         return nums[1][1][next_digit]
#                     else:
#                         return nums[0][digit] + nums[count]
        

#         def check_values(digit, next_digit = None, prev_digit = None, count):
#             nums = {0: ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'], 1:[['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'], ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninty']], 2:' Hundred', 3:' Thousand', 4:' Million', 5:' Billion'}
#             value = None
#             if count == 0:
#                 value = get_teens(digit, next_digit, count, nums)
#             elif count == 1:
#                 if digit == 1 or prev_digit == 0:
#                     pass
#                 else:
#                     value = nums[1][1][digit]
#             elif count == 2:
#                 value = nums[0][digit]
#             elif count ==3: # ten thousand
#                 value = get_teens(digit, next_digit, count, nums)
#             elif count == 4: # hundred thousand
#                 value = nums[0][digit]
#             elif count == 5:
#                 value = nums[0][digit]
#             elif count == 7:
#                 value = get_teens(digit, next_digit, count, nums)
#             elif count == 8:
#                 value == 

#             if count > 1:
#                 value += num_names[binomial_expansion(count)]

#             return value


                
                
#             # elif count > 0:
#             #     binom = binomail_expansion(count)

#             # 12 count = 1
#             # 12345 count = 4
#             # 12345678 count = 7

#             # 123000 count = 5

#         for digit in reversed_num:
#             digit = int(digit)
#             if count < len(reversed_num)-1:
#                 next_digit = int(reversed_num[count+1])
#             else:
#                 next_digit = None
#             if count > 0 and count <= len(reversed_num):
#                 prev_digit = int(reversed_num[count-1])
#             else:
#                 prev_digit = None
#             count += 1
#             if count in (1, 4, 7):
#                 if count == 1:
#                     word.append(num_names[count][digit])
#                 else:
#                     if next_digit != 1:
#                         word.append(num_names[2][digit-2] + ' ' + num_names[count])
#                     else:
#                         word.append(num_names[1][digit] + ' ' + num_names[count])


#             elif count ==2:
#                 if digit != 1:
#                     word.append(num_names[count][digit-2])
#                 else: 
#                     new_digit = digit * 10 + prev_digit
#                     word.append(num_names[1][digit])

#             elif count % 3 == 0:
#                 word.append(num_names[1][digit] + ' ' + num_names[count])
#             else:
#                 if digit != 1:
#                     word.append(num_names[2][digit-2])
#                 else:
#                     new_digit = digit * 10 + prev_digit
#                     word.append(num_names[1][new_digit] + ' ' + num_names[count])

                
                

#         return ' '.join(reversed(word))


#         # dealt with 1, 2, 3, 4, 6, 7
#         # 12345678

#         # 4 and 6 are an issue


# # if divisble 
# # 2 = tens
# # 3 = hundreds 

# # million, hundred thousand, tens of thounands, thousands, hundreds, tens, digit

# numWord = numberToWords()