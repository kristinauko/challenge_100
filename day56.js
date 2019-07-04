/*
Write a program which creates a string that represents 8 X 8 grid
using newline characters to separate lines. At each position of the 
grid there is either a space or a "#" character. Characters should 
form a chessboard. 

Passing this string to console should show this:
# # # # 
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #

When you have a program that generates pattern, define binding size size = 8
and change the program so that it works for any size, outputting a grid of the 
given width and height. 
*/

let size = 8;

for (let num = 1; num <= size; num++) {
    let line = "";
    if (num % 2 == 0) {
        while (line.length < size) {
            line += " #"; 
        } console.log(line);
    } else {while (line.length < size) {
            line = line + "# ";
            } console.log(line);
        }
}
