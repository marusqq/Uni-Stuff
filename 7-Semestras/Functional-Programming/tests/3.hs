module Trecia_Uzduotis
where
import Data.Char

-----------------------------------------------------------------------------------------------------------------------
-- 1 uzduotis
--overlaps (Circle 1 5 4)(Rectangle 4 10 6 1) 
--is skaidriu
data Shape = Circle Float Float Float | Rectangle Float Float Float Float
    deriving (Show, Ord, Eq)

overlaps :: Shape -> Shape -> Bool

--jei atstumas tarp centru mazesnis uz spinduliu suma
overlaps (Circle x1 y1 r1) (Circle x2 y2 r2) = (sqrt((x1-x2)**2 + (y1-y2)**2)) < r1 + r2

--koordinates centro (x1, y1, x2, y2)
overlaps (Rectangle x1 y1 h1 w1) (Rectangle x2 y2 h2 w2) = not (condition1 || condition2)
    where
        --susirandam kairi virsutini kampa 1 staciakampio
        l1x = x1 - w1 / 2
        l1y = y1 + h1 / 2

        --susirandam kairi virsutini kampa 2 staciakampio
        l2x = x2 - w2 / 2
        l2y = y2 + h2 / 2

        --susirandam desini apatini kampa 1 staciakampio
        r1x = x1 + w1 / 2
        r1y = y1 - h2 / 2
        
        --susirandam desini apatini kampa 2 staciakampio
        r2x = x2 + w2 / 2
        r2y = y2 - h2 / 2

        --pagal x asi
        condition1 = l1x >= r2x || l2x >= r1x
        --pagal y asi
        condition2 = l1y <= r2y || l2y <= r1y
              
        
overlaps (Rectangle x y h w) (Circle x1 y1 r) = condition1
    where
        --kairio virsutinio susiradimas
        l1x = x - w / 2
        l1y = y + h / 2

        --desinio apatinio susiradimas susiradimas
        r1x = x + w / 2
        r1y = y - h / 2

        condition1 = ((x1 - (max l1x (min x1 r1x)))**2 + (y1 - (max r1y (min y1 l1y)))**2) < (r**2)
 
--apsukam, kad nereiktu antra karta rasyti funkcionalumo
overlaps (Circle x1 y1 r) (Rectangle x y h w) = overlaps (Rectangle x y h w) (Circle x1 y1 r)

-----------------------------------------------------------------------------------------------------------------------
-- antra uzduotis
--any1 odd [5,40] 
any1 :: (a->Bool) -> [a] -> Bool
any1 truefalsefunc list = length (filter truefalsefunc list ) > 0

--all odd [5,40]
all1 :: (a->Bool) -> [a] -> Bool
all1 truefalsefunc list = length (filter truefalsefunc list ) == length list

--su map ir foldr
truefalsebool b = if b then 1 else 0

filter1 truefalsefunc list = total
    --map grazina ar elementas atitinka salyga ar ne , sudaro true false lista
  where 
      truefalselist =  map (truefalsefunc) list
      total = foldr(\throughlist n -> n + truefalsebool throughlist) 0 truefalselist

all2:: (a->Bool) -> [a] -> Bool
all2 truefalsefunc list = filter1 truefalsefunc list == length list
        
any2 :: (a->Bool) -> [a] -> Bool
any2 truefalsefunc list = filter1 truefalsefunc list > 0

-----------------------------------------------------------------------------------------------------------------------
-- trecia uzduotis
unzip1:: [(a,b)] -> ([a],[b])
unzip1 list = foldr (\(a,b) (as,bs) -> (a:as, b:bs)) ([],[]) list

-----------------------------------------------------------------------------------------------------------------------
-- ketvirta uzduotis
--naudojant map
length1 :: [a] -> Integer
length1 = sum . map (\x-> 1)

--naudojant foldr
length2 :: [a] -> Integer
length2 = foldr (\x n -> 1 + n) 0

-----------------------------------------------------------------------------------------------------------------------
-- penkta uzduotis
function n x maxvalue= if (n+x) <= maxvalue then n + x else n

ff:: Integer -> [Integer] -> Integer
ff maxvalue list = ( (add maxvalue) . (multiply 10) . (remove)) list
    where
        --salinam
        remove = filter (>=0)
        --dauginam
        multiply ten = map(\x -> x*ten)
        --pridedam iki max
        add maxvalue = foldr(\x n -> function n x maxvalue) 0

-----------------------------------------------------------------------------------------------------------------------
-- sesta uzduotis
-- total abs 10
total:: (Integer -> Integer) -> Integer -> Integer
total integerfunc = \n -> foldl(\x y -> (integerfunc x) + y) 0 [0..n]
-----------------------------------------------------------------------------------------------------------------------
-- septinta uzduotis
iter1 n f
  | n > 0 = f . (iter1 (n-1) f)
  --id identity function
  | otherwise = id

iter2 n f 
  | n > 0 = foldr(\x a -> x . a ) f list
  | otherwise = id
  where 
      list = replicate (n-1) f
  -----------------------------------------------------------------------------------------------------------------------
-- astunta uzduotis
splits :: [a] -> [([a],[a])]

splits list = foldr(\x allpos -> (splitAt x list) : allpos) [] [0..n]
    where 
        n = length list

