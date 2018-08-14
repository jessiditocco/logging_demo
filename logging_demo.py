import logging

# Now, we will actually see this in the console when we run the file becuase in Debug mode
# We also will create a filename with all info from script
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def adder(x, y):

	return x + y


num_1 = 10
num_2 = 8
add_result = adder(num_1, num_2)
logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))


# More infor than print statment becuase it has our logging level -- warning, debug, info, ect.
# and we can add a message