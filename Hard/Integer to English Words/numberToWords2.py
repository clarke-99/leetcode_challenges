class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        num_list = [num for num in str(num)]

        below_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 
        'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
        'Seventy', 'Eighty', 'Ninety']
        suffix = {3:'Thousand', 6:'Million', 9:'Billion'}

        def find_num(n):
            if n < 20:
                return below_20[n] + ' '
            elif n < 100:
                if n %10 == 0:
                    return tens[n//10] + ' '
                else:
                    return tens[n//10] + ' ' + find_num(n%10)
            else:
                if n%100 ==0:
                    return below_20[n // 100] + ' Hundred '
                else:
                    return below_20[n // 100] + ' Hundred ' + find_num(n % 100)

    
        word = ''
        while num_list:
            l = len(num_list)
            if l % 3 != 0:
                chunk = l % 3
            else:
                chunk = 3
            current = int(''.join(num_list[0:chunk]))
            if current > 0:
                word += find_num(current)
                if l - chunk in suffix:
                    word += suffix[l-chunk] + ' '

            num_list=num_list[chunk:]

        return word.strip()



