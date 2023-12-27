import sys
from PyQt5.QtWidgets import QApplication, QWidget
from test import testview

# 创建一个应用程序实例
app = QApplication(sys.argv)

# 创建一个QWidget对象
widget = testview()

# 设置窗口的大小和标题
widget.setGeometry(100, 100, 300, 200)
widget.setWindowTitle('My Widget')

# 显示窗口
widget.show()

# 运行应用程序的事件循环
sys.exit(app.exec())
