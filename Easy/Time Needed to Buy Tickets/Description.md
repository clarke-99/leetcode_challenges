## Challenge 2073. Time Needed to Buy Tickets


**Problem:**

In a queue of `n` people, each person wishes to buy a certain number of tickets. Each person buys one ticket per second and then moves to the end of the line to buy more tickets. The problem is to determine how long it will take for the person at position `k` to finish buying all their tickets.

- **Input:** An array `tickets` of length `n`, where `tickets[i]` represents the number of tickets the `i`-th person wants to buy, and an integer `k` indicating the position of the person of interest.
- **Output:** The total time taken for the person at position `k` to buy all their tickets.

## Examples 

**Example 1:**

- **Input:** `tickets = [2,3,2], k = 2`
- **Output:** `6`
- **Explanation:** The person at position 2 takes 6 seconds to buy all their tickets, given that each person in the queue buys one ticket per second.

**Example 2:**

- **Input:** `tickets = [5,1,1,1], k = 0`
- **Output:** `8`
- **Explanation:** The person at position 0 needs 8 seconds to buy all 5 tickets, as they buy one ticket per second in each pass until all tickets are purchased.

### Constraints

- `n == tickets.length`
- `1 <= n <= 100`
- `1 <= tickets[i] <= 100`
- `0 <= k < n`

