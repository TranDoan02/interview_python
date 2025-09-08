import copy

class Sheep:
    def __init__(self, name):
        self.name = name

original = Sheep("Jolly")
cloned = copy.deepcopy(original)
cloned.name = "Dolly"

print(original.name) # Jolly
print(cloned.name)   # Dolly
#Tạo ra bản sao của đối tượng mới từ một đối tượng đã tồn tại, thường dùng cho các đối tượng có 
# thuộc tính phức tạp hoặc cần thiết phải khởi tạo lại từ đầu mỗi lần
#Cho phép tạo bản sao (clone) của một đối tượng hiện có mà không cần biết chi tiết về chúng, 
# hữu ích khi quá trình khởi tạo phức tạp hoặc tốn nhiều tài nguyên

# Prototype
# Việc clone đối tượng có thể gây rắc rối nếu đối tượng phức tạp, chứa tham chiếu đến các tài nguyên hệ thống hoặc các đối tượng sâu (deep copy cần được xử lý cẩn thận).
# Không phải đối tượng nào cũng có thể clone dễ dàng, đặc biệt là khi đối tượng có trạng thái nội bộ hoặc liên kết với các hệ thống bên ngoài.
# Có thể tăng chi phí bộ nhớ nếu nhu cầu clone nhiều đối tượng lớn hoặc phức tạp.
# Đòi hỏi cơ chế sao chép (copy) được triển khai đúng đắn để tránh lỗi hoặc không mong muốn.