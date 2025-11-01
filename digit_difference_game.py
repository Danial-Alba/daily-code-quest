def game(number):
	
    a = number // 10
    b = number % 10

    if a >= b:
        return (a - b)
    
    else:
        return (b - a)