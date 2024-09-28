class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity  # Sức chứa của ngăn xếp
        self.stack = [0.0] * capacity  # Mảng float cấp phát động
        self.top = -1  # Chỉ số của phần tử trên cùng

    def push(self, item):
        if self.isFull():
            print("Ngăn xếp đã đầy.")
        else:
            self.top += 1
            self.stack[self.top] = item  # Đưa phần tử vào ngăn xếp

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống.")
            return None
        item = self.stack[self.top]
        self.top -= 1  # Lấy phần tử ra từ đỉnh ngăn xếp
        return item

    def isEmpty(self):
        return self.top == -1  # Kiểm tra ngăn xếp có trống không

    def isFull(self):
        return self.top >= self.capacity - 1  # Kiểm tra ngăn xếp có đầy không



# ------------------------------------------------------------------------------------
stack = Stack(5)  # Tạo ngăn xếp với sức chứa 5
stack.push(1.0)
stack.push(2.5)
stack.push(3.3)

print("Phần tử lấy ra:", stack.pop())  # Lấy phần tử từ ngăn xếp
print("Phần tử lấy ra:", stack.pop())

