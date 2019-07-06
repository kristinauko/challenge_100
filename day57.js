/* Produce two-dimentional array (n = 8) of random numbers */


function produceArray(n, min, max) {

    let array = new Array()
    
    for (let i = 0; i < n; i++) {
        let new_array = new Array();

        for (let j = 0; j < n; j++) {
            number = Math.random() * (max - min) + min;
            new_array.push(Math.round(number));

        } array.push(new_array);

    } console.log(array);
}

produceArray(8, 1, 7)



