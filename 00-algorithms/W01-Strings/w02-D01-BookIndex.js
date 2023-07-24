/* 
Book Index

Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums
span a consecutive range.
*/

const nums1 = [1, 13, 14, 15, 37, 38, 70];
// const expected1 = "1, 13-15, 37-38, 70";

const nums2 = [5, 6, 7, 8, 9];
// const expected2 = "5-9";

const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
// const expected3 = "1-3, 7, 9, 15-17";


function bookIndex(nums) {
    // var str_nums = "" 
    var expected = ""
    for (var i=0;i<nums.length(nums);i++){
        // console.log('i=${i},num[${i}] = ${nums[i]} ----- i+1 = ${i+1}, nums[i+1] = ${nums[i+1]}')

        // if ( nums[i]-nums[i+1] != 1){
        //     str_nums.push(nums[i])
        // else
        var pageIndex = i
        var currentNumber = nums[i]
        if (currentNumber+1 != nums[i+1]){
            expected += currentNumber + ","
        } else{
            while(nums[pageIndex+1] - nums[i]==1){
                console.log(currentNumber,"----",nums[pageIndex+1]);
                pageIndex+=1
                i = pageIndex
            }
            console.log(i);
        } 
        }

    }

}