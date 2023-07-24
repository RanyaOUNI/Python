/* 
String Encode

You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
*/

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str) {
    var expected = ""
    if(str.length<= 1){
        return str
    }
    for(var i = 0;i<str.length;i++){
        var currentChar = str[i]
        var counter = 0
        console.log(str[i],"************");
        while(currentChar == str[i+1]){
            counter++
            console.log(currentChar,counter);
            i++
        }
        expected+=currentChar+counter
    }
    return expected1
}

console.log(encodeStr(str1));
console.log(encodeStr(str2));
console.log(encodeStr(str3));
console.log(encodeStr(str4));
