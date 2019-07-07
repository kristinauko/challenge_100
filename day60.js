/*
Produce two-dimentional array and find clusters of values (3 or more).
Output the array and coordinates of clusters.
*/

// Number of rows and cols
const gridSize = 8;

// Values min
const min = 1;

// Values max
const max = 7;

//Generate pattern
let map = findCluster();

// Produce two-dimentional array of randomized numbers
function produceArray(n, min, max) {

    let array = new Array();
    
    for (let i = 0; i < n; i++) {
        let new_array = new Array();

        for (let j = 0; j < n; j++) {
            number = Math.random() * (max - min) + min;
            new_array.push(Math.round(number));

        } array.push(new_array);

    } return array;
}


function findCluster() {
    array = produceArray(gridSize, min, max);

    console.log(array)

    let clusters = new Array();
                
    const length = array.length;
    
    // Check for clusters in rows
    for (let i = 0; i < length; i++) {

        let row_cluster = [];

        for (let j = 1; j < length; j++) {

            if (array[i][j-1] == array[i][j] && row_cluster.length == 0) {
                row_cluster.push([j-1, i], [j, i]);
                // console.log(row_cluster);
            } else if (array[i][j-1] == array[i][j]) {
                row_cluster.push([j, i]);
                // console.log(row_cluster);
            } else {
                if (row_cluster.length >= 3){
                clusters.push(row_cluster);
                } row_cluster = [];
                }
            }     
        }  
        
    // Check for clusters in columns
    for (let i = 0; i < length; i++) {

        let col_cluster = [];

        for (let j = 1; j < length; j++) {

            if (array[j-1][i] == array[j][i] && col_cluster.length == 0) {
                col_cluster.push([i, j-1], [i, j]);
                // console.log(row_cluster);
            } else if (array[j-1][i] == array[j][i]) {
                col_cluster.push([i, j]);
                // console.log(row_cluster);
            } else {
                if (col_cluster.length >= 3){
                clusters.push(col_cluster);
                } 
                col_cluster = [];
                    // console.log(row_cluster);
            }
        }     
    }

    console.log(clusters)
}
