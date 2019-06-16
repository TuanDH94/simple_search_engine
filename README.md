# Simple search engine
### Data
50000 product name trong file 'product_names.txt';

100 câu query trong file '100_query.txt'

### Goal
Cho trước 100 câu query và 50000 tên sản phẩm, máy tìm kiếm được xây dựng bằng cách tính tf-idf score và tính độ tương đồng cosine giữa query và product name. Ngoài ra vector tf-idf cũng đã được giảm chiều về 10 chiều.

Máy tìm kiềm có hỗ trợ tìm kiếm không dấu, có hàm preprocessing để khử dấu tiếng việt và các ký tự đặc biệt.

Đã chạy test search 100 câu query, kết quả được lưu trong file 'result.txt'

### Running the application

Require: sklearn, numpy
$ pip install sklearn
$ pip install numpy

Chạy chương trình:
$ python main.py

### Sample output
'''
Nhập từ khóa:

laptop dell

	0.	laptop dell ins-14z 5423 ymry24-silver
	1.	laptop dell xps 13 (9343) 70055805
	2.	laptop dell xps15 9550 70082495
	3.	laptop dell inspiron n3458-txtgh3 (windows 8.1)
	4.	ram laptop kingston 4gb ddr3l-1600 sodimm 1.35v - kvr16ls11/4
Bạn có muốn tiếp tục ? (YES or NO)

YES

Nhập từ khóa:

giày thể thao bitis

	0.	giày thể thao double star lightweight
	1.	combo balo glado classical bll007be - đen + giày sneaker zapas gs081gr - xám
	2.	giày lười thể thao sp24
	3.	combo balo glado classical bll006re - đỏ + giày sneaker gs081ba - đen
	4.	giày sneaker unisex superga superlight s00al80_999 - đen
Bạn có muốn tiếp tục ? (YES or NO)

NO
'''


