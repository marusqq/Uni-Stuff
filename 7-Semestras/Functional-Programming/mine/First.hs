module First
where
import Test.QuickCheck

--1
nAnd :: Bool -> Bool -> Bool
nAnd x y = not x || not y

nAnd2 :: Bool -> Bool -> Bool
nAnd2 x y = not(x&&y)

nAnd3 :: Bool -> Bool -> Bool

nAnd3 True True = False
nAnd3 _ _ = True
--nAnd3 False False = True
--nAnd3 False True = True
--nAnd3 True False = True

--2 
--test_ands1 :: Bool -> Bool -> Bool
testAnds1 :: Bool -> Bool -> Bool
testAnds1 a b  
    | (a == True) && (b == True) = False == (nAnd2 a b)
    | otherwise = True == (nAnd a b)

testAnds2 :: Bool -> Bool -> Bool
testAnds2 a b = (nAnd a b == nAnd3 a b) 
            && (nAnd2 a b == nAnd3 a b)
            && (nAnd a b == nAnd2 a b)

--3
nDigits :: Int -> Int
nDigits num
    |   num >= 0 = length(show num)
    |   num < 0 = nDigits(abs num)

--4
nRoots :: Float -> Float -> Float -> Float
nRoots a b c 
    |   a == 0 = error "the first argument should be non-zero!"
    |   b ^ 2 == 4.0 * c * a = 1
    |   b ^ 2 > 4.0 * c * a = 2
    |   otherwise = 0

--5
smallerRoot :: Float -> Float -> Float -> Float
largerRoot :: Float -> Float -> Float -> Float
--calculateRoots :: Float -> Float

calculateRoots a b c
    |   nRoots a b c == 0 = error "no roots"
    |   otherwise = [((-b) - sqrt(b^2-4*a*c))/2*a, ((-b) + sqrt(b^2-4*a*c))/2*a]
     
smallerRoot a b c = minimum(calculateRoots a b c)
largerRoot a b c = maximum(calculateRoots a b c)

--6
power2 :: Integer -> Integer
power2 number
    |   number == 0 = 1
    |   number < 0 = 0
    |   number > 0 = 2 * power2(number - 1)

--7
mult :: Integer -> Integer -> Integer
mult n m
    |   n == 0 || m == 0 = 0
    |   m < 0 && n < 0 = mult (abs n) (abs m)
    |   m < 0 = mult m n
    |   otherwise = (mult (m - 1) n) + n

--8
prod :: Integer -> Integer -> Integer
prod m n
    |   m > n = error "m must be less than n"
    |   m == n = m
    |   otherwise = n * prod(m) (n-1)

--factorial
fact :: Integer -> Integer
fact 0 = 1
fact x = prod 1 x







