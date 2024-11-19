import FreeCAD as App
import FreeCADGui as Gui
import matplotlib.pyplot as plt
import numpy as np


class PointCloud:

    def getActivePointsObject():
        activeObj_List = Gui.Selection.getSelection()
        if not activeObj_List:
            print("there is no selected object")
            return None
        elif len(activeObj_List) == 1:
            activeObj = activeObj_List[0]
            pointsObject = activeObj.Points
        elif len(activeObj_List) > 1:
            pointsObject = activeObj_List

        return pointsObject

    def getPointsObject(docName, objName):
        pointsObject = App.getDocument(docName).getObject(objName)
        return pointsObject

    def countPoints(pointsObj):
        pointsNum = pointsObj.CountPoints
        return pointsNum

    def getPointsList(pointsObj):
        pointsList = pointsObj.Points
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
        # x_coords = np.array(x_coords)
        # y_coords = np.array(y_coords)

        plt.figure(figsize=(6, 3),dpi=200)

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
        fontSize = 2
        plt.rcParams.update({'font.size': fontSize})

        # 显示图形
        plt.show()

        # 利用kdeplot函数快速绘制
        # sns.kdeplot(x=x_coords, y=y_coords)
        # plt.show()
