/* 
  Given a string,
  return a new string with the duplicates excluded

  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 */

function stringDedupe1(str) {
    var result = ""
    for(var i=0;i<str.length;i++){
        if(result.indexOf(str[i])== -1){
            result+=str[i]
        }
    }
    return result
       
}

function stringDedupe2(str) {
       
}

function stringDedupe3(str) {
    var result = ""
    var freqDict = {}
    for (var i=0;i<str.length;i++){
        if(freqDict[str[i]]==false){
            freqDict[str[i]]=true
            result += str[i]
        }
    }   
}

console.log("EXIST",str1.indexOf("b"));
onsole.log("NOT",str1.indexOf("d"));
console.log("EXIST",str1.includes("b"));
console.log("EXIST",str1.includes("d"));