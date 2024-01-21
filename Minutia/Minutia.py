class Minutia:
    def __init__(self, locX, locY, orientation, minutiaType, closestNeighbor = None, secondClosestNeighbor = None, featureVector = None, globalFeatureVector = None):
        self.locX = locX
        self.locY = locY
        self.orientation = orientation
        self.minutiaType = minutiaType # 0 - Termination; 1 - Bifurcation
        self.closestNeighbor = closestNeighbor
        self.secondClosestNeighbor = secondClosestNeighbor
        self.featureVector = featureVector
        self.globalFeatureVector = globalFeatureVector

    def __str__(self):
        return "locX:\t\t" + str(self.locX) + "\n" \
        + "locY:\t\t" + str(self.locY) + "\n" \
        + "orientation:\t" + str(self.orientation) + "\n" \
        + "minutiaType:\t" + str(self.minutiaType) + "\n" \
        + "closestNeighbor:\t" + str(self.closestNeighbor) + "\n" \
        + "secondClosestNeighbor:\t" + str(self.secondClosestNeighbor) + "\n" \
        + "featureVector:\t\t" + str(self.featureVector) + "\n" \
        + "globalFeatureVector:\t\t" + str(self.globalFeatureVector)