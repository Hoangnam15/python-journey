"""Reference mở rộng Tuần 02: input() và độ rộng khung động."""

name = input("Tên của bạn: ").strip()
message = f"Xin chào {name}!"
width = len(message) + 4

print("+" + "-" * width + "+")
print("| " + message + " |")
print("+" + "-" * width + "+")
