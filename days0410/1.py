"""


socket 简称：套字节
AF_INET: internet 进程间通信
SOCK_DGRAM: 数据报套字节


常用方法：
socket套字节常用操作
socket.bind: 绑定（主机名称，端口）到一个套字节
socket.listen(): 设置并启动监听
socket.accept(): 等待客户端连接
socket.connect(): 连接到指定服务器
socket.recv(): 接收tcp 消息
socket.send()：发送TCP 消息
socket.recvfrom(): 接收UDP消息
socket.sendto():发送UDP 消息
socket.close(): 关闭套字节对象
"""