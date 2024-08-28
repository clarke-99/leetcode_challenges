class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = {0:['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'], 
        1:[['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'], ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']], 2:'Hundred', 3:'Thousand', 6:'Million', 9:'Billion'}

        def check_dig(i):
            while i > 2:
                i -= 3
            return i

        def add_suffix(x, values):
            if any(values) > 0:
                if x == 3:
                    return 'Thousand'
                elif x == 6:
                    return 'Million'
                elif x == 9:
                    return 'Billion'


        num_list = [int(num) for num in str(num)]
        i,l = 0, len(num_list)-1

        if len(num_list) == 1 and num_list[0]==0:
            return 'Zero'


        # 1 2 3 4 0 
    # i   0 1 2 3 4 
    # x   4 3 2 1 0 

        word = []

        while i <= l:
            x = l - i
            s = check_dig(x)
            if num_list[i] == 0:
                if x in (3, 6, 9):
                    j = x
                    sub = 3
                    while j - sub < 0:
                        sub -= 1                        
                    suffix = add_suffix(x, num_list[i-sub:i])
                    if suffix:
                        word.append(suffix)
            else:
                if s in (2, 0):
                    word.append(nums[0][num_list[i]])
                    if s==2 and num_list[i]!=0:
                        word.append(nums[s])
                else:
                    if num_list[i] > 1:
                        word.append(nums[1][1][num_list[i]])
                # elif num_list[i] ==0:
                #     pass
                    else:
                        if num_list[i+1] != 0:
                            word.append(nums[1][0][num_list[i+1]])
                        else:
                            word.append(nums[1][1][num_list[i]])
                        i +=1
                        x-=1
                
                if x in (3, 6, 9):
                    j = x
                    sub = 3
                    while j - sub < 0:
                        sub -= 1   
                    suffix = add_suffix(x, num_list[i-sub:i])
                    if suffix:
                        word.append(suffix)
                
            i += 1

        # word = ' '.join(word)
        return ' '.join(word)
        # return word
        
        
