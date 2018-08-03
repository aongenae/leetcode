################################################################################
#
#   Filename:           single_number.go
#
#   Author:             Arnaud Ongenae
#
#   Leetcode.com:       problem #136
#
#   Problem description:
#   https://leetcode.com/problems/single-number/description/
#
##############################################################################

import (
    "sort"
)

func singleNumber(nums []int) int {

    length := len(nums)
    if length == 1 {
        return nums[0]
    }

    sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })
    current := 0
    for current < length-2 {
        if nums[current] != nums[current+1] {
            return nums[current]
        } else {
            current += 2
        }
    }
    return nums[length-1]
}
