function twoSum(nums: number[], target: number): number[] {
    const lenNums = nums.length
    for (let i = 0; i < lenNums; i++) {
        for (let j = 0; j < lenNums; j++) {
            if (i !== j) {
                const sumOfTwo = nums[i] + nums[j]
                if (sumOfTwo === target) {
                    return [i, j]
                }
            }
        }
    }


};