## Сводка

- **A — только PI**: n 80: первым 32, среди трёх 38, cos первого 0.56, лучший из трёх 0.66
- **B — FROM/FOR/PI**: n 80: первым 32, среди трёх 38, cos первого 0.56, лучший из трёх 0.63
- **C — FROM/FOR/LIKE/PI**: n 80: первым 46, среди трёх 51, cos первого 0.71, лучший из трёх 0.76
- **D — коды C, связки → PI**: n 80: первым 31, среди трёх 34, cos первого 0.56, лучший из трёх 0.64
- **наполнители**: n 128: первым 83, среди трёх 105, cos первого 0.80, лучший из трёх 0.90

## По группам слов (слово первым / из n; cos первого)

| группа | A | B | C | D |
|---|---|---|---|---|
| FROM | 8/20; 0.53 | 12/20; 0.70 | 12/20; 0.73 | 6/20; 0.51 |
| FOR | 11/20; 0.64 | 8/20; 0.59 | 13/20; 0.77 | 8/20; 0.57 |
| LIKE | 6/20; 0.45 | 4/20; 0.34 | 9/20; 0.63 | 6/20; 0.46 |
| PI | 7/20; 0.61 | 8/20; 0.60 | 12/20; 0.71 | 11/20; 0.72 |

По кодерам: enc_A_a A — n 40: первым 16, среди трёх 19, cos первого 0.56, лучший из трёх 0.67; enc_A_b A — n 40: первым 16, среди трёх 19, cos первого 0.56, лучший из трёх 0.65; enc_B_a B — n 40: первым 14, среди трёх 18, cos первого 0.53, лучший из трёх 0.61; enc_B_b B — n 40: первым 18, среди трёх 20, cos первого 0.59, лучший из трёх 0.64; enc_C_a C — n 40: первым 25, среди трёх 28, cos первого 0.74, лучший из трёх 0.81; enc_C_b C — n 40: первым 21, среди трёх 23, cos первого 0.68, лучший из трёх 0.72; enc_C_a D — n 40: первым 17, среди трёх 19, cos первого 0.59, лучший из трёх 0.67; enc_C_b D — n 40: первым 14, среди трёх 15, cos первого 0.54, лучший из трёх 0.61

## По словам (cos первого ответа, среднее по декодерам; что прочитано первым)

| слово | A | B | C | D |
|---|---|---|---|---|
| wine | 0.31 (tea, tea, juice, tea) | 0.29 (tea, coffee, tea, tea) | 0.51 (wine, tea, juice, juice) | 0.29 (tea, berry juice, tea, tea) |
| paper | 0.62 (paper, paper, note, label) | 0.54 (paper, paper, pebble, chip) | 0.82 (paper, paper, note, paper) | 0.29 (page, papyrus scroll, page, leaf) |
| cheese | 0.46 (milk, feed, cheese, cereal) | 1.00 (cheese, cheese, cheese, cheese) | 0.73 (cheese, cheese, egg, meat) | 0.62 (cheese, cheese, feed, chicken) |
| leather | 0.57 (skull, bone, leather, leather) | 0.78 (bone, leather, leather, leather) | 0.60 (shell, shell, leather, leather) | 0.45 (shell, shell, leather, skin) |
| candle | 0.70 (match, candle, wax candle, wax candle) | 0.88 (torch, candle, candle, candle) | 1.00 (candle, candle, candle, candle) | 0.88 (candle, candle, candle, torch) |
| key | 0.62 (key, key, pin, pin) | 0.39 (screw, nail, pin, key) | 0.59 (key, key, nail, nail) | 0.56 (key, key, needle, nail) |
| lid | 0.96 (pot lid, lid, lid, lid) | 0.58 (ceiling, ceiling, lid, lid) | 1.00 (lid, lid, lid, lid) | 0.81 (lid, lid, lid, roof) |
| saddle | 0.52 (elevator, loft, saddle, saddle) | 0.65 (stable, stable, saddle, saddle) | 0.29 (stable, stable, stable, stable) | 0.29 (stable, stable, barn, stable) |
| wallet | 0.60 (pocket money, wallet, wallet, watch) | 0.92 (purse, purse, wallet, wallet) | 0.96 (wallet, wallet, purse, wallet) | 0.80 (tag, wallet, wallet, wallet) |
| sheath | 0.53 (pocketknife, pocket knife, sheath, handle) | 0.43 (flesh, butter, blade, sheath) | 1.00 (sheath, sheath, sheath, sheath) | 0.37 (scalpel, pocket knife, handle, penknife) |
| starfish | 0.23 (fish, fish, whale, milk) | 0.28 (fish, fish, shoal, fish) | 0.29 (sunfish, sunfish, whale, sunfish) | 0.30 (lizard, sunbird, seabird, whale) |
| seahorse | 0.60 (seahorse, seahorse, venom, plankton) | 0.02 (venom, flea, blood, blood) | 0.70 (porpoise, seahorse, minnow, seahorse) | 0.38 (seahorse, horse saliva, venom, minnow) |
| jellyfish | 0.53 (jellyfish, jellyfish, milk, milk) | 0.85 (fish, jellyfish, jellyfish, jellyfish) | 0.79 (jellyfish, caterpillar, jellyfish, jellyfish) | 0.30 (balloon, feather, cream, jellyfish) |
| catfish | 0.31 (eel, worm, eel, venom) | 0.19 (eel, tapeworm, venom, blood) | 0.38 (jellyfish, jellyfish, eel, eel) | 0.32 (jellyfish, tadpole, eel, worm) |
| sunflower | 0.56 (treetop, tree, sunflower, sunflower) | 0.35 (treetop, sunflower, tree, tree) | 1.00 (sunflower, sunflower, sunflower, sunflower) | 1.00 (sunflower, sunflower, sunflower, sunflower) |
| roof | 1.00 (roof, roof, roof, roof) | 0.81 (roof, roof, ceiling, ceiling) | 1.00 (roof, roof, roof, roof) | 1.00 (roof, roof, roof, roof) |
| petal | 0.55 (leaf, leaf, petal, leaf) | 0.61 (petal, petal, seed, seed) | 0.92 (flower, petal, petal, petal) | 0.84 (bud, petal, petal, petal) |
| hoof | 0.65 (hoof, hoof, claw, claw) | 0.65 (hoof, hoof, bone, tooth) | 0.83 (bone, hoof, hoof, hoof) | 1.00 (hoof, hoof, hoof, hoof) |
| nest | 0.44 (birdhouse, aviary, cage, birdcage) | 0.67 (cage, birdcage, nest, nest) | 0.58 (nest, nest, maternity ward, maternity ward) | 0.46 (birdhouse, birdhouse, incubator, hatchery) |
| yolk | 0.41 (blood, milk, egg, embryo) | 0.25 (organ, organ, embryo, embryo) | 0.24 (embryo, embryo, pupil, pupil) | 0.29 (embryo, womb, retina, embryo) |
