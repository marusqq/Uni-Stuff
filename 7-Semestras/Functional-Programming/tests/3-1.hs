module Third_work where
import System.IO

-- 1 ex.
data Shape = Circle Float Float Float | Rectangle Float Float Float Float
overlaps :: Shape -> Shape -> Bool
-- logic taken from https://www.geeksforgeeks.org/check-if-any-point-overlaps-the-given-circle-and-rectangle/
-- Possible overlaps: (Rect, Circle); (Circle, Rect); (Rect, Rect); (Circle, Circle)
checkRectCircleOverlap r xc yc x1 y1 x2 y2 = ((xn - xc)^2 + (yn - yc)^2) <= r * r
  where xn = max x1 (min xc x2)
        yn = max y1 (min yc y2)
		
checkRectanglesOverlap x1 y1 x2 y2 x3 y3 x4 y4 = (xmax < xmin) && (ymax < ymin)
  where xmax = max x1 x3
        ymax = max y1 y3
        xmin = min x2 x4
        ymin = min y2 y4
		
distance x y x1 y1 = sqrt((x-x1)**2 + (y-y1)** 2)  

overlaps (Rectangle x1 y1 x2 y2) (Circle xc yc r) = checkRectCircleOverlap r xc yc x1 y1 x2 y2
overlaps (Circle xc yc r) (Rectangle x1 y1 x2 y2)  = checkRectCircleOverlap r xc yc x1 y1 x2 y2
overlaps (Rectangle x1 y1 x2 y2) (Rectangle x3 y3 x4 y4) = checkRectanglesOverlap x1 y1 x2 y2 x3 y3 x4 y4 
overlaps (Circle xc1 yc1 r) (Circle xc2 yc2 r1) = distance xc1 yc1 xc2 yc2 < r + r1
-- 2 ex.

any1 :: (a->Bool) -> [a] -> Bool
all1 :: (a->Bool) -> [a] -> Bool

-- with filtering
any1 f xs = length (filter f xs ) > 0
all1 f xs = length (filter f xs ) == length xs

-- with map and foldr
any2 :: (a->Bool) -> [a] -> Bool
all2 :: (a->Bool) -> [a] -> Bool

getNumberOfSatystfying func xs = foldr(\x n -> n + (if x then 1 else 0)) 0 getList
  where getList =  map (func) xs

any2 f xs = getNumberOfSatystfying f xs > 0
all2 f xs = getNumberOfSatystfying f xs == length xs

-- 3 ex.

unzip1 :: [(a,b)] -> ([a],[b])

unzip1 xs = foldr f ([],[]) xs
  where f =  \(x,y) (x1,y1) -> (x:x1, y:y1)

--4 ex.
length1 :: [a] -> Integer
lengthWithFoldr :: [a] -> Integer

length1 = sum . map (\x-> 1)
lengthWithFoldr xs = foldr(\x n -> n + 1) 0 xs

-- 5 ex.
ff :: Integer -> [Integer] -> Integer
ff maxNum xs = (sumNumbers . removeNegativeNums . multiplyByTen) xs
  where removeNegativeNums = filter (>=0)
        multiplyByTen = map (*10)
        sumNumbers = foldr (\x sum -> if (sum + x) > maxNum then sum else (sum + x)) 0
		
-- 6 ex.

total :: (Integer -> Integer) -> Integer -> Integer
total f n = foldr(\x n -> (f x) + n) 0 [0..n]

-- 7 ex.
iter n f
  | n > 0 = f . (iter (n-1) f)
  | otherwise = id 
  
iter1 n f 
  | n > 0 = foldr(\x fnc -> x . fnc ) f (replicate (n-1) f)
  | otherwise = id
  
-- 8 ex.
splits :: [a] -> [([a],[a])]
splits str = foldr (\x xs -> xs ++ [(splitAt x str)]) [] [0..(length str)]