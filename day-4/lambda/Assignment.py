from functools import reduce

class Lambda:
    
    def Q1(self):
        reverse_string = lambda a:a[::-1]
        print('Original Word : ', 'Hello')
        print('Reversed String : ', reverse_string('Hello'),'\n')

    def Q2(self, int_list):
        final_list = map(lambda a: str(a), int_list)
        print('Original List : ', int_list)
        print('Converted List : ', list(final_list), '\n')
        
    def Q3(self, name_list):
        e_list = filter(lambda a: a.endswith('e'), name_list)
        print('Original Names List : ', name_list)
        print('Names that contains \'e\' at last : ', list(e_list))
        
    def Q4(self, int_list):
        greatest=reduce(lambda a, b: a if a>b else b, int_list)
        print('Greatest Number : ', greatest)
        
Lambda1=Lambda()
Lambda1.Q1()
Lambda1.Q2([1, 2, 3, 4, 5, 6, 7, 8])
Lambda1.Q3(['smit', 'divyang', 'tape', 'there', 'time', 'cape'])
Lambda1.Q4([1, 2, 3, 4, 5, 6, 7, 8])