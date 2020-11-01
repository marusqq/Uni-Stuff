module Second_Work where
import System.IO
import Data.Char

-- 4 ex.
bubble :: [Integer] -> [Integer]
bubble (x:y:xs) | x > y = y : bubble (x : xs)
                | otherwise = x : bubble (y : xs)
bubble x = x

isSorted :: [Integer] -> Bool
isSorted []       = True
isSorted [x]      = True
isSorted (x:y:xs) = x <= y && isSorted (y:xs)

sortList list 
  | isSorted list = list
  | otherwise = sortList (bubble list)
  
permut :: [Integer] -> [Integer] -> Bool
permut list1 list2 = (sortList list1) == (sortList list2)   


-- 6.1 ex.
itemTotal :: [(String,Float)] -> [(String,Float)]

getPrice :: String -> [(String,Float)] -> Float
getPrice itemName (selectedItem:otherItems)
    | null selectedItem = 0
    | length(otherItems) == 0 && (fst selectedItem) == itemName = (snd selectedItem)
	| (fst selectedItem) == itemName = (snd selectedItem) + getPrice itemName otherItems
    | length(otherItems) == 0 = 0
    | otherwise = 0 + getPrice itemName otherItems
          
getTotalItemSums :: [(String,Float)] -> [(String,Float)] -> [String] -> [(String,Float)] -> [(String,Float)]
getTotalItemSums (selectedItem:otherItems) itemList visitedItems total
    | elem (fst selectedItem) visitedItems && length(otherItems) == 0 = total
    | elem (fst selectedItem) visitedItems = getTotalItemSums otherItems itemList visitedItems total
    | length(otherItems) == 0 = (newItem:total)
    | otherwise = getTotalItemSums otherItems itemList ((fst selectedItem):visitedItems) (newItem:total)
    where newItem = ((fst selectedItem),newPrice)
          newPrice = getPrice (fst selectedItem) itemList 
    
itemTotal list = getTotalItemSums list list [] []

-- 6.2 ex.
itemDiscount :: String -> Integer -> [(String,Float)] -> [(String,Float)]
itemDiscount itemToDiscount discount [] = []
itemDiscount itemToDiscount discount ((item, price): otherItems)
    | itemToDiscount /= item = (item, price): itemDiscount itemToDiscount discount otherItems 
    | otherwise = (item, price - (price * (fromIntegral discount)) / 100) : itemDiscount itemToDiscount discount otherItems
