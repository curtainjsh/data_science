def min_num_bits(n):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count
def count_bits_flipped(message_p, message_q):

#return the count of message_p XOR message_q

    return min_num_bits(message_p^message_q)

# Driver code

message_p = int(input("Enter the message P: "))

message_q = int(input("Enter the message Q: "))

print("The minimum bits which has to be flipped is:",count_bits_flipped(message_p, message_q))
