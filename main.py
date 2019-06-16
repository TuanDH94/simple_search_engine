import simple_search_engine.engine as engine
import _pickle as cPickle

if __name__ == '__main__':
    print('Khởi động máy tìm kiếm ...\n')
    search_engine = engine.SearchEngine()

    file = open('search_model.txt', 'rb')
    dataPickle = file.read()
    file.close()
    print('...\n')
    search_engine.__dict__ = cPickle.loads(dataPickle)
    print('Tìm kiếm sản phẩm trên Tiki\n')
    print('------------------------------\n')
    while(True):
        print('Nhập từ khóa:\n')
        input_str = input()
        print(input_str +'\n')
        product_results = search_engine.search(input_str)
        for i, result in enumerate(product_results):
            print('\t' + str(i) + '.\t' + result)
        print('Bạn có muốn tiếp tục ? (YES or NO)')
        input_command = input()
        if input_command == 'NO':
            break