
/* 
Function takes two-dimentional array and returns the number of all possible 
moves in the grid. 

Move is described as a swap of two items which sit next to each other. Move 
is valid if swap results in a cluster of the same numbers. */

function findMoves(array) {

  let moves = [];
  let temp = 0;
  const LENGTH = array.length;

  // Check horizontal swap
  for (let i = 0; i < LENGTH; i++) {

    let move = 0;

    for (let j = 0; j < LENGTH - 1; j++) {
      temp = array[i][j];
      array[i][j] = array[i][j+1];
      array[i][j+1] = temp;

      move = findClusters(array);

      if (move.length != 0) {
          moves.push(move);
      }
      array[i][j+1] = array[i][j];
      array[i][j] = temp;
    }
  }

  // Check vertical swap
  for (let i = 0; i < LENGTH; i++) {

    let move = 0;

    for (let j = 0; j < LENGTH - 1; j++) {
      temp = array[j][i];
      array[j][i] = array[j+1][i];
      array[j+1][i] = temp;

      move = findClusters(array);

      if (move.length != 0) {
          moves.push(move);
      }
      array[j+1][i] = array[j][i];
      array[j][i] = temp;
    }

  } console.log(moves.length)
  return moves.length;
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
      } 
      else if (array[i][j-1] == array[i][j]) {
        row_cluster.push([i, j]);
        if (j == (length - 1) && row_cluster.length >= 3) {
          clusters.push(row_cluster);
          row_cluster = []; 
        }
      } 
      else {
        if (row_cluster.length >= 3) {
          clusters.push(row_cluster);
        } 
        row_cluster = [];
      }
    }     
  }  
      
  // Check for clusters in columns
  for (let i = 0; i < length; i++) {

    let col_cluster = [];

    for (let j = 1; j < length; j++) {

      if (array[j-1][i] == array[j][i] && col_cluster.length == 0) {
        col_cluster.push([j-1, i], [j, i])
      } 
      else if (array[j-1][i] == array[j][i]) {
        col_cluster.push([j, i]);
        if (j == (length - 1) && col_cluster.length >= 3) {
          clusters.push(col_cluster);
          col_cluster = [];
        }
      } 
      else {
        if (col_cluster.length >= 3) {
          clusters.push(col_cluster);
        }  
        col_cluster = [];  
      }
    }     
  } return clusters
}


               
findMoves([   [ 3, 6, 2, 6, 4, 3, 5, 6 ],
              [ 2, 4, 6, 1, 4, 3, 1, 4 ],
              [ 4, 1, 1, 5, 1, 7, 6, 4 ],
              [ 2, 6, 3, 7, 7, 4, 6, 3 ],
              [ 3, 3, 4, 5, 4, 4, 7, 4 ],
              [ 6, 3, 1, 4, 6, 7, 1, 1 ],
              [ 3, 7, 4, 6, 5, 7, 6, 5 ],
              [ 6, 4, 7, 3, 6, 6, 2, 3 ] ])

