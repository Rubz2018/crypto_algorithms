def left_circular_shift(number, shift):
    # Ensure the shift value is within the range of the number's bits
    shift = shift % (number.bit_length() if number != 0 else 1)
    
    # Perform the left circular shift using bitwise operations
    result = (number << shift) | (number >> (number.bit_length() - shift))
    
    return result

# Example usage
if __name__ == "__main__":
    # Input values
    number_to_shift = 0b11011010  # Binary representation for demonstration
    shift_amount = 3
    
    # Perform left circular shift
    result = left_circular_shift(number_to_shift, shift_amount)
    
    # Display results
    print(f"Original Number:   {bin(number_to_shift)}")
    print(f"Left Circular Shift: {bin(result)}")
