def custom_strip(s):
    # حذف فاصله‌ها از ابتدای رشته
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1

    # حذف فاصله‌ها از انتهای رشته
    end = len(s) - 1
    while end >= start and s[end] == ' ':
        end -= 1

    # برگرداندن رشته بدون فاصله‌ها
    return s[start:end+1]


test_string = "   Hello, World!   "
result = custom_strip(test_string)
print(f"'{result}'") 
