/******************************************************************************
*
*   Filename:           single_number_test.go
*
*   Author:             Arnaud Ongenae
*
*******************************************************************************/

package main

import (
	"testing"
)

func testSum(t *testing.T) {
	input := []int{1, 2, 1}
	result := SingleNumber(input)
	if result != 1 {
		t.Errorf("Result is incorrect, got: %d, expected 1.", result)
	}
}
