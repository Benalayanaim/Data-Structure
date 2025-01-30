#Problem 
#https://www.youtube.com/watch?v=fM4L_dIKA1c&t=2s
#https://leetcode.ca/2016-05-05-157-Read-N-Characters-Given-Read4/


"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

#Solution 1:
def read(buf, n):
    buf4 = [''] * 4  # Temporary buffer for read4
    total_chars_read = 0  # Total characters read so far
    
    while total_chars_read < n:  # Continue reading until we reach 'n' or EOF
        chars_read = read4(buf4)  # Read up to 4 characters into buf4
        
        if chars_read == 0:  # No more characters to read (end of file)
            break
        
        # Copy characters from buf4 to buf
        for i in range(chars_read):
            if total_chars_read == n:  # Stop if we've read 'n' characters
                break
            buf[total_chars_read] = buf4[i]  # Copy one character at a time
            total_chars_read += 1
    
    return total_chars_read  # Return the number of characters actually read



print("===============================================")

#Solution 2:
def read(buf: list[str], n: int) -> int:
    buf4 = [' '] * 4
    i4 = 0  # buf4's index
    n4 = 0  # buf4's size
    i = 0  # buf's index

    while i < n:
      if i4 == n4:  # All the characters in the buf4 are consumed.
        i4 = 0  # Reset the buf4's index.
        n4 = read4(buf4)  # Read <= 4 characters from the file to the buf4.
        if n4 == 0:  # Reach the EOF.
          return i
      buf[i] = buf4[i4]
      i += 1
      i4 += 1

    return i

print("===============================================")

#Solution3:
def read(buf, n):
    buf4 = [''] * 4  # Temporary buffer for read4
    chars_read = 5   # Number of characters read in each read4 call
    i = 0            # Total characters written to buf

    while chars_read >= 4:
        chars_read = read4(buf4)  # Read up to 4 characters into buf4
        for j in range(chars_read):
            buf[i] = buf4[j]
            i += 1
            if i >= n:  # Stop if we've written n characters
                return n
    return i


"Fy chat mteiiii"
#Explanation : https://chatgpt.com/c/6782452e-fc70-800f-b6e1-43a6a7d88885