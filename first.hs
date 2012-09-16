module Main where

main = print $ head $ filter (\x->snd x==915) $ zip [2..] $ map (\x->mod (x^17) 3569) [2..]

