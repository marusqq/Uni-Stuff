module Second 
where
import Data.Char

--TESTS
--  test case:                      result:

-- 1:
--  average [1,2,3,4,5]             3.0
--  average [50,100,150,200]        125.0

-- 2:
--  divides 79                      [1,79]
--  divides 256                     [1,2,4,8,16,32,64,128,256]
--  isPrime 79                      True
--  isPrime 256                     False
--  dividesRecursion 79             [79,1]
--  dividesRecursion 256            [256,128,64,32,16,8,4,2,1]

-- 3:
--  prefix "test" "testuoju"        True
--  prefix "kar" "kapas"            False
--  prefix "tas" "matas"            False
--  substring "inis" "sumuštinis"   True
--  substring "qq" "quqestion"      False

-- 4:
--  permut [1,2,3,4,5,6,7,8,9,10] [10,9,8,7,6,5,4,3,2,1]    True
--  permut [1,2,3] [2,1]                                    False

-- 5:
--  capitalize "test"          "TEST"
--  capitalize "TEST"          "TEST"
--  capitalize "tEsT"          "TEST"

-- 6:
--  itemTotal [("x", 2.00), ("x", 1.50), ("y", 2.6)]                [("y",2.6),("x",3.5)]
--  itemDiscount "x" 50 [("x", 2.00), ("x", 1.50), ("y", 2.6)]      [("x",1.0),("x",0.75),("y",2.6)]
    




--1 list average
average :: [Float] -> Float
average x = sum x / fromIntegral(length x)

--2 divisor finding
--list comprehension
divides :: Integer -> [Integer]
divides num
    |  num < 0 = divides(abs num)
    |  num >= 0 = [x | x <- [1.. num], mod num x == 0]

--recursion
dividesRecursion :: Integer -> [Integer]
dividesRecursion number = dividersGet (abs number) (abs number) []

dividersGet :: Integer -> Integer -> [Integer] -> [Integer]
dividersGet num num2 list
  |  num2 > 0 && (num `mod` num2) == 0 = dividersGet num (num2-1) (list ++ [num2])
  |  num2 > 0 = dividersGet num (num2-1) list
  |  num2 == 0 = list

--prime check
isPrime :: Integer -> Bool
isPrime x
    |  x < 0 = error "only non-negative numbers"
    |  otherwise = length(divides x) == 2

--3 fix prefix, substring 
prefix :: String -> String -> Bool
prefix [] _ = True
prefix _ [] = False
prefix (s1:left_s1) (s2:left_s2)
    |  s1 == s2 = prefix left_s1 left_s2
    |  otherwise = False

substring :: String -> String -> Bool
substring s1 s2
    |  length s1 > length s2 = False
    |  prefix s1 s2 = True
    |  otherwise = substring s1 (tail s2)

--4 permutations two lists
sortBubble :: [Integer] -> [Integer]
sortBubble (first:second:left)
    |  first > second = second : sortBubble(first:left)  
    |  otherwise = first : sortBubble(second:left)
sortBubble first = first

sorted :: [Integer] -> Bool
sorted [] = True
sorted [first] = True
sorted (first:second:left) = first <= second && sorted(second:left)

fullSort l
    | sorted l = l
    | otherwise = fullSort (sortBubble l)

permut :: [Integer] -> [Integer] -> Bool
permut l1 l2 = fullSort(l1) == fullSort(l2)

--5 capitalize
letter :: Char -> Bool
letter char
    | (char <= 'Z' && char >= 'A') || (char <= 'z' && char >= 'a') = True
    | otherwise = False

capitalize :: String -> String
capitalize str = [toUpper chr | chr <- str, letter chr]


--6 
--item total
itemTotal :: [(String, Float)] -> [(String, Float)]
itemTotal [] = []
itemTotal [pair] = [pair]
itemTotal (pair:other_pairs) = combine pair (itemTotal other_pairs)

combine :: (String, Float) -> [(String, Float)] -> [(String, Float)]
combine pair [] = [pair]
combine pair (other_pair:leftovers)
    --fst -> first, snd -> second
    |  fst pair == fst other_pair = (fst pair, snd pair + snd other_pair):leftovers
    |  otherwise = other_pair : combine pair leftovers

--discount
itemDiscount :: String -> Integer -> [(String, Float)] -> [(String, Float)]
itemDiscount _ _ [] = []
itemDiscount name discount (good:other_goods)
    |  discount < 0 || discount > 100 = error "Discount should be from 0% to 100%"
    |  name == fst good = (fst good, snd good * (100 - fromIntegral(discount)) / 100) : itemDiscount name discount other_goods
    |  otherwise = good : itemDiscount name discount other_goods
