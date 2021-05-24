#!/usr/bin/env python3
################################################################################
#
#   Filename:           meeting_rooms_ii.py
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #253
#
#   Problem description:
#   https://leetcode.com/problems/meeting-rooms-ii/
#
################################################################################
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval : interval[0])
        max_meeting_rooms = 0
        meeting_rooms = []
        for interval in intervals:
            if not meeting_rooms:
                heappush(meeting_rooms, interval[1])
                max_meeting_rooms += 1
            else:
                if meeting_rooms[0] > interval[0]:
                    heappush(meeting_rooms, interval[1])
                    max_meeting_rooms += 1
                else:
                    heappop(meeting_rooms)
                    heappush(meeting_rooms, interval[1])
        return max_meeting_rooms
