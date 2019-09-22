class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s=[x[0] for x in intervals]
        e=[x[1] for x in intervals]
        s.sort()
        e.sort()
        room=0
        counter=0
        for start in s:
            if start<e[counter]:
                room+=1
            else:
                counter+=1
        return room