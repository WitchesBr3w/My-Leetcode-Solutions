--// Solution to the leetcode problem number 121 in lua 
--// Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

function maxProfit(prices)
    local minPrice = math.huge
    local maxProfit = 0

    for i = 1, #prices do
        local price = prices[i]

        -- update minimum price seen so far
        if price < minPrice then
            minPrice = price
        end

        -- calculate profit if sold today
        local profit = price - minPrice

        -- update max profit
        if profit > maxProfit then
            maxProfit = profit
        end
    end

    return maxProfit
end

local prices = {7, 1, 5, 3, 6, 4}
print(maxProfit(prices))  -- Output: 5
