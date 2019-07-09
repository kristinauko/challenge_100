/* 
Given function findClusters, swap the middle item in two-dimentional array 
that there would not be clusters of three or more numbers. If it's not possible
to swap items that there would not be clusters, re-create the map.
*/

function generateMap(num, min, max) {

    let generatedMap = [];
    let clusters = [null];
    let count = 0

    while (clusters.length != 0 && count != 7) {

        generatedMap = produceArray(num, min, max);
        console.log(generatedMap);
        clusters = findClusters(generatedMap);

        for (let cluster of clusters) {
            generatedMap = fixCluster(cluster, generatedMap);
        } count += 1;  
        clusters = findClusters(generatedMap);
    } 
    console.log(generatedMap);
}

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


function findClusters(array) {

    let clusters = new Array();           
    const length = array.length;
    
    // Check for clusters in rows
    for (let i = 0; i < length; i++) {
        let row_cluster = [];

        for (let j = 1; j < length; j++) {

            if (array[i][j-1] == array[i][j] && row_cluster.length == 0) {
                row_cluster.push([i, j-1], [i, j]);
            } else if (array[i][j-1] == array[i][j]) {
                row_cluster.push([i, j]);
                if (j == (length - 1) && row_cluster.length >= 3) {
                    clusters.push(row_cluster);
                    row_cluster = []; 
                }
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
                col_cluster.push([j-1, i], [j, i])
            } else if (array[j-1][i] == array[j][i]) {
                col_cluster.push([j, i]);
                if (j == (length - 1) && col_cluster.length >= 3) {
                    clusters.push(col_cluster);
                    col_cluster = [];
                }
            } else {
                if (col_cluster.length >= 3){
                clusters.push(col_cluster);
                }  col_cluster = [];  
            }
        }     
    } return clusters
}


function fixCluster(cluster, array) {

    let xDirection = 0;
    let yDirection = 0;

    if (cluster[0][0] == cluster[1][0] && cluster[1][0] == cluster[2][0]) {
        if (cluster[0][0] == 7) {
            xDirection = -1;
        } else {
            xDirection = 1;
        } yDirection = 0;
    } else if (cluster[0][1] == cluster[1][1] && cluster[1][1] == cluster[2][1]) {
        if (cluster[0][1] == 7) {
            yDirection = -1;
        } else {
            yDirection = 1;
        } xDirection = 0;
    }
    
    for (let c of cluster) {
        let x = c[0];
        let y = c[1];

        if (array[x][y] != array[x + xDirection][y + yDirection]) {
            let temp = array[x][y];
            array[x][y] = array[x + xDirection][y + yDirection]; 
            array[x + xDirection][y + yDirection] = temp; 
            break;
        } 
    } return array
}

generateMap(8, 1, 7);

