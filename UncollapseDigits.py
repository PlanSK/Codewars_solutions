def uncollapse(digits):
    digits_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    temp_str = digits
    digit_words = []
    for _ in range(len(digits)):
        for digit in digits_list:
            if temp_str.startswith(digit):
                digit_words.append(temp_str[:len(digit)])
                temp_str = temp_str[len(digit):]
    return ' '.join(digit_words)

print(uncollapse('fivethreefivesixthreenineonesevenoneeight'))