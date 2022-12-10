const {readFileSync, promises: fsPromises} = require('fs');

function syncReadFile(filename){
    const content = readFileSync(filename, 'utf-8');
    const arr = content.split(/\r?\n/);
    //console.log(arr);
    return arr
}

function score(values){
    return 20* values[19] + 60*values[59] + 100*values[99] + 140*values[139] + 180*values[179] + 220*values[219]
}

function draw(cycle,x){
    let CRTrow = Math.ceil(cycle/40);
    let CRTcol = (cycle % 40);
    //if (CRTcol == 0) {
    //    CRTcol = 40;        
    //}
    let sprite = x //(x % 40);
    //if (sprite == 0) {
    //    sprite = 40
    //}
    console.log(CRTrow,CRTcol,x,sprite) 
    string = ""
    if ((CRTcol >= sprite -1) && (CRTcol <= sprite +1)) {
        string = "#"
    }
    else{
        string = "."
    }   
    if (CRTcol==39){
        string = string+"\n"
    } 
    return string
}

let arr = syncReadFile("Input.txt");
let x = 1;
let value_log = [1];
let cycle =1;
let output = ["#"];

for (let index = 0; index < arr.length; index++) {
    const element = arr[index];
    if (element.includes("addx")){ 
        let split = element.split(/ /);
        let iter = split[1];
        output.push(draw(cycle,x));
        value_log.push(x);
        cycle++;
        x= x+parseInt(iter);
        
        output.push(draw(cycle,x));
        value_log.push(x);
        cycle++;       
    }
    else{
        output.push(draw(cycle,x))
        value_log.push(x); 
        cycle++; 
    }    
}
console.log(score(value_log));
console.log(output.join(''))


