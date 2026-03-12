def calculate_life_sum(birthday_str):
    """計算生日 8 位數相加的函式"""
    total_sum = 0
    # 使用迴圈遍歷字串中的每個數字
    for digit in birthday_str:
        total_sum += int(digit)
    return total_sum

# 主程式
x = input("請輸入西元生日 (8位數，如 19950101): ")

if len(x) == 8 and x.isdigit():
    result = calculate_life_sum(x)
    print(f"您的西元生日 8 位數相加結果為：{result}")
else:
    print("輸入格式錯誤，請輸入 8 位數字。")