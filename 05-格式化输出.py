# 定义字符串变量name 输出我的名字叫 小明 请多多关照
name = "大小明"
print("我的名字叫 %s,请多多关照！" % name)
student_no = 1231231321
print("我的学号是 %06d" % student_no)
price = 9.8
weight = 10
money = price * weight
print("苹果的单价是 %.2f 元/斤，购买了 %.3f 斤，需要支付 %.4f 元" % (price, weight, money))
scale = 0.08
print("数据的比例是 %.2f%%" % (scale * 10))
