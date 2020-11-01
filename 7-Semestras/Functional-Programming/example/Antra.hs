module Antra_Uzduotis
where 
import Data.Char

-- Ketvirta užduotis
salinam :: [Integer] -> Integer -> [Integer]
salinam [] _ = []
salinam (antras:antraslikes) pirmas
   | pirmas == antras = salinam antraslikes pirmas
   | otherwise = antras:(salinam antraslikes pirmas)

permut :: [Integer] -> [Integer] -> Bool
permut [] [] = True
permut (pirmas) (antras:antraslikes)
    |length(pirmas) /= length(antraslikes) + 1 = False
    |otherwise = permut (tail pirmas) (salinam (antras:antraslikes) (head pirmas))


-- Šešta užduotis
itemTotal :: [(String, Float)] -> [(String, Float)]
itemTotal [] = []
itemTotal [pora] = [pora]
itemTotal (pora:likusiosporos) = sudedam pora (itemTotal likusiosporos)

sudedam :: (String, Float) -> [(String, Float)] -> [(String, Float)]
sudedam pora [] = [pora]
sudedam pora (kitapora:darlikusios)
  | fst pora == fst kitapora = (fst pora, snd pora + snd kitapora):darlikusios --fst pirma itema grazina is tuple, snd antra
  | otherwise = kitapora : sudedam pora darlikusios


itemDiscount :: String -> Integer -> [(String, Float)] -> [(String, Float)]
itemDiscount _ _ [] = []
itemDiscount pavadinimas nuolaida (preke:kitosprekes)
  | nuolaida < 0 || nuolaida > 100 = error "nuolaida tik tarp 0 ir 100%"
  | pavadinimas == fst preke = (fst preke, snd preke * (100 - fromIntegral(nuolaida))/100) : itemDiscount pavadinimas nuolaida kitosprekes
  | otherwise = preke : itemDiscount pavadinimas nuolaida kitosprekes
