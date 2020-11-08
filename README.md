# MU Puzzle Unprover
Real small. Just experimentally proves MUs puzzle is impossible. Inspired from this website: http://www.puzzle.mu/ and mainly a TOK exercise.

You start with an axiomatic string 'mi' and you wanna turn it into 'mu'.

Rules: You can add an 'u' after any string with 'i': mi -> miu. Any string after 'm' can be doubled: miu -> miuiu and so forth. 
You can add an 'u' after any string with 'i': mi -> miu. A string with three 'i's can turn into an 'u': miiiu = muu. A string with two 'u's is deleted: muuu -> mu

It's impossible because the only way to solve it is by doubling the string until it cancels down to just one 'u'. Since the 'i's are produced exponentially and 
three 'i's are needed to turn into an 'u', this condition cannot be satisfied because the number of 'i's will never be divisible by 3.

Here's the wikipedia if you wanna know more: https://en.wikipedia.org/wiki/MU_puzzle
