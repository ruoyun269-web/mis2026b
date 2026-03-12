def life(y):
    # 將輸入的字串轉換為數字列表，並計算總和
    # 例如 "19950101" -> 1+9+9+5+0+1+0+1
    result = sum(int(digit) for digit in y if digit.isdigit())
    
    print(f"您的西元生日 8 位數相加結果為：{result}")
    return result

# 1. 獲取使用者輸入
x = input("請輸入西元生日 (8位數，如 19950101): ")

# 2. 顯示第一個字（通常是年份的第一個數字）
if len(x) > 0:
    print(f"生日的第一個數字是：{x[0]}")

# 3. 呼叫函數並執行計算
life(x)