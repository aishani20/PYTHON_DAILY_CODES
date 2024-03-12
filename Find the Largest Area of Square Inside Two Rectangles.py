class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        maximum_takenarea = 0
        numbering = len(bottomLeft)
      

        for zzz in range(numbering):
            for mnh in range(zzz + 1, numbering):
                ais = max(bottomLeft[zzz][0], bottomLeft[mnh][0])
                abh = max(bottomLeft[zzz][1], bottomLeft[mnh][1])
                kar = min(topRight[zzz][0], topRight[mnh][0])
                mhn = min(topRight[zzz][1], topRight[mnh][1])

                if ais < kar and abh < mhn:
                    taking_side_as = min(kar - ais, mhn - abh)
                    maximum_takenarea = max(maximum_takenarea, taking_side_as  * taking_side_as )

        return  maximum_takenarea