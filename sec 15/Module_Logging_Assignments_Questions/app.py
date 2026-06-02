import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%M-%D %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} and  {b}: {result}")
    return a + b

def subtract(a,b):
    result = a - b
    logger.debug(f"Subtracting {a} and  {b}: {result}")
    return a - b

def multiply(a,b):
    result = a * b
    logger.debug(f"Multiplying {a} and  {b}: {result}")
    return a * b

def divide(a,b):    
    if b == 0:
        logger.error("Division by zero is not allowed.")
        return "Error: Division by zero is not allowed."
    result = a / b
    logger.debug(f"Dividing {a} and  {b}: {result}")
    return a / b

if __name__ == "__main__":
    logger.info("Starting the arithmetic operations.")
    a = 10
    b = 5
    add(a,b)
    subtract(a,b)
    multiply(a,b)
    divide(a,b)
    divide(a,0)
    logger.info("Finished the arithmetic operations.")
