import tkinter as tk
import FreeCAD as App
# import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


class PointCloud:

    def getPointsObject(docName, objName):
        pointsObject = App.getDocument(docName).getObject(objName)
        return pointsObject

    def countPoints(pointsObj):
        pointsNum = pointsObj.Points.CountPoints
        return pointsNum

    def getPointsList(pointsObj):
        pointsList = pointsObj.Points.Points
        return pointsList

    def printPointsXYZ(pointsList):
        for point in pointsList:
            print(point)
            x = point.x
            y = point.y
            z = point.z
            print(f"x={x}, y={y}, z={z}")

    def getDensityPlot(pointsList):
        # 提取点的坐标
        x_coords = [point.x for point in pointsList]
        y_coords = [point.y for point in pointsList]
        print(type(x_coords))
        print(type(y_coords))
        x_coords = np.array(x_coords)
        y_coords = np.array(y_coords)
        print(type(x_coords))
        print(type(y_coords))

        plt.figure(figsize=(8, 6), dpi=200)

        # 限制点的密度范围
        minPointNum = 10
        maxPointNum = 20
        norm = plt.Normalize(vmin=minPointNum, vmax=maxPointNum)
        # 生成二维密度图
        myBins = 800
        myCamp = 'inferno'
        plt.hist2d(x_coords, y_coords, bins=myBins, norm=norm, cmap=myCamp)
        colorBar = plt.colorbar()
        colorBar.set_label('Counts in bin')

        # 添加标题和标签
        plt.title('2D Density Plot')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        fontSize = 3
        plt.rcParams.update({'font.size': fontSize})

        # 显示图形
        plt.show()

        # 利用kdeplot函数快速绘制
        # sns.kdeplot(x=x_coords, y=y_coords)
        # plt.show()


print("YYDIY Workbench:")
print("succesfully import")

# 获取 Points 对象
# Surface_Test：当前活动文档的名字
# Points：点云对象的名字
activeDocName = "Surface_Test"
objectName = "SecondFloor"
pointsObject = PointCloud.getPointsObject(activeDocName, objectName)

# 打印点的数量
points_num = PointCloud.countPoints(pointsObject)
print(points_num)

# 获取点列表
pointsList = PointCloud.getPointsList(pointsObject)
# 打印每个点的坐标
# PointCloud.printPointsXYZ(pointsList)

# 将点云转换为密度图
PointCloud.getDensityPlot(pointsList)
