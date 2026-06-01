--// Was a bit bored so why not try to solve one of if not the most famous leetcode problems within lua
--// Of course, leetcode doesn't support lua in its code editor so I had to basically do a bit of improvising to see what would the script
--// look like in the style of class solutions they do

local TwoSum = {}
TwoSum.__index = TwoSum

setmetatable(TwoSum, {
    __call = function(_, nums, target)
        for i, v in ipairs(nums) do
            for k, z in ipairs(nums) do
                if v + z == target and i ~= k then
                    return i, k
                end
            end
        end
    end
})

local i, k = TwoSum({2,7,11,15}, 9)
print(i, k)
