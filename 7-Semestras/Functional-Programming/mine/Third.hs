module Third
where
import Data.Char

------------------------
-- 1 overlaps
-- tests: 
--      - overlaps (Circle 1 5 4)(Rectangle 4 10 6 1) - True
--      - overlaps (Circle 1 1 1)(Circle 1 1 1) - True
------------------------

data Shape = Circle Float Float Float | Rectangle Float Float Float Float
    deriving (Show, Ord, Eq)

overlaps :: Shape -> Shape -> Bool

-- distance < radius1+radius2
overlaps (Circle x1 y1 r1) (Circle x2 y2 r2) = (sqrt((x1-x2)**2 + (y1-y2)**2)) < r1 + r2


-- centre coordinates
overlaps (Rectangle a1 b1 c1 d1) (Rectangle a2 b2 c2 d2) = not (cond1 || cond2)
    where 
        -- top left corner 1
        top_left_corner_1_x = a1 - c1 / 2
        top_left_corner_1_y = b1 + d1 / 2

        -- top left corner 2
        top_left_corner_2_x = a2 - c2 / 2
        top_left_corner_2_y = b2 + d2 / 2

        -- lower right corner 1
        lower_right_corner_1_x = a1 + d1 / 2
        lower_right_corner_1_y = b1 - c1 / 2

        -- lower right corner 2
        lower_right_corner_2_x = a2 + d2 / 2
        lower_right_corner_2_y = b2 - c2 / 2
        
        -- x axis
        cond1 = top_left_corner_1_x >= lower_right_corner_2_x || top_left_corner_2_x >= lower_right_corner_1_x

        -- y axis
        cond2 = top_left_corner_1_y <= lower_right_corner_2_y || top_left_corner_2_y <= lower_right_corner_1_y

overlaps (Rectangle a b c d) (Circle x1 y1 r) = cond1
    where
        -- top left corner
        top_left_corner_x = a - d / 2
        top_left_corner_y = b + c / 2

        -- lower right corner
        lower_right_corner_x = a + d / 2
        lower_right_corner_y =  b - c / 2

        cond1 = ((x1 - (max top_left_corner_x (min x1 lower_right_corner_x)))**2 + (y1 - (max lower_right_corner_y (min y1 top_left_corner_y)))**2) < (r**2)

-- keep functionality from the other side
overlaps (Circle x1 y1 r) (Rectangle a b c d) = overlaps (Rectangle a b c d) (Circle x1 y1 r)

------------------------
-- 2 filter / map & foldr
-- tests: 
--      - any_filter odd [1,22] - True
--      - any_map_foldr odd [1,22] - True
--      - 
--      - all_filter even [0,3] - False
--      - all_map_foldr even [0,3] - False
------------------------

-- for map and foldr
checkbool b = if b then 1 else 0

filter_map_foldr checkboolfunc list = total
    where
        truefalselist = map(checkboolfunc) list
        total = foldr(\throughlist n -> n + checkbool throughlist) 0 truefalselist

-- MAP & FOLDR
any_map_foldr :: (a->Bool) -> [a] -> Bool 
any_map_foldr f list = filter_map_foldr f list > 0

all_map_foldr :: (a->Bool) -> [a] -> Bool
all_map_foldr f list = filter_map_foldr f list == length list



-- FILTER
any_filter :: (a->Bool) -> [a] -> Bool
any_filter f list = length (filter f list) > 0

all_filter :: (a->Bool) -> [a] -> Bool
all_filter f list = filter f list == list


------------------------
-- 3 unzip
-- tests:
--      - unzipCustom ([1],[2]) - ([1],[2])
--      - unzipCustom [(123456789,987654321)] - ([123456789],[987654321])
------------------------

unzipCustom :: [(a,b)] -> ([a],[b])
unzipCustom list = foldr (\(a,b) (a_part,b_part) -> (a:a_part, b:b_part)) ([],[]) list

------------------------
-- 4 lengthCustom
-- tests:
--      - lengthCustom "123456789" - 9
--      - lengthFoldr "test" - 4
------------------------

lengthCustom :: [a] -> Integer
lengthCustom = sum . map (\x -> 1)

lengthFoldr :: [a] -> Integer
lengthFoldr = foldr(\x n -> 1 + n) 0

------------------------
-- 5 ff
-- tests:
--      - ff 200 [-6,1,2,3] - 60
--      - ff 34 [3,0,0,-5,1] - 30
------------------------
add_func a b maxNum = if (a+b) <= maxNum then a + b else a

ff:: Integer -> [Integer] -> Integer
ff maxNum list = ((add maxNum) . removeNegativeNums . multiplyByTen) list
    where 
        -- removal
        removeNegativeNums = filter (>=0)
        -- multiplyByTen
        multiplyByTen = map(*10)
        -- add until max
        add maxNum = foldr(\n x -> add_func n x maxNum) 0

------------------------
-- 6 total
-- tests:
--      - total abs 6 - 21
------------------------

total :: (Integer -> Integer) -> Integer -> Integer
total f a = foldr(\x a -> (f x) + a) 0 [0..a]

------------------------
-- 7 iter (recursion, folding)
-- tests:
--      - iter_recursion 5 increment 1 - 6
--      - iter_folding 5 increment 1 - 6
------------------------

increment :: (Integer -> Integer)
increment a = a + 1

iter_recursion n f 
    | n > 0 = f . (iter_recursion (n-1) f) 
    | otherwise = id

iter_folding n f
    | n > 0 = foldr(\x func -> x . func ) f (replicate (n-1) f)
    | otherwise = id


------------------------
-- 8 splits
-- tests:
--      - splits "Test" - [("","Test"),("T","est"),("Te","st"),("Tes","t"),("Test","")]
--      - splits "xyz" - [("","xyz"),("x","yz"),("xy","z"),("xyz","")]
------------------------
splits :: [a] -> [([a],[a])]
splits word = foldr(\x position -> (splitAt x word) : position) [] [0..length_word]
    where 
        length_word = length word
    