from operations.tail_call import TailCall, TailCaller
 

@TailCaller
def _factorial(number, accumulator):
    if not number:
        return accumulator
    return TailCall(_factorial, number - 1, number * accumulator)
 

def factorial(number):
    return _factorial(number, 1)


@TailCaller
def _fibonacci(number_of_elements, accumulator):
    """Private fibonacci function"""
    if not number_of_elements:
        return accumulator
    return TailCall(_fibonacci, number_of_elements - 1, accumulator + [accumulator[-2] + accumulator[-1]])


def fibonacci(number_of_elements):
    accumulator = [1, 1]
    accumulator_size = len(accumulator)
    if accumulator_size >= number_of_elements:
        return accumulator[:number_of_elements]
    return _fibonacci(number_of_elements - accumulator_size, accumulator)

