/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
// return num of rooms needed
// O(nlogn) time, O(n) space
public class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval a, Interval b) {
                return a.start - b.start;
            }
        });
        Queue<Integer> heap = new PriorityQueue<>();//no need to store interval, we can just store the end time
        heap.offer(intervals[0].end);
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i].start >= heap.peek()) {//if can use room that ends earliest,poll that end time,add curr end time
                heap.poll();
            }
            heap.offer(intervals[i].end);//add curr end time
        }
        return heap.size();//size of heap:num of rooms needed for all meetings(meetings in heap all are overlapping meetings)
    }
}

// return the exact time that has max num of room used (any valid time)
// O(nlogn) time, O(n) space
public class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval a, Interval b) {
                return a.start - b.start;
            }
        });
        Queue<Integer> heap = new PriorityQueue<>();//no need to store interval, we can just store the end time
        heap.offer(intervals[0].end);
        int overlapStart = -1;
        int overlapEnd = -1;
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i].start >= heap.peek()) {//if can use room that ends earliest,poll that end time,add curr end time
                heap.poll();
            } else {
                overlapStart = intervals[i].start;
                overlapEnd = Math.min(heap.peek(), intervals[i].end);//should be min of these two
            }
            heap.offer(intervals[i].end);//add curr end time
        }
        return overlapStart;//you can return any time between overlapStart and overlapEnd
    }
}

// return the num of room used / employees of each non-overlapping time range(you can design you own output)
// O(nlogn) time, O(n) space
public class Solution {
    public class TimeSlot {
        int time;
        boolean isStart;
        public TimeSlot(int t, boolean i) {
            time = t;
            isStart = i;
        }
    }
    
    public List<String> meetingRooms(Interval[] intervals) {
        List<String> res = new ArrayList<>();
        if (intervals == null || intervals.length == 0) {
            return res;
        }
        List<TimeSlot> times = new ArrayList<>();
        for (Interval i : intervals) {//spilt the start time and end time, then sort them
            times.add(new TimeSlot(i.start, true));//use the boolean to regconize if it's a start or end time
            times.add(new TimeSlot(i.end, false));
        }
        Collections.sort(times, new Comparator<TimeSlot>(){
            public int compare(TimeSlot a, TimeSlot b) {
                return a.time - b.time;
            }
        });
        int count = 0;
        int begin = 0;//it's the index of begin time, not the time itself
        for (int i = 1; i < times.size(); i++) {
            if (times.get(i) != times.get(i - 1)) {//only add time range to res when there is a diff between two times
                res.add(times.get(begin) + "-" + times.get(i) + ": " + count);//add to res before count is gonna be changed
                begin = i;//update begintime's index
            }
            if (times.get(i).isStart) {//count curr num of people/rooms
                count++;
            } else {
                count--;
            }
        }
        return res;
    }
}
// eg. [2004, 2007], [2005, 2007], [2006, 2008] -> 2004-2005: 1; 2005-2006: 2; 2006-2007: 3; 2007-2008: 1;
// if the format of intervals are "March, 2014" etc, first convert it to "201403" by "2014" + "03"(hashmap:March->03)
// http://www.1point3acres.com/bbs/thread-109379-2-1.html

// print each room's usage time intervals: Room 1:[2, 6],[7, 9]; Room 2:[3, 5],[8, 10]; etc.
// O(nlogn) time, O(n) space
public class Solution {
    public void MeetingRooms(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) {
            return;
        }
        Arrays.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval a, Interval b) {
                return a.start - b.start;
            }
        });
        Queue<List<Interval>> rooms = new PriorityQueue<>(1, new Comparator<List<Interval>>(){
            public int compare(List<Interval> a, List<Interval> b) {
                return a.getLast().end - b.getLast().end;
            }
        });//store linkedlists of intervals,each list is a room,the last element in list is the meeting that's using the room
        for (Interval i : intervals) {//for each meeting
            List<Interval> room = null;
            if (rooms.isEmpty() || i.start < rooms.peek().getLast().end) {//if need new room(no rooms/all curr rooms overlap)
                room = new LinkedList<>();
            } else {
                room = queue.poll();//else use the previous room that ends earliest (no overlap with curr meeting)
            }
            room.add(i);//add curr meeting into the room, which is at the back of the linkedlist
            rooms.offer(room);
        }
        while (!rooms.isEmpty()) {
            List<Interval> room = rooms.poll();
            //you can maintain a roomNum and System.out.print("Room " + roomNum + ":");
            for (Interval i : room) {//print each meeting in a same room
                System.out.print("[" + i.start + "-" i.end + "],");
            }
            System.out.println();
        }
    }
}

// return the time ranges of free time between startTime and endTime (time ranges that have no meetings):
// O(nlogn) time, O(1) space
public class Solution {
    public List<String> minMeetingRooms(Interval[] intervals, int start, int end) {
        List<String> res = new ArrayList<>();
        if (intervals == null || intervals.length == 0) {
            return res;
        }
        Collections.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval a, Interval b) {
                return a.start - b.start;
            }
        });
        int begin = start;//the beginTime of freeTime (end of last meeting)
        for (Interval i : intervals) {
            if (begin >= end) {//if the start of free time is out of range(exceeds end), break the loop
                break;
            }
            if (i.start > begin) {//only add time range to res when there is a diff(free time) between two times
                res.add(begin + "-" + Math.min(i.start, end));//if the i.start exceeds end, we pick end to be the boundary
            }
            begin = Math.max(begin, i.end);//update begintime
        }
        return res;
    }
}









