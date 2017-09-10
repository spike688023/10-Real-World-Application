"""

這題 主要就是，多用這個變數而已，

還多用個跳脫字元，

還有format 這個要多熟悉。
round(...)
    round(number[, ndigits]) -> number

        Round a number to a given precision in decimal digits (default 0 digits).
        This returns an int when called with one argument, otherwise the
        same type as the number. ndigits may be negative.
"""
def bmi_app():
	height = input('How tall are you? ')
	weight = input('How much do you weight ?')
	bmi_value = int(weight)/(int(height)/100)**2
	print(str(bmi_value))
	print('Your bmi is {}'.format(round(bmi_value, 2)))
	if bmi_value < 18.5:
	    print('You\'d better eat more!')
	elif bmi_value >= 18.5 and bmi_value <= 24:
	    print('Good job!')
	else:
	    print('You\'d better do some exercises')

bmi_app()
