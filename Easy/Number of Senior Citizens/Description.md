**Challenge 2678: Number of Senior Citizens**

**Problem:**
You are given a 0-indexed array of strings `details`. Each string in the array provides information about a passenger encoded as follows:
- The first ten characters represent the phone number.
- The 11th character represents the gender (M for male, F for female, O for others).
- The next two characters represent the age of the passenger.
- The last two characters indicate the seat number.

Your task is to return the number of passengers who are strictly older than 60 years.

**Examples:**

1. **Input:** `details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]`  
   **Output:** `2`  
   **Explanation:** 
   - Passenger at index 0 is 75 years old.
   - Passenger at index 1 is 92 years old.
   - Passenger at index 2 is 40 years old.
   - Therefore, there are 2 passengers older than 60 years.

2. **Input:** `details = ["1313579440F2036", "2921522980M5644"]`  
   **Output:** `0`  
   **Explanation:** Both passengers are younger than 60 years.

**Constraints:**

- 1 <= `details.length` <= 100
- Each string in `details` has a length of 15.
- The strings contain digits and the gender characters ('M', 'F', 'O') as described.
- Phone numbers and seat numbers are distinct.
