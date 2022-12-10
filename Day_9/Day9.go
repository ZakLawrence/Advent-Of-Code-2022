package main

import (
	"os"
	"strconv"
	"strings"
)

type coord struct {
	x int
	y int
}

func (c coord) mult(m int) coord {
	return coord{c.x * m, c.y * m}
}

func (c *coord) add(a coord) {
	c.x = c.x + a.x
	c.y = c.y + a.y
}

func (c coord) print() {
	println(c.x, c.y)
}

func (c1 coord) delta(c2 coord) (int, int) {
	return c1.x - c2.x, c1.y - c2.y
}

var delta = map[string]coord{
	"U": {x: 0, y: 1},
	"D": {x: 0, y: -1},
	"R": {x: 1, y: 0},
	"L": {x: -1, y: 0},
}

var tail_move = map[coord]coord{
	{2, 0}:  {1, 0},
	{-2, 0}: {-1, 0},
	{0, 2}:  {0, 1},
	{0, -2}: {0, -1},

	{2, 1}:   {1, 1},
	{-2, 1}:  {-1, 1},
	{2, -1}:  {1, -1},
	{-2, -1}: {-1, -1},

	{1, 2}:   {1, 1},
	{1, -2}:  {1, -1},
	{-1, 2}:  {-1, 1},
	{-1, -2}: {-1, -1},

	{2, 2}:   {1, 1},
	{2, -2}:  {1, -1},
	{-2, 2}:  {-1, 1},
	{-2, -2}: {-1, -1},
}

func move(s string) (coord, int) {
	line := strings.Fields(s)
	dir := line[0]
	num, _ := strconv.Atoi(line[1])
	return delta[dir], num
}

func follows(input []string, knots int) {
	rope := []*coord{}
	for len(rope) < knots {
		rope = append(rope, &coord{x: 0, y: 0})
	}
	tail_position := map[coord]int{{x: 0, y: 0}: 1}
	head := rope[0]
	for _, temp := range input {
		change, num := move(temp)
		for i := 0; i < num; i++ {
			head.add(change)
			for indx, k := range rope {
				if indx == 0 {
					continue
				}
				dx, dy := rope[indx-1].delta(*k)
				k.add(tail_move[coord{dx, dy}])
				if indx == len(rope)-1 {
					tail_position[*k] += 1
				}
			}
		}
	}
	println(len(tail_position))
}

func read_file(fpath string) []string {
	fileBytes, err := os.ReadFile(fpath)
	if err != nil {
		panic(err)
	}
	fileString := string(fileBytes)
	return strings.Split(fileString, "\n")
}

func main() {
	moves := read_file("Input.txt")
	follows(moves, 2)
	follows(moves, 10)
}
