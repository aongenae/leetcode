/*******************************************************************************
*
*   Filename:           two_sum.go
*
*   Author:             Arnaud Ongenae
*
*   Leetcode.com:       problem #1
*
*   Problem description:
*   https://leetcode.com/problems/two-sum/description/
*
*******************************************************************************/

package main

func twoSum(nums []int, target int) []int {
	buffer := make(map[int]int)
	for index, value := range nums {
		if stored_index, ok := buffer[value]; ok {
			return []int{stored_index, index}
		} else {
			buffer[target-value] = index
		}
	}
	return []int{} // should not reach this line if solution exists
}
