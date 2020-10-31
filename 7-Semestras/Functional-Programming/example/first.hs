module first where
import System.IO

main = do
    print(smallerRoot 1.0 2.0 4.0)
    print(largerRoot 1.0 2.0 4.0)
    print(nRoots 1.0 1.0 1.0)
    print(power2 10)
    print(mult 5 100)
    print(prod 3 5)

-- 1 ex.
-- First nAnd
nAnd :: Bool -> Bool -> Bool
nAnd x y = not(x && y)

-- Second nAnd
nAnd1 True x = not (x)
nAnd1 False x = not (x) -- pakeisti

-- Third nAnd
nAnd2 True True = False
nAnd2 True False = True
nAnd2 False True = True
nAnd2 False False = True

-- 2 ex.


-- 3 ex.
nDigits ::Integer -> Int 
nDigits number 
    |  number >= 0 = length(show number)
    |  number < 0 = nDigits(abs number)

-- 4 ex.
nRoots::Float -> Float -> Float -> Int
nRoots a b c
    | a == 0.0 = error "the first argument should be non-zero!"
    | bPow > d = 2
    | bPow == d = 1
    | bPow < d = 0
    where d = 4.0 * a * c; bPow = b^2

-- 5 ex.
smallerRoot::Float->Float->Float->Float
largerRoot::Float->Float->Float->Float

getRoot::Float->Float->Float->Float
getRoot a b c
    | nRoots a b c < 0 = error "No roots found" -- panaudoti nRoots su 0 1 2 
    | nRoots a b c >= 0 = sqrt d
    where d = b^2 - 4 * a * c

getResults a b c = [((-b) - getRoot a b c) / (2 * a), ((-b) + getRoot a b c) / (2 * a)]

smallerRoot a b c = minimum(getResults a b c)
largerRoot a b c = maximum(getResults a b c)

-- 6 ex.
power2::Integer->Integer
power2 number
    | number < 0 = 0
    | number == 0 = 1
    | number > 0 = 2 * power2(number - 1)

-- 7 ex.
mult::Integer->Integer->Integer
mult m n
    | n < 0 = mult (negate m) (abs n)
    | n > 0 = m + mult m (n-1)
	| n == 0 = 0

-- 8 ex.
prod::Integer->Integer->Integer
prod m n
    | m > n = error "m can't be bigger than n!" --patikrinti su -100 ; 100
	| m == n = m
	| m < n = m * prod (m+1) n