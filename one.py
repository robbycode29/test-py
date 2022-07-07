def main_func():
    print('nada')

def run_directly():
    print('One.py is being run directly!')

def run_indirectly():
    print('One.py imported successfully')

if __name__ == '__main__':
    run_directly()
else:
    run_indirectly()