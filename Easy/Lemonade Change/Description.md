**Challenge 860: Lemonade Change**

**Problem:**
At a lemonade stand, each lemonade costs $5. Customers pay with $5, $10, or $20 bills. You need to provide the correct change for each customer to ensure they effectively pay $5 per lemonade.

Initially, you have no money. As customers pay, you collect bills and provide change if needed. Determine if you can provide the correct change to all customers based on the sequence of payments.

**Examples:**

1. **Input:** `bills = [5,5,5,10,20]`  
   **Output:** `true`  
   **Explanation:** 
   - From the first three customers, you collect three $5 bills.
   - For the fourth customer, you use one $5 bill to give change for their $10 bill.
   - For the fifth customer, you use one $10 bill and one $5 bill to give change for their $20 bill.
   - All customers receive correct change.

2. **Input:** `bills = [5,5,10,10,20]`  
   **Output:** `false`  
   **Explanation:** 
   - From the first two customers, you collect two $5 bills.
   - For the next two customers, you use two $5 bills to provide change for their $10 bills.
   - For the last customer, you need $15 in change. However, you only have two $10 bills, so you cannot provide the correct change.

**Constraints:**

- 1 <= `bills.length` <= 10^5
- `bills[i]` is either 5, 10, or 20.
