import sys
import FreeCADGui as Gui
# import seaborn as sns
from PointCloud import PointCloud

print("PointCloud Workbench:")
print("succesfully import")

# 获取当前活动的 Points 对象
pointsObject = PointCloud.getActivePointsObject()
if pointsObject is None:
    print("pointsObject is None")
elif isinstance(pointsObject, list):
    print("pointsObject is a list")


# 打印点的数量
points_num = PointCloud.countPoints(pointsObject)
print(points_num)

# 获取点列表
pointsList = PointCloud.getPointsList(pointsObject)
# 打印每个点的坐标
# PointCloud.printPointsXYZ(pointsList)

# 将点云转换为密度图
PointCloud.getDensityPlot(pointsList)
