module Main where

--main = print $ head $ filter (\x->snd x==84) $ zip [2..] $ map (\x->mod (x^1985) 33067) [2..]
main = print $ mod (1985^33067) 84

