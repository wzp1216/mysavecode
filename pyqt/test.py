
import matplotlib

from PyQt5.QtWidgets import QWidget,QGraphicsView, QGraphicsScene, QGraphicsPixmapItem,QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt



class testview(QWidget):
    def __init__(self):
        super().__init__()

        # 创建一个GraphicsView和GraphicsScene
        view = QGraphicsView()
        scene = QGraphicsScene()
        
        # 创建一个图像项
        pixmap = QPixmap("./pcb.png")
        item = QGraphicsPixmapItem(pixmap)
        
        # 将图像项添加到场景
        scene.addItem(item)
        
        # 设置场景的尺寸
        scene.setSceneRect(item.boundingRect())
        
        # 在视图中显示场景
        view.setScene(scene)
        
        # 设置视图的显示属性
        view.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        
        # 显示视图
        layout=QVBoxLayout()
        layout.addWidget(view)
        self.setLayout(layout)
        view.show()

