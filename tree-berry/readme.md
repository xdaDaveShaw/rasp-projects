# About

A series of scripts for controlling my [Raspberry pi Xmas tree](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi).

## ThePiHut.com XMAS Tree GPIO <> Tree number mapping

### By GPIO

List of GPIO pin numbers and which LED number on the PCB they relate to.

|GPIO |Tree|
|-----|----|
|2    |star|
|3    |n/a |
|4    |1   |
|5    |7   |
|6    |16  |
|7    |22  |
|8    |6   |
|9    |14  |
|10   |8   |
|11   |21  |
|12   |15  |
|13   |3   |
|14   |19  |
|15   |2   |
|16   |9   |
|17   |10  |
|18   |20  |
|19   |18  |
|20   |17  |
|21   |4   |
|22   |24  |
|23   |23  |
|24   |13  |
|25   |5   |
|26   |12  |
|27   |11  |

### By LED number on PCB

List of LED number on the PCB and which GPIO pin numbers they relate to.

|Tree |GPIO|
|-----|----|
|star |2   |
|n/a  |3   |
|1    |4   |
|2    |15  |
|3    |13  |
|4    |21  |
|5    |25  |
|6    |8   |
|7    |5   |
|8    |10  |
|9    |16  |
|10   |17  |
|11   |27  |
|12   |26  |
|13   |24  |
|14   |9   |
|15   |12  |
|16   |6   |
|17   |20  |
|18   |19  |
|19   |14  |
|20   |18  |
|21   |11  |
|22   |7   |
|23   |23  |
|24   |22  |

### Rows

Separating the tree in 5 horizontal rows, each with number of LEDs on.

|Row     |GPIO Pins|
|--------|---------|
|star    |2        |
|first   |17, 16, 11, 19, 25, 27|
|second  |4, 9, 13, 18, 5, 8, 26|
|third   |22, 24, 20, 12, 6, 15|
|bottom  |14, 10, 23, 21, 7|