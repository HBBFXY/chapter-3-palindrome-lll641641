# 这里编写你的代码
num_str = input()

if len(num_str) != 5:
    print("错误")
elif not (num_str[0] in '0123456789' and num_str[1] in '0123456789' and 
          num_str[2] in '0123456789' and num_str[3] in '0123456789' and 
          num_str[4] in '0123456789'):
    print("错误")
elif num_str[0] == num_str[4] and num_str[1] == num_str[3]:
    print("是回文数")
else:
    print("不是回文数")
