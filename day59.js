/*
Return False if three or more integers of the array standing
next to each other are equal. Otherwise, return True.

Example:
[5, 4, 6, 4, 4, 3, 8] > True
[5, 4, 6, 4, 4, 4, 8] > False
*/


function isValid(l) {

    const length = l.length;
    let count = 0;

    for (let i = 0; i < length; i++) {

        previous = l[i-1];

        if (l[i] == previous && count == 0) {
            count += 2;
        } else if (l[i] == previous) {
            count += 1;
        } else {
            count = 0;
        }

        if (count == 3){
            break;
        } 
        
    }
    console.log(count != 3);
}


isValid([5, 4, 6, 4, 4, 3, 8])
isValid([5, 4, 6, 4, 4, 4, 8])