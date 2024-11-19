import FreeCAD as App
import matplotlib


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
        z_coords = [point.z for point in pointsList]
