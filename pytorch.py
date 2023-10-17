# import torch
# x = torch.empty(5,3)
# x = torch.randn(5,3)
# x= torch.zeros(5,3,dtype=torch.long)
# print(x)
#

# 直接从数据创建tensor
# x = torch.tensor([[5.5, 3],[6.6, 4]],dtype=torch.float)
# print(x)
# import torch
#
# # 创建一个tensor并设置requires_grad=True来追踪其计算历史
# x = torch.ones(2, 2, requires_grad=True)
#
# # 对这个tensor做一次运算：
# y = x + 2
#
# # y是计算的结果，所以它有grad_fn属性
# print(y,'grad_fn')
#
# # 对y进行更多的操作
# z = y * y * 3
# out = z.mean()
#
# print(z, out)
#
# # 使用.backward()来进行反向传播，计算梯度
# out.backward()
#
# # 输出梯度d(out)/dx
# print("x的梯度",x.grad)
# x= torch.rand(3,requires_grad=True)
# print(x)
# y = x*2
# print(y)
# while y.data.norm() < 100:
#     y=y*2
# print(y)
# v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
# y.backward(v)
#
# print(x.grad)

# print(torch.cuda.is_available())
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        # 输入图像channel：1，输出channel：6，5x5卷积核
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)

        # 全连接层
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 使用2x2窗口进行最大池化
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # 如果窗口是方的，只需要指定一个维度
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)

        x = x.view(-1, self.num_flat_features(x))

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # 获取除了batch维度之外的其他维度
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
print(torch.cuda.is_available())
net = Net()
print(net)