# WoW Forever recipe data (from the Crafter's Journal addon)

Raw Lua data files, one block per profession. Source: Crafter's Journal `Data/*.lua` (generated from the Forever client DB2 data, CMaNGOS trainers, QuestieDB vendors). The files are unmodified except for this header. Comments in the files are in Spanish; translations of the schema are below.

## Schema (per recipe, keyed by crafting spell ID)

`ES.Data.<Profession>.recipes[spellID] = { ... }`

| field | meaning |
|---|---|
| `name` | recipe / product name |
| `t = {a,b,c,d}` | skill thresholds: orange, yellow, green, grey |
| `train` | skill required to learn it from a trainer |
| `fee` | trainer price in copper (if absent, the recipe is learned from an item, see `scroll`) |
| `scroll` | item ID of the recipe item (Plans/Pattern/Formula...) that teaches it |
| `scrollPrice` | price in copper if a vendor NPC sells the recipe item |
| `sq` / `oq` | item quality of the recipe item / of the crafted item (0 poor, 1 common, 2 uncommon, 3 rare, 4 epic) |
| `r = {{itemID, qty}, ...}` | reagents |
| `out = {itemID, qty}` | crafted item and quantity |
| `tool` | required tool item ID |
| `bop = true` | crafted item binds on pickup (cannot be sold on the AH, vendor only) |
| `faction` | faction that can learn it, if only one |
| `rep = {faction, level}` | reputation needed for the recipe item (5 friendly, 6 honored, 7 revered, 8 exalted) |
| `tr = {npcIDs}` | trainer NPC IDs that teach it |

Each file also defines, in the same format at the bottom:
- `ES.Data.ItemNames[itemID] = "name"`
- `ES.Data.VendorPrices[itemID] = copper` (price when BUYING from a vendor)
- `ES.Data.SellPrices[itemID] = copper` (price when SELLING to a vendor)
- `ES.Data.GatheredBy[itemID] = ...` (gathering source)
- `ES.Data.Tools[...]`

Money is in copper (100c = 1s, 10000c = 1g). Not included: auction prices (those come from TSM at runtime) and `Data/Sources.lua` (plan drop/vendor sources, NPC IDs only).


---

## Alchemy

```lua
-- Generado por tools/gen_profession.py (Alchemy). No editar a mano.
-- Datos: cliente de WoW Forever (wago.tools DB2), instructores de CMaNGOS classic-db, vendedores de QuestieDB.
local _, ES = ...
ES.Data = ES.Data or {}

-- t = { naranja, amarilla, verde, gris }; fee/train = precio y habilidad del instructor
-- (sin fee = se aprende de pergamino: de dónde sale, en Data/Sources.lua; scrollPrice = su precio si lo vende un PNJ)
-- rep = { facción, nivel } que pide el pergamino para aprenderla (5 amistoso, 6 honorable, 7 venerado, 8 exaltado)
-- r = { {itemID, cantidad} }; out = { itemID, cantidad }
-- sq / oq = calidad del pergamino / de lo fabricado (0 pobre, 1 común, 2 poco común, 3 raro, 4 épico)
-- faction = bando que puede aprenderla, si solo es de uno
-- bop = lo fabricado se liga al recogerlo: no se puede vender en la AH (sí al vendedor)
-- favor / favorRep = se compra con Merchant's Favor en el campamento de tu bando, y la reputación que pide
-- train ajustado a Forever: nivel de Classic menos lo que Forever bajó la amarilla de esa receta
-- basic = se aprende sola al coger la profesión; trainer = de instructor sin precio conocido
--   (receta nueva de Forever que no está en CMaNGOS: se aprende al ponerse amarilla)
ES.Data.Alchemy = {
  skillLine = 171,
  ranks = { -- { tope, precio, habilidad requerida, nivel de personaje }
    { 150, 450, 50, 10 },
    { 225, 5000, 125, 20 },
    { 300, 45000, 200, 35 },
  },
  -- { PNJ instructor, rangos que enseña: 1 aprendiz (75), 2 oficial (150), 4 experto (225), 8 artesano (300) }
  trainers = { { 1215, 1 }, { 1246, 1 }, { 1386, 8 }, { 1470, 1 }, { 2132, 1 }, { 2391, 2 }, { 2837, 2 }, { 3009, 2 }, { 3184, 1 }, { 3347, 2 }, { 3603, 1 }, { 3964, 2 }, { 4160, 4 }, { 4609, 2 }, { 4611, 4 }, { 4900, 2 }, { 5177, 2 }, { 5499, 2 }, { 5500, 1 }, { 7948, 8 }, { 11041, 1 }, { 11042, 2 }, { 11044, 1 }, { 11046, 1 }, { 11047, 1 }, { 246793, 4 }, { 246795, 4 }, { 253004, 1 }, { 257005, 1 }, { 257019, 1 }, { 259585, 8 }, { 275322, 4 } },
  recipes = {
    [2329] = { name = "Elixir of Minor Strength", t = { 1, 55, 75, 95 }, fee = 50, train = 15, r = { { 2449, 1 }, { 765, 1 }, { 3371, 1 } }, out = { 2454, 1 }, oq = 1 },
    [2331] = { name = "Minor Mana Potion", t = { 1, 65, 85, 105 }, fee = 90, train = 25, r = { { 785, 1 }, { 2447, 1 }, { 3371, 1 } }, out = { 2455, 1 }, oq = 1 },
    [2333] = { name = "Elixir of Lesser Agility", t = { 1, 165, 185, 205 }, scroll = 3396, train = 140, sq = 2, r = { { 3355, 1 }, { 2452, 1 }, { 3372, 1 } }, out = { 3390, 1 }, oq = 1 },
    [2365] = { name = "Draught of Tongues", t = { 1, 100, 120, 140 }, scroll = 2556, train = 90, sq = 1, r = { { 2449, 2 }, { 785, 2 }, { 3371, 1 } }, out = { 2460, 1 }, oq = 1 },
    [3170] = { name = "Minor Troll's Blood Elixir", t = { 1, 60, 80, 100 }, fee = 50, train = 15, r = { { 2447, 1 }, { 2449, 2 }, { 3371, 1 } }, out = { 3382, 1 }, oq = 1 },
    [3171] = { name = "Elixir of Wisdom", t = { 1, 120, 140, 160 }, fee = 500, train = 90, r = { { 785, 1 }, { 2450, 2 }, { 3371, 1 } }, out = { 3383, 1 }, oq = 1 },
    [3172] = { name = "Minor Magic Resistance Potion", t = { 1, 135, 155, 175 }, scroll = 3393, train = 110, sq = 1, r = { { 785, 3 }, { 3355, 1 }, { 3371, 1 } }, out = { 3384, 1 }, oq = 1 },
    [3173] = { name = "Lesser Mana Potion", t = { 1, 145, 165, 185 }, fee = 1500, train = 120, r = { { 785, 1 }, { 3820, 1 }, { 3371, 1 } }, out = { 3385, 1 }, oq = 1 },
    [3174] = { name = "Potion of Poison Cleansing", t = { 1, 145, 165, 185 }, scroll = 3394, train = 120, sq = 1, r = { { 1288, 1 }, { 2453, 1 }, { 3372, 1 } }, out = { 3386, 1 }, oq = 1 },
    [3175] = { name = "Limited Invulnerability Potion", t = { 1, 275, 295, 315 }, scroll = 3395, train = 250, sq = 2, r = { { 8839, 2 }, { 8845, 1 }, { 8925, 1 } }, out = { 3387, 1 }, oq = 1 },
    [3176] = { name = "Lesser Troll's Blood Elixir", t = { 1, 150, 170, 190 }, fee = 1500, train = 125, r = { { 2453, 2 }, { 2450, 2 }, { 3372, 1 } }, out = { 3388, 1 }, oq = 1 },
    [3177] = { name = "Elixir of Lesser Defense", t = { 1, 155, 175, 195 }, fee = 2000, train = 130, r = { { 3355, 1 }, { 3820, 1 }, { 3372, 1 } }, out = { 3389, 1 }, oq = 1 },
    [3188] = { name = "Elixir of Ogre Strength", t = { 1, 175, 195, 215 }, scroll = 6211, train = 150, sq = 1, r = { { 2449, 1 }, { 3356, 1 }, { 3372, 1 } }, out = { 3391, 1 }, oq = 1 },
    [3230] = { name = "Elixir of Minor Agility", t = { 1, 80, 100, 120 }, scroll = 2553, train = 50, sq = 2, r = { { 2452, 1 }, { 765, 1 }, { 3371, 1 } }, out = { 2457, 1 }, oq = 1 },
    [3448] = { name = "Lesser Invisibility Potion", t = { 1, 185, 205, 225 }, fee = 5000, train = 165, r = { { 3818, 1 }, { 3355, 1 }, { 3372, 1 } }, out = { 3823, 1 }, oq = 1 },
    [3449] = { name = "Shadow Oil", t = { 1, 190, 210, 230 }, scroll = 6068, train = 165, scrollPrice = 1500, sq = 1, r = { { 3818, 4 }, { 3369, 4 }, { 3372, 1 } }, out = { 3824, 2 }, oq = 1 },
    [3450] = { name = "Elixir of Lesser Fortitude", t = { 1, 195, 215, 235 }, fee = 6000, train = 175, r = { { 3355, 1 }, { 3821, 1 }, { 3372, 1 } }, out = { 3825, 1 }, oq = 1 },
    [3451] = { name = "Troll's Blood Elixir", t = { 1, 200, 220, 240 }, scroll = 3831, train = 180, sq = 1, r = { { 3357, 1 }, { 2453, 1 }, { 3372, 1 } }, out = { 3826, 1 }, oq = 1 },
    [3452] = { name = "Mana Potion", t = { 1, 180, 200, 220 }, fee = 5000, train = 160, r = { { 3820, 1 }, { 3356, 1 }, { 3372, 1 } }, out = { 3827, 1 }, oq = 1 },
    [3453] = { name = "Draught of Detect Lesser Invisibility", t = { 1, 215, 235, 255 }, scroll = 3832, train = 195, sq = 2, r = { { 3358, 1 }, { 3818, 1 }, { 3372, 1 } }, out = { 3828, 1 }, oq = 1 },
    [3454] = { name = "Frost Oil", t = { 1, 220, 240, 260 }, scroll = 14634, train = 200, scrollPrice = 2500, sq = 2, r = { { 3358, 4 }, { 3819, 2 }, { 3372, 1 } }, out = { 3829, 2 }, oq = 1 },
    [4508] = { name = "Minor Discolored Healing Potion", t = { 1, 55, 75, 95 }, fee = 10, train = 50, tr = { 1937, 249713 }, r = { { 3371, 1 }, { 2447, 1 }, { 730, 1 } }, out = { 4596, 1 }, oq = 1 },
    [4942] = { name = "Lesser Stoneshield Potion", t = { 1, 230, 250, 270 }, scroll = 4624, train = 215, sq = 1, r = { { 3858, 1 }, { 3821, 1 }, { 3372, 1 } }, out = { 4623, 1 }, oq = 1 },
    [6617] = { name = "Rage Potion", t = { 1, 90, 110, 130 }, scroll = 5640, train = 60, scrollPrice = 100, sq = 1, r = { { 5635, 1 }, { 2450, 1 }, { 3371, 1 } }, out = { 5631, 1 }, oq = 1 },
    [6618] = { name = "Great Rage Potion", t = { 1, 195, 215, 235 }, scroll = 5643, train = 175, scrollPrice = 2000, sq = 1, r = { { 5637, 1 }, { 3356, 1 }, { 3372, 1 } }, out = { 5633, 1 }, oq = 1 },
    [6624] = { name = "Free Action Potion", t = { 1, 175, 195, 215 }, scroll = 5642, train = 150, scrollPrice = 1800, sq = 1, r = { { 6370, 2 }, { 3820, 1 }, { 3372, 1 } }, out = { 5634, 1 }, oq = 1 },
    [7179] = { name = "Draught of Water Breathing", t = { 1, 120, 140, 160 }, fee = 450, train = 90, r = { { 3820, 1 }, { 6370, 2 }, { 3371, 1 } }, out = { 5996, 1 }, oq = 1 },
    [7183] = { name = "Elixir of Minor Defense", t = { 1, 55, 75, 95 }, basic = true, r = { { 765, 1 }, { 2447, 1 }, { 3371, 1 } }, out = { 5997, 1 }, oq = 1 },
    [7255] = { name = "Holy Protection Potion", t = { 1, 130, 150, 170 }, scroll = 6053, train = 100, scrollPrice = 800, sq = 1, r = { { 2453, 1 }, { 2452, 1 }, { 3371, 1 } }, out = { 6051, 1 }, oq = 1 },
    [7256] = { name = "Shadow Protection Potion", t = { 1, 160, 180, 200 }, scroll = 6054, train = 135, scrollPrice = 900, sq = 1, r = { { 3369, 1 }, { 3356, 1 }, { 3372, 1 } }, out = { 6048, 1 }, oq = 1 },
    [7257] = { name = "Fire Protection Potion", t = { 1, 210, 230, 250 }, scroll = 6055, train = 165, scrollPrice = 1500, sq = 1, r = { { 4402, 1 }, { 6371, 1 }, { 3372, 1 } }, out = { 6049, 1 }, oq = 1 },
    [7258] = { name = "Frost Protection Potion", t = { 1, 205, 225, 245 }, scroll = 6056, train = 190, scrollPrice = 2000, sq = 1, r = { { 3819, 1 }, { 3821, 1 }, { 3372, 1 } }, out = { 6050, 1 }, oq = 1 },
    [7259] = { name = "Nature Protection Potion", t = { 1, 210, 230, 250 }, scroll = 6057, train = 190, scrollPrice = 2000, sq = 1, r = { { 3357, 1 }, { 3820, 1 }, { 3372, 1 } }, out = { 6052, 1 }, oq = 1 },
    [7836] = { name = "Blackmouth Oil", t = { 1, 80, 90, 100 }, fee = 250, train = 80, r = { { 6358, 2 }, { 3371, 1 } }, out = { 6370, 1 }, oq = 1 },
    [7837] = { name = "Fire Oil", t = { 1, 150, 160, 170 }, fee = 1000, train = 130, r = { { 6359, 2 }, { 3371, 1 } }, out = { 6371, 2 }, oq = 1 },
    [7841] = { name = "Swim Speed Potion", t = { 1, 130, 150, 170 }, fee = 1000, train = 100, r = { { 2452, 1 }, { 6370, 1 }, { 3371, 1 } }, out = { 6372, 1 }, oq = 1 },
    [7845] = { name = "Elixir of Fire Power", t = { 1, 165, 185, 205 }, fee = 3000, train = 140, r = { { 6371, 2 }, { 3356, 1 }, { 3372, 1 } }, out = { 6373, 1 }, oq = 1 },
    [8240] = { name = "Elixir of Giant Growth", t = { 1, 120, 140, 160 }, scroll = 6663, train = 90, sq = 2, r = { { 6522, 1 }, { 2449, 1 }, { 3371, 1 } }, out = { 6662, 1 }, oq = 1 },
    [11447] = { name = "Draught of Water Walking", t = { 1, 190, 210, 230 }, scroll = 288206, train = 180, sq = 1, r = { { 6370, 1 }, { 3357, 1 }, { 3372, 1 } }, out = { 8827, 1 }, oq = 1 },
    [11448] = { name = "Greater Mana Potion", t = { 1, 220, 240, 260 }, fee = 9000, train = 205, r = { { 3358, 1 }, { 3821, 1 }, { 3372, 1 } }, out = { 6149, 1 }, oq = 1 },
    [11449] = { name = "Elixir of Agility", t = { 1, 205, 225, 245 }, fee = 6500, train = 185, r = { { 3820, 1 }, { 3821, 1 }, { 3372, 1 } }, out = { 8949, 1 }, oq = 1 },
    [11450] = { name = "Elixir of Defense", t = { 1, 215, 235, 255 }, fee = 7500, train = 195, r = { { 3355, 1 }, { 3821, 1 }, { 3372, 1 } }, out = { 8951, 1 }, oq = 1 },
    [11451] = { name = "Oil of Immolation", t = { 1, 220, 240, 260 }, fee = 8000, train = 205, r = { { 4625, 1 }, { 3821, 1 }, { 8925, 1 } }, out = { 8956, 1 }, oq = 1 },
    [11452] = { name = "Restorative Potion", t = { 1, 225, 245, 265 }, r = { { 7067, 1 }, { 3821, 1 }, { 8925, 1 } }, out = { 9030, 1 }, oq = 1 },
    [11453] = { name = "Magic Resistance Potion", t = { 1, 225, 245, 265 }, scroll = 9293, train = 210, sq = 2, r = { { 3358, 1 }, { 8831, 1 }, { 8925, 1 } }, out = { 9036, 1 }, oq = 1 },
    [11456] = { name = "Goblin Rocket Fuel", t = { 1, 225, 245, 265 }, scroll = 10644, train = 210, sq = 1, r = { { 4625, 1 }, { 9260, 1 }, { 3372, 1 } }, out = { 9061, 2 }, oq = 1 },
    [11458] = { name = "Wildvine Potion", t = { 1, 225, 237, 250 }, scroll = 9294, train = 225, sq = 2, r = { { 8153, 1 }, { 8831, 1 }, { 8925, 1 } }, out = { 9144, 1 }, oq = 1 },
    [11459] = { name = "Philosopher's Stone", t = { 1, 240, 260, 280 }, scroll = 9303, train = 225, scrollPrice = 8000, sq = 1, r = { { 3575, 4 }, { 9262, 1 }, { 8831, 4 }, { 4625, 4 } }, out = { 9149, 1 }, oq = 1, bop = true },
    [11460] = { name = "Draught of Detect Undead", t = { 1, 245, 265, 285 }, fee = 5000, train = 230, r = { { 8836, 1 }, { 8925, 1 } }, out = { 9154, 1 }, oq = 1 },
    [11461] = { name = "Arcane Elixir", t = { 1, 250, 270, 290 }, fee = 10000, train = 235, r = { { 8839, 1 }, { 3821, 1 }, { 8925, 1 } }, out = { 9155, 1 }, oq = 1 },
    [11464] = { name = "Invisibility Potion", t = { 1, 250, 270, 290 }, scroll = 9295, train = 235, sq = 2, r = { { 8845, 1 }, { 8838, 1 }, { 8925, 1 } }, out = { 9172, 1 }, oq = 1 },
    [11465] = { name = "Elixir of Greater Intellect", t = { 1, 250, 270, 290 }, fee = 12000, train = 235, r = { { 8839, 1 }, { 3358, 1 }, { 8925, 1 } }, out = { 9179, 1 }, oq = 1 },
    [11466] = { name = "Gift of Arthas", t = { 1, 255, 275, 295 }, scroll = 9296, train = 240, sq = 2, r = { { 8836, 1 }, { 8839, 1 }, { 8925, 1 } }, out = { 9088, 1 }, oq = 1 },
    [11467] = { name = "Elixir of Greater Agility", t = { 1, 255, 275, 295 }, fee = 12000, train = 240, r = { { 8838, 1 }, { 3821, 1 }, { 8925, 1 } }, out = { 9187, 1 }, oq = 1 },
    [11468] = { name = "Draught of Dream Vision", t = { 1, 255, 275, 295 }, scroll = 9297, train = 240, sq = 2, r = { { 8831, 3 }, { 8925, 1 } }, out = { 9197, 1 }, oq = 1 },
    [11472] = { name = "Elixir of Greater Strength", t = { 1, 260, 280, 300 }, scroll = 9298, train = 245, sq = 2, r = { { 8838, 1 }, { 8846, 1 }, { 8925, 1 } }, out = { 9206, 1 }, oq = 1 },
    [11473] = { name = "Ghost Dye", t = { 1, 260, 280, 300 }, scroll = 9302, train = 245, scrollPrice = 9000, sq = 1, r = { { 8845, 2 }, { 4342, 1 }, { 8925, 1 } }, out = { 9210, 2 }, oq = 1 },
    [11476] = { name = "Elixir of Shadow Power", t = { 1, 265, 285, 305 }, scroll = 9301, train = 250, scrollPrice = 10000, sq = 2, r = { { 8845, 3 }, { 8925, 1 } }, out = { 9264, 1 }, oq = 1 },
    [11477] = { name = "Potion of Demon Slaying", t = { 1, 265, 285, 305 }, scroll = 9300, train = 250, scrollPrice = 10000, sq = 1, r = { { 8846, 1 }, { 8845, 1 }, { 8925, 1 } }, out = { 9224, 1 }, oq = 1 },
    [11478] = { name = "Draught of Detect Demon", t = { 1, 265, 285, 305 }, fee = 14000, train = 250, r = { { 8846, 2 }, { 8925, 1 } }, out = { 9233, 1 }, oq = 1 },
    [11479] = { name = "Transmute: Iron to Gold", t = { 1, 240, 260, 280 }, fee = 2500, train = 225, tr = { 3137, 4254 }, r = { { 3575, 1 } }, tool = 12, out = { 3577, 1 }, oq = 2 },
    [11480] = { name = "Transmute: Mithril to Truesilver", t = { 1, 240, 260, 280 }, fee = 10000, train = 225, tr = { 3137, 4254 }, r = { { 3860, 1 } }, tool = 12, out = { 6037, 1 }, oq = 2 },
    [12609] = { name = "Catseye Draught", t = { 1, 220, 240, 260 }, fee = 8000, train = 200, r = { { 3821, 1 }, { 3818, 1 }, { 3372, 1 } }, out = { 10592, 1 }, oq = 1 },
    [15833] = { name = "Dreamless Sleep Potion", t = { 1, 245, 265, 285 }, fee = 10000, train = 230, r = { { 8831, 3 }, { 8925, 1 } }, out = { 12190, 1 }, oq = 1 },
    [17187] = { name = "Transmute: Arcanite", t = { 1, 275, 282, 290 }, scroll = 12958, train = 275, scrollPrice = 50000, sq = 1, r = { { 12359, 1 }, { 12363, 1 } }, tool = 12, out = { 12360, 1 }, oq = 2 },
    [17551] = { name = "Stonescale Oil", t = { 1, 250, 255, 260 }, fee = 15000, train = 250, r = { { 13422, 1 }, { 3372, 1 } }, out = { 13423, 2 }, oq = 1 },
    [17552] = { name = "Mighty Rage Potion", t = { 1, 270, 290, 310 }, scroll = 13476, train = 255, sq = 2, r = { { 8846, 3 }, { 8925, 1 } }, out = { 13442, 1 }, oq = 1 },
    [17553] = { name = "Superior Mana Potion", t = { 1, 275, 295, 315 }, scroll = 13477, train = 260, scrollPrice = 12000, sq = 1, r = { { 8838, 2 }, { 8839, 2 }, { 8925, 1 } }, out = { 13443, 1 }, oq = 1 },
    [17554] = { name = "Elixir of Greater Defense", t = { 1, 280, 300, 320 }, scroll = 13478, train = 265, scrollPrice = 13000, sq = 1, r = { { 13423, 2 }, { 8838, 1 }, { 8925, 1 } }, out = { 13445, 1 }, oq = 1 },
    [17555] = { name = "Elixir of the Sages", t = { 1, 285, 305, 325 }, scroll = 13479, train = 270, sq = 2, r = { { 13463, 1 }, { 13466, 2 }, { 8925, 1 } }, out = { 13447, 1 }, oq = 1 },
    [17557] = { name = "Elixir of Brute Force", t = { 1, 290, 310, 330 }, scroll = 13481, train = 275, sq = 2, r = { { 8846, 2 }, { 13466, 2 }, { 8925, 1 } }, out = { 13453, 1 }, oq = 1 },
    [17559] = { name = "Transmute: Air to Fire", t = { 1, 275, 282, 290 }, scroll = 13482, train = 275, scrollPrice = 15000, rep = { 529, 5 }, sq = 2, r = { { 7082, 1 } }, tool = 12, out = { 7078, 1 }, oq = 2 },
    [17560] = { name = "Transmute: Fire to Earth", t = { 1, 275, 282, 290 }, scroll = 13483, train = 275, sq = 2, r = { { 7078, 1 } }, tool = 12, out = { 7076, 1 }, oq = 2 },
    [17561] = { name = "Transmute: Earth to Water", t = { 1, 275, 282, 290 }, scroll = 13484, train = 275, scrollPrice = 15000, rep = { 576, 4 }, sq = 2, r = { { 7076, 1 } }, tool = 12, out = { 7080, 1 }, oq = 2 },
    [17562] = { name = "Transmute: Water to Air", t = { 1, 275, 282, 290 }, scroll = 13485, train = 275, scrollPrice = 15000, sq = 2, r = { { 7080, 1 } }, tool = 12, out = { 7082, 1 }, oq = 2 },
    [17563] = { name = "Transmute: Undeath to Water", t = { 1, 275, 282, 290 }, scroll = 13486, train = 275, sq = 2, r = { { 12808, 1 } }, tool = 12, out = { 7080, 1 }, oq = 2 },
    [17564] = { name = "Transmute: Water to Undeath", t = { 1, 275, 282, 290 }, scroll = 13487, train = 275, sq = 2, r = { { 7080, 1 } }, tool = 12, out = { 12808, 1 }, oq = 2 },
    [17565] = { name = "Transmute: Life to Earth", t = { 1, 275, 282, 290 }, scroll = 13488, train = 275, sq = 2, r = { { 12803, 1 } }, tool = 12, out = { 7076, 1 }, oq = 2 },
    [17566] = { name = "Transmute: Earth to Life", t = { 1, 275, 282, 290 }, scroll = 13489, train = 275, sq = 2, r = { { 7076, 1 } }, tool = 12, out = { 12803, 1 }, oq = 2 },
    [17570] = { name = "Greater Stoneshield Potion", t = { 1, 295, 315, 335 }, scroll = 13490, train = 280, sq = 2, r = { { 13423, 3 }, { 10620, 1 }, { 8925, 1 } }, out = { 13455, 1 }, oq = 1 },
    [17571] = { name = "Elixir of the Mongoose", t = { 1, 295, 315, 335 }, scroll = 13491, train = 280, sq = 2, r = { { 13465, 2 }, { 13466, 2 }, { 8925, 1 } }, out = { 13452, 1 }, oq = 1 },
    [17572] = { name = "Purification Potion", t = { 1, 300, 320, 340 }, scroll = 13492, train = 285, sq = 2, r = { { 13467, 2 }, { 13466, 2 }, { 8925, 1 } }, out = { 13462, 1 }, oq = 1 },
    [17573] = { name = "Greater Arcane Elixir", t = { 1, 300, 320, 340 }, scroll = 13493, train = 285, sq = 2, r = { { 13463, 3 }, { 13465, 1 }, { 8925, 1 } }, out = { 13454, 1 }, oq = 1 },
    [17574] = { name = "Greater Fire Protection Potion", t = { 1, 305, 325, 345 }, scroll = 13494, train = 290, sq = 2, r = { { 7068, 1 }, { 13463, 1 }, { 8925, 1 } }, out = { 13457, 1 }, oq = 1 },
    [17575] = { name = "Greater Frost Protection Potion", t = { 1, 305, 325, 345 }, scroll = 13495, train = 290, sq = 2, r = { { 7070, 1 }, { 13463, 1 }, { 8925, 1 } }, out = { 13456, 1 }, oq = 1 },
    [17576] = { name = "Greater Nature Protection Potion", t = { 1, 305, 325, 345 }, scroll = 13496, train = 290, sq = 2, r = { { 7067, 1 }, { 13463, 1 }, { 8925, 1 } }, out = { 13458, 1 }, oq = 1 },
    [17577] = { name = "Greater Arcane Protection Potion", t = { 1, 305, 325, 345 }, scroll = 13497, train = 290, sq = 2, r = { { 11176, 1 }, { 13463, 1 }, { 8925, 1 } }, out = { 13461, 1 }, oq = 1 },
    [17578] = { name = "Greater Shadow Protection Potion", t = { 1, 305, 325, 345 }, scroll = 13499, train = 290, sq = 2, r = { { 3824, 1 }, { 13463, 1 }, { 8925, 1 } }, out = { 13459, 1 }, oq = 1 },
    [17579] = { name = "Greater Holy Protection Potion", t = { 1, 305, 325, 345 }, scroll = 13500, train = 290, sq = 2, r = { { 7069, 1 }, { 13463, 1 }, { 8925, 1 } }, out = { 13460, 1 }, oq = 1 },
    [17580] = { name = "Major Mana Potion", t = { 1, 310, 330, 350 }, scroll = 13501, train = 295, scrollPrice = 30000, sq = 2, r = { { 13463, 3 }, { 13467, 2 }, { 8925, 1 } }, out = { 13444, 1 }, oq = 1 },
    [17632] = { name = "Alchemist's Stone", t = { 1, 315, 322, 330 }, scroll = 13517, train = 275, scrollPrice = 40000, sq = 1, r = { { 7078, 8 }, { 7076, 8 }, { 7082, 8 }, { 7080, 8 }, { 12803, 8 }, { 9262, 2 }, { 13468, 4 } }, out = { 13503, 1 }, oq = 2, bop = true },
    [17634] = { name = "Flask of Petrification", t = { 1, 315, 322, 330 }, scroll = 13518, train = 300, scrollPrice = 40000, sq = 2, r = { { 13423, 30 }, { 13465, 10 }, { 13468, 1 }, { 8925, 1 } }, tool = 12, out = { 13506, 1 }, oq = 1 },
    [17635] = { name = "Flask of the Titans", t = { 1, 315, 322, 330 }, scroll = 13519, train = 300, scrollPrice = 40000, sq = 2, r = { { 8846, 30 }, { 13423, 10 }, { 13468, 1 }, { 8925, 1 } }, out = { 13510, 1 }, oq = 1 },
    [17636] = { name = "Flask of Distilled Wisdom", t = { 1, 315, 322, 330 }, scroll = 13520, train = 300, scrollPrice = 40000, sq = 2, r = { { 13463, 30 }, { 13467, 10 }, { 13468, 1 }, { 8925, 1 } }, out = { 13511, 1 }, oq = 1 },
    [17637] = { name = "Flask of Supreme Power", t = { 1, 315, 322, 330 }, scroll = 13521, train = 300, scrollPrice = 40000, sq = 2, r = { { 13463, 30 }, { 13465, 10 }, { 13468, 1 }, { 8925, 1 } }, out = { 13512, 1 }, oq = 1 },
    [17638] = { name = "Flask of Chromatic Resistance", t = { 1, 315, 322, 330 }, scroll = 13522, train = 300, scrollPrice = 40000, sq = 2, r = { { 13467, 30 }, { 13465, 10 }, { 13468, 1 }, { 8925, 1 } }, out = { 13513, 1 }, oq = 1 },
    [21923] = { name = "Elixir of Frost Power", t = { 1, 210, 230, 250 }, scroll = 17709, train = 190, sq = 1, r = { { 3819, 2 }, { 3358, 1 }, { 3372, 1 } }, out = { 17708, 1 }, oq = 1 },
    [22430] = { name = "Refined Scale of Onyxia", t = { 1, 315, 322, 330 }, r = { { 15410, 1 } }, tool = 12, out = { 17967, 1 }, oq = 3 },
    [22732] = { name = "Major Rejuvenation Potion", t = { 1, 310, 320, 330 }, scroll = 18257, train = 300, sq = 3, r = { { 10286, 1 }, { 13464, 4 }, { 13463, 4 }, { 18256, 1 } }, out = { 18253, 1 }, oq = 1 },
    [22808] = { name = "Draught of Greater Water Breathing", t = { 1, 230, 250, 270 }, fee = 10000, train = 215, r = { { 7972, 1 }, { 8831, 2 }, { 8925, 1 } }, out = { 18294, 1 }, oq = 1 },
    [24266] = { name = "Gurubashi Mojo Madness", t = { 1, 315, 322, 330 }, r = { { 12938, 1 }, { 19943, 1 }, { 12804, 6 }, { 13468, 1 } }, out = { 19931, 3 }, oq = 3 },
    [24365] = { name = "Mageblood Elixir", t = { 1, 290, 310, 330 }, scroll = 20011, train = 275, scrollPrice = 50000, rep = { 270, 6 }, sq = 1, r = { { 13463, 1 }, { 13466, 2 }, { 8925, 1 } }, out = { 20007, 1 }, oq = 1 },
    [24366] = { name = "Greater Dreamless Sleep Potion", t = { 1, 290, 310, 330 }, scroll = 20012, train = 275, scrollPrice = 50000, rep = { 270, 4 }, sq = 1, r = { { 13463, 2 }, { 13464, 1 }, { 8925, 1 } }, out = { 20002, 1 }, oq = 1 },
    [24367] = { name = "Living Action Potion", t = { 1, 300, 320, 340 }, scroll = 20013, train = 285, scrollPrice = 50000, rep = { 270, 7 }, sq = 1, r = { { 13467, 2 }, { 13465, 2 }, { 10286, 2 }, { 8925, 1 } }, out = { 20008, 1 }, oq = 1 },
    [24368] = { name = "Major Troll's Blood Elixir", t = { 1, 305, 325, 345 }, scroll = 20014, train = 290, scrollPrice = 50000, rep = { 270, 5 }, sq = 1, r = { { 8846, 1 }, { 13466, 2 }, { 8925, 1 } }, out = { 20004, 1 }, oq = 1 },
    [25146] = { name = "Transmute: Elemental Fire", t = { 1, 301, 305, 310 }, scroll = 20761, train = 300, rep = { 59, 4 }, sq = 1, r = { { 7077, 1 } }, tool = 12, out = { 7068, 3 }, oq = 1 },
    [26277] = { name = "Elixir of Holy Power", t = { 1, 265, 285, 305 }, scroll = 21547, train = 250, sq = 2, r = { { 6371, 3 }, { 4625, 3 }, { 8925, 1 } }, out = { 21546, 1 }, oq = 1 },
    [426607] = { name = "Elixir of Coalesced Regret", t = { 1, 90, 100, 110 }, scroll = 210709, train = 90, gone = true, sq = 2, r = { { 3820, 5 }, { 3372, 1 }, { 3369, 5 }, { 11083, 1 } }, out = { 210708, 1 }, oq = 1 },
    [435969] = { name = "Insulating Gniodine", t = { 1, 200, 210, 220 }, scroll = 215433, train = 200, sq = 3, r = { { 3372, 1 }, { 213371, 5 } }, out = { 213372, 1 }, oq = 1 },
    [435971] = { name = "Mildly Irradiated Rejuvenation Potion", t = { 1, 225, 230, 235 }, scroll = 215163, train = 225, sq = 4, r = { { 213371, 1 }, { 2456, 1 }, { 215430, 3 }, { 8925, 5 } }, out = { 215162, 5 }, oq = 1 },
    [1213544] = { name = "Flask of Unyielding Sorrow", t = { 1, 315, 322, 330 }, scroll = 234252, train = 305, sq = 1, r = { { 16203, 1 }, { 234012, 1 }, { 13511, 1 }, { 8925, 1 } }, tool = 12, out = { 233966, 1 }, oq = 1 },
    [1230564] = { name = "Mana Well", t = { 1, 20, 20, 20 }, fee = 0, train = 20, r = { { 2447, 1 }, { 3371, 1 } }, out = { 279956, 1 }, oq = 1 },
    [1231583] = { name = "Major Discolored Healing Potion", t = { 1, 290, 310, 330 }, fee = 10000, train = 250, tr = { 1937, 249713 }, r = { { 8925, 1 }, { 13466, 1 }, { 730, 1 } }, out = { 241650, 1 }, oq = 1 },
    [1244421] = { name = "Distilled Firewater", t = { 1, 260, 265, 270 }, scroll = 236754, train = 250, sq = 2, r = { { 3819, 4 }, { 8846, 2 }, { 3372, 1 } }, out = { 246948, 1 }, oq = 1 },
    [1244645] = { name = "Lesser Discolored Healing Potion", t = { 1, 85, 105, 125 }, fee = 100, train = 85, tr = { 1937, 249713 }, r = { { 3371, 1 }, { 2450, 1 }, { 730, 1 } }, out = { 247239, 1 }, oq = 1 },
    [1244646] = { name = "Discolored Healing Potion", t = { 1, 135, 155, 175 }, fee = 500, train = 135, tr = { 1937, 249713 }, r = { { 3372, 1 }, { 2453, 1 }, { 730, 1 } }, out = { 247240, 1 }, oq = 1 },
    [1244647] = { name = "Greater Discolored Healing Potion", t = { 1, 175, 195, 215 }, fee = 1500, train = 175, tr = { 1937, 249713 }, r = { { 3372, 1 }, { 3356, 1 }, { 730, 1 } }, out = { 247241, 1 }, oq = 1 },
    [1244648] = { name = "Superior Discolored Healing Potion", t = { 1, 230, 250, 270 }, fee = 5000, train = 230, tr = { 1937, 249713 }, r = { { 8925, 1 }, { 8838, 1 }, { 730, 1 } }, out = { 247242, 1 }, oq = 1 },
    [1245246] = { name = "Minor Arcane Elixir", t = { 1, 10, 12, 15 }, basic = true, r = { { 2447, 1 }, { 3371, 1 } }, out = { 247754, 1 }, oq = 1 },
    [1245250] = { name = "Elixir of Minor Force", t = { 1, 10, 12, 15 }, basic = true, r = { { 765, 1 }, { 3371, 1 } }, out = { 247755, 1 }, oq = 1 },
    [1249630] = { name = "Cerulean Dye", t = { 1, 50, 70, 90 }, fee = 135, train = 40, r = { { 249399, 2 }, { 3371, 1 } }, out = { 249409, 1 }, oq = 2 },
    [1249631] = { name = "Magenta Dye", t = { 1, 130, 142, 155 }, fee = 1500, train = 120, r = { { 249424, 2 }, { 3372, 1 } }, out = { 249430, 1 }, oq = 2 },
    [1249632] = { name = "Viridian Dye", t = { 1, 230, 250, 270 }, fee = 10000, train = 215, r = { { 249274, 2 }, { 8925, 1 } }, out = { 249431, 1 }, oq = 2 },
    [1249633] = { name = "Sulfuric Acid", t = { 1, 50, 70, 90 }, fee = 135, train = 40, r = { { 249391, 2 }, { 3371, 1 } }, out = { 249410, 1 }, oq = 2 },
    [1250775] = { name = "Revealing Draught", t = { 1, 205, 207, 210 }, scroll = 250362, train = 195, sq = 1, r = { { 3818, 3 }, { 3358, 1 }, { 3372, 1 } }, out = { 250326, 1 }, oq = 1 },
    [1250776] = { name = "Potion of Predatory Senses", t = { 1, 200, 202, 205 }, scroll = 250363, train = 195, sq = 1, r = { { 3818, 2 }, { 3821, 2 }, { 3372, 1 } }, out = { 250327, 1 }, oq = 1 },
    [1250777] = { name = "Elixir of Cunning", t = { 1, 280, 282, 285 }, scroll = 250364, train = 275, sq = 1, favor = 180, favorRep = 6, r = { { 13463, 3 }, { 8846, 2 }, { 8925, 1 } }, out = { 250328, 1 }, oq = 1 },
    [1250778] = { name = "Elixir of the Phalanx", t = { 1, 255, 257, 260 }, scroll = 250365, train = 250, sq = 1, favor = 180, favorRep = 6, r = { { 13464, 2 }, { 8838, 4 }, { 8925, 1 } }, out = { 250329, 1 }, oq = 1 },
    [1250779] = { name = "Minor Cleric's Elixir", t = { 1, 50, 52, 55 }, scroll = 250366, train = 45, sq = 1, r = { { 785, 2 }, { 2453, 1 }, { 3371, 1 } }, out = { 250330, 1 }, oq = 1 },
    [1250780] = { name = "Lesser Cleric's Elixir", t = { 1, 100, 102, 105 }, scroll = 250367, train = 95, sq = 1, favor = 45, r = { { 3356, 2 }, { 3357, 2 }, { 3372, 1 } }, out = { 250331, 1 }, oq = 1 },
    [1250781] = { name = "Cleric's Elixir", t = { 1, 150, 152, 155 }, scroll = 250368, train = 145, sq = 1, r = { { 3819, 2 }, { 4625, 2 }, { 3372, 1 } }, out = { 250332, 1 }, oq = 1 },
    [1250782] = { name = "Greater Cleric's Elixir", t = { 1, 200, 202, 205 }, scroll = 250369, train = 195, sq = 1, favor = 120, favorRep = 5, r = { { 8836, 3 }, { 8831, 1 }, { 8925, 1 } }, out = { 250333, 1 }, oq = 1 },
    [1250783] = { name = "Elixir of Fortitude", t = { 1, 155, 157, 160 }, scroll = 250370, train = 150, sq = 1, r = { { 3821, 4 }, { 3372, 1 } }, out = { 250334, 1 }, oq = 1 },
    [1250784] = { name = "Elixir of Greater Fortitude", t = { 1, 205, 207, 210 }, scroll = 250371, train = 200, sq = 1, favor = 120, favorRep = 5, r = { { 8838, 4 }, { 8925, 1 } }, out = { 250335, 1 }, oq = 1 },
    [1250785] = { name = "Elixir of Wicked Regeneration", t = { 1, 290, 292, 295 }, scroll = 250372, train = 285, sq = 1, favor = 180, favorRep = 6, r = { { 13464, 3 }, { 13463, 2 }, { 8925, 1 } }, out = { 250336, 1 }, oq = 1 },
    [1250786] = { name = "Elixir of the Owl", t = { 1, 285, 287, 290 }, scroll = 250373, train = 280, sq = 1, favor = 180, favorRep = 6, r = { { 13463, 4 }, { 13465, 2 }, { 18256, 1 } }, out = { 250337, 1 }, oq = 1 },
    [1250787] = { name = "Elixir of Sages", t = { 1, 280, 282, 285 }, scroll = 250374, train = 275, sq = 1, favor = 180, favorRep = 6, r = { { 13463, 4 }, { 13464, 2 }, { 18256, 1 } }, out = { 250338, 1 }, oq = 1 },
    [1250788] = { name = "Minor Mageblood Elixir", t = { 1, 30, 32, 35 }, scroll = 250375, train = 25, sq = 1, r = { { 785, 2 }, { 3371, 1 } }, out = { 250339, 1 }, oq = 1 },
    [1250789] = { name = "Lesser Mageblood Elixir", t = { 1, 80, 82, 85 }, scroll = 250376, train = 75, sq = 1, favor = 45, r = { { 3356, 3 }, { 3371, 1 } }, out = { 250340, 1 }, oq = 1 },
    [1250790] = { name = "Greater Mageblood Elixir", t = { 1, 180, 182, 185 }, scroll = 250377, train = 175, sq = 1, favor = 120, favorRep = 5, r = { { 8839, 3 }, { 8836, 2 }, { 8925, 1 } }, out = { 250341, 1 }, oq = 1 },
    [1250791] = { name = "Lesser Arcane Elixir", t = { 1, 125, 127, 130 }, scroll = 250378, train = 120, sq = 1, favor = 45, r = { { 3356, 4 }, { 3372, 1 } }, out = { 250342, 1 }, oq = 1 },
    [1250792] = { name = "Elixir of Nature Power", t = { 1, 290, 292, 295 }, scroll = 250379, train = 285, sq = 1, favor = 180, favorRep = 6, r = { { 13464, 4 }, { 8838, 2 }, { 8925, 1 } }, out = { 250343, 1 }, oq = 1 },
    [1250793] = { name = "Elixir of Minor Spirit", t = { 1, 20, 22, 25 }, scroll = 250380, train = 15, sq = 1, r = { { 2449, 2 }, { 2447, 1 }, { 3371, 1 } }, out = { 250344, 1 }, oq = 1 },
    [1250794] = { name = "Elixir of Lesser Spirit", t = { 1, 70, 72, 75 }, scroll = 250381, train = 65, sq = 1, favor = 45, r = { { 3355, 2 }, { 785, 1 }, { 3371, 1 } }, out = { 250345, 1 }, oq = 1 },
    [1250795] = { name = "Elixir of Spirit", t = { 1, 120, 122, 125 }, scroll = 250382, train = 115, sq = 1, r = { { 3358, 3 }, { 3356, 1 }, { 3372, 1 } }, out = { 250346, 1 }, oq = 1 },
    [1250796] = { name = "Elixir of Greater Spirit", t = { 1, 170, 172, 175 }, scroll = 250383, train = 165, sq = 1, favor = 120, favorRep = 5, r = { { 8836, 3 }, { 8831, 2 }, { 8925, 1 } }, out = { 250347, 1 }, oq = 1 },
    [1250797] = { name = "Elixir of the Whale", t = { 1, 280, 282, 285 }, scroll = 250384, train = 275, sq = 1, favor = 180, favorRep = 6, r = { { 13463, 3 }, { 8846, 1 }, { 8925, 1 } }, out = { 250348, 1 }, oq = 1 },
    [1250798] = { name = "Elixir of Strength", t = { 1, 155, 157, 160 }, scroll = 250385, train = 150, sq = 1, r = { { 3355, 3 }, { 3821, 1 }, { 3372, 1 } }, out = { 250349, 1 }, oq = 1 },
    [1250799] = { name = "Elixir of Ferocity", t = { 1, 280, 282, 285 }, scroll = 250386, train = 275, sq = 1, favor = 180, favorRep = 6, r = { { 8846, 3 }, { 8845, 1 }, { 8925, 1 } }, out = { 250350, 1 }, oq = 1 },
    [1250800] = { name = "Elixir of the Grizzly", t = { 1, 305, 307, 310 }, scroll = 250387, train = 300, sq = 1, favor = 240, favorRep = 6, r = { { 8846, 3 }, { 8839, 1 }, { 8925, 1 } }, out = { 250351, 1 }, oq = 1 },
    [1250801] = { name = "Elixir of Lesser Intellect", t = { 1, 100, 102, 105 }, scroll = 250388, train = 95, sq = 1, favor = 45, r = { { 3356, 3 }, { 3372, 1 } }, out = { 250353, 1 }, oq = 1 },
    [1250802] = { name = "Elixir of Intellect", t = { 1, 140, 142, 145 }, scroll = 250389, train = 135, sq = 1, r = { { 3358, 3 }, { 3372, 1 } }, out = { 250354, 1 }, oq = 1 },
    [1251729] = { name = "Minor Spellblasting Potion", t = { 1, 40, 42, 45 }, scroll = 250976, train = 35, sq = 1, r = { { 765, 1 }, { 2447, 1 }, { 3371, 1 } }, out = { 250932, 1 }, oq = 1 },
    [1251730] = { name = "Lesser Spellblasting Potion", t = { 1, 90, 92, 95 }, scroll = 250977, train = 85, sq = 1, r = { { 785, 1 }, { 765, 2 }, { 3371, 1 } }, out = { 250933, 1 }, oq = 1 },
    [1251731] = { name = "Spellblasting Potion", t = { 1, 140, 142, 145 }, scroll = 250978, train = 135, sq = 1, favor = 45, r = { { 3355, 1 }, { 3369, 1 }, { 3371, 1 } }, out = { 250934, 1 }, oq = 1 },
    [1251732] = { name = "Greater Spellblasting Potion", t = { 1, 190, 192, 195 }, scroll = 250979, train = 185, sq = 2, r = { { 3356, 2 }, { 3818, 1 }, { 3372, 1 } }, out = { 250935, 1 }, oq = 1 },
    [1251733] = { name = "Superior Spellblasting Potion", t = { 1, 240, 242, 245 }, scroll = 250980, train = 235, sq = 1, r = { { 3819, 2 }, { 3358, 2 }, { 3372, 1 } }, out = { 250936, 1 }, oq = 1 },
    [1251734] = { name = "Major Spellblasting Potion", t = { 1, 290, 292, 295 }, scroll = 250981, train = 285, sq = 1, favor = 180, favorRep = 6, r = { { 13463, 2 }, { 13465, 1 }, { 18256, 1 } }, out = { 250937, 1 }, oq = 1 },
    [1251735] = { name = "Minor Frenzy Potion", t = { 1, 45, 47, 50 }, scroll = 250982, train = 40, sq = 1, r = { { 2449, 1 }, { 765, 1 }, { 3371, 1 } }, out = { 250938, 1 }, oq = 1 },
    [1251736] = { name = "Lesser Frenzy Potion", t = { 1, 95, 97, 100 }, scroll = 250983, train = 90, sq = 1, r = { { 2450, 1 }, { 2449, 2 }, { 3371, 1 } }, out = { 250939, 1 }, oq = 1 },
    [1251737] = { name = "Frenzy Potion", t = { 1, 145, 147, 150 }, scroll = 250984, train = 140, sq = 1, favor = 45, r = { { 3818, 2 }, { 2450, 2 }, { 3372, 1 } }, out = { 250940, 1 }, oq = 1 },
    [1251738] = { name = "Greater Frenzy Potion", t = { 1, 195, 197, 200 }, scroll = 250985, train = 190, sq = 2, r = { { 4625, 3 }, { 3818, 2 }, { 3372, 1 } }, out = { 250941, 1 }, oq = 1 },
    [1251739] = { name = "Superior Frenzy Potion", t = { 1, 245, 247, 250 }, scroll = 250986, train = 240, sq = 1, r = { { 8839, 3 }, { 4625, 2 }, { 8925, 1 } }, out = { 250942, 1 }, oq = 1 },
    [1251740] = { name = "Major Frenzy Potion", t = { 1, 295, 297, 300 }, scroll = 250987, train = 290, sq = 1, favor = 240, favorRep = 6, r = { { 13466, 3 }, { 8839, 2 }, { 18256, 1 } }, out = { 250943, 1 }, oq = 1 },
    [1251741] = { name = "Minor Mender's Potion", t = { 1, 35, 37, 40 }, scroll = 250988, train = 30, sq = 1, r = { { 785, 2 }, { 2453, 1 }, { 3371, 1 } }, out = { 250944, 1 }, oq = 1 },
    [1251742] = { name = "Lesser Mender's Potion", t = { 1, 85, 87, 90 }, scroll = 250989, train = 80, sq = 1, r = { { 3356, 2 }, { 3357, 2 }, { 3372, 1 } }, out = { 250945, 1 }, oq = 1 },
    [1251743] = { name = "Mender's Potion", t = { 1, 135, 137, 140 }, scroll = 250990, train = 130, sq = 1, favor = 45, r = { { 3819, 2 }, { 4625, 2 }, { 3372, 1 } }, out = { 250946, 1 }, oq = 1 },
    [1251744] = { name = "Greater Mender's Potion", t = { 1, 185, 187, 190 }, scroll = 250991, train = 180, sq = 1, r = { { 8836, 2 }, { 8831, 1 }, { 8925, 1 } }, out = { 250947, 1 }, oq = 1 },
    [1251745] = { name = "Superior Mender's Potion", t = { 1, 235, 237, 240 }, scroll = 250992, train = 230, sq = 1, r = { { 8838, 2 }, { 8836, 1 }, { 8925, 1 } }, out = { 250948, 1 }, oq = 1 },
    [1251747] = { name = "Major Mender's Potion", t = { 1, 285, 287, 290 }, scroll = 250993, train = 280, sq = 1, favor = 180, favorRep = 6, r = { { 13463, 3 }, { 8838, 1 }, { 18256, 1 } }, out = { 250949, 1 }, oq = 1 },
    [1251748] = { name = "Potion of Venomous Blood", t = { 1, 280, 282, 285 }, scroll = 250994, train = 275, sq = 1, favor = 180, favorRep = 6, r = { { 8846, 3 }, { 13466, 2 }, { 8925, 1 } }, out = { 250950, 1 }, oq = 1 },
    [1251749] = { name = "Caustic Smog Potion", t = { 1, 270, 272, 275 }, scroll = 250995, train = 265, sq = 1, favor = 180, favorRep = 6, r = { { 8845, 2 }, { 3369, 2 }, { 8925, 1 } }, out = { 250951, 1 }, oq = 1 },
    [1251751] = { name = "Dragonfire Potion", t = { 1, 250, 252, 255 }, scroll = 250997, train = 245, sq = 1, favor = 120, favorRep = 5, r = { { 13465, 2 }, { 4625, 2 }, { 8925, 1 } }, out = { 250953, 1 }, oq = 1 },
    [1251752] = { name = "Potion of Elemental Purging", t = { 1, 285, 287, 290 }, scroll = 250998, train = 280, sq = 1, favor = 180, favorRep = 6, r = { { 4625, 2 }, { 3819, 2 }, { 8925, 1 } }, out = { 250954, 1 }, oq = 1 },
    [1251753] = { name = "Potion of Beast Slaying", t = { 1, 285, 287, 290 }, scroll = 250999, train = 280, sq = 1, r = { { 8846, 2 }, { 13466, 2 }, { 18256, 1 } }, out = { 250955, 1 }, oq = 1 },
    [1263005] = { name = "Fermenter", t = { 1, 140, 140, 140 }, scroll = 273085, train = 140, sq = 2, r = { { 3372, 1 }, { 3356, 1 }, { 2452, 1 } }, out = { 279970, 1 }, oq = 1 },
    [1293559] = { name = "Flask of Natural Accuracy", t = { 1, 320, 325, 330 }, scroll = 274277, train = 300, sq = 3, r = { { 248822, 1 }, { 248821, 12 }, { 13464, 9 }, { 18256, 1 } }, out = { 274273, 1 }, oq = 2 },
    [1293560] = { name = "Flask of Natural Aggression", t = { 1, 320, 325, 330 }, scroll = 274278, train = 300, sq = 3, r = { { 248822, 1 }, { 248821, 18 }, { 13465, 6 }, { 18256, 1 } }, out = { 274274, 1 }, oq = 2 },
    [1293561] = { name = "Flask of Natural Precision", t = { 1, 320, 325, 330 }, scroll = 274279, train = 300, sq = 3, r = { { 248822, 1 }, { 248823, 12 }, { 13463, 9 }, { 18256, 1 } }, out = { 274275, 1 }, oq = 2 },
    [1293562] = { name = "Flask of Natural Swiftness", t = { 1, 320, 325, 330 }, scroll = 274280, train = 300, sq = 3, r = { { 248822, 1 }, { 248823, 18 }, { 13467, 6 }, { 18256, 1 } }, out = { 274276, 1 }, oq = 2 },
    [1317279] = { name = "Transmute: Legionite", t = { 1, 275, 282, 290 }, scroll = 284871, train = 275, sq = 1, r = { { 251291, 1 }, { 248819, 1 } }, tool = 12, out = { 251290, 1 }, oq = 2 },
    [2332] = { name = "Minor Rejuvenation Potion", t = { 40, 70, 90, 110 }, fee = 150, train = 40, r = { { 785, 2 }, { 2447, 1 }, { 3371, 1 } }, out = { 2456, 1 }, oq = 1 },
    [2334] = { name = "Elixir of Minor Fortitude", t = { 50, 80, 100, 120 }, fee = 250, train = 50, r = { { 2449, 2 }, { 2447, 1 }, { 3371, 1 } }, out = { 2458, 1 }, oq = 1 },
    [2335] = { name = "Swiftness Potion", t = { 60, 90, 110, 130 }, scroll = 2555, train = 60, sq = 2, r = { { 2452, 1 }, { 2450, 1 }, { 3371, 1 } }, out = { 2459, 1 }, oq = 1 },
  },
}

-- Herramientas: [categoría] = { objeto, máscara } (un bastón superior cubre a los inferiores)
ES.Data.Tools = ES.Data.Tools or {}
ES.Data.Tools[12] = { item = 9149, mask = 1, family = "stone" }
ES.Data.Tools[14] = { item = 6219, mask = 1, family = "spanner" }
ES.Data.Tools[15] = { item = 10498, mask = 2, family = "adjustor" }
ES.Data.Tools[162] = { item = 5956, mask = 4, family = "hammer" }
ES.Data.Tools[373] = { item = 6218, mask = 1, family = "rod" }
ES.Data.Tools[374] = { item = 6339, mask = 3, family = "rod" }
ES.Data.Tools[375] = { item = 11130, mask = 7, family = "rod" }
ES.Data.Tools[376] = { item = 11145, mask = 15, family = "rod" }
ES.Data.Tools[377] = { item = 16207, mask = 31, family = "rod" }

ES.Data.VendorPrices = ES.Data.VendorPrices or {}
ES.Data.SellPrices = ES.Data.SellPrices or {}
ES.Data.VendorPrices[3371] = 4
ES.Data.VendorPrices[3372] = 40
ES.Data.VendorPrices[4342] = 2500
ES.Data.VendorPrices[8925] = 500
ES.Data.VendorPrices[18256] = 6000
ES.Data.SellPrices[730] = 16
ES.Data.SellPrices[765] = 10
ES.Data.SellPrices[785] = 20
ES.Data.SellPrices[1288] = 185
ES.Data.SellPrices[2447] = 10
ES.Data.SellPrices[2449] = 20
ES.Data.SellPrices[2450] = 25
ES.Data.SellPrices[2452] = 15
ES.Data.SellPrices[2453] = 25
ES.Data.SellPrices[2454] = 20
ES.Data.SellPrices[2455] = 10
ES.Data.SellPrices[2456] = 15
ES.Data.SellPrices[2457] = 15
ES.Data.SellPrices[2458] = 15
ES.Data.SellPrices[2459] = 25
ES.Data.SellPrices[3355] = 50
ES.Data.SellPrices[3356] = 30
ES.Data.SellPrices[3357] = 75
ES.Data.SellPrices[3358] = 175
ES.Data.SellPrices[3369] = 25
ES.Data.SellPrices[3371] = 1
ES.Data.SellPrices[3372] = 10
ES.Data.SellPrices[3382] = 10
ES.Data.SellPrices[3383] = 100
ES.Data.SellPrices[3384] = 20
ES.Data.SellPrices[3385] = 30
ES.Data.SellPrices[3386] = 35
ES.Data.SellPrices[3387] = 30
ES.Data.SellPrices[3388] = 40
ES.Data.SellPrices[3389] = 40
ES.Data.SellPrices[3390] = 35
ES.Data.SellPrices[3391] = 20
ES.Data.SellPrices[3575] = 200
ES.Data.SellPrices[3577] = 600
ES.Data.SellPrices[3818] = 125
ES.Data.SellPrices[3819] = 100
ES.Data.SellPrices[3820] = 100
ES.Data.SellPrices[3821] = 150
ES.Data.SellPrices[3823] = 100
ES.Data.SellPrices[3824] = 150
ES.Data.SellPrices[3825] = 110
ES.Data.SellPrices[3826] = 105
ES.Data.SellPrices[3827] = 120
ES.Data.SellPrices[3828] = 150
ES.Data.SellPrices[3829] = 150
ES.Data.SellPrices[3858] = 250
ES.Data.SellPrices[3860] = 400
ES.Data.SellPrices[4342] = 625
ES.Data.SellPrices[4402] = 250
ES.Data.SellPrices[4596] = 25
ES.Data.SellPrices[4623] = 375
ES.Data.SellPrices[4625] = 250
ES.Data.SellPrices[5631] = 30
ES.Data.SellPrices[5633] = 150
ES.Data.SellPrices[5634] = 75
ES.Data.SellPrices[5635] = 45
ES.Data.SellPrices[5637] = 75
ES.Data.SellPrices[5996] = 95
ES.Data.SellPrices[5997] = 5
ES.Data.SellPrices[6037] = 1250
ES.Data.SellPrices[6048] = 100
ES.Data.SellPrices[6049] = 170
ES.Data.SellPrices[6050] = 300
ES.Data.SellPrices[6051] = 62
ES.Data.SellPrices[6052] = 300
ES.Data.SellPrices[6149] = 120
ES.Data.SellPrices[6358] = 4
ES.Data.SellPrices[6359] = 5
ES.Data.SellPrices[6370] = 10
ES.Data.SellPrices[6371] = 12
ES.Data.SellPrices[6372] = 35
ES.Data.SellPrices[6373] = 35
ES.Data.SellPrices[6522] = 4
ES.Data.SellPrices[6662] = 95
ES.Data.SellPrices[7067] = 400
ES.Data.SellPrices[7068] = 400
ES.Data.SellPrices[7069] = 400
ES.Data.SellPrices[7070] = 400
ES.Data.SellPrices[7076] = 400
ES.Data.SellPrices[7077] = 400
ES.Data.SellPrices[7078] = 400
ES.Data.SellPrices[7080] = 400
ES.Data.SellPrices[7082] = 400
ES.Data.SellPrices[7972] = 400
ES.Data.SellPrices[8153] = 5
ES.Data.SellPrices[8827] = 125
ES.Data.SellPrices[8831] = 300
ES.Data.SellPrices[8836] = 95
ES.Data.SellPrices[8838] = 60
ES.Data.SellPrices[8839] = 375
ES.Data.SellPrices[8845] = 375
ES.Data.SellPrices[8846] = 250
ES.Data.SellPrices[8925] = 125
ES.Data.SellPrices[8949] = 200
ES.Data.SellPrices[8951] = 200
ES.Data.SellPrices[8956] = 200
ES.Data.SellPrices[9030] = 200
ES.Data.SellPrices[9036] = 20
ES.Data.SellPrices[9061] = 250
ES.Data.SellPrices[9088] = 250
ES.Data.SellPrices[9144] = 250
ES.Data.SellPrices[9149] = 250
ES.Data.SellPrices[9154] = 300
ES.Data.SellPrices[9155] = 400
ES.Data.SellPrices[9172] = 500
ES.Data.SellPrices[9179] = 1000
ES.Data.SellPrices[9187] = 600
ES.Data.SellPrices[9197] = 600
ES.Data.SellPrices[9206] = 700
ES.Data.SellPrices[9210] = 750
ES.Data.SellPrices[9224] = 700
ES.Data.SellPrices[9233] = 500
ES.Data.SellPrices[9260] = 400
ES.Data.SellPrices[9262] = 1000
ES.Data.SellPrices[9264] = 35
ES.Data.SellPrices[10286] = 400
ES.Data.SellPrices[10592] = 150
ES.Data.SellPrices[10620] = 250
ES.Data.SellPrices[11083] = 1
ES.Data.SellPrices[11176] = 1
ES.Data.SellPrices[12190] = 250
ES.Data.SellPrices[12359] = 600
ES.Data.SellPrices[12360] = 5000
ES.Data.SellPrices[12363] = 2000
ES.Data.SellPrices[12803] = 500
ES.Data.SellPrices[12804] = 2000
ES.Data.SellPrices[12808] = 1000
ES.Data.SellPrices[13422] = 10
ES.Data.SellPrices[13423] = 125
ES.Data.SellPrices[13442] = 500
ES.Data.SellPrices[13443] = 400
ES.Data.SellPrices[13444] = 1500
ES.Data.SellPrices[13445] = 500
ES.Data.SellPrices[13447] = 1250
ES.Data.SellPrices[13452] = 1250
ES.Data.SellPrices[13453] = 1250
ES.Data.SellPrices[13454] = 750
ES.Data.SellPrices[13455] = 750
ES.Data.SellPrices[13456] = 750
ES.Data.SellPrices[13457] = 750
ES.Data.SellPrices[13458] = 750
ES.Data.SellPrices[13459] = 100
ES.Data.SellPrices[13460] = 750
ES.Data.SellPrices[13461] = 750
ES.Data.SellPrices[13462] = 750
ES.Data.SellPrices[13463] = 100
ES.Data.SellPrices[13464] = 100
ES.Data.SellPrices[13465] = 150
ES.Data.SellPrices[13466] = 250
ES.Data.SellPrices[13467] = 250
ES.Data.SellPrices[13468] = 1000
ES.Data.SellPrices[13503] = 25000
ES.Data.SellPrices[13506] = 5000
ES.Data.SellPrices[13510] = 5000
ES.Data.SellPrices[13511] = 5000
ES.Data.SellPrices[13512] = 5000
ES.Data.SellPrices[13513] = 5000
ES.Data.SellPrices[15410] = 5000
ES.Data.SellPrices[16203] = 1
ES.Data.SellPrices[17708] = 35
ES.Data.SellPrices[17967] = 5000
ES.Data.SellPrices[18253] = 15
ES.Data.SellPrices[18256] = 1500
ES.Data.SellPrices[18294] = 250
ES.Data.SellPrices[19943] = 2000
ES.Data.SellPrices[20002] = 1000
ES.Data.SellPrices[20004] = 1000
ES.Data.SellPrices[20007] = 1000
ES.Data.SellPrices[20008] = 600
ES.Data.SellPrices[21546] = 35
ES.Data.SellPrices[210708] = 40
ES.Data.SellPrices[215430] = 250
ES.Data.SellPrices[234012] = 15
ES.Data.SellPrices[241650] = 25
ES.Data.SellPrices[246948] = 200
ES.Data.SellPrices[247239] = 25
ES.Data.SellPrices[247240] = 75
ES.Data.SellPrices[247241] = 125
ES.Data.SellPrices[247242] = 250
ES.Data.SellPrices[247754] = 5
ES.Data.SellPrices[247755] = 25
ES.Data.SellPrices[248819] = 3000
ES.Data.SellPrices[248821] = 225
ES.Data.SellPrices[248822] = 1500
ES.Data.SellPrices[248823] = 150
ES.Data.SellPrices[249274] = 250
ES.Data.SellPrices[249391] = 100
ES.Data.SellPrices[249399] = 30
ES.Data.SellPrices[249409] = 75
ES.Data.SellPrices[249410] = 125
ES.Data.SellPrices[249424] = 95
ES.Data.SellPrices[249430] = 250
ES.Data.SellPrices[249431] = 375
ES.Data.SellPrices[250327] = 100
ES.Data.SellPrices[250328] = 125
ES.Data.SellPrices[250329] = 125
ES.Data.SellPrices[250330] = 25
ES.Data.SellPrices[250331] = 50
ES.Data.SellPrices[250332] = 75
ES.Data.SellPrices[250333] = 100
ES.Data.SellPrices[250334] = 75
ES.Data.SellPrices[250335] = 100
ES.Data.SellPrices[250336] = 125
ES.Data.SellPrices[250337] = 125
ES.Data.SellPrices[250338] = 125
ES.Data.SellPrices[250339] = 25
ES.Data.SellPrices[250340] = 50
ES.Data.SellPrices[250341] = 100
ES.Data.SellPrices[250342] = 50
ES.Data.SellPrices[250343] = 125
ES.Data.SellPrices[250344] = 25
ES.Data.SellPrices[250345] = 50
ES.Data.SellPrices[250346] = 75
ES.Data.SellPrices[250347] = 100
ES.Data.SellPrices[250348] = 125
ES.Data.SellPrices[250349] = 75
ES.Data.SellPrices[250350] = 125
ES.Data.SellPrices[250351] = 125
ES.Data.SellPrices[250353] = 50
ES.Data.SellPrices[250354] = 75
ES.Data.SellPrices[250932] = 1
ES.Data.SellPrices[250933] = 25
ES.Data.SellPrices[250934] = 25
ES.Data.SellPrices[250935] = 1
ES.Data.SellPrices[250936] = 1
ES.Data.SellPrices[250937] = 1
ES.Data.SellPrices[250938] = 1
ES.Data.SellPrices[250939] = 1
ES.Data.SellPrices[250940] = 1
ES.Data.SellPrices[250941] = 1
ES.Data.SellPrices[250942] = 1
ES.Data.SellPrices[250943] = 1
ES.Data.SellPrices[250944] = 1
ES.Data.SellPrices[250945] = 1
ES.Data.SellPrices[250946] = 1
ES.Data.SellPrices[250947] = 1
ES.Data.SellPrices[250948] = 1
ES.Data.SellPrices[250949] = 1
ES.Data.SellPrices[250950] = 1
ES.Data.SellPrices[250951] = 1
ES.Data.SellPrices[250953] = 1
ES.Data.SellPrices[250954] = 1
ES.Data.SellPrices[250955] = 1
ES.Data.SellPrices[251290] = 5000
ES.Data.SellPrices[251291] = 1500
ES.Data.SellPrices[274273] = 5000
ES.Data.SellPrices[274274] = 5000
ES.Data.SellPrices[274275] = 5000
ES.Data.SellPrices[274276] = 5000

-- Nombre de cada objeto (inglés, del cliente): se muestra mientras el juego no lo ha cargado
ES.Data.ItemNames = ES.Data.ItemNames or {}
ES.Data.ItemNames[730] = "Murloc Eye"
ES.Data.ItemNames[765] = "Silverleaf"
ES.Data.ItemNames[785] = "Mageroyal"
ES.Data.ItemNames[1288] = "Large Venom Sac"
ES.Data.ItemNames[2447] = "Peacebloom"
ES.Data.ItemNames[2449] = "Earthroot"
ES.Data.ItemNames[2450] = "Briarthorn"
ES.Data.ItemNames[2452] = "Swiftthistle"
ES.Data.ItemNames[2453] = "Bruiseweed"
ES.Data.ItemNames[2454] = "Elixir of Minor Strength"
ES.Data.ItemNames[2455] = "Minor Mana Potion"
ES.Data.ItemNames[2456] = "Minor Rejuvenation Potion"
ES.Data.ItemNames[2457] = "Elixir of Minor Agility"
ES.Data.ItemNames[2458] = "Elixir of Minor Fortitude"
ES.Data.ItemNames[2459] = "Swiftness Potion"
ES.Data.ItemNames[3355] = "Wild Steelbloom"
ES.Data.ItemNames[3356] = "Kingsblood"
ES.Data.ItemNames[3357] = "Liferoot"
ES.Data.ItemNames[3358] = "Khadgar's Whisker"
ES.Data.ItemNames[3369] = "Grave Moss"
ES.Data.ItemNames[3371] = "Empty Vial"
ES.Data.ItemNames[3372] = "Leaded Vial"
ES.Data.ItemNames[3382] = "Minor Troll's Blood Elixir"
ES.Data.ItemNames[3383] = "Elixir of Wisdom"
ES.Data.ItemNames[3384] = "Minor Magic Resistance Potion"
ES.Data.ItemNames[3385] = "Lesser Mana Potion"
ES.Data.ItemNames[3386] = "Potion of Poison Cleansing"
ES.Data.ItemNames[3387] = "Limited Invulnerability Potion"
ES.Data.ItemNames[3388] = "Lesser Troll's Blood Elixir"
ES.Data.ItemNames[3389] = "Elixir of Lesser Defense"
ES.Data.ItemNames[3390] = "Elixir of Lesser Agility"
ES.Data.ItemNames[3391] = "Elixir of Ogre Strength"
ES.Data.ItemNames[3575] = "Iron Bar"
ES.Data.ItemNames[3577] = "Gold Bar"
ES.Data.ItemNames[3818] = "Fadeleaf"
ES.Data.ItemNames[3819] = "Wintersbite"
ES.Data.ItemNames[3820] = "Stranglekelp"
ES.Data.ItemNames[3821] = "Goldthorn"
ES.Data.ItemNames[3823] = "Lesser Invisibility Potion"
ES.Data.ItemNames[3824] = "Shadow Oil"
ES.Data.ItemNames[3825] = "Elixir of Lesser Fortitude"
ES.Data.ItemNames[3826] = "Troll's Blood Elixir"
ES.Data.ItemNames[3827] = "Mana Potion"
ES.Data.ItemNames[3828] = "Draught of Detect Lesser Invisibility"
ES.Data.ItemNames[3829] = "Frost Oil"
ES.Data.ItemNames[3858] = "Mithril Ore"
ES.Data.ItemNames[3860] = "Mithril Bar"
ES.Data.ItemNames[4342] = "Purple Dye"
ES.Data.ItemNames[4402] = "Small Flame Sac"
ES.Data.ItemNames[4596] = "Minor Discolored Healing Potion"
ES.Data.ItemNames[4623] = "Lesser Stoneshield Potion"
ES.Data.ItemNames[4625] = "Firebloom"
ES.Data.ItemNames[5631] = "Rage Potion"
ES.Data.ItemNames[5633] = "Great Rage Potion"
ES.Data.ItemNames[5634] = "Free Action Potion"
ES.Data.ItemNames[5635] = "Sharp Claw"
ES.Data.ItemNames[5637] = "Large Fang"
ES.Data.ItemNames[5996] = "Draught of Water Breathing"
ES.Data.ItemNames[5997] = "Elixir of Minor Defense"
ES.Data.ItemNames[6037] = "Truesilver Bar"
ES.Data.ItemNames[6048] = "Shadow Protection Potion"
ES.Data.ItemNames[6049] = "Fire Protection Potion"
ES.Data.ItemNames[6050] = "Frost Protection Potion"
ES.Data.ItemNames[6051] = "Holy Protection Potion"
ES.Data.ItemNames[6052] = "Nature Protection Potion"
ES.Data.ItemNames[6149] = "Greater Mana Potion"
ES.Data.ItemNames[6358] = "Oily Blackmouth"
ES.Data.ItemNames[6359] = "Firefin Snapper"
ES.Data.ItemNames[6370] = "Blackmouth Oil"
ES.Data.ItemNames[6371] = "Fire Oil"
ES.Data.ItemNames[6372] = "Swim Speed Potion"
ES.Data.ItemNames[6373] = "Elixir of Fire Power"
ES.Data.ItemNames[6522] = "Deviate Fish"
ES.Data.ItemNames[6662] = "Elixir of Giant Growth"
ES.Data.ItemNames[7067] = "Elemental Earth"
ES.Data.ItemNames[7068] = "Elemental Fire"
ES.Data.ItemNames[7069] = "Elemental Air"
ES.Data.ItemNames[7070] = "Elemental Water"
ES.Data.ItemNames[7076] = "Essence of Earth"
ES.Data.ItemNames[7077] = "Heart of Fire"
ES.Data.ItemNames[7078] = "Essence of Fire"
ES.Data.ItemNames[7080] = "Essence of Water"
ES.Data.ItemNames[7082] = "Essence of Air"
ES.Data.ItemNames[7972] = "Ichor of Undeath"
ES.Data.ItemNames[8153] = "Wildvine"
ES.Data.ItemNames[8827] = "Draught of Water Walking"
ES.Data.ItemNames[8831] = "Purple Lotus"
ES.Data.ItemNames[8836] = "Arthas' Tears"
ES.Data.ItemNames[8838] = "Sungrass"
ES.Data.ItemNames[8839] = "Blindweed"
ES.Data.ItemNames[8845] = "Ghost Mushroom"
ES.Data.ItemNames[8846] = "Gromsblood"
ES.Data.ItemNames[8925] = "Crystal Vial"
ES.Data.ItemNames[8949] = "Elixir of Agility"
ES.Data.ItemNames[8951] = "Elixir of Defense"
ES.Data.ItemNames[8956] = "Oil of Immolation"
ES.Data.ItemNames[9030] = "Restorative Potion"
ES.Data.ItemNames[9036] = "Magic Resistance Potion"
ES.Data.ItemNames[9061] = "Goblin Rocket Fuel"
ES.Data.ItemNames[9088] = "Gift of Arthas"
ES.Data.ItemNames[9144] = "Wildvine Potion"
ES.Data.ItemNames[9149] = "Philosopher's Stone"
ES.Data.ItemNames[9154] = "Draught of Detect Undead"
ES.Data.ItemNames[9155] = "Arcane Elixir"
ES.Data.ItemNames[9172] = "Invisibility Potion"
ES.Data.ItemNames[9179] = "Elixir of Greater Intellect"
ES.Data.ItemNames[9187] = "Elixir of Greater Agility"
ES.Data.ItemNames[9197] = "Draught of Dream Vision"
ES.Data.ItemNames[9206] = "Elixir of Greater Strength"
ES.Data.ItemNames[9210] = "Ghost Dye"
ES.Data.ItemNames[9224] = "Potion of Demon Slaying"
ES.Data.ItemNames[9233] = "Draught of Detect Demon"
ES.Data.ItemNames[9260] = "Volatile Rum"
ES.Data.ItemNames[9262] = "Black Vitriol"
ES.Data.ItemNames[9264] = "Elixir of Shadow Power"
ES.Data.ItemNames[10286] = "Heart of the Wild"
ES.Data.ItemNames[10592] = "Catseye Draught"
ES.Data.ItemNames[10620] = "Thorium Ore"
ES.Data.ItemNames[11083] = "Soul Dust"
ES.Data.ItemNames[11176] = "Dream Dust"
ES.Data.ItemNames[12190] = "Dreamless Sleep Potion"
ES.Data.ItemNames[12359] = "Thorium Bar"
ES.Data.ItemNames[12360] = "Arcanite Bar"
ES.Data.ItemNames[12363] = "Arcane Crystal"
ES.Data.ItemNames[12803] = "Living Essence"
ES.Data.ItemNames[12804] = "Powerful Mojo"
ES.Data.ItemNames[12808] = "Essence of Undeath"
ES.Data.ItemNames[12938] = "Blood of Heroes"
ES.Data.ItemNames[13422] = "Stonescale Eel"
ES.Data.ItemNames[13423] = "Stonescale Oil"
ES.Data.ItemNames[13442] = "Mighty Rage Potion"
ES.Data.ItemNames[13443] = "Superior Mana Potion"
ES.Data.ItemNames[13444] = "Major Mana Potion"
ES.Data.ItemNames[13445] = "Elixir of Greater Defense"
ES.Data.ItemNames[13447] = "Elixir of the Sages"
ES.Data.ItemNames[13452] = "Elixir of the Mongoose"
ES.Data.ItemNames[13453] = "Elixir of Brute Force"
ES.Data.ItemNames[13454] = "Greater Arcane Elixir"
ES.Data.ItemNames[13455] = "Greater Stoneshield Potion"
ES.Data.ItemNames[13456] = "Greater Frost Protection Potion"
ES.Data.ItemNames[13457] = "Greater Fire Protection Potion"
ES.Data.ItemNames[13458] = "Greater Nature Protection Potion"
ES.Data.ItemNames[13459] = "Greater Shadow Protection Potion"
ES.Data.ItemNames[13460] = "Greater Holy Protection Potion"
ES.Data.ItemNames[13461] = "Greater Arcane Protection Potion"
ES.Data.ItemNames[13462] = "Purification Potion"
ES.Data.ItemNames[13463] = "Dreamfoil"
ES.Data.ItemNames[13464] = "Golden Sansam"
ES.Data.ItemNames[13465] = "Mountain Silversage"
ES.Data.ItemNames[13466] = "Plaguebloom"
ES.Data.ItemNames[13467] = "Icecap"
ES.Data.ItemNames[13468] = "Black Lotus"
ES.Data.ItemNames[13503] = "Alchemist's Stone"
ES.Data.ItemNames[13506] = "Flask of Petrification"
ES.Data.ItemNames[13510] = "Flask of the Titans"
ES.Data.ItemNames[13511] = "Flask of Distilled Wisdom"
ES.Data.ItemNames[13512] = "Flask of Supreme Power"
ES.Data.ItemNames[13513] = "Flask of Chromatic Resistance"
ES.Data.ItemNames[15410] = "Scale of Onyxia"
ES.Data.ItemNames[16203] = "Greater Eternal Essence"
ES.Data.ItemNames[17708] = "Elixir of Frost Power"
ES.Data.ItemNames[17967] = "Refined Scale of Onyxia"
ES.Data.ItemNames[18253] = "Major Rejuvenation Potion"
ES.Data.ItemNames[18256] = "Imbued Vial"
ES.Data.ItemNames[18294] = "Draught of Greater Water Breathing"
ES.Data.ItemNames[19931] = "Gurubashi Mojo Madness"
ES.Data.ItemNames[19943] = "Massive Mojo"
ES.Data.ItemNames[20002] = "Greater Dreamless Sleep Potion"
ES.Data.ItemNames[20004] = "Major Troll's Blood Elixir"
ES.Data.ItemNames[20007] = "Mageblood Elixir"
ES.Data.ItemNames[20008] = "Living Action Potion"
ES.Data.ItemNames[21546] = "Elixir of Holy Power"
ES.Data.ItemNames[210708] = "Elixir of Coalesced Regret"
ES.Data.ItemNames[213371] = "Crate of Tainted Gniodine Solution"
ES.Data.ItemNames[215430] = "Gnomeregan Fallout"
ES.Data.ItemNames[234012] = "Hive Thistle"
ES.Data.ItemNames[241650] = "Major Discolored Healing Potion"
ES.Data.ItemNames[246948] = "Distilled Firewater"
ES.Data.ItemNames[247239] = "Lesser Discolored Healing Potion"
ES.Data.ItemNames[247240] = "Discolored Healing Potion"
ES.Data.ItemNames[247241] = "Greater Discolored Healing Potion"
ES.Data.ItemNames[247242] = "Superior Discolored Healing Potion"
ES.Data.ItemNames[247754] = "Minor Arcane Elixir"
ES.Data.ItemNames[247755] = "Elixir of Minor Force"
ES.Data.ItemNames[248819] = "Fel Crystal"
ES.Data.ItemNames[248821] = "Demonsage"
ES.Data.ItemNames[248822] = "Death Lotus"
ES.Data.ItemNames[248823] = "Marefoil"
ES.Data.ItemNames[249274] = "Stranglevine"
ES.Data.ItemNames[249391] = "Pyrite"
ES.Data.ItemNames[249399] = "Frilled Lichen"
ES.Data.ItemNames[249409] = "Cerulean Dye"
ES.Data.ItemNames[249410] = "Sulfuric Acid"
ES.Data.ItemNames[249424] = "Rosecap"
ES.Data.ItemNames[249430] = "Magenta Dye"
ES.Data.ItemNames[249431] = "Viridian Dye"
ES.Data.ItemNames[250327] = "Potion of Predatory Senses"
ES.Data.ItemNames[250328] = "Elixir of Cunning"
ES.Data.ItemNames[250329] = "Elixir of the Phalanx"
ES.Data.ItemNames[250330] = "Minor Cleric's Elixir"
ES.Data.ItemNames[250331] = "Lesser Cleric's Elixir"
ES.Data.ItemNames[250332] = "Cleric's Elixir"
ES.Data.ItemNames[250333] = "Greater Cleric's Elixir"
ES.Data.ItemNames[250334] = "Elixir of Fortitude"
ES.Data.ItemNames[250335] = "Elixir of Greater Fortitude"
ES.Data.ItemNames[250336] = "Elixir of Wicked Regeneration"
ES.Data.ItemNames[250337] = "Elixir of the Owl"
ES.Data.ItemNames[250338] = "Elixir of Sages"
ES.Data.ItemNames[250339] = "Minor Mageblood Elixir"
ES.Data.ItemNames[250340] = "Lesser Mageblood Elixir"
ES.Data.ItemNames[250341] = "Greater Mageblood Elixir"
ES.Data.ItemNames[250342] = "Lesser Arcane Elixir"
ES.Data.ItemNames[250343] = "Elixir of Nature Power"
ES.Data.ItemNames[250344] = "Elixir of Minor Spirit"
ES.Data.ItemNames[250345] = "Elixir of Lesser Spirit"
ES.Data.ItemNames[250346] = "Elixir of Spirit"
ES.Data.ItemNames[250347] = "Elixir of Greater Spirit"
ES.Data.ItemNames[250348] = "Elixir of the Whale"
ES.Data.ItemNames[250349] = "Elixir of Strength"
ES.Data.ItemNames[250350] = "Elixir of Ferocity"
ES.Data.ItemNames[250351] = "Elixir of the Grizzly"
ES.Data.ItemNames[250353] = "Elixir of Lesser Intellect"
ES.Data.ItemNames[250354] = "Elixir of Intellect"
ES.Data.ItemNames[250932] = "Minor Spellblasting Potion"
ES.Data.ItemNames[250933] = "Lesser Spellblasting Potion"
ES.Data.ItemNames[250934] = "Spellblasting Potion"
ES.Data.ItemNames[250935] = "Greater Spellblasting Potion"
ES.Data.ItemNames[250936] = "Superior Spellblasting Potion"
ES.Data.ItemNames[250937] = "Major Spellblasting Potion"
ES.Data.ItemNames[250938] = "Minor Frenzy Potion"
ES.Data.ItemNames[250939] = "Lesser Frenzy Potion"
ES.Data.ItemNames[250940] = "Frenzy Potion"
ES.Data.ItemNames[250941] = "Greater Frenzy Potion"
ES.Data.ItemNames[250942] = "Superior Frenzy Potion"
ES.Data.ItemNames[250943] = "Major Frenzy Potion"
ES.Data.ItemNames[250944] = "Minor Mender's Potion"
ES.Data.ItemNames[250945] = "Lesser Mender's Potion"
ES.Data.ItemNames[250946] = "Mender's Potion"
ES.Data.ItemNames[250947] = "Greater Mender's Potion"
ES.Data.ItemNames[250948] = "Superior Mender's Potion"
ES.Data.ItemNames[250949] = "Major Mender's Potion"
ES.Data.ItemNames[250950] = "Potion of Venomous Blood"
ES.Data.ItemNames[250951] = "Caustic Smog Potion"
ES.Data.ItemNames[250953] = "Dragonfire Potion"
ES.Data.ItemNames[250954] = "Potion of Elemental Purging"
ES.Data.ItemNames[250955] = "Potion of Beast Slaying"
ES.Data.ItemNames[251290] = "Legionite Bar"
ES.Data.ItemNames[251291] = "Heavy Thorium Bar"
ES.Data.ItemNames[274273] = "Flask of Natural Accuracy"
ES.Data.ItemNames[274274] = "Flask of Natural Aggression"
ES.Data.ItemNames[274275] = "Flask of Natural Precision"
ES.Data.ItemNames[274276] = "Flask of Natural Swiftness"
ES.Data.ItemNames[279956] = "Mana Well"
ES.Data.ItemNames[279970] = "Fermenter"

-- Material -> profesión de recolección que lo consigue (393 Desuello, 182 Herboristería, 186 Minería).
-- Sin uso por ahora: reservado para la vía "Vender en bruto" de Ganar dinero (docs/PLAN.md, G1).
ES.Data.GatheredBy = ES.Data.GatheredBy or {}
ES.Data.GatheredBy[765] = 182
ES.Data.GatheredBy[785] = 182
ES.Data.GatheredBy[2447] = 182
ES.Data.GatheredBy[2449] = 182
ES.Data.GatheredBy[2450] = 182
ES.Data.GatheredBy[2452] = 182
ES.Data.GatheredBy[2453] = 182
ES.Data.GatheredBy[3355] = 182
ES.Data.GatheredBy[3356] = 182
ES.Data.GatheredBy[3357] = 182
ES.Data.GatheredBy[3358] = 182
ES.Data.GatheredBy[3369] = 182
ES.Data.GatheredBy[3575] = 186
ES.Data.GatheredBy[3818] = 182
ES.Data.GatheredBy[3819] = 182
ES.Data.GatheredBy[3820] = 182
ES.Data.GatheredBy[3821] = 182
ES.Data.GatheredBy[3858] = 186
ES.Data.GatheredBy[3860] = 186
ES.Data.GatheredBy[4625] = 182
ES.Data.GatheredBy[8153] = 182
ES.Data.GatheredBy[8831] = 182
ES.Data.GatheredBy[8836] = 182
ES.Data.GatheredBy[8838] = 182
ES.Data.GatheredBy[8839] = 182
ES.Data.GatheredBy[8845] = 182
ES.Data.GatheredBy[8846] = 182
ES.Data.GatheredBy[10620] = 186
ES.Data.GatheredBy[12359] = 186
ES.Data.GatheredBy[13463] = 182
ES.Data.GatheredBy[13464] = 182
ES.Data.GatheredBy[13465] = 182
ES.Data.GatheredBy[13466] = 182
ES.Data.GatheredBy[13467] = 182
ES.Data.GatheredBy[13468] = 182
ES.Data.GatheredBy[15410] = 393
ES.Data.GatheredBy[234012] = 182
ES.Data.GatheredBy[248821] = 182
ES.Data.GatheredBy[248822] = 182
ES.Data.GatheredBy[248823] = 182
ES.Data.GatheredBy[249274] = 182
ES.Data.GatheredBy[249391] = 186
ES.Data.GatheredBy[249399] = 182
ES.Data.GatheredBy[249424] = 182
ES.Data.GatheredBy[251291] = 186

```

---

## Blacksmithing

```lua
-- Generado por tools/gen_profession.py (Blacksmithing). No editar a mano.
-- Datos: cliente de WoW Forever (wago.tools DB2), instructores de CMaNGOS classic-db, vendedores de QuestieDB.
local _, ES = ...
ES.Data = ES.Data or {}

-- t = { naranja, amarilla, verde, gris }; fee/train = precio y habilidad del instructor
-- (sin fee = se aprende de pergamino: de dónde sale, en Data/Sources.lua; scrollPrice = su precio si lo vende un PNJ)
-- rep = { facción, nivel } que pide el pergamino para aprenderla (5 amistoso, 6 honorable, 7 venerado, 8 exaltado)
-- r = { {itemID, cantidad} }; out = { itemID, cantidad }
-- sq / oq = calidad del pergamino / de lo fabricado (0 pobre, 1 común, 2 poco común, 3 raro, 4 épico)
-- faction = bando que puede aprenderla, si solo es de uno
-- bop = lo fabricado se liga al recogerlo: no se puede vender en la AH (sí al vendedor)
-- favor / favorRep = se compra con Merchant's Favor en el campamento de tu bando, y la reputación que pide
-- train ajustado a Forever: nivel de Classic menos lo que Forever bajó la amarilla de esa receta
-- basic = se aprende sola al coger la profesión; trainer = de instructor sin precio conocido
--   (receta nueva de Forever que no está en CMaNGOS: se aprende al ponerse amarilla)
ES.Data.Blacksmithing = {
  skillLine = 164,
  ranks = { -- { tope, precio, habilidad requerida, nivel de personaje }
    { 150, 450, 50, 10 },
    { 225, 4500, 125, 20 },
    { 300, 50000, 200, 35 },
  },
  -- { PNJ instructor, rangos que enseña: 1 aprendiz (75), 2 oficial (150), 4 experto (225), 8 artesano (300) }
  trainers = { { 514, 1 }, { 957, 1 }, { 1241, 1 }, { 1383, 2 }, { 2836, 8 }, { 2998, 2 }, { 3136, 2 }, { 3174, 1 }, { 3355, 4 }, { 3478, 2 }, { 3557, 1 }, { 4258, 4 }, { 4596, 2 }, { 4605, 1 }, { 5511, 2 }, { 6299, 1 }, { 10266, 1 }, { 10276, 2 }, { 10277, 1 }, { 10278, 1 }, { 251913, 3 }, { 252479, 3 }, { 256658, 1 }, { 259250, 1 }, { 276067, 3 } },
  recipes = {
    [2660] = { name = "Rough Sharpening Stone", t = { 1, 15, 35, 55 }, basic = true, r = { { 2835, 1 } }, out = { 2862, 1 }, oq = 1 },
    [2661] = { name = "Copper Chain Belt", t = { 1, 70, 90, 110 }, fee = 100, train = 30, r = { { 2840, 6 } }, tool = 162, out = { 2851, 1 }, oq = 2 },
    [2663] = { name = "Copper Bracers", t = { 1, 20, 40, 60 }, basic = true, r = { { 2840, 2 } }, tool = 162, out = { 2853, 1 }, oq = 1 },
    [2664] = { name = "Runed Copper Bracers", t = { 1, 90, 102, 115 }, fee = 500, train = 65, r = { { 2840, 10 }, { 3470, 3 } }, tool = 162, out = { 2854, 1 }, oq = 2 },
    [2671] = { name = "Rough Bronze Bracers", t = { 1, 115, 130, 145 }, scroll = 5577, train = 105, sq = 1, r = { { 2841, 4 } }, tool = 162, out = { 2867, 1 }, oq = 2 },
    [2673] = { name = "Silvered Bronze Breastplate", t = { 1, 135, 150, 165 }, scroll = 5578, train = 105, sq = 2, r = { { 2841, 10 }, { 2842, 2 }, { 3478, 2 }, { 1705, 1 } }, tool = 162, out = { 2869, 1 }, oq = 2 },
    [2737] = { name = "Copper Mace", t = { 1, 55, 75, 95 }, fee = 50, train = 15, r = { { 2840, 6 }, { 2880, 1 }, { 2589, 2 } }, tool = 162, out = { 2844, 1 }, oq = 1 },
    [2738] = { name = "Copper Axe", t = { 1, 60, 80, 100 }, fee = 50, train = 20, r = { { 2840, 6 }, { 2880, 1 }, { 2589, 2 } }, tool = 162, out = { 2845, 1 }, oq = 1 },
    [3115] = { name = "Rough Weightstone", t = { 1, 15, 35, 55 }, basic = true, r = { { 2835, 1 } }, out = { 3239, 1 }, oq = 1 },
    [3116] = { name = "Coarse Weightstone", t = { 1, 40, 47, 55 }, fee = 100, train = 40, r = { { 2836, 1 } }, out = { 3240, 1 }, oq = 1 },
    [3117] = { name = "Heavy Weightstone", t = { 1, 100, 107, 115 }, fee = 1000, train = 100, r = { { 2838, 1 } }, out = { 3241, 1 }, oq = 1 },
    [3292] = { name = "Heavy Copper Broadsword", t = { 1, 110, 130, 150 }, fee = 500, train = 70, r = { { 2840, 14 }, { 2880, 2 }, { 818, 2 }, { 2319, 2 } }, tool = 162, out = { 3487, 1 }, oq = 2 },
    [3293] = { name = "Copper Battle Axe", t = { 1, 70, 90, 110 }, fee = 250, train = 30, r = { { 2840, 12 }, { 2880, 2 }, { 774, 2 }, { 3470, 2 }, { 2318, 2 } }, tool = 162, out = { 3488, 1 }, oq = 2 },
    [3294] = { name = "Thick War Axe", t = { 1, 85, 105, 125 }, fee = 500, train = 45, r = { { 2840, 10 }, { 2880, 2 }, { 2842, 2 }, { 3470, 2 }, { 2318, 2 } }, tool = 162, out = { 3489, 1 }, oq = 2 },
    [3295] = { name = "Deadly Bronze Poniard", t = { 1, 130, 145, 160 }, scroll = 2883, train = 100, sq = 2, r = { { 2841, 4 }, { 3466, 1 }, { 2459, 1 }, { 1210, 2 }, { 3478, 2 }, { 2319, 2 } }, tool = 162, out = { 3490, 1 }, oq = 2 },
    [3296] = { name = "Heavy Bronze Mace", t = { 1, 135, 150, 165 }, fee = 1000, train = 105, r = { { 2841, 8 }, { 3466, 1 }, { 1206, 1 }, { 1210, 1 }, { 3478, 2 }, { 2319, 2 } }, tool = 162, out = { 3491, 1 }, oq = 2 },
    [3297] = { name = "Mighty Iron Hammer", t = { 1, 150, 165, 180 }, scroll = 3608, train = 120, sq = 2, r = { { 3575, 6 }, { 3466, 2 }, { 3391, 1 }, { 1705, 2 }, { 3478, 2 }, { 2319, 2 } }, tool = 162, out = { 3492, 1 }, oq = 2 },
    [3319] = { name = "Copper Chain Boots", t = { 1, 60, 80, 100 }, fee = 50, train = 20, r = { { 2840, 8 } }, tool = 162, out = { 3469, 1 }, oq = 2 },
    [3320] = { name = "Rough Grinding Stone", t = { 1, 45, 65, 85 }, fee = 100, train = 25, r = { { 2835, 2 } }, out = { 3470, 1 }, oq = 1 },
    [3321] = { name = "Copper Chain Vest", t = { 1, 70, 90, 110 }, scroll = 3609, train = 30, sq = 2, r = { { 2840, 8 }, { 774, 1 }, { 3470, 2 } }, tool = 162, out = { 3471, 1 }, oq = 2 },
    [3323] = { name = "Runed Copper Gauntlets", t = { 1, 75, 95, 115 }, fee = 100, train = 35, r = { { 2840, 8 }, { 3470, 2 } }, tool = 162, out = { 3472, 1 }, oq = 2 },
    [3324] = { name = "Runed Copper Pants", t = { 1, 75, 95, 115 }, fee = 200, train = 35, r = { { 2840, 8 }, { 2320, 3 }, { 3470, 3 } }, tool = 162, out = { 3473, 1 }, oq = 2 },
    [3325] = { name = "Gemmed Copper Gauntlets", t = { 1, 75, 95, 115 }, scroll = 3610, train = 35, sq = 2, r = { { 2840, 8 }, { 818, 1 }, { 774, 1 } }, tool = 162, out = { 3474, 1 }, oq = 2 },
    [3326] = { name = "Coarse Grinding Stone", t = { 1, 50, 70, 90 }, fee = 250, train = 50, r = { { 2836, 2 } }, out = { 3478, 1 }, oq = 1 },
    [3328] = { name = "Rough Bronze Shoulders", t = { 1, 115, 130, 145 }, fee = 500, train = 85, r = { { 2841, 5 }, { 1210, 1 }, { 3478, 1 } }, tool = 162, out = { 3480, 1 }, oq = 2 },
    [3330] = { name = "Silvered Bronze Shoulders", t = { 1, 130, 145, 160 }, scroll = 2882, train = 100, sq = 2, r = { { 2841, 8 }, { 2842, 2 }, { 3478, 2 } }, tool = 162, out = { 3481, 1 }, oq = 2 },
    [3331] = { name = "Silvered Bronze Boots", t = { 1, 135, 150, 165 }, fee = 500, train = 105, r = { { 2841, 6 }, { 2842, 1 }, { 3478, 2 } }, tool = 162, out = { 3482, 1 }, oq = 2 },
    [3333] = { name = "Silvered Bronze Gauntlets", t = { 1, 140, 155, 170 }, fee = 1000, train = 110, r = { { 2841, 8 }, { 2842, 1 }, { 3478, 2 } }, tool = 162, out = { 3483, 1 }, oq = 2 },
    [3334] = { name = "Green Iron Boots", t = { 1, 150, 165, 180 }, scroll = 3611, train = 120, sq = 2, r = { { 3575, 4 }, { 1705, 2 }, { 3478, 2 }, { 2605, 1 } }, tool = 162, out = { 3484, 1 }, oq = 2 },
    [3336] = { name = "Green Iron Gauntlets", t = { 1, 155, 170, 185 }, scroll = 3612, train = 125, sq = 2, r = { { 3575, 4 }, { 5498, 2 }, { 3478, 2 }, { 2605, 1 } }, tool = 162, out = { 3485, 1 }, oq = 2 },
    [3337] = { name = "Heavy Grinding Stone", t = { 1, 100, 112, 125 }, fee = 1000, train = 100, r = { { 2838, 3 } }, out = { 3486, 1 }, oq = 1 },
    [3491] = { name = "Big Bronze Knife", t = { 1, 110, 125, 140 }, fee = 600, train = 80, r = { { 2841, 6 }, { 2880, 4 }, { 3470, 2 }, { 818, 1 }, { 2319, 1 } }, tool = 162, out = { 3848, 1 }, oq = 2 },
    [3492] = { name = "Hardened Iron Shortsword", t = { 1, 160, 172, 185 }, scroll = 12162, train = 135, scrollPrice = 3000, sq = 1, r = { { 3575, 6 }, { 3466, 2 }, { 3486, 1 }, { 1705, 2 }, { 4234, 3 } }, tool = 162, out = { 3849, 1 }, oq = 2 },
    [3493] = { name = "Jade Serpentblade", t = { 1, 175, 187, 200 }, scroll = 3866, train = 150, sq = 2, r = { { 3575, 8 }, { 3466, 2 }, { 3486, 2 }, { 1529, 2 }, { 4234, 3 } }, tool = 162, out = { 3850, 1 }, oq = 2 },
    [3494] = { name = "Solid Iron Maul", t = { 1, 155, 167, 180 }, scroll = 10858, train = 130, scrollPrice = 3000, sq = 1, r = { { 3575, 8 }, { 3466, 2 }, { 3486, 1 }, { 2842, 4 }, { 4234, 2 } }, tool = 162, out = { 3851, 1 }, oq = 2 },
    [3495] = { name = "Golden Iron Destroyer", t = { 1, 170, 182, 195 }, scroll = 3867, train = 145, sq = 2, r = { { 3575, 10 }, { 3577, 4 }, { 1705, 2 }, { 3466, 2 }, { 4234, 2 }, { 3486, 2 } }, tool = 162, out = { 3852, 1 }, oq = 2 },
    [3496] = { name = "Moonsteel Broadsword", t = { 1, 180, 192, 205 }, scroll = 12163, train = 155, scrollPrice = 4400, sq = 1, r = { { 3859, 8 }, { 3466, 2 }, { 3486, 2 }, { 1705, 3 }, { 4234, 3 } }, tool = 162, out = { 3853, 1 }, oq = 2 },
    [3497] = { name = "Frost Tiger Blade", t = { 1, 200, 212, 225 }, scroll = 3868, train = 175, sq = 2, r = { { 3859, 8 }, { 3466, 2 }, { 3486, 2 }, { 1529, 2 }, { 3829, 1 }, { 4234, 4 } }, tool = 162, out = { 3854, 1 }, oq = 2 },
    [3498] = { name = "Massive Iron Axe", t = { 1, 185, 197, 210 }, scroll = 12164, train = 160, scrollPrice = 4400, sq = 1, r = { { 3575, 14 }, { 3466, 2 }, { 3486, 2 }, { 3577, 4 }, { 4234, 2 } }, tool = 162, out = { 3855, 1 }, oq = 2 },
    [3500] = { name = "Shadow Crescent Axe", t = { 1, 200, 212, 225 }, scroll = 3869, train = 175, sq = 2, r = { { 3859, 10 }, { 3466, 2 }, { 3486, 3 }, { 3864, 2 }, { 3824, 1 }, { 4234, 3 } }, tool = 162, out = { 3856, 1 }, oq = 2 },
    [3501] = { name = "Green Iron Bracers", t = { 1, 165, 177, 190 }, fee = 1000, train = 140, tr = { 2836, 3355, 4258 }, r = { { 3575, 6 }, { 2605, 1 } }, tool = 162, out = { 3835, 1 }, oq = 2 },
    [3502] = { name = "Green Iron Helm", t = { 1, 170, 182, 195 }, fee = 1250, train = 145, tr = { 2836, 3355, 4258 }, r = { { 3575, 12 }, { 3864, 1 }, { 2605, 1 } }, tool = 162, out = { 3836, 1 }, oq = 2 },
    [3503] = { name = "Golden Scale Coif", t = { 1, 190, 202, 215 }, scroll = 6047, train = 165, scrollPrice = 4400, sq = 1, r = { { 3859, 8 }, { 3577, 2 }, { 3486, 2 } }, tool = 162, out = { 3837, 1 }, oq = 2 },
    [3504] = { name = "Green Iron Shoulders", t = { 1, 160, 172, 185 }, scroll = 3870, train = 135, sq = 2, r = { { 3575, 7 }, { 3486, 1 }, { 2605, 1 } }, tool = 162, out = { 3840, 1 }, oq = 2 },
    [3505] = { name = "Golden Scale Shoulders", t = { 1, 175, 187, 200 }, scroll = 3871, train = 150, sq = 3, r = { { 3859, 6 }, { 3577, 2 }, { 3486, 1 } }, tool = 162, out = { 3841, 1 }, oq = 2 },
    [3506] = { name = "Green Iron Leggings", t = { 1, 155, 167, 180 }, fee = 5000, train = 130, tr = { 2836, 3355, 4258 }, r = { { 3575, 8 }, { 3486, 1 }, { 2605, 1 } }, tool = 162, out = { 3842, 1 }, oq = 2 },
    [3507] = { name = "Golden Scale Leggings", t = { 1, 170, 182, 195 }, scroll = 3872, train = 145, sq = 2, r = { { 3575, 10 }, { 3577, 2 }, { 3486, 1 } }, tool = 162, out = { 3843, 1 }, oq = 2 },
    [3508] = { name = "Green Iron Hauberk", t = { 1, 180, 192, 205 }, fee = 7500, train = 155, r = { { 3575, 20 }, { 3486, 4 }, { 1529, 2 }, { 1206, 2 }, { 4255, 1 } }, tool = 162, out = { 3844, 1 }, oq = 3 },
    [3511] = { name = "Golden Scale Cuirass", t = { 1, 195, 207, 220 }, scroll = 3873, train = 170, sq = 2, r = { { 3859, 12 }, { 3577, 2 }, { 3486, 4 }, { 1529, 2 } }, tool = 162, out = { 3845, 1 }, oq = 2 },
    [3513] = { name = "Polished Steel Boots", t = { 1, 185, 197, 210 }, scroll = 3874, train = 160, sq = 2, r = { { 3859, 8 }, { 3864, 1 }, { 1705, 1 }, { 3486, 2 } }, tool = 162, out = { 3846, 1 }, oq = 2 },
    [3515] = { name = "Golden Scale Boots", t = { 1, 200, 212, 225 }, scroll = 3875, train = 175, sq = 3, r = { { 3859, 10 }, { 3577, 4 }, { 3486, 4 }, { 3864, 1 } }, tool = 162, out = { 3847, 1 }, oq = 2 },
    [6517] = { name = "Pearl-handled Dagger", t = { 1, 115, 130, 145 }, fee = 800, train = 85, r = { { 2841, 6 }, { 3466, 1 }, { 5498, 2 }, { 3478, 2 } }, tool = 162, out = { 5540, 1 }, oq = 2 },
    [6518] = { name = "Iridescent Hammer", t = { 1, 145, 160, 175 }, scroll = 5543, train = 115, sq = 2, r = { { 2841, 10 }, { 3466, 1 }, { 5500, 1 }, { 3478, 2 }, { 2319, 2 } }, tool = 162, out = { 5541, 1 }, oq = 2 },
    [7221] = { name = "Iron Shield Spike", t = { 1, 155, 170, 185 }, scroll = 6044, train = 125, sq = 2, r = { { 3575, 6 }, { 3478, 4 } }, tool = 162, out = { 6042, 1 }, oq = 1 },
    [7222] = { name = "Iron Counterweight", t = { 1, 165, 177, 190 }, scroll = 6045, train = 140, sq = 2, r = { { 3575, 4 }, { 3478, 2 }, { 1705, 1 } }, tool = 162, out = { 6043, 1 }, oq = 1 },
    [7223] = { name = "Golden Scale Bracers", t = { 1, 185, 197, 210 }, fee = 1000, train = 160, r = { { 3859, 5 }, { 3486, 2 } }, tool = 162, out = { 6040, 1 }, oq = 2 },
    [7224] = { name = "Steel Weapon Chain", t = { 1, 190, 202, 215 }, scroll = 6046, train = 165, sq = 2, r = { { 3859, 8 }, { 3486, 2 }, { 4234, 4 } }, tool = 162, out = { 6041, 1 }, oq = 1 },
    [7408] = { name = "Heavy Copper Maul", t = { 1, 80, 100, 120 }, fee = 300, train = 40, r = { { 2840, 12 }, { 2880, 2 }, { 2318, 2 } }, tool = 162, out = { 6214, 1 }, oq = 2 },
    [7817] = { name = "Rough Bronze Boots", t = { 1, 100, 115, 130 }, fee = 200, train = 70, r = { { 2841, 6 }, { 3470, 6 } }, tool = 162, out = { 6350, 1 }, oq = 2 },
    [7818] = { name = "Silver Rod", t = { 1, 80, 82, 85 }, fee = 100, train = 75, r = { { 2842, 1 }, { 3470, 2 } }, tool = 162, out = { 6338, 1 }, oq = 1 },
    [8366] = { name = "Ironforge Chain", t = { 1, 80, 100, 120 }, scroll = 6734, train = 70, sq = 1, r = { { 2840, 12 }, { 774, 2 }, { 3470, 2 } }, tool = 162, out = { 6730, 1 }, oq = 2 },
    [8367] = { name = "Ironforge Breastplate", t = { 1, 115, 135, 155 }, scroll = 6735, train = 100, sq = 2, r = { { 2840, 16 }, { 818, 2 }, { 3470, 3 } }, tool = 162, out = { 6731, 1 }, oq = 2 },
    [8368] = { name = "Ironforge Gauntlets", t = { 1, 140, 155, 170 }, scroll = 6736, train = 130, sq = 1, r = { { 2841, 8 }, { 1210, 3 }, { 3478, 4 } }, tool = 162, out = { 6733, 1 }, oq = 2 },
    [8768] = { name = "Iron Buckle", t = { 1, 125, 127, 130 }, fee = 250, train = 125, r = { { 3575, 1 } }, tool = 162, out = { 7071, 2 }, oq = 1 },
    [8880] = { name = "Copper Dagger", t = { 1, 65, 85, 105 }, fee = 100, train = 25, r = { { 2840, 6 }, { 2880, 1 }, { 3470, 1 }, { 2318, 1 } }, tool = 162, out = { 7166, 1 }, oq = 2 },
    [9811] = { name = "Barbaric Iron Shoulders", t = { 1, 160, 172, 185 }, scroll = 7978, train = 135, sq = 2, r = { { 3575, 8 }, { 5635, 4 }, { 1210, 2 }, { 3486, 2 } }, tool = 162, out = { 7913, 1 }, oq = 2 },
    [9813] = { name = "Barbaric Iron Breastplate", t = { 1, 160, 172, 185 }, scroll = 7979, train = 135, sq = 2, r = { { 3575, 20 }, { 3486, 4 } }, tool = 162, out = { 7914, 1 }, oq = 2 },
    [9814] = { name = "Barbaric Iron Helm", t = { 1, 175, 187, 200 }, scroll = 7980, train = 150, sq = 2, r = { { 3575, 10 }, { 5637, 2 }, { 5635, 2 } }, tool = 162, out = { 7915, 1 }, oq = 2 },
    [9818] = { name = "Barbaric Iron Boots", t = { 1, 180, 192, 205 }, scroll = 7981, train = 155, sq = 2, r = { { 3575, 12 }, { 5637, 4 }, { 818, 4 }, { 3486, 2 } }, tool = 162, out = { 7916, 1 }, oq = 2 },
    [9820] = { name = "Barbaric Iron Gloves", t = { 1, 185, 197, 210 }, scroll = 7982, train = 160, sq = 2, r = { { 3575, 14 }, { 3486, 3 }, { 5637, 2 } }, tool = 162, out = { 7917, 1 }, oq = 2 },
    [9916] = { name = "Steel Breastplate", t = { 1, 200, 212, 225 }, fee = 2500, train = 175, r = { { 3859, 16 }, { 3486, 3 } }, tool = 162, out = { 7963, 1 }, oq = 2 },
    [9918] = { name = "Solid Sharpening Stone", t = { 1, 175, 180, 185 }, fee = 2500, train = 175, r = { { 7912, 1 } }, out = { 7964, 1 }, oq = 1 },
    [9920] = { name = "Solid Grinding Stone", t = { 1, 175, 180, 185 }, fee = 2500, train = 175, r = { { 7912, 4 } }, out = { 7966, 1 }, oq = 1 },
    [9921] = { name = "Solid Weightstone", t = { 1, 175, 180, 185 }, fee = 2500, train = 175, r = { { 7912, 1 } }, out = { 7965, 1 }, oq = 1 },
    [9926] = { name = "Heavy Mithril Shoulder", t = { 1, 200, 210, 220 }, fee = 5000, train = 180, r = { { 3860, 8 }, { 4234, 6 } }, tool = 162, out = { 7918, 1 }, oq = 2 },
    [9928] = { name = "Heavy Mithril Gauntlet", t = { 1, 200, 210, 220 }, fee = 5000, train = 180, r = { { 3860, 6 }, { 4338, 4 } }, tool = 162, out = { 7919, 1 }, oq = 2 },
    [9931] = { name = "Mithril Plate Pants", t = { 1, 205, 215, 225 }, fee = 5000, train = 185, r = { { 3860, 12 } }, tool = 162, out = { 7920, 1 }, oq = 2 },
    [9933] = { name = "Heavy Mithril Pants", t = { 1, 205, 215, 225 }, scroll = 7975, train = 185, sq = 2, r = { { 3860, 10 }, { 1705, 2 } }, tool = 162, out = { 7921, 1 }, oq = 2 },
    [9935] = { name = "Steel Plate Helm", t = { 1, 210, 220, 230 }, fee = 5000, train = 190, r = { { 3859, 14 }, { 7966, 1 } }, tool = 162, out = { 7922, 1 }, oq = 2 },
    [9937] = { name = "Mithril Plate Bracers", t = { 1, 210, 220, 230 }, scroll = 7995, train = 190, scrollPrice = 6000, sq = 1, r = { { 3860, 8 }, { 3864, 2 } }, tool = 162, out = { 7924, 1 }, oq = 2 },
    [9939] = { name = "Mithril Shield Spike", t = { 1, 210, 220, 230 }, scroll = 7976, train = 190, sq = 3, r = { { 3860, 4 }, { 6037, 2 }, { 7966, 4 } }, tool = 162, out = { 7967, 1 }, oq = 2 },
    [9942] = { name = "Mithril Plate Gloves", t = { 1, 215, 225, 235 }, scroll = 7977, train = 205, sq = 1, r = { { 3860, 8 }, { 4234, 6 }, { 4338, 4 } }, tool = 162, out = { 7925, 1 }, oq = 2 },
    [9945] = { name = "Ornate Mithril Pants", t = { 1, 215, 225, 235 }, scroll = 7983, train = 195, sq = 2, r = { { 3860, 12 }, { 6037, 1 }, { 7966, 1 }, { 7909, 1 } }, tool = 162, out = { 7926, 1 }, oq = 2 },
    [9950] = { name = "Ornate Mithril Gloves", t = { 1, 215, 225, 235 }, scroll = 7984, train = 195, sq = 2, r = { { 3860, 10 }, { 4338, 6 }, { 6037, 1 }, { 7966, 1 } }, tool = 162, out = { 7927, 1 }, oq = 2 },
    [9952] = { name = "Ornate Mithril Shoulders", t = { 1, 220, 230, 240 }, scroll = 7985, train = 200, sq = 2, r = { { 3860, 12 }, { 6037, 1 }, { 4304, 6 } }, tool = 162, out = { 7928, 1 }, oq = 2 },
    [9954] = { name = "Truesilver Gauntlets", t = { 1, 220, 230, 240 }, fee = 10000, train = 200, spec = "Armorsmith", tr = { 7230 }, r = { { 3860, 10 }, { 6037, 8 }, { 7909, 3 }, { 3864, 3 }, { 5966, 1 }, { 7966, 2 } }, tool = 162, out = { 7938, 1 }, oq = 3 },
    [9957] = { name = "Orcish War Leggings", t = { 1, 225, 235, 245 }, scroll = 7994, train = 215, sq = 1, r = { { 3860, 12 }, { 7067, 1 } }, tool = 162, out = { 7929, 1 }, oq = 2 },
    [9959] = { name = "Heavy Mithril Breastplate", t = { 1, 225, 235, 245 }, fee = 15000, train = 205, tr = { 2836 }, r = { { 3860, 16 } }, tool = 162, out = { 7930, 1 }, oq = 2 },
    [9961] = { name = "Mithril Coif", t = { 1, 225, 235, 245 }, fee = 15000, train = 205, tr = { 2836 }, r = { { 3860, 10 }, { 4338, 6 } }, tool = 162, out = { 7931, 1 }, oq = 2 },
    [9964] = { name = "Mithril Spurs", t = { 1, 230, 240, 250 }, scroll = 7989, train = 210, sq = 2, r = { { 3860, 4 }, { 7966, 3 } }, tool = 162, out = { 7969, 1 }, oq = 2 },
    [9966] = { name = "Mithril Plate Shoulders", t = { 1, 230, 240, 250 }, scroll = 7991, train = 210, sq = 3, r = { { 3860, 14 }, { 4304, 4 }, { 3864, 4 } }, tool = 162, out = { 7932, 1 }, oq = 2 },
    [9968] = { name = "Heavy Mithril Boots", t = { 1, 230, 240, 250 }, fee = 20000, train = 210, tr = { 2836 }, r = { { 3860, 14 }, { 4304, 4 } }, tool = 162, out = { 7933, 1 }, oq = 2 },
    [9970] = { name = "Heavy Mithril Helm", t = { 1, 230, 240, 250 }, scroll = 7990, train = 220, sq = 2, r = { { 3860, 14 }, { 7909, 1 } }, tool = 162, out = { 7934, 1 }, oq = 2 },
    [9972] = { name = "Ornate Mithril Breastplate", t = { 1, 235, 245, 255 }, scroll = 7986, train = 225, sq = 1, r = { { 3860, 16 }, { 6037, 6 }, { 7077, 1 }, { 7966, 1 } }, tool = 162, out = { 7935, 1 }, oq = 2 },
    [9974] = { name = "Truesilver Breastplate", t = { 1, 240, 250, 260 }, fee = 10000, train = 220, spec = "Armorsmith", tr = { 7230 }, r = { { 3860, 12 }, { 6037, 24 }, { 7910, 4 }, { 7971, 4 }, { 7966, 2 } }, tool = 162, out = { 7939, 1 }, oq = 3 },
    [9979] = { name = "Ornate Mithril Boots", t = { 1, 240, 250, 260 }, scroll = 7988, train = 230, sq = 1, r = { { 3860, 14 }, { 6037, 2 }, { 4304, 4 }, { 7966, 1 }, { 7909, 1 } }, tool = 162, out = { 7936, 1 }, oq = 2 },
    [9980] = { name = "Ornate Mithril Helm", t = { 1, 240, 250, 260 }, scroll = 7987, train = 230, sq = 1, r = { { 3860, 16 }, { 6037, 2 }, { 7971, 1 }, { 7966, 1 } }, tool = 162, out = { 7937, 1 }, oq = 2 },
    [9983] = { name = "Copper Claymore", t = { 1, 65, 85, 105 }, fee = 100, train = 25, r = { { 2840, 10 }, { 2880, 2 }, { 3470, 1 }, { 2318, 1 } }, tool = 162, out = { 7955, 1 }, oq = 2 },
    [9985] = { name = "Bronze Warhammer", t = { 1, 155, 170, 185 }, fee = 250, train = 100, r = { { 2841, 8 }, { 3466, 1 }, { 2319, 1 } }, tool = 162, out = { 7956, 1 }, oq = 2 },
    [9986] = { name = "Bronze Greatsword", t = { 1, 135, 150, 165 }, fee = 500, train = 105, r = { { 2841, 12 }, { 3466, 2 }, { 2319, 2 } }, tool = 162, out = { 7957, 1 }, oq = 2 },
    [9987] = { name = "Bronze Battle Axe", t = { 1, 140, 155, 170 }, fee = 500, train = 110, r = { { 2841, 14 }, { 3466, 1 }, { 2319, 2 } }, tool = 162, out = { 7958, 1 }, oq = 2 },
    [9993] = { name = "Heavy Mithril Axe", t = { 1, 210, 222, 235 }, fee = 10000, train = 185, r = { { 3860, 12 }, { 3864, 2 }, { 7966, 1 }, { 4234, 4 } }, tool = 162, out = { 7941, 1 }, oq = 2 },
    [9995] = { name = "Blue Glittering Axe", t = { 1, 220, 232, 245 }, scroll = 7992, train = 195, sq = 2, r = { { 3860, 16 }, { 7909, 2 }, { 7966, 1 }, { 4304, 4 } }, tool = 162, out = { 7942, 1 }, oq = 2 },
    [9997] = { name = "Wicked Mithril Blade", t = { 1, 225, 237, 250 }, scroll = 8029, train = 200, sq = 2, r = { { 3860, 14 }, { 6037, 4 }, { 7966, 1 }, { 4304, 2 } }, tool = 162, out = { 7943, 1 }, oq = 2 },
    [10001] = { name = "Big Black Mace", t = { 1, 230, 242, 255 }, fee = 15000, train = 205, tr = { 2836 }, r = { { 3860, 16 }, { 7971, 1 }, { 1210, 4 }, { 7966, 1 }, { 4304, 2 } }, tool = 162, out = { 7945, 1 }, oq = 2 },
    [10003] = { name = "The Shatterer", t = { 1, 235, 247, 260 }, gone = true, r = { { 3860, 24 }, { 7075, 4 }, { 6037, 6 }, { 3864, 5 }, { 1529, 5 }, { 7966, 4 }, { 4304, 4 } }, tool = 162, out = { 7954, 1 }, oq = 3 },
    [10005] = { name = "Dazzling Mithril Rapier", t = { 1, 240, 252, 265 }, scroll = 7993, train = 215, sq = 2, r = { { 3860, 14 }, { 7909, 1 }, { 1705, 2 }, { 1206, 2 }, { 7966, 1 }, { 4338, 2 } }, tool = 162, out = { 7944, 1 }, oq = 2 },
    [10007] = { name = "Phantom Blade", t = { 1, 245, 257, 270 }, gone = true, r = { { 3860, 28 }, { 7081, 6 }, { 6037, 8 }, { 3823, 2 }, { 7909, 6 }, { 7966, 4 }, { 4304, 2 } }, tool = 162, out = { 7961, 1 }, oq = 3 },
    [10009] = { name = "Runed Mithril Hammer", t = { 1, 245, 257, 270 }, scroll = 8028, train = 220, sq = 3, r = { { 3860, 18 }, { 7075, 2 }, { 7966, 1 }, { 4304, 4 } }, tool = 162, out = { 7946, 1 }, oq = 2 },
    [10011] = { name = "Blight", t = { 1, 250, 262, 275 }, gone = true, r = { { 3860, 28 }, { 7972, 10 }, { 6037, 10 }, { 7966, 6 }, { 4304, 6 } }, tool = 162, out = { 7959, 1 }, oq = 3 },
    [10013] = { name = "Ebon Shiv", t = { 1, 255, 267, 280 }, scroll = 8030, train = 230, scrollPrice = 10000, sq = 1, r = { { 3860, 12 }, { 6037, 6 }, { 7910, 2 }, { 7966, 1 }, { 4304, 2 } }, tool = 162, out = { 7947, 1 }, oq = 2 },
    [10015] = { name = "Truesilver Champion", t = { 1, 260, 272, 285 }, gone = true, r = { { 3860, 30 }, { 6037, 16 }, { 7910, 6 }, { 7081, 4 }, { 7966, 8 }, { 4304, 6 } }, tool = 162, out = { 7960, 1 }, oq = 3 },
    [11454] = { name = "Inlaid Mithril Cylinder", t = { 1, 200, 212, 225 }, scroll = 10713, train = 200, sq = 1, r = { { 3860, 5 }, { 3577, 1 }, { 6037, 1 } }, tool = 162, out = { 9060, 1 }, oq = 1 },
    [11643] = { name = "Golden Scale Gauntlets", t = { 1, 200, 210, 220 }, scroll = 9367, train = 180, sq = 2, r = { { 3859, 10 }, { 3577, 4 }, { 3486, 4 }, { 3864, 1 } }, tool = 162, out = { 9366, 1 }, oq = 2 },
    [12259] = { name = "Silvered Bronze Leggings", t = { 1, 155, 167, 180 }, scroll = 10424, train = 130, sq = 2, r = { { 2841, 12 }, { 2842, 4 }, { 3478, 2 } }, tool = 162, out = { 10423, 1 }, oq = 2 },
    [12260] = { name = "Rough Copper Vest", t = { 1, 15, 35, 55 }, basic = true, r = { { 2840, 4 } }, tool = 162, out = { 10421, 1 }, oq = 2 },
    [14379] = { name = "Golden Rod", t = { 1, 130, 132, 135 }, fee = 250, train = 125, r = { { 3577, 1 }, { 3478, 2 } }, tool = 162, out = { 11128, 1 }, oq = 1 },
    [14380] = { name = "Truesilver Rod", t = { 1, 180, 182, 185 }, fee = 2500, train = 175, r = { { 6037, 1 }, { 3486, 1 } }, tool = 162, out = { 11144, 1 }, oq = 1 },
    [15292] = { name = "Dark Iron Pulverizer", t = { 1, 260, 270, 280 }, scroll = 11610, train = 240, sq = 3, r = { { 11371, 18 }, { 7077, 4 } }, tool = 162, out = { 11608, 1 }, oq = 3 },
    [15293] = { name = "Dark Iron Mail", t = { 1, 265, 275, 285 }, scroll = 11614, train = 245, sq = 2, r = { { 11371, 10 }, { 7077, 2 } }, tool = 162, out = { 11606, 1 }, oq = 2 },
    [15294] = { name = "Dark Iron Sunderer", t = { 1, 270, 280, 290 }, scroll = 11611, train = 250, sq = 3, r = { { 11371, 26 }, { 7077, 4 } }, tool = 162, out = { 11607, 1 }, oq = 3 },
    [15295] = { name = "Dark Iron Shoulders", t = { 1, 275, 285, 295 }, scroll = 11615, train = 255, sq = 2, r = { { 11371, 6 }, { 7077, 1 } }, tool = 162, out = { 11605, 1 }, oq = 2 },
    [15296] = { name = "Dark Iron Plate", t = { 1, 280, 290, 300 }, scroll = 11612, train = 260, sq = 3, r = { { 11371, 20 }, { 7077, 8 } }, tool = 162, out = { 11604, 1 }, oq = 3, bop = true },
    [15972] = { name = "Glinting Steel Dagger", t = { 1, 180, 192, 205 }, fee = 7500, train = 155, r = { { 3859, 10 }, { 3466, 2 }, { 1206, 1 }, { 7067, 1 }, { 4234, 1 } }, tool = 162, out = { 12259, 1 }, oq = 2 },
    [15973] = { name = "Searing Golden Blade", t = { 1, 190, 202, 215 }, scroll = 12261, train = 165, sq = 2, r = { { 3859, 10 }, { 3577, 4 }, { 7068, 2 }, { 4234, 2 } }, tool = 162, out = { 12260, 1 }, oq = 2 },
    [16639] = { name = "Dense Grinding Stone", t = { 1, 230, 232, 235 }, fee = 10000, train = 225, tr = { 2836 }, r = { { 12365, 4 } }, out = { 12644, 1 }, oq = 1 },
    [16640] = { name = "Dense Weightstone", t = { 1, 230, 232, 235 }, fee = 10000, train = 225, tr = { 2836 }, r = { { 12365, 1 } }, out = { 12643, 1 }, oq = 1 },
    [16641] = { name = "Dense Sharpening Stone", t = { 1, 230, 232, 235 }, fee = 10000, train = 225, tr = { 2836 }, r = { { 12365, 1 } }, out = { 12404, 1 }, oq = 1 },
    [16642] = { name = "Thorium Armor", t = { 1, 245, 255, 265 }, scroll = 12682, train = 225, sq = 2, r = { { 12359, 16 }, { 12361, 1 }, { 11188, 4 } }, tool = 162, out = { 12405, 1 }, oq = 2 },
    [16643] = { name = "Thorium Belt", t = { 1, 245, 255, 265 }, scroll = 12683, train = 225, sq = 2, r = { { 12359, 12 }, { 11186, 4 } }, tool = 162, out = { 12406, 1 }, oq = 2 },
    [16644] = { name = "Thorium Bracers", t = { 1, 250, 260, 270 }, scroll = 12684, train = 230, sq = 2, r = { { 12359, 12 }, { 11184, 4 } }, tool = 162, out = { 12408, 1 }, oq = 2 },
    [16645] = { name = "Radiant Belt", t = { 1, 255, 265, 275 }, scroll = 12685, train = 235, sq = 2, r = { { 12359, 10 }, { 7077, 2 } }, tool = 162, out = { 12416, 1 }, oq = 2 },
    [16646] = { name = "Imperial Plate Shoulders", t = { 1, 260, 270, 280 }, scroll = 12687, train = 240, sq = 2, r = { { 12359, 24 }, { 8170, 6 }, { 3864, 2 } }, tool = 162, out = { 12428, 1 }, oq = 2 },
    [16647] = { name = "Imperial Plate Belt", t = { 1, 260, 270, 280 }, scroll = 12688, train = 240, sq = 2, r = { { 12359, 22 }, { 8170, 6 }, { 7909, 1 } }, tool = 162, out = { 12424, 1 }, oq = 2 },
    [16648] = { name = "Radiant Breastplate", t = { 1, 265, 275, 285 }, scroll = 12689, train = 245, sq = 2, r = { { 12359, 18 }, { 7077, 2 }, { 7910, 1 } }, tool = 162, out = { 12415, 1 }, oq = 2 },
    [16649] = { name = "Imperial Plate Bracers", t = { 1, 265, 275, 285 }, scroll = 12690, train = 245, sq = 2, r = { { 12359, 20 }, { 7910, 1 } }, tool = 162, out = { 12425, 1 }, oq = 2 },
    [16651] = { name = "Thorium Shield Spike", t = { 1, 270, 280, 290 }, scroll = 12692, train = 250, sq = 2, r = { { 12359, 4 }, { 12644, 4 }, { 7076, 2 } }, tool = 162, out = { 12645, 1 }, oq = 2 },
    [16652] = { name = "Thorium Boots", t = { 1, 275, 285, 295 }, scroll = 12693, train = 255, sq = 2, r = { { 12359, 20 }, { 8170, 8 }, { 11185, 4 } }, tool = 162, out = { 12409, 1 }, oq = 2 },
    [16653] = { name = "Thorium Helm", t = { 1, 275, 285, 295 }, scroll = 12694, train = 255, sq = 2, r = { { 12359, 24 }, { 7910, 1 }, { 11188, 4 } }, tool = 162, out = { 12410, 1 }, oq = 2 },
    [16654] = { name = "Radiant Gloves", t = { 1, 280, 290, 300 }, scroll = 12695, train = 260, sq = 2, r = { { 12359, 18 }, { 7077, 4 } }, tool = 162, out = { 12418, 1 }, oq = 2 },
    [16655] = { name = "Fiery Plate Gauntlets", t = { 1, 285, 295, 305 }, scroll = 12699, train = 265, sq = 3, r = { { 12359, 20 }, { 12655, 6 }, { 7078, 2 }, { 7910, 4 } }, tool = 162, out = { 12631, 1 }, oq = 3 },
    [16656] = { name = "Radiant Boots", t = { 1, 285, 295, 305 }, scroll = 12697, train = 265, sq = 2, r = { { 12359, 14 }, { 7077, 4 } }, tool = 162, out = { 12419, 1 }, oq = 2 },
    [16657] = { name = "Imperial Plate Boots", t = { 1, 290, 300, 310 }, scroll = 12700, train = 270, sq = 2, r = { { 12359, 34 }, { 7910, 1 }, { 7909, 1 } }, tool = 162, out = { 12426, 1 }, oq = 2 },
    [16658] = { name = "Imperial Plate Helm", t = { 1, 290, 300, 310 }, scroll = 12701, train = 270, sq = 2, r = { { 12359, 34 }, { 7910, 2 } }, tool = 162, out = { 12427, 1 }, oq = 2 },
    [16659] = { name = "Radiant Circlet", t = { 1, 290, 300, 310 }, scroll = 12702, train = 270, sq = 2, r = { { 12359, 18 }, { 7077, 4 } }, tool = 162, out = { 12417, 1 }, oq = 2 },
    [16660] = { name = "Dawnbringer Shoulders", t = { 1, 285, 295, 305 }, scroll = 12698, train = 265, scrollPrice = 22000, rep = { 529, 6 }, sq = 3, r = { { 12359, 20 }, { 12360, 4 }, { 12364, 2 }, { 7080, 2 } }, tool = 162, out = { 12625, 1 }, oq = 3 },
    [16662] = { name = "Thorium Leggings", t = { 1, 295, 305, 315 }, scroll = 12704, train = 275, sq = 2, r = { { 12359, 26 }, { 11186, 4 } }, tool = 162, out = { 12414, 1 }, oq = 2 },
    [16663] = { name = "Imperial Plate Chest", t = { 1, 295, 305, 315 }, scroll = 12705, train = 275, sq = 2, r = { { 12359, 40 }, { 7910, 2 } }, tool = 162, out = { 12422, 1 }, oq = 2 },
    [16664] = { name = "Runic Plate Shoulders", t = { 1, 295, 305, 315 }, scroll = 12706, train = 275, sq = 2, r = { { 12359, 20 }, { 12360, 2 }, { 3577, 6 } }, tool = 162, out = { 12610, 1 }, oq = 2 },
    [16665] = { name = "Runic Plate Boots", t = { 1, 295, 305, 315 }, scroll = 12707, train = 275, sq = 2, r = { { 12359, 20 }, { 12360, 2 }, { 2842, 10 } }, tool = 162, out = { 12611, 1 }, oq = 2 },
    [16667] = { name = "Demon Forged Breastplate", t = { 1, 280, 290, 300 }, scroll = 12696, train = 260, sq = 3, r = { { 12359, 40 }, { 12662, 10 }, { 12361, 4 }, { 7910, 4 } }, tool = 162, out = { 12628, 1 }, oq = 1 },
    [16724] = { name = "Whitesoul Helm", t = { 1, 310, 320, 330 }, scroll = 12711, train = 290, sq = 3, r = { { 12359, 20 }, { 12655, 4 }, { 6037, 6 }, { 3577, 6 }, { 12800, 2 } }, tool = 162, out = { 12633, 1 }, oq = 3 },
    [16725] = { name = "Radiant Leggings", t = { 1, 300, 310, 320 }, scroll = 12713, train = 280, sq = 2, r = { { 12359, 20 }, { 7077, 4 } }, tool = 162, out = { 12420, 1 }, oq = 2 },
    [16726] = { name = "Runic Plate Helm", t = { 1, 300, 310, 320 }, scroll = 12714, train = 280, sq = 2, r = { { 12359, 30 }, { 12360, 2 }, { 6037, 2 }, { 12364, 1 } }, tool = 162, out = { 12612, 1 }, oq = 2 },
    [16729] = { name = "Lionheart Helm", t = { 1, 320, 330, 340 }, scroll = 12717, train = 300, sq = 4, r = { { 12359, 80 }, { 12360, 12 }, { 8146, 40 }, { 12361, 10 }, { 12800, 4 } }, tool = 162, out = { 12640, 1 }, oq = 4 },
    [16730] = { name = "Imperial Plate Leggings", t = { 1, 300, 310, 320 }, scroll = 12715, train = 280, sq = 2, r = { { 12359, 44 }, { 7910, 2 } }, tool = 162, out = { 12429, 1 }, oq = 2 },
    [16731] = { name = "Runic Breastplate", t = { 1, 305, 315, 325 }, scroll = 12718, train = 285, sq = 2, r = { { 12359, 40 }, { 12360, 2 }, { 7910, 1 } }, tool = 162, out = { 12613, 1 }, oq = 2 },
    [16732] = { name = "Runic Plate Leggings", t = { 1, 305, 315, 325 }, scroll = 12719, train = 285, sq = 2, r = { { 12359, 40 }, { 12360, 2 }, { 7910, 1 } }, tool = 162, out = { 12614, 1 }, oq = 2 },
    [16741] = { name = "Stronghold Gauntlets", t = { 1, 320, 330, 340 }, scroll = 228118, train = 300, sq = 4, r = { { 12360, 15 }, { 12655, 20 }, { 7076, 10 }, { 12361, 4 }, { 12799, 4 } }, tool = 162, out = { 12639, 1 }, oq = 4 },
    [16742] = { name = "Enchanted Thorium Helm", t = { 1, 320, 330, 340 }, scroll = 12725, train = 300, sq = 3, r = { { 12360, 6 }, { 12655, 16 }, { 7076, 6 }, { 12799, 2 }, { 12800, 1 } }, tool = 162, out = { 12620, 1 }, oq = 3 },
    [16744] = { name = "Enchanted Thorium Leggings", t = { 1, 320, 330, 340 }, scroll = 12726, train = 300, sq = 3, r = { { 12360, 10 }, { 12655, 20 }, { 7080, 6 }, { 12361, 2 }, { 12364, 1 } }, tool = 162, out = { 12619, 1 }, oq = 3 },
    [16745] = { name = "Enchanted Thorium Breastplate", t = { 1, 320, 330, 340 }, scroll = 12727, train = 300, sq = 3, r = { { 12360, 8 }, { 12655, 24 }, { 7076, 4 }, { 7080, 4 }, { 12364, 2 }, { 12800, 2 } }, tool = 162, out = { 12618, 1 }, oq = 3 },
    [16960] = { name = "Thorium Greatsword", t = { 1, 260, 272, 285 }, scroll = 12816, train = 250, sq = 1, r = { { 12359, 16 }, { 12644, 2 }, { 8170, 4 } }, tool = 162, out = { 12764, 1 }, oq = 2 },
    [16965] = { name = "Bleakwood Hew", t = { 1, 270, 282, 295 }, scroll = 12817, train = 260, sq = 1, r = { { 12359, 30 }, { 12803, 6 }, { 8153, 6 }, { 12799, 6 }, { 12644, 2 }, { 8170, 8 } }, tool = 162, out = { 12769, 1 }, oq = 3 },
    [16967] = { name = "Inlaid Thorium Hammer", t = { 1, 270, 282, 295 }, scroll = 12818, train = 260, sq = 1, r = { { 12359, 30 }, { 3577, 4 }, { 6037, 2 }, { 12361, 2 }, { 8170, 4 } }, tool = 162, out = { 12772, 1 }, oq = 2 },
    [16969] = { name = "Ornate Thorium Handaxe", t = { 1, 275, 287, 300 }, scroll = 12819, train = 250, scrollPrice = 16000, sq = 2, r = { { 12359, 20 }, { 12799, 2 }, { 12644, 2 }, { 8170, 4 } }, tool = 162, out = { 12773, 1 }, oq = 2, bop = true },
    [16970] = { name = "Dawn's Edge", t = { 1, 275, 287, 300 }, scroll = 12821, train = 250, sq = 3, r = { { 12359, 30 }, { 12655, 4 }, { 7910, 4 }, { 12361, 4 }, { 12644, 2 }, { 8170, 4 } }, tool = 162, out = { 12774, 1 }, oq = 3 },
    [16971] = { name = "Huge Thorium Battleaxe", t = { 1, 280, 292, 305 }, scroll = 12823, train = 255, scrollPrice = 20000, sq = 1, r = { { 12359, 40 }, { 12644, 6 }, { 8170, 6 } }, tool = 162, out = { 12775, 1 }, oq = 2 },
    [16973] = { name = "Enchanted Battlehammer", t = { 1, 280, 292, 305 }, scroll = 12824, train = 255, sq = 2, r = { { 12359, 20 }, { 12655, 6 }, { 12364, 2 }, { 12804, 4 }, { 8170, 4 } }, tool = 162, out = { 12776, 1 }, oq = 3 },
    [16978] = { name = "Blazing Rapier", t = { 1, 280, 292, 305 }, scroll = 12825, train = 255, sq = 2, r = { { 12655, 10 }, { 7078, 4 }, { 7077, 4 }, { 12800, 2 }, { 12644, 2 } }, tool = 162, out = { 12777, 1 }, oq = 3 },
    [16980] = { name = "Rune Edge", t = { 1, 285, 297, 310 }, scroll = 12826, train = 275, sq = 1, r = { { 12359, 30 }, { 12799, 2 }, { 12644, 2 }, { 8170, 4 } }, tool = 162, out = { 12779, 1 }, oq = 1 },
    [16983] = { name = "Serenity", t = { 1, 285, 297, 310 }, scroll = 12827, train = 260, sq = 2, r = { { 12655, 6 }, { 12360, 2 }, { 12804, 4 }, { 12799, 2 }, { 12361, 2 }, { 12364, 1 } }, tool = 162, out = { 12781, 1 }, oq = 3 },
    [16984] = { name = "Volcanic Hammer", t = { 1, 290, 302, 315 }, scroll = 12828, train = 265, sq = 2, r = { { 12359, 30 }, { 7077, 4 }, { 7910, 4 }, { 8170, 4 } }, tool = 162, out = { 12792, 1 }, oq = 2 },
    [16985] = { name = "Corruption", t = { 1, 290, 302, 315 }, scroll = 12830, train = 265, sq = 1, r = { { 12359, 40 }, { 12360, 2 }, { 12662, 16 }, { 12808, 8 }, { 12361, 2 }, { 12644, 2 }, { 8170, 4 } }, tool = 162, out = { 12782, 1 }, oq = 3, bop = true },
    [16986] = { name = "Blood Talon", t = { 1, 325, 337, 350 }, scroll = 12831, train = 315, sq = 1, r = { { 12655, 10 }, { 12360, 10 }, { 12662, 8 }, { 7910, 10 }, { 12644, 2 } }, tool = 162, out = { 12795, 1 }, oq = 3, bop = true },
    [16987] = { name = "Darkspear", t = { 1, 325, 337, 350 }, scroll = 12832, train = 315, sq = 1, r = { { 12655, 20 }, { 12804, 20 }, { 12364, 2 }, { 12800, 2 }, { 12644, 2 } }, tool = 162, out = { 12802, 1 }, oq = 3 },
    [16988] = { name = "Hammer of the Titans", t = { 1, 320, 330, 340 }, scroll = 12833, train = 300, sq = 3, r = { { 12359, 50 }, { 12360, 15 }, { 12809, 4 }, { 12810, 6 }, { 7076, 10 } }, tool = 162, out = { 12796, 1 }, oq = 3 },
    [16990] = { name = "Arcanite Champion", t = { 1, 320, 330, 340 }, scroll = 12834, train = 300, sq = 3, r = { { 12360, 15 }, { 12800, 8 }, { 12811, 1 }, { 12799, 4 }, { 12810, 8 }, { 12644, 2 } }, tool = 162, out = { 12790, 1 }, oq = 3 },
    [16991] = { name = "Annihilator", t = { 1, 295, 305, 315 }, scroll = 12835, train = 300, sq = 3, r = { { 12359, 40 }, { 12360, 12 }, { 12808, 10 }, { 12364, 8 }, { 12644, 2 }, { 12810, 4 } }, tool = 162, out = { 12798, 1 }, oq = 3 },
    [16992] = { name = "Frostguard", t = { 1, 320, 330, 340 }, scroll = 12836, train = 300, sq = 3, r = { { 12360, 18 }, { 12361, 8 }, { 12800, 8 }, { 7080, 4 }, { 12644, 2 }, { 12810, 4 } }, tool = 162, out = { 12797, 1 }, oq = 3 },
    [16993] = { name = "Masterwork Stormhammer", t = { 1, 320, 330, 340 }, scroll = 12837, train = 300, sq = 3, r = { { 12655, 20 }, { 12364, 8 }, { 12799, 8 }, { 7076, 6 }, { 12810, 4 } }, tool = 162, out = { 12794, 1 }, oq = 3 },
    [16994] = { name = "Arcanite Reaper", t = { 1, 320, 330, 340 }, scroll = 12838, train = 300, sq = 3, r = { { 12360, 20 }, { 12810, 6 }, { 12644, 2 } }, tool = 162, out = { 12784, 1 }, oq = 3 },
    [16995] = { name = "Heartseeker", t = { 1, 320, 330, 340 }, scroll = 12839, train = 300, sq = 3, r = { { 12360, 10 }, { 12655, 10 }, { 12810, 2 }, { 7910, 6 }, { 12800, 6 }, { 12799, 6 }, { 12644, 4 } }, tool = 162, out = { 12783, 1 }, oq = 3 },
    [19666] = { name = "Silver Skeleton Key", t = { 1, 75, 85, 95 }, fee = 100, train = 75, r = { { 2842, 1 }, { 3470, 1 } }, tool = 162, out = { 15869, 2 }, oq = 2 },
    [19667] = { name = "Golden Skeleton Key", t = { 1, 125, 135, 145 }, fee = 250, train = 125, r = { { 3577, 1 }, { 3486, 1 } }, tool = 162, out = { 15870, 2 }, oq = 2 },
    [19668] = { name = "Truesilver Skeleton Key", t = { 1, 175, 185, 195 }, fee = 2500, train = 175, r = { { 6037, 1 }, { 7966, 1 } }, tool = 162, out = { 15871, 2 }, oq = 2 },
    [19669] = { name = "Arcanite Skeleton Key", t = { 1, 250, 255, 260 }, fee = 10000, train = 250, r = { { 12360, 1 }, { 12644, 1 } }, tool = 162, out = { 15872, 2 }, oq = 2 },
    [20201] = { name = "Arcanite Rod", t = { 1, 250, 255, 260 }, fee = 10000, train = 250, r = { { 12360, 3 }, { 12644, 1 } }, tool = 162, out = { 16206, 1 }, oq = 1 },
    [20872] = { name = "Fiery Chain Girdle", t = { 1, 290, 300, 310 }, scroll = 17049, train = 270, rep = { 59, 5 }, sq = 3, r = { { 11371, 6 }, { 17010, 3 }, { 17011, 3 } }, tool = 162, out = { 16989, 1 }, oq = 4 },
    [20873] = { name = "Fiery Chain Shoulders", t = { 1, 320, 330, 340 }, scroll = 17053, train = 300, rep = { 59, 6 }, sq = 3, r = { { 11371, 16 }, { 17010, 4 }, { 17011, 5 } }, tool = 162, out = { 16988, 1 }, oq = 4 },
    [20874] = { name = "Dark Iron Bracers", t = { 1, 290, 300, 310 }, scroll = 17051, train = 270, rep = { 59, 4 }, sq = 3, r = { { 11371, 4 }, { 17010, 2 }, { 17011, 2 } }, tool = 162, out = { 17014, 1 }, oq = 4 },
    [20876] = { name = "Dark Iron Leggings", t = { 1, 320, 330, 340 }, scroll = 17052, train = 300, rep = { 59, 6 }, sq = 3, r = { { 11371, 16 }, { 17010, 4 }, { 17011, 6 } }, tool = 162, out = { 17013, 1 }, oq = 4 },
    [20890] = { name = "Dark Iron Reaver", t = { 1, 320, 330, 340 }, scroll = 17059, train = 300, rep = { 59, 5 }, sq = 3, r = { { 11371, 16 }, { 17010, 12 }, { 11382, 2 }, { 12810, 2 } }, tool = 162, out = { 17015, 1 }, oq = 3 },
    [20897] = { name = "Dark Iron Destroyer", t = { 1, 320, 330, 340 }, scroll = 17060, train = 300, rep = { 59, 5 }, sq = 3, r = { { 11371, 18 }, { 17011, 12 }, { 11382, 2 }, { 12810, 2 } }, tool = 162, out = { 17016, 1 }, oq = 3 },
    [21161] = { name = "Sulfuron Hammer", t = { 1, 325, 337, 350 }, scroll = 18592, train = 300, sq = 4, r = { { 17203, 8 }, { 11371, 20 }, { 12360, 50 }, { 7078, 25 }, { 11382, 10 }, { 17011, 10 }, { 17010, 10 } }, tool = 162, out = { 17193, 1 }, oq = 4 },
    [21913] = { name = "Edge of Winter", t = { 1, 190, 202, 215 }, scroll = 17706, train = 165, sq = 2, r = { { 3859, 10 }, { 3829, 1 }, { 7070, 2 }, { 7069, 2 }, { 4234, 2 } }, tool = 162, out = { 17704, 1 }, oq = 2 },
    [22757] = { name = "Elemental Sharpening Stone", t = { 1, 275, 285, 295 }, scroll = 18264, train = 300, sq = 3, r = { { 7067, 2 }, { 12365, 3 } }, out = { 18262, 1 }, oq = 2 },
    [23632] = { name = "Girdle of the Dawn", t = { 1, 285, 295, 305 }, scroll = 19203, train = 265, scrollPrice = 22000, rep = { 529, 5 }, sq = 1, r = { { 12359, 8 }, { 6037, 6 }, { 12811, 1 } }, tool = 162, out = { 19051, 1 }, oq = 3 },
    [23633] = { name = "Gloves of the Dawn", t = { 1, 320, 330, 340 }, scroll = 19205, train = 300, scrollPrice = 40000, rep = { 529, 6 }, sq = 1, r = { { 12360, 2 }, { 6037, 10 }, { 12811, 1 } }, tool = 162, out = { 19057, 1 }, oq = 3 },
    [23636] = { name = "Dark Iron Helm", t = { 1, 320, 330, 340 }, scroll = 19206, train = 300, rep = { 59, 5 }, sq = 1, r = { { 17011, 4 }, { 17010, 2 }, { 11371, 4 } }, tool = 162, out = { 19148, 1 }, oq = 4 },
    [23637] = { name = "Dark Iron Gauntlets", t = { 1, 320, 330, 340 }, scroll = 19207, train = 300, rep = { 59, 6 }, sq = 1, r = { { 17011, 3 }, { 17010, 5 }, { 17012, 4 }, { 11371, 4 }, { 11382, 2 } }, tool = 162, out = { 19164, 1 }, oq = 4 },
    [23638] = { name = "Black Amnesty", t = { 1, 320, 330, 340 }, scroll = 19208, train = 300, rep = { 59, 6 }, sq = 1, r = { { 17011, 3 }, { 17010, 6 }, { 12360, 12 }, { 11382, 1 }, { 11371, 4 } }, tool = 162, out = { 19166, 1 }, oq = 4 },
    [23639] = { name = "Blackfury", t = { 1, 320, 330, 340 }, scroll = 19209, train = 300, rep = { 59, 6 }, sq = 1, r = { { 17011, 5 }, { 17010, 2 }, { 12360, 16 }, { 11371, 6 } }, tool = 162, out = { 19167, 1 }, oq = 4 },
    [23650] = { name = "Ebon Hand", t = { 1, 295, 305, 315 }, scroll = 19210, train = 300, rep = { 59, 7 }, sq = 1, r = { { 17011, 4 }, { 17010, 7 }, { 12360, 12 }, { 11371, 8 }, { 12800, 4 } }, tool = 162, out = { 19170, 1 }, oq = 4 },
    [23652] = { name = "Blackguard", t = { 1, 295, 305, 315 }, scroll = 19211, train = 300, rep = { 59, 7 }, sq = 1, r = { { 17011, 6 }, { 17010, 6 }, { 12360, 10 }, { 11371, 6 }, { 12809, 12 } }, tool = 162, out = { 19168, 1 }, oq = 4 },
    [23653] = { name = "Nightfall", t = { 1, 295, 305, 315 }, scroll = 19212, train = 300, rep = { 59, 7 }, sq = 1, r = { { 17011, 8 }, { 17010, 5 }, { 12360, 10 }, { 11371, 12 }, { 12364, 4 } }, tool = 162, out = { 19169, 1 }, oq = 4 },
    [24136] = { name = "Bloodsoul Breastplate", t = { 1, 320, 330, 340 }, scroll = 19776, train = 300, scrollPrice = 50000, rep = { 270, 6 }, sq = 1, r = { { 12359, 20 }, { 19774, 10 }, { 19726, 2 }, { 7910, 2 } }, tool = 162, out = { 19690, 1 }, oq = 3 },
    [24137] = { name = "Bloodsoul Shoulders", t = { 1, 320, 330, 340 }, scroll = 19777, train = 300, scrollPrice = 50000, rep = { 270, 5 }, sq = 1, r = { { 12359, 16 }, { 19774, 8 }, { 19726, 2 }, { 7910, 1 } }, tool = 162, out = { 19691, 1 }, oq = 3 },
    [24138] = { name = "Bloodsoul Gauntlets", t = { 1, 320, 330, 340 }, scroll = 19778, train = 300, scrollPrice = 50000, rep = { 270, 4 }, sq = 1, r = { { 12359, 12 }, { 19774, 6 }, { 19726, 2 }, { 12810, 4 } }, tool = 162, out = { 19692, 1 }, oq = 3 },
    [24139] = { name = "Darksoul Breastplate", t = { 1, 320, 330, 340 }, scroll = 19779, train = 300, scrollPrice = 50000, rep = { 270, 6 }, sq = 1, r = { { 12359, 20 }, { 19774, 14 }, { 12799, 2 } }, tool = 162, out = { 19693, 1 }, oq = 3 },
    [24140] = { name = "Darksoul Leggings", t = { 1, 320, 330, 340 }, scroll = 19780, train = 300, scrollPrice = 50000, rep = { 270, 5 }, sq = 1, r = { { 12359, 18 }, { 19774, 12 }, { 12799, 2 } }, tool = 162, out = { 19694, 1 }, oq = 3 },
    [24141] = { name = "Darksoul Shoulders", t = { 1, 320, 330, 340 }, scroll = 19781, train = 300, scrollPrice = 50000, rep = { 270, 4 }, sq = 1, r = { { 12359, 16 }, { 19774, 10 }, { 12799, 1 } }, tool = 162, out = { 19695, 1 }, oq = 3 },
    [24399] = { name = "Dark Iron Boots", t = { 1, 320, 330, 340 }, scroll = 20040, train = 300, rep = { 59, 7 }, sq = 1, r = { { 17011, 3 }, { 17010, 3 }, { 17012, 4 }, { 11371, 6 } }, tool = 162, out = { 20039, 1 }, oq = 4 },
    [24912] = { name = "Darkrune Gauntlets", t = { 1, 320, 330, 340 }, scroll = 20553, train = 300, sq = 3, r = { { 12359, 12 }, { 20520, 6 }, { 6037, 6 }, { 12810, 2 } }, tool = 162, out = { 20549, 1 }, oq = 3 },
    [24913] = { name = "Darkrune Helm", t = { 1, 320, 330, 340 }, scroll = 20555, train = 300, sq = 3, r = { { 12359, 16 }, { 20520, 8 }, { 6037, 8 }, { 11754, 1 } }, tool = 162, out = { 20551, 1 }, oq = 3 },
    [24914] = { name = "Darkrune Breastplate", t = { 1, 320, 330, 340 }, scroll = 20554, train = 300, sq = 3, r = { { 12359, 20 }, { 20520, 10 }, { 6037, 10 } }, tool = 162, out = { 20550, 1 }, oq = 3 },
    [27585] = { name = "Heavy Obsidian Belt", t = { 1, 320, 330, 340 }, scroll = 22209, train = 310, gone = true, sq = 1, r = { { 22202, 14 }, { 12655, 4 }, { 7076, 2 } }, tool = 162, out = { 22197, 1 }, oq = 3 },
    [27586] = { name = "Jagged Obsidian Shield", t = { 1, 320, 330, 340 }, scroll = 22219, train = 300, rep = { 609, 6 }, sq = 1, r = { { 22203, 8 }, { 22202, 24 }, { 12655, 8 }, { 7076, 4 } }, tool = 162, out = { 22198, 1 }, oq = 4 },
    [27587] = { name = "Thick Obsidian Breastplate", t = { 1, 320, 330, 340 }, scroll = 22222, train = 300, sq = 3, r = { { 22203, 18 }, { 22202, 40 }, { 12655, 12 }, { 7076, 10 }, { 12364, 4 } }, tool = 162, out = { 22196, 1 }, oq = 4 },
    [27588] = { name = "Light Obsidian Belt", t = { 1, 320, 330, 340 }, scroll = 22214, train = 310, gone = true, sq = 1, r = { { 22202, 14 }, { 12810, 4 } }, tool = 162, out = { 22195, 1 }, oq = 3 },
    [27589] = { name = "Black Grasp of the Destroyer", t = { 1, 320, 330, 340 }, scroll = 22220, train = 300, sq = 3, r = { { 22203, 8 }, { 22202, 24 }, { 12810, 8 }, { 13512, 1 } }, tool = 162, out = { 22194, 1 }, oq = 4 },
    [27590] = { name = "Obsidian Mail Tunic", t = { 1, 320, 330, 340 }, scroll = 22221, train = 300, rep = { 609, 7 }, sq = 1, r = { { 22203, 15 }, { 22202, 36 }, { 12810, 12 }, { 12809, 10 }, { 12800, 4 } }, tool = 162, out = { 22191, 1 }, oq = 4 },
    [27829] = { name = "Titanic Leggings", t = { 1, 320, 330, 340 }, scroll = 22388, train = 300, sq = 4, r = { { 12360, 12 }, { 12655, 20 }, { 7076, 10 }, { 13510, 2 } }, tool = 162, out = { 22385, 1 }, oq = 4 },
    [27830] = { name = "Persuader", t = { 1, 320, 330, 340 }, scroll = 22390, train = 300, sq = 4, r = { { 12360, 15 }, { 11371, 10 }, { 12808, 20 }, { 20520, 20 }, { 15417, 10 }, { 12753, 2 } }, tool = 162, out = { 22384, 1 }, oq = 4 },
    [27832] = { name = "Sageblade", t = { 1, 320, 330, 340 }, scroll = 22389, train = 300, sq = 4, r = { { 12360, 12 }, { 20725, 2 }, { 13512, 2 }, { 12810, 4 } }, tool = 162, out = { 22383, 1 }, oq = 4 },
    [28242] = { name = "Icebane Breastplate", t = { 1, 320, 330, 340 }, scroll = 22703, train = 300, rep = { 529, 7 }, sq = 1, r = { { 22682, 7 }, { 12359, 16 }, { 12360, 2 }, { 7080, 4 } }, tool = 162, out = { 22669, 1 }, oq = 4 },
    [28243] = { name = "Icebane Gauntlets", t = { 1, 320, 330, 340 }, scroll = 22704, train = 300, rep = { 529, 6 }, sq = 1, r = { { 22682, 5 }, { 12359, 12 }, { 12360, 2 }, { 7080, 2 } }, tool = 162, out = { 22670, 1 }, oq = 4 },
    [28244] = { name = "Icebane Bracers", t = { 1, 320, 330, 340 }, scroll = 22705, train = 300, rep = { 749, 6 }, sq = 1, r = { { 22682, 4 }, { 12359, 12 }, { 12360, 2 }, { 7080, 2 } }, tool = 162, out = { 22671, 1 }, oq = 4 },
    [28461] = { name = "Ironvine Breastplate", t = { 1, 320, 330, 340 }, scroll = 22766, train = 310, gone = true, sq = 1, r = { { 12655, 12 }, { 19726, 2 }, { 12360, 2 }, { 12803, 2 } }, tool = 162, out = { 22762, 1 }, oq = 1 },
    [28462] = { name = "Ironvine Gloves", t = { 1, 320, 330, 340 }, scroll = 22767, train = 310, gone = true, sq = 1, r = { { 12655, 8 }, { 19726, 1 }, { 12803, 2 } }, tool = 162, out = { 22763, 1 }, oq = 1 },
    [28463] = { name = "Ironvine Belt", t = { 1, 320, 330, 340 }, scroll = 22768, train = 310, gone = true, sq = 1, r = { { 12655, 6 }, { 12803, 2 } }, tool = 162, out = { 22764, 1 }, oq = 1 },
    [427061] = { name = "Mantle of the Second War", t = { 1, 140, 150, 160 }, scroll = 210779, train = 150, gone = true, sq = 2, r = { { 2841, 20 }, { 1206, 2 }, { 1705, 2 }, { 5500, 2 }, { 2842, 4 } }, tool = 162, out = { 210773, 1 }, oq = 1 },
    [430397] = { name = "Blackfathom Sharpening Stone", t = { 1, 100, 110, 120 }, scroll = 211846, train = 90, sq = 1, r = { { 2863, 1 }, { 10938, 1 } }, out = { 211845, 1 }, oq = 2 },
    [435906] = { name = "Reflective Truesilver Braincage", t = { 1, 225, 230, 235 }, scroll = 215383, train = 225, sq = 4, r = { { 3860, 25 }, { 213376, 4 }, { 213379, 2 }, { 213383, 1 } }, tool = 162, out = { 215167, 1 }, oq = 1 },
    [435908] = { name = "Tempered Interference-Negating Helmet", t = { 1, 225, 230, 235 }, scroll = 215155, train = 225, sq = 4, r = { { 3860, 25 }, { 213376, 4 }, { 213379, 1 }, { 213369, 2 } }, tool = 162, out = { 215161, 1 }, oq = 1 },
    [435910] = { name = "Low-Background Truesilver Plates", t = { 1, 200, 210, 220 }, scroll = 215384, train = 200, sq = 3, r = { { 6037, 1 }, { 213373, 5 } }, tool = 162, out = { 213376, 1 }, oq = 3 },
    [461647] = { name = "Skyrider's Masterwork Stormhammer", t = { 1, 320, 330, 340 }, scroll = 227905, train = 300, sq = 3, r = { { 12794, 1 }, { 18262, 10 }, { 12360, 15 } }, tool = 162, out = { 227886, 1 }, oq = 1 },
    [461651] = { name = "Fiery Plate Gauntlets of the Hidden Technique", t = { 1, 310, 320, 330 }, scroll = 227909, train = 290, sq = 3, r = { { 12359, 20 }, { 12655, 6 }, { 7078, 2 }, { 7910, 4 } }, tool = 162, out = { 227865, 1 }, oq = 1 },
    [461667] = { name = "Tempered Dark Iron Plate", t = { 1, 305, 315, 325 }, scroll = 227901, train = 285, sq = 3, r = { { 11371, 20 }, { 7077, 8 } }, tool = 162, out = { 227871, 1 }, oq = 1 },
    [461669] = { name = "Refined Arcanite Champion", t = { 1, 320, 330, 340 }, scroll = 228117, train = 300, sq = 3, r = { { 12790, 1 }, { 18262, 10 } }, tool = 162, out = { 228125, 1 }, oq = 1 },
    [461671] = { name = "Stronger-hold Gauntlets", t = { 1, 320, 330, 340 }, scroll = 228250, train = 300, sq = 4, r = { { 12360, 15 }, { 12655, 20 }, { 7076, 10 }, { 12361, 4 }, { 12799, 4 } }, tool = 162, out = { 227885, 1 }, oq = 1 },
    [461675] = { name = "Refined Arcanite Reaper", t = { 1, 320, 330, 340 }, scroll = 228114, train = 300, sq = 3, r = { { 12784, 1 }, { 18262, 10 } }, tool = 162, out = { 227845, 1 }, oq = 1 },
    [461712] = { name = "Refined Hammer of the Titans", t = { 1, 320, 330, 340 }, scroll = 228305, train = 310, sq = 1, r = { { 12796, 1 }, { 18262, 10 } }, tool = 162, out = { 228230, 1 }, oq = 1 },
    [461714] = { name = "Desecration", t = { 1, 315, 327, 340 }, scroll = 228306, train = 305, sq = 1, r = { { 12359, 40 }, { 12360, 2 }, { 12662, 16 }, { 12808, 8 }, { 12361, 2 }, { 12644, 2 }, { 8170, 4 } }, tool = 162, out = { 227857, 1 }, oq = 1 },
    [461716] = { name = "Deadly Heartseeker", t = { 1, 320, 330, 340 }, scroll = 228307, train = 310, sq = 1, r = { { 12360, 10 }, { 12655, 10 }, { 12810, 2 }, { 7910, 6 }, { 12800, 6 }, { 12799, 6 }, { 12644, 4 } }, tool = 162, out = { 227884, 1 }, oq = 1 },
    [461718] = { name = "Tranquility", t = { 1, 310, 322, 335 }, scroll = 228308, train = 300, sq = 1, r = { { 12655, 6 }, { 12360, 2 }, { 12804, 4 }, { 12799, 2 }, { 12361, 2 }, { 12364, 1 } }, tool = 162, out = { 227881, 1 }, oq = 1 },
    [461730] = { name = "Hardened Frostguard", t = { 1, 320, 330, 340 }, scroll = 228310, train = 300, sq = 3, r = { { 12797, 1 }, { 18262, 10 } }, tool = 162, out = { 227887, 1 }, oq = 1 },
    [461733] = { name = "Finely-Enchanted Battlehammer", t = { 1, 305, 317, 330 }, scroll = 228311, train = 280, sq = 2, r = { { 12359, 20 }, { 12655, 6 }, { 12364, 2 }, { 12804, 4 }, { 8170, 4 } }, tool = 162, out = { 227880, 1 }, oq = 1 },
    [461735] = { name = "Invincible Mail", t = { 1, 320, 330, 340 }, scroll = 228312, train = 300, sq = 4, r = { { 12360, 30 }, { 12655, 30 }, { 12364, 6 }, { 12800, 6 } }, tool = 162, out = { 227876, 1 }, oq = 1 },
    [461737] = { name = "Tempest Gauntlets", t = { 1, 315, 325, 335 }, scroll = 228313, train = 295, sq = 3, r = { { 12359, 20 }, { 12655, 4 }, { 7080, 4 }, { 12361, 4 } }, tool = 162, out = { 227870, 1 }, oq = 1 },
    [461739] = { name = "Warcrest of the Great Chief", t = { 1, 320, 330, 340 }, scroll = 228314, train = 300, sq = 3, r = { { 12359, 40 }, { 12655, 4 }, { 8168, 60 }, { 12799, 6 }, { 12364, 2 } }, tool = 162, out = { 227872, 1 }, oq = 1 },
    [461743] = { name = "Sageblade of the Archmagus", t = { 1, 320, 330, 340 }, scroll = 228315, train = 300, sq = 4, r = { { 12360, 12 }, { 20725, 2 }, { 13512, 2 }, { 12810, 4 } }, tool = 162, out = { 227850, 1 }, oq = 1 },
    [1213643] = { name = "Obsidian Grinding Stone", t = { 1, 315, 322, 330 }, scroll = 234279, train = 305, sq = 1, r = { { 22202, 5 } }, tool = 162, out = { 234004, 1 }, oq = 1 },
    [1214309] = { name = "Dreamscale Visor", t = { 1, 320, 330, 340 }, scroll = 234488, train = 310, sq = 1, r = { { 12360, 20 }, { 12810, 4 }, { 8146, 8 }, { 20381, 8 }, { 12803, 4 } }, tool = 162, out = { 234487, 1 }, oq = 1 },
    [1224631] = { name = "Scarlet Soldier's Helmet", t = { 1, 285, 295, 305 }, scroll = 238322, train = 280, sq = 3, r = { { 12938, 1 }, { 12811, 2 }, { 12359, 24 } }, tool = 162, out = { 238288, 1 }, oq = 1 },
    [1224632] = { name = "Scarlet Soldier's Spaulders", t = { 1, 285, 295, 305 }, scroll = 238323, train = 280, sq = 3, r = { { 12811, 1 }, { 12359, 20 } }, tool = 162, out = { 238289, 1 }, oq = 1 },
    [1224633] = { name = "Scarlet Soldier's Chestplate", t = { 1, 285, 295, 305 }, scroll = 238324, train = 280, sq = 3, r = { { 12938, 1 }, { 12811, 1 }, { 12359, 24 } }, tool = 162, out = { 238290, 1 }, oq = 1 },
    [1224635] = { name = "Scarlet Soldier's Protectors", t = { 1, 260, 282, 305 }, scroll = 238325, train = 250, sq = 3, r = { { 12359, 16 } }, tool = 162, out = { 238291, 1 }, oq = 1 },
    [1224636] = { name = "Scarlet Soldier's Grips", t = { 1, 270, 287, 305 }, scroll = 238326, train = 260, sq = 3, r = { { 12811, 1 }, { 12359, 20 } }, tool = 162, out = { 238292, 1 }, oq = 1 },
    [1224637] = { name = "Scarlet Soldier's Waistguard", t = { 1, 260, 282, 305 }, scroll = 238327, train = 250, sq = 3, r = { { 12811, 1 }, { 12359, 20 } }, tool = 162, out = { 238293, 1 }, oq = 1 },
    [1224638] = { name = "Scarlet Soldier's Legplates", t = { 1, 280, 292, 305 }, scroll = 238328, train = 270, sq = 3, r = { { 12938, 1 }, { 12811, 1 }, { 12359, 20 } }, tool = 162, out = { 238294, 1 }, oq = 1 },
    [1224639] = { name = "Scarlet Soldier's Stompers", t = { 1, 270, 287, 305 }, scroll = 238329, train = 260, sq = 3, r = { { 12811, 1 }, { 12359, 20 } }, tool = 162, out = { 238295, 1 }, oq = 1 },
    [1230171] = { name = "Sharpening Wheel", t = { 1, 20, 20, 20 }, fee = 0, train = 20, r = { { 2835, 1 }, { 2840, 1 } }, out = { 279944, 1 }, oq = 1 },
    [1245287] = { name = "Copper Rod", t = { 1, 10, 12, 15 }, basic = true, r = { { 2840, 1 } }, tool = 162, out = { 6217, 1 }, oq = 1 },
    [1252232] = { name = "Sterling Silver Boots", t = { 1, 130, 145, 160 }, scroll = 251335, train = 100, sq = 2, r = { { 2842, 6 }, { 2840, 2 }, { 3478, 2 }, { 2319, 2 } }, tool = 162, out = { 250483, 1 }, oq = 2 },
    [1252233] = { name = "Sterling Silver Leggings", t = { 1, 135, 150, 165 }, scroll = 251336, train = 105, sq = 2, r = { { 2842, 10 }, { 2840, 3 }, { 3478, 3 } }, tool = 162, out = { 250484, 1 }, oq = 2 },
    [1252234] = { name = "Sterling Silver Gauntlet", t = { 1, 135, 150, 165 }, scroll = 251337, train = 105, sq = 2, r = { { 2842, 6 }, { 2840, 2 }, { 3478, 2 } }, tool = 162, out = { 250485, 1 }, oq = 2 },
    [1252235] = { name = "Sterling Silver Shoulders", t = { 1, 140, 155, 170 }, scroll = 251338, train = 110, sq = 2, r = { { 2842, 6 }, { 2840, 2 }, { 3478, 2 } }, tool = 162, out = { 250486, 1 }, oq = 2 },
    [1252236] = { name = "Sterling Silver Breastplate", t = { 1, 155, 170, 185 }, scroll = 251339, train = 125, sq = 2, r = { { 2842, 12 }, { 2840, 4 }, { 3478, 3 } }, tool = 162, out = { 250487, 1 }, oq = 2 },
    [1252252] = { name = "Veteran's Boots", t = { 1, 115, 130, 145 }, scroll = 251355, train = 85, sq = 3, favor = 30, r = { { 2841, 12 }, { 3478, 2 }, { 249427, 4 }, { 5498, 5 } }, tool = 162, out = { 250503, 1 }, oq = 3, bop = true },
    [1252253] = { name = "Guard's Boots", t = { 1, 115, 130, 145 }, scroll = 251356, train = 85, sq = 3, favor = 30, r = { { 2841, 12 }, { 3478, 2 }, { 249427, 4 }, { 1210, 5 } }, tool = 162, out = { 250504, 1 }, oq = 3, bop = true },
    [1252254] = { name = "Protector's Boots", t = { 1, 115, 130, 145 }, scroll = 251357, train = 85, sq = 3, favor = 30, r = { { 2841, 12 }, { 3478, 2 }, { 249427, 4 }, { 818, 5 } }, tool = 162, out = { 250505, 1 }, oq = 3, bop = true },
    [1252255] = { name = "Acolyte's Boots", t = { 1, 115, 130, 145 }, scroll = 251358, train = 85, sq = 3, favor = 30, r = { { 2841, 12 }, { 3478, 2 }, { 249427, 4 }, { 10940, 5 } }, tool = 162, out = { 250506, 1 }, oq = 3, bop = true },
    [1252256] = { name = "Crusader's Boots", t = { 1, 115, 130, 145 }, scroll = 251359, train = 85, sq = 3, favor = 30, r = { { 2841, 12 }, { 3478, 2 }, { 249427, 4 }, { 10938, 5 } }, tool = 162, out = { 250507, 1 }, oq = 3, bop = true },
    [1252257] = { name = "Veteran's Gloves", t = { 1, 110, 125, 140 }, scroll = 251360, train = 80, sq = 3, favor = 30, r = { { 2841, 10 }, { 3470, 4 }, { 249410, 2 }, { 5498, 3 } }, tool = 162, out = { 250508, 1 }, oq = 3, bop = true },
    [1252258] = { name = "Guard's Gloves", t = { 1, 110, 125, 140 }, scroll = 251361, train = 80, sq = 3, favor = 30, r = { { 2841, 10 }, { 3470, 4 }, { 249410, 2 }, { 1210, 3 } }, tool = 162, out = { 250509, 1 }, oq = 3, bop = true },
    [1252259] = { name = "Protector's Gloves", t = { 1, 110, 125, 140 }, scroll = 251362, train = 80, sq = 3, favor = 30, r = { { 2841, 10 }, { 3470, 4 }, { 249410, 2 }, { 818, 3 } }, tool = 162, out = { 250510, 1 }, oq = 3, bop = true },
    [1252260] = { name = "Acolyte's Gloves", t = { 1, 110, 125, 140 }, scroll = 251363, train = 80, sq = 3, favor = 30, r = { { 2841, 10 }, { 3470, 4 }, { 249410, 2 }, { 10940, 3 } }, tool = 162, out = { 250511, 1 }, oq = 3, bop = true },
    [1252261] = { name = "Crusader's Gloves", t = { 1, 110, 125, 140 }, scroll = 251364, train = 80, sq = 3, favor = 30, r = { { 2841, 10 }, { 3470, 4 }, { 249410, 2 }, { 10938, 3 } }, tool = 162, out = { 250512, 1 }, oq = 3, bop = true },
    [1252262] = { name = "Veteran's Chain Belt", t = { 1, 85, 105, 125 }, scroll = 251365, train = 45, sq = 3, favor = 30, r = { { 2840, 12 }, { 3470, 4 }, { 249427, 2 }, { 5498, 2 } }, tool = 162, out = { 250513, 1 }, oq = 3, bop = true },
    [1252263] = { name = "Guard's Chain Belt", t = { 1, 85, 105, 125 }, scroll = 251366, train = 45, sq = 3, favor = 30, r = { { 2840, 12 }, { 3470, 4 }, { 249427, 2 }, { 1210, 2 } }, tool = 162, out = { 250514, 1 }, oq = 3, bop = true },
    [1252264] = { name = "Protector's Chain Belt", t = { 1, 85, 105, 125 }, scroll = 251367, train = 45, sq = 3, favor = 30, r = { { 2840, 12 }, { 3470, 4 }, { 249427, 2 }, { 818, 2 } }, tool = 162, out = { 250515, 1 }, oq = 3, bop = true },
    [1252265] = { name = "Acolyte's Chain Belt", t = { 1, 85, 105, 125 }, scroll = 251368, train = 45, sq = 3, favor = 30, r = { { 2840, 12 }, { 3470, 4 }, { 249427, 2 }, { 10940, 2 } }, tool = 162, out = { 250516, 1 }, oq = 3, bop = true },
    [1252266] = { name = "Crusader's Chain Belt", t = { 1, 85, 105, 125 }, scroll = 251369, train = 45, sq = 3, favor = 30, r = { { 2840, 12 }, { 3470, 4 }, { 249427, 2 }, { 10938, 2 } }, tool = 162, out = { 250517, 1 }, oq = 3, bop = true },
    [1252267] = { name = "Veteran's Silvered Chain Shirt", t = { 1, 140, 155, 170 }, scroll = 251370, train = 110, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 6 }, { 2842, 5 }, { 249427, 6 }, { 5498, 8 } }, tool = 162, out = { 250518, 1 }, oq = 3, bop = true },
    [1252268] = { name = "Guard's Silvered Chain Shirt", t = { 1, 140, 155, 170 }, scroll = 251371, train = 110, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 6 }, { 2842, 5 }, { 249427, 6 }, { 1210, 8 } }, tool = 162, out = { 250519, 1 }, oq = 3, bop = true },
    [1252269] = { name = "Protector's Silvered Chain Shirt", t = { 1, 140, 155, 170 }, scroll = 251372, train = 110, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 6 }, { 2842, 5 }, { 249427, 6 }, { 818, 8 } }, tool = 162, out = { 250520, 1 }, oq = 3, bop = true },
    [1252270] = { name = "Acolyte's Silvered Chain Shirt", t = { 1, 140, 155, 170 }, scroll = 251373, train = 110, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 6 }, { 2842, 5 }, { 249427, 6 }, { 10940, 8 } }, tool = 162, out = { 250521, 1 }, oq = 3, bop = true },
    [1252271] = { name = "Crusader's Silvered Chain Shirt", t = { 1, 140, 155, 170 }, scroll = 251374, train = 110, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 6 }, { 2842, 5 }, { 249427, 6 }, { 10938, 8 } }, tool = 162, out = { 250522, 1 }, oq = 3, bop = true },
    [1252272] = { name = "Veteran's Silvered Chain Leggings", t = { 1, 155, 170, 185 }, scroll = 251375, train = 125, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 8 }, { 2842, 6 }, { 249427, 6 }, { 5498, 8 } }, tool = 162, out = { 250523, 1 }, oq = 3, bop = true },
    [1252273] = { name = "Guard's Silvered Chain Leggings", t = { 1, 155, 170, 185 }, scroll = 251376, train = 125, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 8 }, { 2842, 6 }, { 249427, 6 }, { 1210, 8 } }, tool = 162, out = { 250524, 1 }, oq = 3, bop = true },
    [1252274] = { name = "Protector's Silvered Chain Leggings", t = { 1, 155, 170, 185 }, scroll = 251377, train = 125, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 8 }, { 2842, 6 }, { 249427, 6 }, { 818, 8 } }, tool = 162, out = { 250525, 1 }, oq = 3, bop = true },
    [1252275] = { name = "Acolyte's Silvered Chain Leggings", t = { 1, 155, 170, 185 }, scroll = 251378, train = 125, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 8 }, { 2842, 6 }, { 249427, 6 }, { 10940, 8 } }, tool = 162, out = { 250526, 1 }, oq = 3, bop = true },
    [1252276] = { name = "Crusader's Silvered Chain Leggings", t = { 1, 155, 170, 185 }, scroll = 251379, train = 125, sq = 3, favor = 30, r = { { 2841, 20 }, { 3478, 8 }, { 2842, 6 }, { 249427, 6 }, { 10938, 8 } }, tool = 162, out = { 250527, 1 }, oq = 3, bop = true },
    [1252277] = { name = "Veteran's Silvered Chain Helm", t = { 1, 125, 140, 155 }, scroll = 251380, train = 95, sq = 3, favor = 30, r = { { 2841, 15 }, { 3478, 6 }, { 2842, 4 }, { 249427, 4 }, { 5498, 6 } }, tool = 162, out = { 250528, 1 }, oq = 3, bop = true },
    [1252278] = { name = "Guard's Silvered Chain Helm", t = { 1, 125, 140, 155 }, scroll = 251381, train = 95, sq = 3, favor = 30, r = { { 2841, 15 }, { 3478, 6 }, { 2842, 4 }, { 249427, 4 }, { 1210, 6 } }, tool = 162, out = { 250529, 1 }, oq = 3, bop = true },
    [1252279] = { name = "Protector's Silvered Chain Helm", t = { 1, 125, 140, 155 }, scroll = 251382, train = 95, sq = 3, favor = 30, r = { { 2841, 15 }, { 3478, 6 }, { 2842, 4 }, { 249427, 4 }, { 818, 6 } }, tool = 162, out = { 250530, 1 }, oq = 3, bop = true },
    [1252280] = { name = "Acolyte's Silvered Chain Helm", t = { 1, 125, 140, 155 }, scroll = 251383, train = 95, sq = 3, favor = 30, r = { { 2841, 15 }, { 3478, 6 }, { 2842, 4 }, { 249427, 4 }, { 10940, 6 } }, tool = 162, out = { 250531, 1 }, oq = 3, bop = true },
    [1252281] = { name = "Crusader's Silvered Chain Helm", t = { 1, 125, 140, 155 }, scroll = 251384, train = 95, sq = 3, favor = 30, r = { { 2841, 15 }, { 3478, 6 }, { 2842, 4 }, { 249427, 4 }, { 10938, 6 } }, tool = 162, out = { 250532, 1 }, oq = 3, bop = true },
    [1252282] = { name = "Hard Gold Cuirass", t = { 1, 170, 182, 195 }, scroll = 251385, train = 145, sq = 2, r = { { 3577, 12 }, { 3859, 3 }, { 3486, 2 } }, tool = 162, out = { 250533, 1 }, oq = 2 },
    [1252283] = { name = "Hard Gold Boots", t = { 1, 175, 187, 200 }, scroll = 251386, train = 150, sq = 2, r = { { 3577, 6 }, { 3859, 2 }, { 3486, 2 }, { 4234, 2 } }, tool = 162, out = { 250534, 1 }, oq = 2 },
    [1252284] = { name = "Hard Gold Bracers", t = { 1, 185, 197, 210 }, scroll = 251387, train = 160, sq = 2, r = { { 3577, 6 }, { 3859, 1 }, { 3486, 2 } }, tool = 162, out = { 250535, 1 }, oq = 2 },
    [1252285] = { name = "Hard Gold Leggings", t = { 1, 190, 202, 215 }, scroll = 251388, train = 165, sq = 2, r = { { 3577, 10 }, { 3859, 2 }, { 3486, 2 } }, tool = 162, out = { 250536, 1 }, oq = 2 },
    [1252286] = { name = "Hard Gold Coif", t = { 1, 195, 207, 220 }, scroll = 251389, train = 170, sq = 2, r = { { 3577, 10 }, { 3859, 2 }, { 3486, 2 } }, tool = 162, out = { 250537, 1 }, oq = 2 },
    [1252287] = { name = "Hard Gold Gauntlet", t = { 1, 200, 212, 225 }, scroll = 251390, train = 175, scrollPrice = 6250, sq = 2, r = { { 3577, 8 }, { 3859, 2 }, { 3486, 2 } }, tool = 162, out = { 250538, 1 }, oq = 2 },
    [1252288] = { name = "Hard Gold Pauldrons", t = { 1, 200, 212, 225 }, scroll = 251391, train = 175, sq = 2, r = { { 3577, 8 }, { 3859, 2 }, { 3486, 2 } }, tool = 162, out = { 250539, 1 }, oq = 2 },
    [1252289] = { name = "Shining Mithril Breastplate", t = { 1, 215, 225, 235 }, scroll = 251392, train = 195, sq = 2, r = { { 3860, 8 }, { 6037, 9 }, { 3486, 2 }, { 7971, 2 } }, tool = 162, out = { 250540, 1 }, oq = 2 },
    [1252290] = { name = "Shining Mithril Pauldrons", t = { 1, 215, 225, 235 }, scroll = 251393, train = 195, sq = 2, r = { { 3860, 6 }, { 6037, 3 }, { 3486, 2 }, { 4304, 2 } }, tool = 162, out = { 250541, 1 }, oq = 2 },
    [1252291] = { name = "Shining Mithril Boots", t = { 1, 220, 230, 240 }, scroll = 251394, train = 200, sq = 2, r = { { 3860, 4 }, { 6037, 3 }, { 3486, 2 }, { 4304, 4 } }, tool = 162, out = { 250542, 1 }, oq = 2 },
    [1252292] = { name = "Shining Mithril Helm", t = { 1, 235, 245, 255 }, scroll = 251395, train = 215, sq = 3, r = { { 3860, 8 }, { 6037, 9 }, { 3486, 2 }, { 7075, 1 } }, tool = 162, out = { 250543, 1 }, oq = 2 },
    [1252293] = { name = "Shining Mithril Pants", t = { 1, 240, 250, 260 }, scroll = 251396, train = 220, sq = 2, r = { { 3860, 6 }, { 6037, 9 }, { 3486, 2 }, { 7075, 1 } }, tool = 162, out = { 250544, 1 }, oq = 2 },
    [1252294] = { name = "Shining Mithril Gauntlet", t = { 1, 240, 250, 260 }, scroll = 251397, train = 220, sq = 2, r = { { 3860, 5 }, { 6037, 6 }, { 3486, 2 }, { 7909, 2 } }, tool = 162, out = { 250545, 1 }, oq = 2 },
    [1252310] = { name = "Officer's Sabatons", t = { 1, 260, 270, 280 }, scroll = 251413, train = 240, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 20 }, { 7966, 3 }, { 249432, 4 }, { 249410, 4 }, { 1529, 6 }, { 249427, 4 } }, tool = 162, out = { 250561, 1 }, oq = 3, bop = true },
    [1252311] = { name = "Sentinel's Sabatons", t = { 1, 260, 270, 280 }, scroll = 251414, train = 240, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 20 }, { 7966, 3 }, { 249432, 4 }, { 249410, 4 }, { 8831, 6 }, { 249427, 4 } }, tool = 162, out = { 250562, 1 }, oq = 3, bop = true },
    [1252312] = { name = "Warder's Sabatons", t = { 1, 260, 270, 280 }, scroll = 251415, train = 240, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 20 }, { 7966, 3 }, { 249432, 4 }, { 249410, 4 }, { 7971, 6 }, { 249427, 4 } }, tool = 162, out = { 250563, 1 }, oq = 3, bop = true },
    [1252313] = { name = "Prefect's Sabatons", t = { 1, 260, 270, 280 }, scroll = 251416, train = 240, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 20 }, { 7966, 3 }, { 249432, 4 }, { 249410, 4 }, { 13926, 6 }, { 249427, 4 } }, tool = 162, out = { 250564, 1 }, oq = 3, bop = true },
    [1252314] = { name = "Justicar's Sabatons", t = { 1, 260, 270, 280 }, scroll = 251417, train = 240, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 20 }, { 7966, 3 }, { 249432, 4 }, { 249410, 4 }, { 7079, 6 }, { 249427, 4 } }, tool = 162, out = { 250565, 1 }, oq = 3, bop = true },
    [1252315] = { name = "Officer's Gauntlet", t = { 1, 200, 212, 225 }, scroll = 251418, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 3859, 10 }, { 3486, 4 }, { 249432, 4 }, { 249410, 2 }, { 1529, 4 } }, tool = 162, out = { 250566, 1 }, oq = 3, bop = true },
    [1252316] = { name = "Sentinel's Gauntlet", t = { 1, 200, 212, 225 }, scroll = 251419, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 3859, 10 }, { 3486, 4 }, { 249432, 4 }, { 249410, 2 }, { 8831, 4 } }, tool = 162, out = { 250567, 1 }, oq = 3, bop = true },
    [1252317] = { name = "Warder's Gauntlet", t = { 1, 200, 212, 225 }, scroll = 251420, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 3859, 10 }, { 3486, 4 }, { 249432, 4 }, { 249410, 2 }, { 7971, 4 } }, tool = 162, out = { 250568, 1 }, oq = 3, bop = true },
    [1252318] = { name = "Prefect's Gauntlet", t = { 1, 200, 212, 225 }, scroll = 251421, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 3859, 10 }, { 3486, 4 }, { 249432, 4 }, { 249410, 2 }, { 13926, 4 } }, tool = 162, out = { 250569, 1 }, oq = 3, bop = true },
    [1252319] = { name = "Justicar's Gauntlet", t = { 1, 200, 212, 225 }, scroll = 251422, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 3859, 10 }, { 3486, 4 }, { 249432, 4 }, { 249410, 2 }, { 7079, 4 } }, tool = 162, out = { 250570, 1 }, oq = 3, bop = true },
    [1252320] = { name = "Officer's Waistguard", t = { 1, 270, 280, 290 }, scroll = 251423, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 24 }, { 7966, 4 }, { 249432, 6 }, { 249410, 6 }, { 1529, 10 } }, tool = 162, out = { 250571, 1 }, oq = 3, bop = true },
    [1252321] = { name = "Sentinel's Waistguard", t = { 1, 270, 280, 290 }, scroll = 251424, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 24 }, { 7966, 4 }, { 249432, 6 }, { 249410, 6 }, { 8831, 10 } }, tool = 162, out = { 250572, 1 }, oq = 3, bop = true },
    [1252322] = { name = "Warder's Waistguard", t = { 1, 270, 280, 290 }, scroll = 251425, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 24 }, { 7966, 4 }, { 249432, 6 }, { 249410, 6 }, { 7971, 10 } }, tool = 162, out = { 250573, 1 }, oq = 3, bop = true },
    [1252323] = { name = "Prefect's Waistguard", t = { 1, 270, 280, 290 }, scroll = 251426, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 24 }, { 7966, 4 }, { 249432, 6 }, { 249410, 6 }, { 13926, 10 } }, tool = 162, out = { 250574, 1 }, oq = 3, bop = true },
    [1252324] = { name = "Justicar's Waistguard", t = { 1, 270, 280, 290 }, scroll = 251427, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 24 }, { 7966, 4 }, { 249432, 6 }, { 249410, 6 }, { 7079, 10 } }, tool = 162, out = { 250575, 1 }, oq = 3, bop = true },
    [1252325] = { name = "Officer's Pauldrons", t = { 1, 230, 240, 250 }, scroll = 251428, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 3860, 20 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 1529, 8 }, { 11139, 1 } }, tool = 162, out = { 250576, 1 }, oq = 3, bop = true },
    [1252326] = { name = "Sentinel's Pauldrons", t = { 1, 230, 240, 250 }, scroll = 251429, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 3860, 20 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 8831, 8 }, { 11139, 1 } }, tool = 162, out = { 250577, 1 }, oq = 3, bop = true },
    [1252327] = { name = "Warder's Pauldrons", t = { 1, 230, 240, 250 }, scroll = 251430, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 3860, 20 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 7971, 8 }, { 11139, 1 } }, tool = 162, out = { 250578, 1 }, oq = 3, bop = true },
    [1252328] = { name = "Prefect's Pauldrons", t = { 1, 230, 240, 250 }, scroll = 251431, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 3860, 20 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 13926, 8 }, { 11139, 1 } }, tool = 162, out = { 250579, 1 }, oq = 3, bop = true },
    [1252329] = { name = "Justicar's Pauldrons", t = { 1, 230, 240, 250 }, scroll = 251432, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 3860, 20 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 7079, 8 }, { 11139, 1 } }, tool = 162, out = { 250580, 1 }, oq = 3, bop = true },
    [1252330] = { name = "Officer's Wristguards", t = { 1, 250, 262, 275 }, scroll = 251433, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 16 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 1529, 6 }, { 11139, 1 } }, tool = 162, out = { 250581, 1 }, oq = 3, bop = true },
    [1252331] = { name = "Sentinel's Wristguards", t = { 1, 250, 262, 275 }, scroll = 251434, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 16 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 8831, 6 }, { 11139, 1 } }, tool = 162, out = { 250582, 1 }, oq = 3, bop = true },
    [1252332] = { name = "Warder's Wristguards", t = { 1, 250, 262, 275 }, scroll = 251435, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 16 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 7971, 6 }, { 11139, 1 } }, tool = 162, out = { 250583, 1 }, oq = 3, bop = true },
    [1252333] = { name = "Prefect's Wristguards", t = { 1, 250, 262, 275 }, scroll = 251436, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 16 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 13926, 6 }, { 11139, 1 } }, tool = 162, out = { 250584, 1 }, oq = 3, bop = true },
    [1252334] = { name = "Justicar's Wristguards", t = { 1, 250, 262, 275 }, scroll = 251437, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 16 }, { 7966, 2 }, { 249432, 6 }, { 249410, 4 }, { 7079, 6 }, { 11139, 1 } }, tool = 162, out = { 250585, 1 }, oq = 3, bop = true },
    [1252335] = { name = "Blessed Plate Pauldrons", t = { 1, 260, 270, 280 }, scroll = 251438, train = 240, sq = 2, r = { { 12359, 20 }, { 12361, 1 }, { 8170, 6 } }, tool = 162, out = { 250586, 1 }, oq = 2 },
    [1252336] = { name = "Blessed Plate Boots", t = { 1, 260, 270, 280 }, scroll = 251439, train = 240, sq = 2, r = { { 12359, 24 }, { 12361, 1 }, { 8170, 6 } }, tool = 162, out = { 250587, 1 }, oq = 2 },
    [1252337] = { name = "Blessed Plate Gauntlet", t = { 1, 265, 275, 285 }, scroll = 251440, train = 245, sq = 2, r = { { 12359, 20 }, { 12361, 2 } }, tool = 162, out = { 250588, 1 }, oq = 2 },
    [1252338] = { name = "Imperial Plate Gauntlets", t = { 1, 275, 285, 295 }, scroll = 251441, train = 255, sq = 2, r = { { 12359, 24 }, { 7910, 1 } }, tool = 162, out = { 250589, 1 }, oq = 2 },
    [1252339] = { name = "Blessed Plate Bracers", t = { 1, 275, 285, 295 }, scroll = 251442, train = 255, sq = 2, r = { { 12359, 16 }, { 12361, 1 } }, tool = 162, out = { 250590, 1 }, oq = 2 },
    [1252340] = { name = "Blessed Plate Leggings", t = { 1, 290, 300, 310 }, scroll = 251443, train = 270, sq = 2, r = { { 12359, 40 }, { 12361, 2 } }, tool = 162, out = { 250591, 1 }, oq = 2 },
    [1252341] = { name = "Blessed Plate Belt", t = { 1, 290, 300, 310 }, scroll = 251444, train = 270, sq = 2, r = { { 12359, 18 }, { 12361, 1 }, { 7071, 1 }, { 8170, 6 } }, tool = 162, out = { 250592, 1 }, oq = 2 },
    [1252342] = { name = "Blessed Plate Helm", t = { 1, 295, 305, 315 }, scroll = 251445, train = 275, sq = 2, r = { { 12359, 30 }, { 12361, 2 } }, tool = 162, out = { 250593, 1 }, oq = 2 },
    [1252343] = { name = "Blessed Plate Chest", t = { 1, 300, 310, 320 }, scroll = 251446, train = 280, sq = 2, r = { { 12359, 36 }, { 12361, 2 } }, tool = 162, out = { 250594, 1 }, oq = 2 },
    [1252344] = { name = "Enriched Thorium Breastplate", t = { 1, 320, 330, 340 }, scroll = 251447, train = 300, sq = 3, favor = 120, favorRep = 6, r = { { 251290, 8 }, { 251291, 24 }, { 7082, 4 }, { 7078, 4 }, { 249726, 4 } }, tool = 162, out = { 250595, 1 }, oq = 3, bop = true },
    [1252345] = { name = "Enriched Thorium Leggings", t = { 1, 320, 330, 340 }, scroll = 251448, train = 300, sq = 3, favor = 120, favorRep = 6, r = { { 251290, 10 }, { 251291, 20 }, { 7082, 6 }, { 249726, 3 } }, tool = 162, out = { 250596, 1 }, oq = 3, bop = true },
    [1252346] = { name = "Enriched Thorium Helm", t = { 1, 320, 330, 340 }, scroll = 251449, train = 300, sq = 3, favor = 120, favorRep = 6, r = { { 251290, 6 }, { 251291, 16 }, { 7078, 6 }, { 249726, 3 } }, tool = 162, out = { 250597, 1 }, oq = 3, bop = true },
    [1252347] = { name = "Champion's Legplates", t = { 1, 320, 330, 340 }, scroll = 251450, train = 300, sq = 4, r = { { 251290, 12 }, { 251291, 20 }, { 7082, 10 }, { 13512, 2 } }, tool = 162, out = { 250598, 1 }, oq = 4 },
    [1252348] = { name = "Stalwart Helm", t = { 1, 320, 330, 340 }, scroll = 251451, train = 300, sq = 4, r = { { 251290, 12 }, { 12359, 80 }, { 7910, 10 }, { 12800, 4 }, { 7971, 20 } }, tool = 162, out = { 250599, 1 }, oq = 4 },
    [1252349] = { name = "Martyr's Legplates", t = { 1, 320, 330, 340 }, scroll = 251452, train = 300, sq = 4, r = { { 251290, 12 }, { 251291, 20 }, { 7078, 10 }, { 13511, 2 } }, tool = 162, out = { 250600, 1 }, oq = 4 },
    [1252350] = { name = "Breastplate of Salvation", t = { 1, 320, 330, 340 }, scroll = 251453, train = 300, sq = 4, r = { { 251290, 12 }, { 12359, 80 }, { 12361, 10 }, { 12800, 4 }, { 12662, 20 } }, tool = 162, out = { 250601, 1 }, oq = 4 },
    [1252351] = { name = "Brass Knuckles", t = { 1, 110, 125, 140 }, scroll = 251454, train = 80, sq = 2, r = { { 2841, 6 }, { 2880, 4 }, { 3470, 2 }, { 1210, 2 }, { 2319, 1 } }, tool = 162, out = { 250602, 1 }, oq = 2 },
    [1252352] = { name = "Bronze Dory", t = { 1, 125, 140, 155 }, scroll = 251455, train = 95, sq = 2, r = { { 2841, 8 }, { 2880, 4 }, { 2319, 1 } }, tool = 162, out = { 250603, 1 }, oq = 2 },
    [1252353] = { name = "Iron Fists", t = { 1, 155, 167, 180 }, scroll = 251456, train = 130, sq = 2, r = { { 3575, 6 }, { 3466, 2 }, { 3486, 1 }, { 2842, 2 }, { 4234, 2 } }, tool = 162, out = { 250604, 1 }, oq = 2 },
    [1252354] = { name = "Steel Spear", t = { 1, 185, 197, 210 }, scroll = 251457, train = 160, sq = 2, r = { { 3859, 10 }, { 3466, 2 }, { 7069, 1 }, { 3486, 4 }, { 4234, 1 } }, tool = 162, out = { 250605, 1 }, oq = 2 },
    [1252355] = { name = "Iron Morningstar", t = { 1, 190, 202, 215 }, scroll = 251458, train = 165, scrollPrice = 6000, sq = 2, r = { { 3575, 14 }, { 3466, 2 }, { 3486, 2 }, { 3864, 4 }, { 4234, 2 } }, tool = 162, out = { 250606, 1 }, oq = 2 },
    [1252356] = { name = "Mithril Shortsword", t = { 1, 200, 210, 220 }, scroll = 251459, train = 180, sq = 2, r = { { 3860, 8 }, { 3466, 2 }, { 3486, 2 }, { 1705, 4 }, { 4234, 2 } }, tool = 162, out = { 250607, 1 }, oq = 2 },
    [1252357] = { name = "Mithril Warhammer", t = { 1, 210, 220, 230 }, scroll = 251460, train = 190, scrollPrice = 7500, sq = 2, r = { { 3860, 12 }, { 3864, 2 }, { 7966, 1 }, { 4234, 4 } }, tool = 162, out = { 250608, 1 }, oq = 2 },
    [1252358] = { name = "Mithril Claws", t = { 1, 215, 225, 235 }, scroll = 251461, train = 195, sq = 2, r = { { 3860, 8 }, { 1529, 1 }, { 7966, 1 }, { 4234, 2 } }, tool = 162, out = { 250609, 1 }, oq = 2 },
    [1252359] = { name = "Mithril Claymore", t = { 1, 215, 225, 235 }, scroll = 251462, train = 195, sq = 2, r = { { 3860, 16 }, { 3577, 6 }, { 7966, 2 }, { 4234, 4 } }, tool = 162, out = { 250610, 1 }, oq = 2 },
    [1252360] = { name = "Mithril Stiletto", t = { 1, 230, 240, 250 }, scroll = 251463, train = 210, sq = 2, r = { { 3860, 16 }, { 1210, 6 }, { 3577, 2 }, { 7966, 1 } }, tool = 162, out = { 250611, 1 }, oq = 2 },
    [1252361] = { name = "Charged Mithril Battleaxe", t = { 1, 235, 245, 255 }, scroll = 251464, train = 215, sq = 2, r = { { 3860, 20 }, { 7082, 6 }, { 7966, 4 }, { 4234, 4 } }, tool = 162, out = { 250612, 1 }, oq = 2 },
    [1252362] = { name = "Thorium Greatmace", t = { 1, 270, 280, 290 }, scroll = 251465, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 30 }, { 251291, 4 }, { 7076, 4 }, { 249726, 10 }, { 12644, 2 } }, tool = 162, out = { 250613, 1 }, oq = 3, bop = true },
    [1252363] = { name = "Thorium Cestus", t = { 1, 270, 280, 290 }, scroll = 251466, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 12359, 20 }, { 251291, 8 }, { 7082, 4 }, { 249726, 10 }, { 12644, 1 } }, tool = 162, out = { 250614, 1 }, oq = 3, bop = true },
    [1252364] = { name = "Thorium Poleaxe", t = { 1, 280, 292, 305 }, scroll = 251467, train = 260, sq = 3, r = { { 12359, 20 }, { 251291, 6 }, { 249726, 10 }, { 12803, 4 }, { 8170, 4 } }, tool = 162, out = { 250615, 1 }, oq = 3 },
    [1252365] = { name = "Bold Dirk", t = { 1, 290, 300, 310 }, scroll = 251468, train = 270, scrollPrice = 100000, sq = 3, r = { { 12359, 30 }, { 7082, 4 }, { 249726, 10 }, { 8170, 4 } }, tool = 162, out = { 250616, 1 }, oq = 2 },
    [1252366] = { name = "Stormcarver", t = { 1, 320, 330, 340 }, scroll = 251469, train = 300, rep = { 576, 6 }, sq = 3, r = { { 251290, 20 }, { 249726, 10 }, { 12644, 2 } }, tool = 162, out = { 250617, 1 }, oq = 3 },
    [1252367] = { name = "Bagh Nakh", t = { 1, 320, 330, 340 }, scroll = 251470, train = 300, rep = { 576, 6 }, sq = 3, r = { { 251290, 10 }, { 251291, 10 }, { 249726, 10 }, { 7910, 4 }, { 12361, 4 } }, tool = 162, out = { 250618, 1 }, oq = 3 },
    [1252368] = { name = "Legionite Glaive", t = { 1, 320, 330, 340 }, scroll = 251471, train = 300, sq = 3, favor = 120, favorRep = 6, r = { { 251290, 15 }, { 251291, 8 }, { 249726, 10 }, { 248820, 4 }, { 248822, 1 } }, tool = 162, out = { 250619, 1 }, oq = 3, bop = true },
    [1263041] = { name = "Anvil", t = { 1, 140, 140, 140 }, scroll = 273086, train = 140, sq = 2, r = { { 2841, 5 }, { 3478, 2 }, { 2319, 2 } }, out = { 279988, 1 }, oq = 1 },
    [1292945] = { name = "Justice Leggings", t = { 1, 320, 325, 330 }, scroll = 273976, train = 300, sq = 4, r = { { 274030, 5 }, { 12360, 4 }, { 251291, 18 }, { 18567, 1 } }, tool = 162, out = { 273908, 1 }, oq = 1 },
    [1292946] = { name = "Justice Gauntlets", t = { 1, 320, 325, 330 }, scroll = 273977, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273909, 1 }, oq = 1 },
    [1292947] = { name = "Justice Spaulders", t = { 1, 320, 325, 330 }, scroll = 273978, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273910, 1 }, oq = 1 },
    [1292948] = { name = "Justice Greaves", t = { 1, 320, 325, 330 }, scroll = 273979, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273911, 1 }, oq = 1 },
    [1292949] = { name = "Justice Legplates", t = { 1, 320, 325, 330 }, scroll = 273980, train = 300, sq = 4, r = { { 274030, 5 }, { 12360, 4 }, { 251291, 18 }, { 18567, 1 } }, tool = 162, out = { 273912, 1 }, oq = 1 },
    [1292950] = { name = "Justice Gloves", t = { 1, 320, 325, 330 }, scroll = 273981, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273913, 1 }, oq = 1 },
    [1292951] = { name = "Justice Epaulets", t = { 1, 320, 325, 330 }, scroll = 273982, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273914, 1 }, oq = 1 },
    [1292952] = { name = "Justice Treads", t = { 1, 320, 325, 330 }, scroll = 273983, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273915, 1 }, oq = 1 },
    [1292953] = { name = "Justice Legguards", t = { 1, 320, 325, 330 }, scroll = 273984, train = 300, sq = 4, r = { { 274030, 5 }, { 12360, 4 }, { 251291, 18 }, { 18567, 1 } }, tool = 162, out = { 273916, 1 }, oq = 1 },
    [1292954] = { name = "Justice Handguards", t = { 1, 320, 325, 330 }, scroll = 273985, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273917, 1 }, oq = 1 },
    [1292955] = { name = "Justice Pauldrons", t = { 1, 320, 325, 330 }, scroll = 273986, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273918, 1 }, oq = 1 },
    [1292956] = { name = "Justice Sabatons", t = { 1, 320, 325, 330 }, scroll = 273987, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273919, 1 }, oq = 1 },
    [1292981] = { name = "Legplates of Glory", t = { 1, 320, 325, 330 }, scroll = 274012, train = 300, sq = 4, r = { { 274030, 5 }, { 12360, 4 }, { 251291, 18 }, { 18567, 1 } }, tool = 162, out = { 273944, 1 }, oq = 1 },
    [1292982] = { name = "Gauntlets of Glory", t = { 1, 320, 325, 330 }, scroll = 274013, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273945, 1 }, oq = 1 },
    [1292983] = { name = "Shoulders of Glory", t = { 1, 320, 325, 330 }, scroll = 274014, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273946, 1 }, oq = 1 },
    [1292984] = { name = "Greaves of Glory", t = { 1, 320, 325, 330 }, scroll = 274015, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273947, 1 }, oq = 1 },
    [1292985] = { name = "Legguards of Glory", t = { 1, 320, 325, 330 }, scroll = 274016, train = 300, sq = 4, r = { { 274030, 5 }, { 12360, 4 }, { 251291, 18 }, { 18567, 1 } }, tool = 162, out = { 273948, 1 }, oq = 1 },
    [1292986] = { name = "Handguards of Glory", t = { 1, 320, 325, 330 }, scroll = 274017, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273949, 1 }, oq = 1 },
    [1292987] = { name = "Pauldrons of Glory", t = { 1, 320, 325, 330 }, scroll = 274018, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273950, 1 }, oq = 1 },
    [1292988] = { name = "Sabatons of Glory", t = { 1, 320, 325, 330 }, scroll = 274019, train = 300, sq = 4, r = { { 274030, 3 }, { 12360, 2 }, { 251291, 12 }, { 18567, 1 } }, tool = 162, out = { 273951, 1 }, oq = 1 },
    [1297138] = { name = "Goregasher Grips", t = { 1, 290, 292, 295 }, scroll = 275598, train = 285, scrollPrice = 75000, rep = { 609, 4 }, sq = 3, r = { { 12359, 7 }, { 12655, 5 }, { 7078, 3 }, { 18567, 1 } }, tool = 162, out = { 275622, 1 }, oq = 3 },
    [1297139] = { name = "Goregasher Support", t = { 1, 295, 297, 300 }, scroll = 275599, train = 290, scrollPrice = 75000, rep = { 609, 5 }, sq = 3, r = { { 12359, 11 }, { 12655, 5 }, { 7078, 3 }, { 18567, 1 } }, tool = 162, out = { 275623, 1 }, oq = 3 },
    [1297140] = { name = "Goregasher Stompers", t = { 1, 295, 297, 300 }, scroll = 275600, train = 295, scrollPrice = 75000, rep = { 609, 5 }, sq = 3, r = { { 12359, 9 }, { 12655, 5 }, { 7078, 3 }, { 18567, 1 } }, tool = 162, out = { 275624, 1 }, oq = 3 },
    [1297141] = { name = "Clutchlord's Grips", t = { 1, 290, 292, 295 }, scroll = 275601, train = 285, scrollPrice = 75000, rep = { 609, 4 }, sq = 3, r = { { 12359, 7 }, { 12655, 5 }, { 7076, 3 }, { 18567, 1 } }, tool = 162, out = { 275625, 1 }, oq = 3 },
    [1297142] = { name = "Clutchlord's Support", t = { 1, 295, 297, 300 }, scroll = 275602, train = 290, scrollPrice = 75000, rep = { 609, 5 }, sq = 3, r = { { 12359, 11 }, { 12655, 5 }, { 7076, 3 }, { 18567, 1 } }, tool = 162, out = { 275626, 1 }, oq = 3 },
    [1297143] = { name = "Clutchlord's Stompers", t = { 1, 295, 297, 300 }, scroll = 275603, train = 295, scrollPrice = 75000, rep = { 609, 5 }, sq = 3, r = { { 12359, 9 }, { 12655, 5 }, { 7076, 3 }, { 18567, 1 } }, tool = 162, out = { 275627, 1 }, oq = 3 },
    [1301421] = { name = "Cloudy Skyforged Chainmail", t = { 1, 65, 67, 70 }, scroll = 276928, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2840, 8 }, { 2880, 1 } }, out = { 276992, 1 }, oq = 2 },
    [1301422] = { name = "Cloudy Skyforged Wristguards", t = { 1, 55, 57, 60 }, scroll = 276929, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2840, 5 } }, tool = 162, out = { 276993, 1 }, oq = 2 },
    [1301423] = { name = "Cloudy Skyforged Gauntlets", t = { 1, 60, 62, 65 }, scroll = 276930, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2840, 7 } }, tool = 162, out = { 276994, 1 }, oq = 2 },
    [1301424] = { name = "Cloudy Skyforged Chain", t = { 1, 55, 57, 60 }, scroll = 276931, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2840, 6 } }, tool = 162, out = { 276995, 1 }, oq = 2 },
    [1301425] = { name = "Cloudy Skyforged Legguards", t = { 1, 65, 67, 70 }, scroll = 276932, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2840, 8 }, { 2880, 1 } }, tool = 162, out = { 276996, 1 }, oq = 2 },
    [1301426] = { name = "Cloudy Skyforged Greaves", t = { 1, 60, 62, 65 }, scroll = 276933, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2840, 7 } }, tool = 162, out = { 276997, 1 }, oq = 2 },
    [1301445] = { name = "Azure Skyforged Chainmail", t = { 1, 65, 67, 70 }, scroll = 276952, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2840, 8 }, { 2880, 1 } }, tool = 162, out = { 277016, 1 }, oq = 2 },
    [1301446] = { name = "Azure Skyforged Wristguards", t = { 1, 55, 57, 60 }, scroll = 276953, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2840, 5 } }, tool = 162, out = { 277017, 1 }, oq = 2 },
    [1301447] = { name = "Azure Skyforged Gauntlets", t = { 1, 60, 62, 65 }, scroll = 276954, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2840, 7 } }, tool = 162, out = { 277018, 1 }, oq = 2 },
    [1301448] = { name = "Azure Skyforged Chain", t = { 1, 55, 57, 60 }, scroll = 276955, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2840, 6 } }, tool = 162, out = { 277019, 1 }, oq = 2 },
    [1301449] = { name = "Azure Skyforged Legguards", t = { 1, 65, 67, 70 }, scroll = 276956, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2840, 8 }, { 2880, 1 } }, tool = 162, out = { 277020, 1 }, oq = 2 },
    [1301450] = { name = "Azure Skyforged Greaves", t = { 1, 60, 62, 65 }, scroll = 276957, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2840, 7 } }, tool = 162, out = { 277021, 1 }, oq = 2 },
    [1301526] = { name = "Cloudy Skyforged Helm", t = { 1, 185, 187, 190 }, scroll = 276976, train = 175, scrollPrice = 100000, rep = { 2787, 4 }, sq = 2, r = { { 3575, 18 }, { 3486, 5 }, { 5498, 1 } }, tool = 162, out = { 277040, 1 }, oq = 2 },
    [1301527] = { name = "Cloudy Skyforged Pauldrons", t = { 1, 185, 187, 190 }, scroll = 276977, train = 175, scrollPrice = 100000, rep = { 2787, 4 }, sq = 2, r = { { 3575, 14 }, { 3486, 3 }, { 5498, 1 } }, tool = 162, out = { 277041, 1 }, oq = 2 },
    [1301534] = { name = "Azure Skyforged Helm", t = { 1, 185, 187, 190 }, scroll = 276984, train = 175, scrollPrice = 100000, rep = { 2740, 4 }, sq = 2, r = { { 3575, 18 }, { 3486, 5 }, { 7909, 1 } }, tool = 162, out = { 277048, 1 }, oq = 2 },
    [1301535] = { name = "Azure Skyforged Pauldrons", t = { 1, 185, 187, 190 }, scroll = 276985, train = 175, scrollPrice = 100000, rep = { 2740, 4 }, sq = 2, r = { { 3575, 14 }, { 3486, 3 }, { 7909, 1 } }, tool = 162, out = { 277049, 1 }, oq = 2 },
    [1302598] = { name = "Rough Copper Chain Boots", t = { 1, 60, 65, 70 }, scroll = 277673, train = 50, sq = 2, r = { { 2840, 9 } }, tool = 162, out = { 277672, 1 }, oq = 2 },
    [1306533] = { name = "Ironwood Blade", t = { 1, 310, 317, 325 }, scroll = 279308, train = 300, sq = 4, r = { { 274030, 2 }, { 251290, 1 }, { 251291, 14 } }, tool = 162, out = { 279259, 1 }, oq = 4 },
    [1306534] = { name = "Forest Defender's Axe", t = { 1, 310, 317, 325 }, scroll = 279309, train = 300, sq = 4, r = { { 274030, 4 }, { 251290, 1 }, { 251291, 20 } }, tool = 162, out = { 279260, 1 }, oq = 4 },
    [1306535] = { name = "Greenhammer", t = { 1, 310, 317, 325 }, scroll = 279310, train = 300, sq = 4, r = { { 274030, 2 }, { 251290, 1 }, { 251291, 16 } }, tool = 162, out = { 279261, 1 }, oq = 4 },
    [1306536] = { name = "Evergreen Shield", t = { 1, 310, 317, 325 }, scroll = 279311, train = 300, sq = 4, r = { { 274030, 2 }, { 251290, 1 }, { 251291, 10 } }, tool = 162, out = { 279262, 1 }, oq = 4 },
    [1306537] = { name = "Depleted Thorium Sabatons", t = { 1, 310, 317, 325 }, scroll = 279312, train = 300, sq = 4, r = { { 274030, 2 }, { 251290, 1 }, { 251291, 12 } }, tool = 162, out = { 279263, 1 }, oq = 4 },
    [1306538] = { name = "Heavy Thorium Gauntlets", t = { 1, 310, 317, 325 }, scroll = 279313, train = 300, sq = 4, r = { { 274030, 2 }, { 251290, 1 }, { 251291, 14 } }, tool = 162, out = { 279264, 1 }, oq = 4 },
    [1306539] = { name = "Azerothium Legplates", t = { 1, 310, 317, 325 }, scroll = 279314, train = 300, sq = 4, r = { { 274030, 3 }, { 251290, 1 }, { 251291, 18 } }, tool = 162, out = { 279265, 1 }, oq = 4 },
    [1317962] = { name = "Cracked Blacksmith Hammer", t = { 1, 115, 117, 120 }, scroll = 285289, train = 110, scrollPrice = 5000, sq = 2, r = { { 2841, 18 }, { 2842, 2 }, { 818, 1 } }, out = { 285279, 1 }, oq = 2, bop = true },
    [1317963] = { name = "Mithril Blacksmith Hammer", t = { 1, 200, 202, 205 }, scroll = 285290, train = 195, scrollPrice = 5000, sq = 2, r = { { 3860, 10 }, { 3577, 2 }, { 7910, 1 } }, out = { 285280, 1 }, oq = 2, bop = true },
    [1317964] = { name = "Arcanite Blacksmith Hammer", t = { 1, 275, 277, 280 }, scroll = 285291, train = 270, scrollPrice = 5000, sq = 3, r = { { 11371, 4 }, { 12360, 1 }, { 12361, 1 } }, out = { 285281, 1 }, oq = 3, bop = true },
    [2662] = { name = "Copper Chain Pants", t = { 40, 50, 70, 90 }, fee = 50, train = 15, r = { { 2840, 4 } }, tool = 162, out = { 2852, 1 }, oq = 2 },
    [2739] = { name = "Copper Shortsword", t = { 40, 65, 85, 105 }, fee = 50, train = 25, r = { { 2840, 6 }, { 2880, 1 }, { 2589, 2 } }, tool = 162, out = { 2847, 1 }, oq = 2 },
    [2665] = { name = "Coarse Sharpening Stone", t = { 75, 40, 47, 55 }, fee = 100, train = 40, r = { { 2836, 1 } }, out = { 2863, 1 }, oq = 1 },
    [2740] = { name = "Bronze Mace", t = { 75, 115, 130, 145 }, fee = 200, train = 85, r = { { 2841, 6 }, { 2880, 4 }, { 2319, 1 } }, tool = 162, out = { 2848, 1 }, oq = 2 },
    [2666] = { name = "Runed Copper Belt", t = { 80, 85, 105, 125 }, fee = 200, train = 45, r = { { 2840, 10 } }, tool = 162, out = { 2857, 1 }, oq = 2 },
    [2741] = { name = "Bronze Axe", t = { 85, 120, 135, 150 }, fee = 200, train = 90, r = { { 2841, 7 }, { 2880, 4 }, { 2319, 1 } }, tool = 162, out = { 2849, 1 }, oq = 2 },
    [2667] = { name = "Runed Copper Breastplate", t = { 90, 95, 115, 135 }, scroll = 2881, train = 55, sq = 2, r = { { 2840, 12 }, { 1210, 1 }, { 3470, 2 } }, tool = 162, out = { 2864, 1 }, oq = 2 },
    [2668] = { name = "Rough Bronze Leggings", t = { 95, 120, 135, 150 }, fee = 300, train = 80, r = { { 2841, 6 } }, tool = 162, out = { 2865, 1 }, oq = 2 },
    [2742] = { name = "Bronze Shortsword", t = { 95, 125, 140, 155 }, fee = 200, train = 95, r = { { 2841, 5 }, { 2880, 4 }, { 2319, 2 } }, tool = 162, out = { 2850, 1 }, oq = 2 },
    [2670] = { name = "Rough Bronze Cuirass", t = { 105, 120, 135, 150 }, fee = 500, train = 80, r = { { 2841, 7 } }, tool = 162, out = { 2866, 1 }, oq = 2 },
    [2672] = { name = "Patterned Bronze Bracers", t = { 120, 125, 140, 155 }, fee = 500, train = 95, r = { { 2841, 5 }, { 3478, 2 } }, tool = 162, out = { 2868, 1 }, oq = 2 },
    [2674] = { name = "Heavy Sharpening Stone", t = { 125, 100, 107, 115 }, fee = 1000, train = 100, r = { { 2838, 1 } }, out = { 2871, 1 }, oq = 1 },
    [2675] = { name = "Shining Silver Breastplate", t = { 135, 150, 165, 180 }, fee = 1000, train = 120, r = { { 2841, 20 }, { 1206, 2 }, { 1705, 2 }, { 5500, 2 }, { 2842, 4 } }, tool = 162, out = { 2870, 1 }, oq = 3 },
  },
}

-- Herramientas: [categoría] = { objeto, máscara } (un bastón superior cubre a los inferiores)
ES.Data.Tools = ES.Data.Tools or {}
ES.Data.Tools[12] = { item = 9149, mask = 1, family = "stone" }
ES.Data.Tools[14] = { item = 6219, mask = 1, family = "spanner" }
ES.Data.Tools[15] = { item = 10498, mask = 2, family = "adjustor" }
ES.Data.Tools[162] = { item = 5956, mask = 4, family = "hammer" }
ES.Data.Tools[373] = { item = 6218, mask = 1, family = "rod" }
ES.Data.Tools[374] = { item = 6339, mask = 3, family = "rod" }
ES.Data.Tools[375] = { item = 11130, mask = 7, family = "rod" }
ES.Data.Tools[376] = { item = 11145, mask = 15, family = "rod" }
ES.Data.Tools[377] = { item = 16207, mask = 31, family = "rod" }

ES.Data.VendorPrices = ES.Data.VendorPrices or {}
ES.Data.SellPrices = ES.Data.SellPrices or {}
ES.Data.VendorPrices[2320] = 10
ES.Data.VendorPrices[2605] = 100
ES.Data.VendorPrices[2880] = 100
ES.Data.VendorPrices[3466] = 2000
ES.Data.VendorPrices[5956] = 18
ES.Data.VendorPrices[6217] = 124
ES.Data.VendorPrices[10938] = 800
ES.Data.VendorPrices[10940] = 800
ES.Data.VendorPrices[18567] = 150000
ES.Data.SellPrices[774] = 15
ES.Data.SellPrices[818] = 100
ES.Data.SellPrices[1206] = 400
ES.Data.SellPrices[1210] = 250
ES.Data.SellPrices[1529] = 700
ES.Data.SellPrices[1705] = 600
ES.Data.SellPrices[2318] = 15
ES.Data.SellPrices[2319] = 50
ES.Data.SellPrices[2320] = 2
ES.Data.SellPrices[2459] = 25
ES.Data.SellPrices[2589] = 13
ES.Data.SellPrices[2605] = 25
ES.Data.SellPrices[2835] = 2
ES.Data.SellPrices[2836] = 15
ES.Data.SellPrices[2838] = 60
ES.Data.SellPrices[2840] = 10
ES.Data.SellPrices[2841] = 50
ES.Data.SellPrices[2842] = 100
ES.Data.SellPrices[2844] = 106
ES.Data.SellPrices[2845] = 109
ES.Data.SellPrices[2847] = 110
ES.Data.SellPrices[2848] = 898
ES.Data.SellPrices[2849] = 917
ES.Data.SellPrices[2850] = 1136
ES.Data.SellPrices[2851] = 56
ES.Data.SellPrices[2852] = 67
ES.Data.SellPrices[2853] = 17
ES.Data.SellPrices[2854] = 225
ES.Data.SellPrices[2857] = 198
ES.Data.SellPrices[2862] = 3
ES.Data.SellPrices[2863] = 10
ES.Data.SellPrices[2864] = 630
ES.Data.SellPrices[2865] = 577
ES.Data.SellPrices[2866] = 601
ES.Data.SellPrices[2867] = 317
ES.Data.SellPrices[2868] = 507
ES.Data.SellPrices[2869] = 1831
ES.Data.SellPrices[2870] = 2935
ES.Data.SellPrices[2871] = 40
ES.Data.SellPrices[2880] = 25
ES.Data.SellPrices[3239] = 3
ES.Data.SellPrices[3240] = 10
ES.Data.SellPrices[3241] = 40
ES.Data.SellPrices[3391] = 20
ES.Data.SellPrices[3466] = 500
ES.Data.SellPrices[3469] = 49
ES.Data.SellPrices[3470] = 5
ES.Data.SellPrices[3471] = 142
ES.Data.SellPrices[3472] = 71
ES.Data.SellPrices[3473] = 299
ES.Data.SellPrices[3474] = 216
ES.Data.SellPrices[3478] = 10
ES.Data.SellPrices[3480] = 532
ES.Data.SellPrices[3481] = 916
ES.Data.SellPrices[3482] = 918
ES.Data.SellPrices[3483] = 965
ES.Data.SellPrices[3484] = 1767
ES.Data.SellPrices[3485] = 1295
ES.Data.SellPrices[3486] = 100
ES.Data.SellPrices[3487] = 1135
ES.Data.SellPrices[3488] = 480
ES.Data.SellPrices[3489] = 715
ES.Data.SellPrices[3490] = 2044
ES.Data.SellPrices[3491] = 2741
ES.Data.SellPrices[3492] = 4552
ES.Data.SellPrices[3575] = 200
ES.Data.SellPrices[3577] = 600
ES.Data.SellPrices[3823] = 100
ES.Data.SellPrices[3824] = 150
ES.Data.SellPrices[3829] = 150
ES.Data.SellPrices[3835] = 1106
ES.Data.SellPrices[3836] = 3053
ES.Data.SellPrices[3837] = 3084
ES.Data.SellPrices[3840] = 2571
ES.Data.SellPrices[3841] = 3106
ES.Data.SellPrices[3842] = 2906
ES.Data.SellPrices[3843] = 3882
ES.Data.SellPrices[3844] = 5658
ES.Data.SellPrices[3845] = 6558
ES.Data.SellPrices[3846] = 3937
ES.Data.SellPrices[3847] = 4977
ES.Data.SellPrices[3848] = 915
ES.Data.SellPrices[3849] = 5468
ES.Data.SellPrices[3850] = 7304
ES.Data.SellPrices[3851] = 6258
ES.Data.SellPrices[3852] = 8360
ES.Data.SellPrices[3853] = 8615
ES.Data.SellPrices[3854] = 8860
ES.Data.SellPrices[3855] = 11248
ES.Data.SellPrices[3856] = 10386
ES.Data.SellPrices[3859] = 60
ES.Data.SellPrices[3860] = 400
ES.Data.SellPrices[3864] = 800
ES.Data.SellPrices[4234] = 150
ES.Data.SellPrices[4255] = 2366
ES.Data.SellPrices[4304] = 300
ES.Data.SellPrices[4338] = 250
ES.Data.SellPrices[5498] = 200
ES.Data.SellPrices[5500] = 750
ES.Data.SellPrices[5540] = 2107
ES.Data.SellPrices[5541] = 3693
ES.Data.SellPrices[5635] = 45
ES.Data.SellPrices[5637] = 75
ES.Data.SellPrices[5956] = 3
ES.Data.SellPrices[5966] = 1374
ES.Data.SellPrices[6037] = 1250
ES.Data.SellPrices[6040] = 1315
ES.Data.SellPrices[6041] = 1500
ES.Data.SellPrices[6042] = 250
ES.Data.SellPrices[6043] = 500
ES.Data.SellPrices[6214] = 466
ES.Data.SellPrices[6217] = 24
ES.Data.SellPrices[6338] = 125
ES.Data.SellPrices[6350] = 295
ES.Data.SellPrices[6730] = 298
ES.Data.SellPrices[6731] = 690
ES.Data.SellPrices[6733] = 1145
ES.Data.SellPrices[7067] = 400
ES.Data.SellPrices[7068] = 400
ES.Data.SellPrices[7069] = 400
ES.Data.SellPrices[7070] = 400
ES.Data.SellPrices[7071] = 100
ES.Data.SellPrices[7075] = 400
ES.Data.SellPrices[7076] = 400
ES.Data.SellPrices[7077] = 400
ES.Data.SellPrices[7078] = 400
ES.Data.SellPrices[7079] = 400
ES.Data.SellPrices[7080] = 400
ES.Data.SellPrices[7081] = 400
ES.Data.SellPrices[7082] = 400
ES.Data.SellPrices[7166] = 194
ES.Data.SellPrices[7909] = 1000
ES.Data.SellPrices[7910] = 5000
ES.Data.SellPrices[7912] = 100
ES.Data.SellPrices[7913] = 2500
ES.Data.SellPrices[7914] = 3330
ES.Data.SellPrices[7915] = 3337
ES.Data.SellPrices[7916] = 3700
ES.Data.SellPrices[7917] = 2711
ES.Data.SellPrices[7918] = 3701
ES.Data.SellPrices[7919] = 2476
ES.Data.SellPrices[7920] = 8053
ES.Data.SellPrices[7921] = 5387
ES.Data.SellPrices[7922] = 1944
ES.Data.SellPrices[7924] = 4103
ES.Data.SellPrices[7925] = 4447
ES.Data.SellPrices[7926] = 5952
ES.Data.SellPrices[7927] = 2987
ES.Data.SellPrices[7928] = 4857
ES.Data.SellPrices[7929] = 7739
ES.Data.SellPrices[7930] = 7045
ES.Data.SellPrices[7931] = 7955
ES.Data.SellPrices[7932] = 8661
ES.Data.SellPrices[7933] = 5769
ES.Data.SellPrices[7934] = 5790
ES.Data.SellPrices[7935] = 8368
ES.Data.SellPrices[7936] = 6739
ES.Data.SellPrices[7937] = 6763
ES.Data.SellPrices[7938] = 4028
ES.Data.SellPrices[7939] = 10899
ES.Data.SellPrices[7941] = 12520
ES.Data.SellPrices[7942] = 14659
ES.Data.SellPrices[7943] = 15891
ES.Data.SellPrices[7944] = 14671
ES.Data.SellPrices[7945] = 17291
ES.Data.SellPrices[7946] = 14460
ES.Data.SellPrices[7947] = 24892
ES.Data.SellPrices[7954] = 23159
ES.Data.SellPrices[7955] = 241
ES.Data.SellPrices[7956] = 1544
ES.Data.SellPrices[7957] = 2205
ES.Data.SellPrices[7958] = 2435
ES.Data.SellPrices[7959] = 33857
ES.Data.SellPrices[7960] = 38548
ES.Data.SellPrices[7961] = 25508
ES.Data.SellPrices[7963] = 5615
ES.Data.SellPrices[7964] = 40
ES.Data.SellPrices[7965] = 40
ES.Data.SellPrices[7966] = 200
ES.Data.SellPrices[7967] = 250
ES.Data.SellPrices[7969] = 250
ES.Data.SellPrices[7971] = 1000
ES.Data.SellPrices[7972] = 400
ES.Data.SellPrices[8146] = 500
ES.Data.SellPrices[8153] = 5
ES.Data.SellPrices[8168] = 100
ES.Data.SellPrices[8170] = 500
ES.Data.SellPrices[8831] = 300
ES.Data.SellPrices[9060] = 1000
ES.Data.SellPrices[9366] = 3689
ES.Data.SellPrices[10421] = 32
ES.Data.SellPrices[10423] = 2366
ES.Data.SellPrices[10938] = 1
ES.Data.SellPrices[10940] = 1
ES.Data.SellPrices[11128] = 500
ES.Data.SellPrices[11139] = 1
ES.Data.SellPrices[11144] = 1000
ES.Data.SellPrices[11371] = 600
ES.Data.SellPrices[11382] = 750
ES.Data.SellPrices[11604] = 19428
ES.Data.SellPrices[11605] = 10776
ES.Data.SellPrices[11606] = 19255
ES.Data.SellPrices[11607] = 51225
ES.Data.SellPrices[11608] = 45760
ES.Data.SellPrices[12259] = 8072
ES.Data.SellPrices[12260] = 8165
ES.Data.SellPrices[12359] = 600
ES.Data.SellPrices[12360] = 5000
ES.Data.SellPrices[12361] = 7000
ES.Data.SellPrices[12364] = 10000
ES.Data.SellPrices[12365] = 250
ES.Data.SellPrices[12404] = 75
ES.Data.SellPrices[12405] = 9239
ES.Data.SellPrices[12406] = 4636
ES.Data.SellPrices[12408] = 4998
ES.Data.SellPrices[12409] = 10336
ES.Data.SellPrices[12410] = 10372
ES.Data.SellPrices[12414] = 17376
ES.Data.SellPrices[12415] = 17003
ES.Data.SellPrices[12416] = 7595
ES.Data.SellPrices[12417] = 17034
ES.Data.SellPrices[12418] = 10242
ES.Data.SellPrices[12419] = 16421
ES.Data.SellPrices[12420] = 25330
ES.Data.SellPrices[12422] = 16204
ES.Data.SellPrices[12424] = 5533
ES.Data.SellPrices[12425] = 6044
ES.Data.SellPrices[12426] = 12062
ES.Data.SellPrices[12427] = 12106
ES.Data.SellPrices[12428] = 8646
ES.Data.SellPrices[12429] = 17923
ES.Data.SellPrices[12610] = 12247
ES.Data.SellPrices[12611] = 12293
ES.Data.SellPrices[12612] = 12956
ES.Data.SellPrices[12613] = 18205
ES.Data.SellPrices[12614] = 18272
ES.Data.SellPrices[12618] = 23972
ES.Data.SellPrices[12619] = 24058
ES.Data.SellPrices[12620] = 17245
ES.Data.SellPrices[12625] = 13080
ES.Data.SellPrices[12631] = 8919
ES.Data.SellPrices[12633] = 14859
ES.Data.SellPrices[12639] = 15271
ES.Data.SellPrices[12640] = 21894
ES.Data.SellPrices[12643] = 75
ES.Data.SellPrices[12644] = 200
ES.Data.SellPrices[12645] = 500
ES.Data.SellPrices[12655] = 500
ES.Data.SellPrices[12662] = 600
ES.Data.SellPrices[12764] = 23534
ES.Data.SellPrices[12769] = 46154
ES.Data.SellPrices[12772] = 38871
ES.Data.SellPrices[12773] = 33079
ES.Data.SellPrices[12774] = 36044
ES.Data.SellPrices[12775] = 39949
ES.Data.SellPrices[12776] = 48124
ES.Data.SellPrices[12777] = 38648
ES.Data.SellPrices[12781] = 42721
ES.Data.SellPrices[12782] = 56808
ES.Data.SellPrices[12783] = 58215
ES.Data.SellPrices[12784] = 73036
ES.Data.SellPrices[12790] = 74619
ES.Data.SellPrices[12792] = 39255
ES.Data.SellPrices[12794] = 56304
ES.Data.SellPrices[12795] = 48821
ES.Data.SellPrices[12796] = 70912
ES.Data.SellPrices[12797] = 56943
ES.Data.SellPrices[12798] = 57150
ES.Data.SellPrices[12799] = 7000
ES.Data.SellPrices[12800] = 10000
ES.Data.SellPrices[12802] = 62625
ES.Data.SellPrices[12803] = 500
ES.Data.SellPrices[12804] = 2000
ES.Data.SellPrices[12808] = 1000
ES.Data.SellPrices[12809] = 10000
ES.Data.SellPrices[12810] = 500
ES.Data.SellPrices[12811] = 20000
ES.Data.SellPrices[13510] = 5000
ES.Data.SellPrices[13511] = 5000
ES.Data.SellPrices[13512] = 5000
ES.Data.SellPrices[13926] = 10000
ES.Data.SellPrices[15417] = 500
ES.Data.SellPrices[15869] = 50
ES.Data.SellPrices[15870] = 300
ES.Data.SellPrices[15871] = 625
ES.Data.SellPrices[15872] = 625
ES.Data.SellPrices[16206] = 1000
ES.Data.SellPrices[16988] = 31460
ES.Data.SellPrices[16989] = 18610
ES.Data.SellPrices[17010] = 2000
ES.Data.SellPrices[17011] = 2000
ES.Data.SellPrices[17012] = 1000
ES.Data.SellPrices[17013] = 26441
ES.Data.SellPrices[17014] = 12637
ES.Data.SellPrices[17015] = 63738
ES.Data.SellPrices[17016] = 63973
ES.Data.SellPrices[17193] = 122311
ES.Data.SellPrices[17203] = 100000
ES.Data.SellPrices[17704] = 9178
ES.Data.SellPrices[18262] = 1250
ES.Data.SellPrices[18567] = 37500
ES.Data.SellPrices[19051] = 9365
ES.Data.SellPrices[19057] = 11606
ES.Data.SellPrices[19148] = 25399
ES.Data.SellPrices[19164] = 22425
ES.Data.SellPrices[19166] = 92896
ES.Data.SellPrices[19167] = 116531
ES.Data.SellPrices[19168] = 102890
ES.Data.SellPrices[19169] = 129112
ES.Data.SellPrices[19170] = 103689
ES.Data.SellPrices[19690] = 39683
ES.Data.SellPrices[19691] = 30000
ES.Data.SellPrices[19692] = 19980
ES.Data.SellPrices[19693] = 24192
ES.Data.SellPrices[19694] = 24286
ES.Data.SellPrices[19695] = 18285
ES.Data.SellPrices[19726] = 500
ES.Data.SellPrices[19774] = 5000
ES.Data.SellPrices[20039] = 31709
ES.Data.SellPrices[20381] = 5000
ES.Data.SellPrices[20520] = 2000
ES.Data.SellPrices[20549] = 11484
ES.Data.SellPrices[20550] = 23051
ES.Data.SellPrices[20551] = 17352
ES.Data.SellPrices[20725] = 1
ES.Data.SellPrices[22191] = 73128
ES.Data.SellPrices[22194] = 33521
ES.Data.SellPrices[22195] = 22885
ES.Data.SellPrices[22196] = 49624
ES.Data.SellPrices[22197] = 14282
ES.Data.SellPrices[22198] = 67440
ES.Data.SellPrices[22202] = 2500
ES.Data.SellPrices[22203] = 5000
ES.Data.SellPrices[22383] = 84291
ES.Data.SellPrices[22384] = 80554
ES.Data.SellPrices[22385] = 25276
ES.Data.SellPrices[22669] = 68390
ES.Data.SellPrices[22670] = 34321
ES.Data.SellPrices[22671] = 34452
ES.Data.SellPrices[22682] = 20000
ES.Data.SellPrices[211845] = 125
ES.Data.SellPrices[213369] = 280
ES.Data.SellPrices[213379] = 280
ES.Data.SellPrices[248820] = 15000
ES.Data.SellPrices[248822] = 1500
ES.Data.SellPrices[249410] = 125
ES.Data.SellPrices[249427] = 125
ES.Data.SellPrices[249432] = 250
ES.Data.SellPrices[249726] = 3000
ES.Data.SellPrices[250483] = 1267
ES.Data.SellPrices[250484] = 1908
ES.Data.SellPrices[250485] = 957
ES.Data.SellPrices[250486] = 490
ES.Data.SellPrices[250487] = 485
ES.Data.SellPrices[250503] = 1054
ES.Data.SellPrices[250504] = 1057
ES.Data.SellPrices[250505] = 1061
ES.Data.SellPrices[250506] = 1065
ES.Data.SellPrices[250507] = 1069
ES.Data.SellPrices[250508] = 487
ES.Data.SellPrices[250509] = 489
ES.Data.SellPrices[250510] = 504
ES.Data.SellPrices[250511] = 506
ES.Data.SellPrices[250512] = 508
ES.Data.SellPrices[250513] = 335
ES.Data.SellPrices[250514] = 336
ES.Data.SellPrices[250515] = 337
ES.Data.SellPrices[250516] = 339
ES.Data.SellPrices[250517] = 340
ES.Data.SellPrices[250518] = 2464
ES.Data.SellPrices[250519] = 2473
ES.Data.SellPrices[250520] = 2482
ES.Data.SellPrices[250521] = 2491
ES.Data.SellPrices[250522] = 2500
ES.Data.SellPrices[250523] = 3340
ES.Data.SellPrices[250524] = 3352
ES.Data.SellPrices[250525] = 3363
ES.Data.SellPrices[250526] = 3137
ES.Data.SellPrices[250527] = 3149
ES.Data.SellPrices[250528] = 1439
ES.Data.SellPrices[250529] = 1444
ES.Data.SellPrices[250530] = 1450
ES.Data.SellPrices[250531] = 1455
ES.Data.SellPrices[250532] = 1460
ES.Data.SellPrices[250533] = 3929
ES.Data.SellPrices[250534] = 3268
ES.Data.SellPrices[250535] = 2634
ES.Data.SellPrices[250536] = 5711
ES.Data.SellPrices[250537] = 5036
ES.Data.SellPrices[250538] = 3354
ES.Data.SellPrices[250539] = 5073
ES.Data.SellPrices[250540] = 11586
ES.Data.SellPrices[250541] = 8704
ES.Data.SellPrices[250542] = 8110
ES.Data.SellPrices[250543] = 10255
ES.Data.SellPrices[250544] = 14716
ES.Data.SellPrices[250545] = 7428
ES.Data.SellPrices[250561] = 15856
ES.Data.SellPrices[250562] = 15918
ES.Data.SellPrices[250563] = 15979
ES.Data.SellPrices[250564] = 16041
ES.Data.SellPrices[250565] = 16101
ES.Data.SellPrices[250566] = 3850
ES.Data.SellPrices[250567] = 3864
ES.Data.SellPrices[250568] = 3878
ES.Data.SellPrices[250569] = 3893
ES.Data.SellPrices[250570] = 3908
ES.Data.SellPrices[250571] = 13177
ES.Data.SellPrices[250572] = 13225
ES.Data.SellPrices[250573] = 13274
ES.Data.SellPrices[250574] = 13677
ES.Data.SellPrices[250575] = 13726
ES.Data.SellPrices[250576] = 12276
ES.Data.SellPrices[250577] = 12320
ES.Data.SellPrices[250578] = 12364
ES.Data.SellPrices[250579] = 12408
ES.Data.SellPrices[250580] = 12450
ES.Data.SellPrices[250581] = 9390
ES.Data.SellPrices[250582] = 9426
ES.Data.SellPrices[250583] = 9462
ES.Data.SellPrices[250584] = 9498
ES.Data.SellPrices[250585] = 9535
ES.Data.SellPrices[250586] = 13467
ES.Data.SellPrices[250587] = 13517
ES.Data.SellPrices[250588] = 10241
ES.Data.SellPrices[250589] = 12244
ES.Data.SellPrices[250590] = 12621
ES.Data.SellPrices[250591] = 28034
ES.Data.SellPrices[250592] = 14148
ES.Data.SellPrices[250593] = 22196
ES.Data.SellPrices[250594] = 31247
ES.Data.SellPrices[250595] = 39509
ES.Data.SellPrices[250596] = 41634
ES.Data.SellPrices[250597] = 31277
ES.Data.SellPrices[250598] = 50706
ES.Data.SellPrices[250599] = 38092
ES.Data.SellPrices[250600] = 51067
ES.Data.SellPrices[250601] = 46368
ES.Data.SellPrices[250602] = 1562
ES.Data.SellPrices[250603] = 488
ES.Data.SellPrices[250604] = 4754
ES.Data.SellPrices[250605] = 2501
ES.Data.SellPrices[250606] = 9416
ES.Data.SellPrices[250607] = 11906
ES.Data.SellPrices[250608] = 4356
ES.Data.SellPrices[250609] = 4079
ES.Data.SellPrices[250610] = 20470
ES.Data.SellPrices[250611] = 4133
ES.Data.SellPrices[250612] = 10273
ES.Data.SellPrices[250613] = 48384
ES.Data.SellPrices[250614] = 38843
ES.Data.SellPrices[250615] = 54752
ES.Data.SellPrices[250616] = 40772
ES.Data.SellPrices[250617] = 74598
ES.Data.SellPrices[250618] = 59891
ES.Data.SellPrices[250619] = 75130
ES.Data.SellPrices[251290] = 5000
ES.Data.SellPrices[251291] = 1500
ES.Data.SellPrices[275622] = 15752
ES.Data.SellPrices[275623] = 15809
ES.Data.SellPrices[275624] = 23622
ES.Data.SellPrices[275625] = 15927
ES.Data.SellPrices[275626] = 15986
ES.Data.SellPrices[275627] = 23882
ES.Data.SellPrices[277672] = 49
ES.Data.SellPrices[279259] = 10484
ES.Data.SellPrices[279260] = 5062
ES.Data.SellPrices[279261] = 53222
ES.Data.SellPrices[279262] = 19893
ES.Data.SellPrices[279263] = 13732
ES.Data.SellPrices[279264] = 13149
ES.Data.SellPrices[279265] = 13732
ES.Data.SellPrices[285279] = 1411
ES.Data.SellPrices[285280] = 7658
ES.Data.SellPrices[285281] = 26186

-- Nombre de cada objeto (inglés, del cliente): se muestra mientras el juego no lo ha cargado
ES.Data.ItemNames = ES.Data.ItemNames or {}
ES.Data.ItemNames[774] = "Malachite"
ES.Data.ItemNames[818] = "Tigerseye"
ES.Data.ItemNames[1206] = "Moss Agate"
ES.Data.ItemNames[1210] = "Shadowgem"
ES.Data.ItemNames[1529] = "Jade"
ES.Data.ItemNames[1705] = "Lesser Moonstone"
ES.Data.ItemNames[2318] = "Light Leather"
ES.Data.ItemNames[2319] = "Medium Leather"
ES.Data.ItemNames[2320] = "Coarse Thread"
ES.Data.ItemNames[2459] = "Swiftness Potion"
ES.Data.ItemNames[2589] = "Linen Cloth"
ES.Data.ItemNames[2605] = "Green Dye"
ES.Data.ItemNames[2835] = "Rough Stone"
ES.Data.ItemNames[2836] = "Coarse Stone"
ES.Data.ItemNames[2838] = "Heavy Stone"
ES.Data.ItemNames[2840] = "Copper Bar"
ES.Data.ItemNames[2841] = "Bronze Bar"
ES.Data.ItemNames[2842] = "Silver Bar"
ES.Data.ItemNames[2844] = "Copper Mace"
ES.Data.ItemNames[2845] = "Copper Axe"
ES.Data.ItemNames[2847] = "Copper Shortsword"
ES.Data.ItemNames[2848] = "Bronze Mace"
ES.Data.ItemNames[2849] = "Bronze Axe"
ES.Data.ItemNames[2850] = "Bronze Shortsword"
ES.Data.ItemNames[2851] = "Copper Chain Belt"
ES.Data.ItemNames[2852] = "Copper Chain Pants"
ES.Data.ItemNames[2853] = "Copper Bracers"
ES.Data.ItemNames[2854] = "Runed Copper Bracers"
ES.Data.ItemNames[2857] = "Runed Copper Belt"
ES.Data.ItemNames[2862] = "Rough Sharpening Stone"
ES.Data.ItemNames[2863] = "Coarse Sharpening Stone"
ES.Data.ItemNames[2864] = "Runed Copper Breastplate"
ES.Data.ItemNames[2865] = "Rough Bronze Leggings"
ES.Data.ItemNames[2866] = "Rough Bronze Cuirass"
ES.Data.ItemNames[2867] = "Rough Bronze Bracers"
ES.Data.ItemNames[2868] = "Patterned Bronze Bracers"
ES.Data.ItemNames[2869] = "Silvered Bronze Breastplate"
ES.Data.ItemNames[2870] = "Shining Silver Breastplate"
ES.Data.ItemNames[2871] = "Heavy Sharpening Stone"
ES.Data.ItemNames[2880] = "Weak Flux"
ES.Data.ItemNames[3239] = "Rough Weightstone"
ES.Data.ItemNames[3240] = "Coarse Weightstone"
ES.Data.ItemNames[3241] = "Heavy Weightstone"
ES.Data.ItemNames[3391] = "Elixir of Ogre Strength"
ES.Data.ItemNames[3466] = "Strong Flux"
ES.Data.ItemNames[3469] = "Copper Chain Boots"
ES.Data.ItemNames[3470] = "Rough Grinding Stone"
ES.Data.ItemNames[3471] = "Copper Chain Vest"
ES.Data.ItemNames[3472] = "Runed Copper Gauntlets"
ES.Data.ItemNames[3473] = "Runed Copper Pants"
ES.Data.ItemNames[3474] = "Gemmed Copper Gauntlets"
ES.Data.ItemNames[3478] = "Coarse Grinding Stone"
ES.Data.ItemNames[3480] = "Rough Bronze Shoulders"
ES.Data.ItemNames[3481] = "Silvered Bronze Shoulders"
ES.Data.ItemNames[3482] = "Silvered Bronze Boots"
ES.Data.ItemNames[3483] = "Silvered Bronze Gauntlets"
ES.Data.ItemNames[3484] = "Green Iron Boots"
ES.Data.ItemNames[3485] = "Green Iron Gauntlets"
ES.Data.ItemNames[3486] = "Heavy Grinding Stone"
ES.Data.ItemNames[3487] = "Heavy Copper Broadsword"
ES.Data.ItemNames[3488] = "Copper Battle Axe"
ES.Data.ItemNames[3489] = "Thick War Axe"
ES.Data.ItemNames[3490] = "Deadly Bronze Poniard"
ES.Data.ItemNames[3491] = "Heavy Bronze Mace"
ES.Data.ItemNames[3492] = "Mighty Iron Hammer"
ES.Data.ItemNames[3575] = "Iron Bar"
ES.Data.ItemNames[3577] = "Gold Bar"
ES.Data.ItemNames[3823] = "Lesser Invisibility Potion"
ES.Data.ItemNames[3824] = "Shadow Oil"
ES.Data.ItemNames[3829] = "Frost Oil"
ES.Data.ItemNames[3835] = "Green Iron Bracers"
ES.Data.ItemNames[3836] = "Green Iron Helm"
ES.Data.ItemNames[3837] = "Golden Scale Coif"
ES.Data.ItemNames[3840] = "Green Iron Shoulders"
ES.Data.ItemNames[3841] = "Golden Scale Shoulders"
ES.Data.ItemNames[3842] = "Green Iron Leggings"
ES.Data.ItemNames[3843] = "Golden Scale Leggings"
ES.Data.ItemNames[3844] = "Green Iron Hauberk"
ES.Data.ItemNames[3845] = "Golden Scale Cuirass"
ES.Data.ItemNames[3846] = "Polished Steel Boots"
ES.Data.ItemNames[3847] = "Golden Scale Boots"
ES.Data.ItemNames[3848] = "Big Bronze Knife"
ES.Data.ItemNames[3849] = "Hardened Iron Shortsword"
ES.Data.ItemNames[3850] = "Jade Serpentblade"
ES.Data.ItemNames[3851] = "Solid Iron Maul"
ES.Data.ItemNames[3852] = "Golden Iron Destroyer"
ES.Data.ItemNames[3853] = "Moonsteel Broadsword"
ES.Data.ItemNames[3854] = "Frost Tiger Blade"
ES.Data.ItemNames[3855] = "Massive Iron Axe"
ES.Data.ItemNames[3856] = "Shadow Crescent Axe"
ES.Data.ItemNames[3859] = "Steel Bar"
ES.Data.ItemNames[3860] = "Mithril Bar"
ES.Data.ItemNames[3864] = "Citrine"
ES.Data.ItemNames[4234] = "Heavy Leather"
ES.Data.ItemNames[4255] = "Green Leather Armor"
ES.Data.ItemNames[4304] = "Thick Leather"
ES.Data.ItemNames[4338] = "Mageweave Cloth"
ES.Data.ItemNames[5498] = "Small Lustrous Pearl"
ES.Data.ItemNames[5500] = "Iridescent Pearl"
ES.Data.ItemNames[5540] = "Pearl-handled Dagger"
ES.Data.ItemNames[5541] = "Iridescent Hammer"
ES.Data.ItemNames[5635] = "Sharp Claw"
ES.Data.ItemNames[5637] = "Large Fang"
ES.Data.ItemNames[5956] = "Blacksmith Hammer"
ES.Data.ItemNames[5966] = "Guardian Gloves"
ES.Data.ItemNames[6037] = "Truesilver Bar"
ES.Data.ItemNames[6040] = "Golden Scale Bracers"
ES.Data.ItemNames[6041] = "Steel Weapon Chain"
ES.Data.ItemNames[6042] = "Iron Shield Spike"
ES.Data.ItemNames[6043] = "Iron Counterweight"
ES.Data.ItemNames[6214] = "Heavy Copper Maul"
ES.Data.ItemNames[6217] = "Copper Rod"
ES.Data.ItemNames[6338] = "Silver Rod"
ES.Data.ItemNames[6350] = "Rough Bronze Boots"
ES.Data.ItemNames[6730] = "Ironforge Chain"
ES.Data.ItemNames[6731] = "Ironforge Breastplate"
ES.Data.ItemNames[6733] = "Ironforge Gauntlets"
ES.Data.ItemNames[7067] = "Elemental Earth"
ES.Data.ItemNames[7068] = "Elemental Fire"
ES.Data.ItemNames[7069] = "Elemental Air"
ES.Data.ItemNames[7070] = "Elemental Water"
ES.Data.ItemNames[7071] = "Iron Buckle"
ES.Data.ItemNames[7075] = "Core of Earth"
ES.Data.ItemNames[7076] = "Essence of Earth"
ES.Data.ItemNames[7077] = "Heart of Fire"
ES.Data.ItemNames[7078] = "Essence of Fire"
ES.Data.ItemNames[7079] = "Globe of Water"
ES.Data.ItemNames[7080] = "Essence of Water"
ES.Data.ItemNames[7081] = "Breath of Wind"
ES.Data.ItemNames[7082] = "Essence of Air"
ES.Data.ItemNames[7166] = "Copper Dagger"
ES.Data.ItemNames[7909] = "Aquamarine"
ES.Data.ItemNames[7910] = "Star Ruby"
ES.Data.ItemNames[7912] = "Solid Stone"
ES.Data.ItemNames[7913] = "Barbaric Iron Shoulders"
ES.Data.ItemNames[7914] = "Barbaric Iron Breastplate"
ES.Data.ItemNames[7915] = "Barbaric Iron Helm"
ES.Data.ItemNames[7916] = "Barbaric Iron Boots"
ES.Data.ItemNames[7917] = "Barbaric Iron Gloves"
ES.Data.ItemNames[7918] = "Heavy Mithril Shoulder"
ES.Data.ItemNames[7919] = "Heavy Mithril Gauntlet"
ES.Data.ItemNames[7920] = "Mithril Plate Pants"
ES.Data.ItemNames[7921] = "Heavy Mithril Pants"
ES.Data.ItemNames[7922] = "Steel Plate Helm"
ES.Data.ItemNames[7924] = "Mithril Plate Bracers"
ES.Data.ItemNames[7925] = "Mithril Plate Gloves"
ES.Data.ItemNames[7926] = "Ornate Mithril Pants"
ES.Data.ItemNames[7927] = "Ornate Mithril Gloves"
ES.Data.ItemNames[7928] = "Ornate Mithril Shoulders"
ES.Data.ItemNames[7929] = "Orcish War Leggings"
ES.Data.ItemNames[7930] = "Heavy Mithril Breastplate"
ES.Data.ItemNames[7931] = "Mithril Coif"
ES.Data.ItemNames[7932] = "Mithril Plate Shoulders"
ES.Data.ItemNames[7933] = "Heavy Mithril Boots"
ES.Data.ItemNames[7934] = "Heavy Mithril Helm"
ES.Data.ItemNames[7935] = "Ornate Mithril Breastplate"
ES.Data.ItemNames[7936] = "Ornate Mithril Boots"
ES.Data.ItemNames[7937] = "Ornate Mithril Helm"
ES.Data.ItemNames[7938] = "Truesilver Gauntlets"
ES.Data.ItemNames[7939] = "Truesilver Breastplate"
ES.Data.ItemNames[7941] = "Heavy Mithril Axe"
ES.Data.ItemNames[7942] = "Blue Glittering Axe"
ES.Data.ItemNames[7943] = "Wicked Mithril Blade"
ES.Data.ItemNames[7944] = "Dazzling Mithril Rapier"
ES.Data.ItemNames[7945] = "Big Black Mace"
ES.Data.ItemNames[7946] = "Runed Mithril Hammer"
ES.Data.ItemNames[7947] = "Ebon Shiv"
ES.Data.ItemNames[7954] = "The Shatterer"
ES.Data.ItemNames[7955] = "Copper Claymore"
ES.Data.ItemNames[7956] = "Bronze Warhammer"
ES.Data.ItemNames[7957] = "Bronze Greatsword"
ES.Data.ItemNames[7958] = "Bronze Battle Axe"
ES.Data.ItemNames[7959] = "Blight"
ES.Data.ItemNames[7960] = "Truesilver Champion"
ES.Data.ItemNames[7961] = "Phantom Blade"
ES.Data.ItemNames[7963] = "Steel Breastplate"
ES.Data.ItemNames[7964] = "Solid Sharpening Stone"
ES.Data.ItemNames[7965] = "Solid Weightstone"
ES.Data.ItemNames[7966] = "Solid Grinding Stone"
ES.Data.ItemNames[7967] = "Mithril Shield Spike"
ES.Data.ItemNames[7969] = "Mithril Spurs"
ES.Data.ItemNames[7971] = "Black Pearl"
ES.Data.ItemNames[7972] = "Ichor of Undeath"
ES.Data.ItemNames[8146] = "Wicked Claw"
ES.Data.ItemNames[8153] = "Wildvine"
ES.Data.ItemNames[8168] = "Jet Black Feather"
ES.Data.ItemNames[8170] = "Rugged Leather"
ES.Data.ItemNames[8831] = "Purple Lotus"
ES.Data.ItemNames[9060] = "Inlaid Mithril Cylinder"
ES.Data.ItemNames[9366] = "Golden Scale Gauntlets"
ES.Data.ItemNames[10421] = "Rough Copper Vest"
ES.Data.ItemNames[10423] = "Silvered Bronze Leggings"
ES.Data.ItemNames[10938] = "Lesser Magic Essence"
ES.Data.ItemNames[10940] = "Strange Dust"
ES.Data.ItemNames[11128] = "Golden Rod"
ES.Data.ItemNames[11139] = "Large Glowing Shard"
ES.Data.ItemNames[11144] = "Truesilver Rod"
ES.Data.ItemNames[11184] = "Blue Power Crystal"
ES.Data.ItemNames[11185] = "Green Power Crystal"
ES.Data.ItemNames[11186] = "Red Power Crystal"
ES.Data.ItemNames[11188] = "Yellow Power Crystal"
ES.Data.ItemNames[11371] = "Dark Iron Bar"
ES.Data.ItemNames[11382] = "Blood of the Mountain"
ES.Data.ItemNames[11604] = "Dark Iron Plate"
ES.Data.ItemNames[11605] = "Dark Iron Shoulders"
ES.Data.ItemNames[11606] = "Dark Iron Mail"
ES.Data.ItemNames[11607] = "Dark Iron Sunderer"
ES.Data.ItemNames[11608] = "Dark Iron Pulverizer"
ES.Data.ItemNames[11754] = "Black Diamond"
ES.Data.ItemNames[12259] = "Glinting Steel Dagger"
ES.Data.ItemNames[12260] = "Searing Golden Blade"
ES.Data.ItemNames[12359] = "Thorium Bar"
ES.Data.ItemNames[12360] = "Arcanite Bar"
ES.Data.ItemNames[12361] = "Blue Sapphire"
ES.Data.ItemNames[12364] = "Huge Emerald"
ES.Data.ItemNames[12365] = "Dense Stone"
ES.Data.ItemNames[12404] = "Dense Sharpening Stone"
ES.Data.ItemNames[12405] = "Thorium Armor"
ES.Data.ItemNames[12406] = "Thorium Belt"
ES.Data.ItemNames[12408] = "Thorium Bracers"
ES.Data.ItemNames[12409] = "Thorium Boots"
ES.Data.ItemNames[12410] = "Thorium Helm"
ES.Data.ItemNames[12414] = "Thorium Leggings"
ES.Data.ItemNames[12415] = "Radiant Breastplate"
ES.Data.ItemNames[12416] = "Radiant Belt"
ES.Data.ItemNames[12417] = "Radiant Circlet"
ES.Data.ItemNames[12418] = "Radiant Gloves"
ES.Data.ItemNames[12419] = "Radiant Boots"
ES.Data.ItemNames[12420] = "Radiant Leggings"
ES.Data.ItemNames[12422] = "Imperial Plate Chest"
ES.Data.ItemNames[12424] = "Imperial Plate Belt"
ES.Data.ItemNames[12425] = "Imperial Plate Bracers"
ES.Data.ItemNames[12426] = "Imperial Plate Boots"
ES.Data.ItemNames[12427] = "Imperial Plate Helm"
ES.Data.ItemNames[12428] = "Imperial Plate Shoulders"
ES.Data.ItemNames[12429] = "Imperial Plate Leggings"
ES.Data.ItemNames[12610] = "Runic Plate Shoulders"
ES.Data.ItemNames[12611] = "Runic Plate Boots"
ES.Data.ItemNames[12612] = "Runic Plate Helm"
ES.Data.ItemNames[12613] = "Runic Breastplate"
ES.Data.ItemNames[12614] = "Runic Plate Leggings"
ES.Data.ItemNames[12618] = "Enchanted Thorium Breastplate"
ES.Data.ItemNames[12619] = "Enchanted Thorium Leggings"
ES.Data.ItemNames[12620] = "Enchanted Thorium Helm"
ES.Data.ItemNames[12625] = "Dawnbringer Shoulders"
ES.Data.ItemNames[12631] = "Fiery Plate Gauntlets"
ES.Data.ItemNames[12633] = "Whitesoul Helm"
ES.Data.ItemNames[12639] = "Stronghold Gauntlets"
ES.Data.ItemNames[12640] = "Lionheart Helm"
ES.Data.ItemNames[12643] = "Dense Weightstone"
ES.Data.ItemNames[12644] = "Dense Grinding Stone"
ES.Data.ItemNames[12645] = "Thorium Shield Spike"
ES.Data.ItemNames[12655] = "Enchanted Thorium Bar"
ES.Data.ItemNames[12662] = "Demonic Rune"
ES.Data.ItemNames[12753] = "Skin of Shadow"
ES.Data.ItemNames[12764] = "Thorium Greatsword"
ES.Data.ItemNames[12769] = "Bleakwood Hew"
ES.Data.ItemNames[12772] = "Inlaid Thorium Hammer"
ES.Data.ItemNames[12773] = "Ornate Thorium Handaxe"
ES.Data.ItemNames[12774] = "Dawn's Edge"
ES.Data.ItemNames[12775] = "Huge Thorium Battleaxe"
ES.Data.ItemNames[12776] = "Enchanted Battlehammer"
ES.Data.ItemNames[12777] = "Blazing Rapier"
ES.Data.ItemNames[12781] = "Serenity"
ES.Data.ItemNames[12782] = "Corruption"
ES.Data.ItemNames[12783] = "Heartseeker"
ES.Data.ItemNames[12784] = "Arcanite Reaper"
ES.Data.ItemNames[12790] = "Arcanite Champion"
ES.Data.ItemNames[12792] = "Volcanic Hammer"
ES.Data.ItemNames[12794] = "Masterwork Stormhammer"
ES.Data.ItemNames[12795] = "Blood Talon"
ES.Data.ItemNames[12796] = "Hammer of the Titans"
ES.Data.ItemNames[12797] = "Frostguard"
ES.Data.ItemNames[12798] = "Annihilator"
ES.Data.ItemNames[12799] = "Large Opal"
ES.Data.ItemNames[12800] = "Azerothian Diamond"
ES.Data.ItemNames[12802] = "Darkspear"
ES.Data.ItemNames[12803] = "Living Essence"
ES.Data.ItemNames[12804] = "Powerful Mojo"
ES.Data.ItemNames[12808] = "Essence of Undeath"
ES.Data.ItemNames[12809] = "Guardian Stone"
ES.Data.ItemNames[12810] = "Enchanted Leather"
ES.Data.ItemNames[12811] = "Righteous Orb"
ES.Data.ItemNames[12938] = "Blood of Heroes"
ES.Data.ItemNames[13510] = "Flask of the Titans"
ES.Data.ItemNames[13511] = "Flask of Distilled Wisdom"
ES.Data.ItemNames[13512] = "Flask of Supreme Power"
ES.Data.ItemNames[13926] = "Golden Pearl"
ES.Data.ItemNames[15417] = "Devilsaur Leather"
ES.Data.ItemNames[15869] = "Silver Skeleton Key"
ES.Data.ItemNames[15870] = "Golden Skeleton Key"
ES.Data.ItemNames[15871] = "Truesilver Skeleton Key"
ES.Data.ItemNames[15872] = "Arcanite Skeleton Key"
ES.Data.ItemNames[16206] = "Arcanite Rod"
ES.Data.ItemNames[16988] = "Fiery Chain Shoulders"
ES.Data.ItemNames[16989] = "Fiery Chain Girdle"
ES.Data.ItemNames[17010] = "Fiery Core"
ES.Data.ItemNames[17011] = "Lava Core"
ES.Data.ItemNames[17012] = "Core Leather"
ES.Data.ItemNames[17013] = "Dark Iron Leggings"
ES.Data.ItemNames[17014] = "Dark Iron Bracers"
ES.Data.ItemNames[17015] = "Dark Iron Reaver"
ES.Data.ItemNames[17016] = "Dark Iron Destroyer"
ES.Data.ItemNames[17193] = "Sulfuron Hammer"
ES.Data.ItemNames[17203] = "Sulfuron Ingot"
ES.Data.ItemNames[17704] = "Edge of Winter"
ES.Data.ItemNames[18262] = "Elemental Sharpening Stone"
ES.Data.ItemNames[18567] = "Elemental Flux"
ES.Data.ItemNames[19051] = "Girdle of the Dawn"
ES.Data.ItemNames[19057] = "Gloves of the Dawn"
ES.Data.ItemNames[19148] = "Dark Iron Helm"
ES.Data.ItemNames[19164] = "Dark Iron Gauntlets"
ES.Data.ItemNames[19166] = "Black Amnesty"
ES.Data.ItemNames[19167] = "Blackfury"
ES.Data.ItemNames[19168] = "Blackguard"
ES.Data.ItemNames[19169] = "Nightfall"
ES.Data.ItemNames[19170] = "Ebon Hand"
ES.Data.ItemNames[19690] = "Bloodsoul Breastplate"
ES.Data.ItemNames[19691] = "Bloodsoul Shoulders"
ES.Data.ItemNames[19692] = "Bloodsoul Gauntlets"
ES.Data.ItemNames[19693] = "Darksoul Breastplate"
ES.Data.ItemNames[19694] = "Darksoul Leggings"
ES.Data.ItemNames[19695] = "Darksoul Shoulders"
ES.Data.ItemNames[19726] = "Bloodvine"
ES.Data.ItemNames[19774] = "Souldarite"
ES.Data.ItemNames[20039] = "Dark Iron Boots"
ES.Data.ItemNames[20381] = "Dreamscale"
ES.Data.ItemNames[20520] = "Dark Rune"
ES.Data.ItemNames[20549] = "Darkrune Gauntlets"
ES.Data.ItemNames[20550] = "Darkrune Breastplate"
ES.Data.ItemNames[20551] = "Darkrune Helm"
ES.Data.ItemNames[20725] = "Nexus Crystal"
ES.Data.ItemNames[22191] = "Obsidian Mail Tunic"
ES.Data.ItemNames[22194] = "Black Grasp of the Destroyer"
ES.Data.ItemNames[22195] = "Light Obsidian Belt"
ES.Data.ItemNames[22196] = "Thick Obsidian Breastplate"
ES.Data.ItemNames[22197] = "Heavy Obsidian Belt"
ES.Data.ItemNames[22198] = "Jagged Obsidian Shield"
ES.Data.ItemNames[22202] = "Small Obsidian Shard"
ES.Data.ItemNames[22203] = "Large Obsidian Shard"
ES.Data.ItemNames[22383] = "Sageblade"
ES.Data.ItemNames[22384] = "Persuader"
ES.Data.ItemNames[22385] = "Titanic Leggings"
ES.Data.ItemNames[22669] = "Icebane Breastplate"
ES.Data.ItemNames[22670] = "Icebane Gauntlets"
ES.Data.ItemNames[22671] = "Icebane Bracers"
ES.Data.ItemNames[22682] = "Frozen Rune"
ES.Data.ItemNames[211845] = "Blackfathom Sharpening Stone"
ES.Data.ItemNames[213369] = "Faintly Glowing Leather"
ES.Data.ItemNames[213373] = "Reflective Scrapmetal"
ES.Data.ItemNames[213376] = "Low-Background Truesilver Plates"
ES.Data.ItemNames[213379] = "Hyperconductive Arcano-Filament"
ES.Data.ItemNames[213383] = "Polished Truesilver Gears"
ES.Data.ItemNames[248820] = "Torbernite"
ES.Data.ItemNames[248822] = "Death Lotus"
ES.Data.ItemNames[249410] = "Sulfuric Acid"
ES.Data.ItemNames[249427] = "Pristine Leather"
ES.Data.ItemNames[249432] = "Sandpaper"
ES.Data.ItemNames[249726] = "Azerothium Bar"
ES.Data.ItemNames[250483] = "Sterling Silver Boots"
ES.Data.ItemNames[250484] = "Sterling Silver Leggings"
ES.Data.ItemNames[250485] = "Sterling Silver Gauntlet"
ES.Data.ItemNames[250486] = "Sterling Silver Shoulders"
ES.Data.ItemNames[250487] = "Sterling Silver Breastplate"
ES.Data.ItemNames[250503] = "Veteran's Boots"
ES.Data.ItemNames[250504] = "Guard's Boots"
ES.Data.ItemNames[250505] = "Protector's Boots"
ES.Data.ItemNames[250506] = "Acolyte's Boots"
ES.Data.ItemNames[250507] = "Crusader's Boots"
ES.Data.ItemNames[250508] = "Veteran's Gloves"
ES.Data.ItemNames[250509] = "Guard's Gloves"
ES.Data.ItemNames[250510] = "Protector's Gloves"
ES.Data.ItemNames[250511] = "Acolyte's Gloves"
ES.Data.ItemNames[250512] = "Crusader's Gloves"
ES.Data.ItemNames[250513] = "Veteran's Chain Belt"
ES.Data.ItemNames[250514] = "Guard's Chain Belt"
ES.Data.ItemNames[250515] = "Protector's Chain Belt"
ES.Data.ItemNames[250516] = "Acolyte's Chain Belt"
ES.Data.ItemNames[250517] = "Crusader's Chain Belt"
ES.Data.ItemNames[250518] = "Veteran's Silvered Chain Shirt"
ES.Data.ItemNames[250519] = "Guard's Silvered Chain Shirt"
ES.Data.ItemNames[250520] = "Protector's Silvered Chain Shirt"
ES.Data.ItemNames[250521] = "Acolyte's Silvered Chain Shirt"
ES.Data.ItemNames[250522] = "Crusader's Silvered Chain Shirt"
ES.Data.ItemNames[250523] = "Veteran's Silvered Chain Leggings"
ES.Data.ItemNames[250524] = "Guard's Silvered Chain Leggings"
ES.Data.ItemNames[250525] = "Protector's Silvered Chain Leggings"
ES.Data.ItemNames[250526] = "Acolyte's Silvered Chain Leggings"
ES.Data.ItemNames[250527] = "Crusader's Silvered Chain Leggings"
ES.Data.ItemNames[250528] = "Veteran's Silvered Chain Helm"
ES.Data.ItemNames[250529] = "Guard's Silvered Chain Helm"
ES.Data.ItemNames[250530] = "Protector's Silvered Chain Helm"
ES.Data.ItemNames[250531] = "Acolyte's Silvered Chain Helm"
ES.Data.ItemNames[250532] = "Crusader's Silvered Chain Helm"
ES.Data.ItemNames[250533] = "Hard Gold Cuirass"
ES.Data.ItemNames[250534] = "Hard Gold Boots"
ES.Data.ItemNames[250535] = "Hard Gold Bracers"
ES.Data.ItemNames[250536] = "Hard Gold Leggings"
ES.Data.ItemNames[250537] = "Hard Gold Coif"
ES.Data.ItemNames[250538] = "Hard Gold Gauntlet"
ES.Data.ItemNames[250539] = "Hard Gold Pauldrons"
ES.Data.ItemNames[250540] = "Shining Mithril Breastplate"
ES.Data.ItemNames[250541] = "Shining Mithril Pauldrons"
ES.Data.ItemNames[250542] = "Shining Mithril Boots"
ES.Data.ItemNames[250543] = "Shining Mithril Helm"
ES.Data.ItemNames[250544] = "Shining Mithril Pants"
ES.Data.ItemNames[250545] = "Shining Mithril Gauntlet"
ES.Data.ItemNames[250561] = "Officer's Sabatons"
ES.Data.ItemNames[250562] = "Sentinel's Sabatons"
ES.Data.ItemNames[250563] = "Warder's Sabatons"
ES.Data.ItemNames[250564] = "Prefect's Sabatons"
ES.Data.ItemNames[250565] = "Justicar's Sabatons"
ES.Data.ItemNames[250566] = "Officer's Gauntlet"
ES.Data.ItemNames[250567] = "Sentinel's Gauntlet"
ES.Data.ItemNames[250568] = "Warder's Gauntlet"
ES.Data.ItemNames[250569] = "Prefect's Gauntlet"
ES.Data.ItemNames[250570] = "Justicar's Gauntlet"
ES.Data.ItemNames[250571] = "Officer's Waistguard"
ES.Data.ItemNames[250572] = "Sentinel's Waistguard"
ES.Data.ItemNames[250573] = "Warder's Waistguard"
ES.Data.ItemNames[250574] = "Prefect's Waistguard"
ES.Data.ItemNames[250575] = "Justicar's Waistguard"
ES.Data.ItemNames[250576] = "Officer's Pauldrons"
ES.Data.ItemNames[250577] = "Sentinel's Pauldrons"
ES.Data.ItemNames[250578] = "Warder's Pauldrons"
ES.Data.ItemNames[250579] = "Prefect's Pauldrons"
ES.Data.ItemNames[250580] = "Justicar's Pauldrons"
ES.Data.ItemNames[250581] = "Officer's Wristguards"
ES.Data.ItemNames[250582] = "Sentinel's Wristguards"
ES.Data.ItemNames[250583] = "Warder's Wristguards"
ES.Data.ItemNames[250584] = "Prefect's Wristguards"
ES.Data.ItemNames[250585] = "Justicar's Wristguards"
ES.Data.ItemNames[250586] = "Blessed Plate Pauldrons"
ES.Data.ItemNames[250587] = "Blessed Plate Boots"
ES.Data.ItemNames[250588] = "Blessed Plate Gauntlet"
ES.Data.ItemNames[250589] = "Imperial Plate Gauntlets"
ES.Data.ItemNames[250590] = "Blessed Plate Bracers"
ES.Data.ItemNames[250591] = "Blessed Plate Leggings"
ES.Data.ItemNames[250592] = "Blessed Plate Belt"
ES.Data.ItemNames[250593] = "Blessed Plate Helm"
ES.Data.ItemNames[250594] = "Blessed Plate Chest"
ES.Data.ItemNames[250595] = "Enriched Thorium Breastplate"
ES.Data.ItemNames[250596] = "Enriched Thorium Leggings"
ES.Data.ItemNames[250597] = "Enriched Thorium Helm"
ES.Data.ItemNames[250598] = "Champion's Legplates"
ES.Data.ItemNames[250599] = "Stalwart Helm"
ES.Data.ItemNames[250600] = "Martyr's Legplates"
ES.Data.ItemNames[250601] = "Breastplate of Salvation"
ES.Data.ItemNames[250602] = "Brass Knuckles"
ES.Data.ItemNames[250603] = "Bronze Dory"
ES.Data.ItemNames[250604] = "Iron Fists"
ES.Data.ItemNames[250605] = "Steel Spear"
ES.Data.ItemNames[250606] = "Iron Morningstar"
ES.Data.ItemNames[250607] = "Mithril Shortsword"
ES.Data.ItemNames[250608] = "Mithril Warhammer"
ES.Data.ItemNames[250609] = "Mithril Claws"
ES.Data.ItemNames[250610] = "Mithril Claymore"
ES.Data.ItemNames[250611] = "Mithril Stiletto"
ES.Data.ItemNames[250612] = "Charged Mithril Battleaxe"
ES.Data.ItemNames[250613] = "Thorium Greatmace"
ES.Data.ItemNames[250614] = "Thorium Cestus"
ES.Data.ItemNames[250615] = "Thorium Poleaxe"
ES.Data.ItemNames[250616] = "Bold Dirk"
ES.Data.ItemNames[250617] = "Stormcarver"
ES.Data.ItemNames[250618] = "Bagh Nakh"
ES.Data.ItemNames[250619] = "Legionite Glaive"
ES.Data.ItemNames[251290] = "Legionite Bar"
ES.Data.ItemNames[251291] = "Heavy Thorium Bar"
ES.Data.ItemNames[274030] = "Malleable Essence of Nature"
ES.Data.ItemNames[275622] = "Goregasher Grips"
ES.Data.ItemNames[275623] = "Goregasher Support"
ES.Data.ItemNames[275624] = "Goregasher Stompers"
ES.Data.ItemNames[275625] = "Clutchlord's Grips"
ES.Data.ItemNames[275626] = "Clutchlord's Support"
ES.Data.ItemNames[275627] = "Clutchlord's Stompers"
ES.Data.ItemNames[276992] = "Cloudy Skyforged Chainmail"
ES.Data.ItemNames[276993] = "Cloudy Skyforged Wristguards"
ES.Data.ItemNames[276994] = "Cloudy Skyforged Gauntlets"
ES.Data.ItemNames[276995] = "Cloudy Skyforged Chain"
ES.Data.ItemNames[276996] = "Cloudy Skyforged Legguards"
ES.Data.ItemNames[276997] = "Cloudy Skyforged Greaves"
ES.Data.ItemNames[277016] = "Azure Skyforged Chainmail"
ES.Data.ItemNames[277017] = "Azure Skyforged Wristguards"
ES.Data.ItemNames[277018] = "Azure Skyforged Gauntlets"
ES.Data.ItemNames[277019] = "Azure Skyforged Chain"
ES.Data.ItemNames[277020] = "Azure Skyforged Legguards"
ES.Data.ItemNames[277021] = "Azure Skyforged Greaves"
ES.Data.ItemNames[277040] = "Cloudy Skyforged Helm"
ES.Data.ItemNames[277041] = "Cloudy Skyforged Pauldrons"
ES.Data.ItemNames[277048] = "Azure Skyforged Helm"
ES.Data.ItemNames[277049] = "Azure Skyforged Pauldrons"
ES.Data.ItemNames[277672] = "Rough Copper Chain Boots"
ES.Data.ItemNames[279259] = "Ironwood Blade"
ES.Data.ItemNames[279260] = "Forest Defender's Axe"
ES.Data.ItemNames[279261] = "Greenhammer"
ES.Data.ItemNames[279262] = "Evergreen Shield"
ES.Data.ItemNames[279263] = "Depleted Thorium Sabatons"
ES.Data.ItemNames[279264] = "Heavy Thorium Gauntlets"
ES.Data.ItemNames[279265] = "Azerothium Legplates"
ES.Data.ItemNames[279944] = "Sharpening Wheel"
ES.Data.ItemNames[279988] = "Anvil"
ES.Data.ItemNames[285279] = "Cracked Blacksmith Hammer"
ES.Data.ItemNames[285280] = "Mithril Blacksmith Hammer"
ES.Data.ItemNames[285281] = "Arcanite Blacksmith Hammer"

-- Material -> profesión de recolección que lo consigue (393 Desuello, 182 Herboristería, 186 Minería).
-- Sin uso por ahora: reservado para la vía "Vender en bruto" de Ganar dinero (docs/PLAN.md, G1).
ES.Data.GatheredBy = ES.Data.GatheredBy or {}
ES.Data.GatheredBy[2318] = 393
ES.Data.GatheredBy[2319] = 393
ES.Data.GatheredBy[2835] = 186
ES.Data.GatheredBy[2836] = 186
ES.Data.GatheredBy[2838] = 186
ES.Data.GatheredBy[2840] = 186
ES.Data.GatheredBy[2841] = 186
ES.Data.GatheredBy[2842] = 186
ES.Data.GatheredBy[3575] = 186
ES.Data.GatheredBy[3859] = 186
ES.Data.GatheredBy[3860] = 186
ES.Data.GatheredBy[4234] = 393
ES.Data.GatheredBy[4304] = 393
ES.Data.GatheredBy[7912] = 186
ES.Data.GatheredBy[8153] = 182
ES.Data.GatheredBy[8168] = 393
ES.Data.GatheredBy[8170] = 393
ES.Data.GatheredBy[8831] = 182
ES.Data.GatheredBy[11371] = 186
ES.Data.GatheredBy[12359] = 186
ES.Data.GatheredBy[12365] = 186
ES.Data.GatheredBy[12809] = 186
ES.Data.GatheredBy[15417] = 393
ES.Data.GatheredBy[17012] = 393
ES.Data.GatheredBy[17203] = 186
ES.Data.GatheredBy[19726] = 182
ES.Data.GatheredBy[20381] = 393
ES.Data.GatheredBy[22202] = 186
ES.Data.GatheredBy[22203] = 186
ES.Data.GatheredBy[213373] = 186
ES.Data.GatheredBy[248822] = 182
ES.Data.GatheredBy[249427] = 393
ES.Data.GatheredBy[249726] = 186
ES.Data.GatheredBy[251291] = 186

```

---

## Cooking

```lua
-- Generado por tools/gen_profession.py (Cooking). No editar a mano.
-- Datos: cliente de WoW Forever (wago.tools DB2), instructores de CMaNGOS classic-db, vendedores de QuestieDB.
local _, ES = ...
ES.Data = ES.Data or {}

-- t = { naranja, amarilla, verde, gris }; fee/train = precio y habilidad del instructor
-- (sin fee = se aprende de pergamino: de dónde sale, en Data/Sources.lua; scrollPrice = su precio si lo vende un PNJ)
-- rep = { facción, nivel } que pide el pergamino para aprenderla (5 amistoso, 6 honorable, 7 venerado, 8 exaltado)
-- r = { {itemID, cantidad} }; out = { itemID, cantidad }
-- sq / oq = calidad del pergamino / de lo fabricado (0 pobre, 1 común, 2 poco común, 3 raro, 4 épico)
-- faction = bando que puede aprenderla, si solo es de uno
-- bop = lo fabricado se liga al recogerlo: no se puede vender en la AH (sí al vendedor)
-- favor / favorRep = se compra con Merchant's Favor en el campamento de tu bando, y la reputación que pide
-- train ajustado a Forever: nivel de Classic menos lo que Forever bajó la amarilla de esa receta
-- basic = se aprende sola al coger la profesión; trainer = de instructor sin precio conocido
--   (receta nueva de Forever que no está en CMaNGOS: se aprende al ponerse amarilla)
ES.Data.Cooking = {
  skillLine = 185,
  ranks = { -- { tope, precio, habilidad requerida, nivel de personaje }
    { 150, 500, 50, 10 },
    { 225, 10000, 125, 35 },
    { 300, 0, 225, 35 },
  },
  -- { PNJ instructor, rangos que enseña: 1 aprendiz (75), 2 oficial (150), 4 experto (225), 8 artesano (300) }
  trainers = { { 1355, 3 }, { 1382, 3 }, { 1430, 3 }, { 1699, 3 }, { 3026, 3 }, { 3067, 3 }, { 3087, 3 }, { 3399, 3 }, { 4210, 3 }, { 4552, 3 }, { 5159, 3 }, { 5482, 3 }, { 6286, 3 }, { 8306, 3 }, { 251905, 3 }, { 252084, 3 }, { 256655, 3 }, { 257006, 3 }, { 265944, 3 } },
  recipes = {
    [2538] = { name = "Charred Wolf Meat", t = { 1, 45, 65, 85 }, basic = true, r = { { 2672, 1 } }, out = { 2679, 1 }, oq = 1 },
    [2539] = { name = "Spiced Wolf Meat", t = { 1, 50, 70, 90 }, fee = 50, train = 10, r = { { 2672, 1 }, { 2678, 1 } }, out = { 2680, 1 }, oq = 1 },
    [2540] = { name = "Roasted Boar Meat", t = { 1, 45, 65, 85 }, basic = true, r = { { 769, 1 } }, out = { 2681, 1 }, oq = 1 },
    [2541] = { name = "Coyote Steak", t = { 1, 90, 110, 130 }, fee = 100, train = 50, r = { { 2673, 1 } }, out = { 2684, 1 }, oq = 1 },
    [2542] = { name = "Goretusk Liver Pie", t = { 1, 90, 110, 130 }, scroll = 2697, train = 50, scrollPrice = 400, sq = 1, r = { { 723, 1 }, { 2678, 1 } }, out = { 724, 1 }, oq = 1 },
    [2543] = { name = "Westfall Stew", t = { 1, 115, 135, 155 }, scroll = 728, train = 75, scrollPrice = 200, sq = 1, r = { { 729, 1 }, { 730, 1 }, { 731, 1 } }, out = { 733, 1 }, oq = 1 },
    [2544] = { name = "Crab Cake", t = { 1, 115, 135, 155 }, fee = 200, train = 75, r = { { 2674, 1 }, { 2678, 1 } }, out = { 2683, 1 }, oq = 1 },
    [2545] = { name = "Cooked Crab Claw", t = { 1, 125, 145, 165 }, scroll = 2698, train = 85, scrollPrice = 400, sq = 1, r = { { 2675, 1 }, { 2678, 1 } }, out = { 2682, 1 }, oq = 1 },
    [2546] = { name = "Dry Pork Ribs", t = { 1, 120, 140, 160 }, fee = 150, train = 80, r = { { 2677, 1 }, { 2678, 1 } }, out = { 2687, 1 }, oq = 1 },
    [2547] = { name = "Redridge Goulash", t = { 1, 135, 155, 175 }, scroll = 2699, train = 100, scrollPrice = 800, sq = 1, r = { { 1081, 1 }, { 1080, 1 } }, out = { 1082, 1 }, oq = 1 },
    [2548] = { name = "Succulent Pork Ribs", t = { 1, 130, 150, 170 }, scroll = 2700, train = 110, scrollPrice = 400, sq = 1, r = { { 2677, 2 }, { 2692, 1 } }, out = { 2685, 1 }, oq = 1 },
    [2549] = { name = "Seasoned Wolf Kabob", t = { 1, 140, 160, 180 }, scroll = 2701, train = 100, scrollPrice = 1600, sq = 1, r = { { 1015, 2 }, { 2678, 1 } }, out = { 1017, 3 }, oq = 1 },
    [2795] = { name = "Beer Basted Boar Ribs", t = { 1, 60, 80, 100 }, scroll = 2889, train = 25, scrollPrice = 240, sq = 1, r = { { 2886, 1 }, { 2894, 1 } }, out = { 2888, 1 }, oq = 1 },
    [3370] = { name = "Crocolisk Steak", t = { 1, 120, 140, 160 }, scroll = 3678, train = 80, scrollPrice = 400, sq = 1, r = { { 2924, 1 }, { 2678, 1 } }, out = { 3662, 1 }, oq = 1 },
    [3371] = { name = "Blood Sausage", t = { 1, 100, 120, 140 }, scroll = 3679, train = 60, scrollPrice = 400, sq = 1, r = { { 3173, 1 }, { 3172, 1 }, { 3174, 1 } }, out = { 3220, 2 }, oq = 1 },
    [3372] = { name = "Murloc Fin Soup", t = { 1, 130, 150, 170 }, scroll = 3680, train = 90, scrollPrice = 1600, sq = 1, r = { { 1468, 2 }, { 2692, 1 } }, out = { 3663, 1 }, oq = 1 },
    [3373] = { name = "Crocolisk Gumbo", t = { 1, 160, 180, 200 }, scroll = 3681, train = 120, scrollPrice = 1600, sq = 1, r = { { 3667, 1 }, { 2692, 1 } }, out = { 3664, 1 }, oq = 1 },
    [3376] = { name = "Curiously Tasty Omelet", t = { 1, 170, 190, 210 }, scroll = 3682, train = 130, scrollPrice = 1600, sq = 1, r = { { 3685, 1 }, { 2692, 1 } }, out = { 3665, 1 }, oq = 1 },
    [3377] = { name = "Gooey Spider Cake", t = { 1, 150, 170, 190 }, scroll = 3683, train = 110, scrollPrice = 1600, sq = 1, r = { { 2251, 2 }, { 2692, 1 } }, out = { 3666, 1 }, oq = 1 },
    [3397] = { name = "Big Bear Steak", t = { 1, 150, 170, 190 }, scroll = 3734, train = 110, scrollPrice = 1600, sq = 1, r = { { 3730, 1 }, { 2692, 1 } }, out = { 3726, 1 }, oq = 1 },
    [3398] = { name = "Hot Lion Chops", t = { 1, 175, 195, 215 }, scroll = 3735, train = 125, scrollPrice = 1800, sq = 1, r = { { 3731, 1 }, { 2692, 1 } }, out = { 3727, 1 }, oq = 1 },
    [3399] = { name = "Tasty Lion Steak", t = { 1, 190, 210, 230 }, scroll = 3736, train = 150, sq = 1, r = { { 3731, 2 }, { 3713, 1 } }, out = { 3728, 1 }, oq = 1 },
    [3400] = { name = "Soothing Turtle Bisque", t = { 1, 215, 235, 255 }, scroll = 3737, train = 175, sq = 1, r = { { 3712, 1 }, { 3713, 1 } }, out = { 3729, 1 }, oq = 1 },
    [4094] = { name = "Barbecued Buzzard Wing", t = { 1, 215, 235, 255 }, fee = 500, train = 175, tr = { 2818 }, r = { { 3404, 1 }, { 2692, 1 } }, out = { 4457, 1 }, oq = 1 },
    [6412] = { name = "Kaldorei Spider Kabob", t = { 1, 50, 70, 90 }, scroll = 5482, train = 10, sq = 1, r = { { 5465, 1 } }, out = { 5472, 1 }, oq = 1 },
    [6413] = { name = "Scorpid Surprise", t = { 1, 60, 80, 100 }, scroll = 5483, train = 20, scrollPrice = 140, sq = 1, r = { { 5466, 1 } }, out = { 5473, 1 }, oq = 1 },
    [6414] = { name = "Roasted Kodo Meat", t = { 1, 75, 95, 115 }, scroll = 5484, train = 35, scrollPrice = 240, sq = 1, r = { { 5467, 1 }, { 2678, 1 } }, out = { 5474, 2 }, oq = 1 },
    [6415] = { name = "Fillet of Frenzy", t = { 1, 90, 110, 130 }, scroll = 5485, train = 50, scrollPrice = 400, sq = 1, r = { { 5468, 1 }, { 2678, 1 } }, out = { 5476, 2 }, oq = 1 },
    [6416] = { name = "Strider Stew", t = { 1, 90, 110, 130 }, scroll = 5486, train = 50, scrollPrice = 440, sq = 1, r = { { 5469, 1 }, { 4536, 1 } }, out = { 5477, 2 }, oq = 1 },
    [6417] = { name = "Dig Rat Stew", t = { 1, 130, 150, 170 }, scroll = 5487, train = 90, sq = 1, r = { { 5051, 1 } }, out = { 5478, 2 }, oq = 1 },
    [6418] = { name = "Crispy Lizard Tail", t = { 1, 140, 160, 180 }, scroll = 5488, train = 100, scrollPrice = 400, sq = 1, r = { { 5470, 1 }, { 2692, 1 } }, out = { 5479, 2 }, oq = 1 },
    [6419] = { name = "Lean Venison", t = { 1, 150, 170, 190 }, scroll = 5489, train = 110, scrollPrice = 1200, sq = 1, r = { { 5471, 1 }, { 2678, 4 } }, out = { 5480, 2 }, oq = 1 },
    [6499] = { name = "Boiled Clams", t = { 1, 90, 110, 130 }, fee = 100, train = 50, r = { { 5503, 1 }, { 159, 1 } }, out = { 5525, 1 }, oq = 1 },
    [6500] = { name = "Goblin Deviled Clams", t = { 1, 165, 185, 205 }, fee = 300, train = 125, r = { { 5504, 1 }, { 2692, 1 } }, out = { 5527, 1 }, oq = 1 },
    [6501] = { name = "Clam Chowder", t = { 1, 130, 150, 170 }, scroll = 5528, train = 90, scrollPrice = 800, sq = 1, r = { { 5503, 1 }, { 1179, 1 }, { 2678, 1 } }, out = { 5526, 1 }, oq = 1 },
    [7213] = { name = "Giant Clam Scorcho", t = { 1, 215, 235, 255 }, scroll = 6039, train = 175, scrollPrice = 5000, sq = 1, r = { { 4655, 1 }, { 2692, 1 } }, out = { 6038, 1 }, oq = 1 },
    [7751] = { name = "Brilliant Smallfish", t = { 1, 45, 65, 85 }, scroll = 6325, train = 1, scrollPrice = 40, sq = 1, r = { { 6291, 1 } }, out = { 6290, 1 }, oq = 1 },
    [7752] = { name = "Slitherskin Mackerel", t = { 1, 45, 65, 85 }, scroll = 6326, train = 1, scrollPrice = 40, sq = 1, r = { { 6303, 1 } }, out = { 787, 1 }, oq = 1 },
    [7753] = { name = "Longjaw Mud Snapper", t = { 1, 90, 110, 130 }, scroll = 6328, train = 50, scrollPrice = 400, sq = 1, r = { { 6289, 1 } }, out = { 4592, 1 }, oq = 1 },
    [7754] = { name = "Loch Frenzy Delight", t = { 1, 90, 110, 130 }, scroll = 6329, train = 50, scrollPrice = 400, sq = 1, r = { { 6317, 1 }, { 2678, 1 } }, out = { 6316, 1 }, oq = 1 },
    [7755] = { name = "Bristle Whisker Catfish", t = { 1, 140, 160, 180 }, scroll = 6330, train = 100, scrollPrice = 1200, sq = 1, r = { { 6308, 1 } }, out = { 4593, 1 }, oq = 1 },
    [7827] = { name = "Rainbow Fin Albacore", t = { 1, 90, 110, 130 }, scroll = 6368, train = 50, scrollPrice = 400, sq = 1, r = { { 6361, 1 } }, out = { 5095, 1 }, oq = 1 },
    [7828] = { name = "Rockscale Cod", t = { 1, 190, 210, 230 }, scroll = 6369, train = 175, scrollPrice = 2200, sq = 1, r = { { 6362, 1 } }, out = { 4594, 1 }, oq = 1 },
    [8238] = { name = "Savory Deviate Delight", t = { 1, 125, 145, 165 }, scroll = 6661, train = 85, sq = 2, r = { { 6522, 1 }, { 2678, 1 } }, out = { 6657, 1 }, oq = 1 },
    [8604] = { name = "Herb Baked Egg", t = { 1, 45, 65, 85 }, basic = true, r = { { 6889, 1 }, { 2678, 1 } }, out = { 6888, 1 }, oq = 1 },
    [8607] = { name = "Smoked Bear Meat", t = { 1, 80, 100, 120 }, scroll = 6892, train = 40, scrollPrice = 250, sq = 1, r = { { 3173, 1 } }, out = { 6890, 1 }, oq = 1 },
    [9513] = { name = "Thistle Tea", t = { 1, 100, 120, 140 }, scroll = 18160, train = 60, scrollPrice = 200, sq = 2, r = { { 2452, 1 }, { 159, 1 } }, out = { 7676, 1 }, oq = 1 },
    [13028] = { name = "Goldthorn Tea", t = { 1, 215, 235, 255 }, gone = true, r = { { 3821, 1 }, { 159, 1 } }, out = { 10841, 4 }, oq = 1 },
    [15853] = { name = "Lean Wolf Steak", t = { 1, 165, 185, 205 }, scroll = 12227, train = 125, scrollPrice = 1600, sq = 1, r = { { 1015, 1 }, { 2678, 1 } }, out = { 12209, 1 }, oq = 1 },
    [15855] = { name = "Roast Raptor", t = { 1, 215, 235, 255 }, scroll = 12228, train = 175, scrollPrice = 5000, sq = 1, r = { { 12184, 1 }, { 2692, 1 } }, out = { 12210, 1 }, oq = 1 },
    [15856] = { name = "Hot Wolf Ribs", t = { 1, 215, 235, 255 }, scroll = 12229, train = 175, scrollPrice = 5000, sq = 1, r = { { 12203, 1 }, { 2692, 1 } }, out = { 13851, 1 }, oq = 1 },
    [15861] = { name = "Jungle Stew", t = { 1, 215, 235, 255 }, scroll = 12231, train = 175, scrollPrice = 3000, sq = 1, r = { { 12202, 1 }, { 159, 1 }, { 4536, 2 } }, out = { 12212, 2 }, oq = 1 },
    [15863] = { name = "Carrion Surprise", t = { 1, 215, 235, 255 }, scroll = 12232, train = 175, scrollPrice = 5000, sq = 1, r = { { 12037, 1 }, { 2692, 1 } }, out = { 12213, 1 }, oq = 1 },
    [15865] = { name = "Mystery Stew", t = { 1, 215, 235, 255 }, scroll = 12233, train = 175, scrollPrice = 3000, sq = 1, r = { { 12037, 1 }, { 2596, 1 } }, out = { 12214, 1 }, oq = 1 },
    [15906] = { name = "Dragonbreath Chili", t = { 1, 240, 260, 280 }, scroll = 12239, train = 200, scrollPrice = 7000, sq = 1, r = { { 12037, 1 }, { 4402, 1 }, { 2692, 1 } }, out = { 12217, 1 }, oq = 1 },
    [15910] = { name = "Heavy Kodo Stew", t = { 1, 240, 260, 280 }, scroll = 12240, train = 200, scrollPrice = 7000, sq = 1, r = { { 12204, 2 }, { 3713, 1 }, { 159, 1 } }, out = { 12215, 2 }, oq = 1 },
    [15915] = { name = "Spiced Chili Crab", t = { 1, 265, 285, 305 }, scroll = 16111, train = 225, scrollPrice = 12000, sq = 1, r = { { 12206, 1 }, { 2692, 2 } }, out = { 12216, 1 }, oq = 1 },
    [15933] = { name = "Monster Omelet", t = { 1, 265, 285, 305 }, scroll = 16110, train = 225, scrollPrice = 12000, sq = 1, r = { { 12207, 1 }, { 3713, 2 } }, out = { 12218, 1 }, oq = 1 },
    [15935] = { name = "Crispy Bat Wing", t = { 1, 45, 65, 85 }, scroll = 12226, train = 1, scrollPrice = 25, sq = 1, r = { { 12223, 1 }, { 2678, 1 } }, out = { 12224, 1 }, oq = 1 },
    [18238] = { name = "Spotted Yellowtail", t = { 1, 265, 285, 305 }, scroll = 13939, train = 225, scrollPrice = 16000, sq = 1, r = { { 4603, 1 } }, out = { 6887, 1 }, oq = 1 },
    [18239] = { name = "Cooked Glossy Mightfish", t = { 1, 265, 285, 305 }, scroll = 13940, train = 225, scrollPrice = 16000, sq = 1, r = { { 13754, 1 }, { 3713, 1 } }, out = { 13927, 1 }, oq = 1 },
    [18240] = { name = "Grilled Squid", t = { 1, 280, 300, 320 }, scroll = 13942, train = 240, scrollPrice = 16000, sq = 1, r = { { 13755, 1 }, { 3713, 1 } }, out = { 13928, 1 }, oq = 1 },
    [18241] = { name = "Filet of Redgill", t = { 1, 265, 285, 305 }, scroll = 13941, train = 225, scrollPrice = 16000, sq = 1, r = { { 13758, 1 } }, out = { 13930, 1 }, oq = 1 },
    [18242] = { name = "Hot Smoked Bass", t = { 1, 280, 300, 320 }, scroll = 13943, train = 240, scrollPrice = 16000, sq = 1, r = { { 13756, 1 }, { 2692, 2 } }, out = { 13929, 1 }, oq = 1 },
    [18243] = { name = "Nightfin Soup", t = { 1, 290, 310, 330 }, scroll = 13945, train = 250, scrollPrice = 20000, sq = 1, r = { { 13759, 1 }, { 159, 1 } }, out = { 13931, 1 }, oq = 1 },
    [18244] = { name = "Poached Sunscale Salmon", t = { 1, 290, 310, 330 }, scroll = 13946, train = 250, scrollPrice = 20000, sq = 1, r = { { 13760, 1 } }, out = { 13932, 1 }, oq = 1 },
    [18245] = { name = "Lobster Stew", t = { 1, 315, 335, 355 }, scroll = 13947, train = 275, scrollPrice = 20000, sq = 1, r = { { 13888, 1 }, { 159, 1 } }, out = { 13933, 1 }, oq = 1 },
    [18246] = { name = "Mightfish Steak", t = { 1, 315, 335, 355 }, scroll = 13948, train = 275, scrollPrice = 20000, sq = 1, r = { { 13893, 1 }, { 2692, 1 }, { 3713, 1 } }, out = { 13934, 1 }, oq = 1 },
    [18247] = { name = "Baked Salmon", t = { 1, 315, 335, 355 }, scroll = 13949, train = 275, scrollPrice = 20000, sq = 1, r = { { 13889, 1 }, { 3713, 1 } }, out = { 13935, 1 }, oq = 1 },
    [20626] = { name = "Undermine Clam Chowder", t = { 1, 265, 285, 305 }, scroll = 16767, train = 225, scrollPrice = 3000, sq = 1, r = { { 7974, 2 }, { 2692, 1 }, { 1179, 1 } }, out = { 16766, 2 }, oq = 1 },
    [20916] = { name = "Mithril Headed Trout", t = { 1, 215, 235, 255 }, scroll = 17062, train = 175, scrollPrice = 2200, sq = 1, r = { { 8365, 1 } }, out = { 8364, 1 }, oq = 1 },
    [21143] = { name = "Gingerbread Cookie", t = { 1, 45, 65, 85 }, scroll = 17200, train = 1, scrollPrice = 25, sq = 1, r = { { 6889, 1 }, { 17194, 1 } }, out = { 17197, 1 }, oq = 1 },
    [21144] = { name = "Egg Nog", t = { 1, 75, 95, 115 }, scroll = 17201, train = 35, scrollPrice = 240, sq = 1, r = { { 6889, 1 }, { 1179, 1 }, { 17196, 1 }, { 17194, 1 } }, out = { 17198, 1 }, oq = 1 },
    [21175] = { name = "Spider Sausage", t = { 1, 240, 260, 280 }, fee = 4000, train = 200, tr = { 1355, 1382, 1430, 1699, 3026, 3067, 3087, 3399, 4210, 4552, 5159, 5482, 6286, 8306, 251905, 252084, 256655, 257006, 265944 }, r = { { 12205, 2 } }, out = { 17222, 1 }, oq = 1 },
    [22480] = { name = "Tender Wolf Steak", t = { 1, 265, 285, 305 }, scroll = 18046, train = 225, scrollPrice = 12000, sq = 1, r = { { 12208, 1 }, { 3713, 1 } }, out = { 18045, 1 }, oq = 1 },
    [22761] = { name = "Runn Tum Tuber Surprise", t = { 1, 315, 335, 355 }, scroll = 18267, train = 275, sq = 2, r = { { 18255, 1 }, { 3713, 1 } }, out = { 18254, 1 }, oq = 1 },
    [24418] = { name = "Heavy Crocolisk Stew", t = { 1, 160, 180, 200 }, scroll = 20075, train = 150, scrollPrice = 2000, sq = 1, r = { { 3667, 2 }, { 3713, 1 } }, out = { 20074, 1 }, oq = 1 },
    [24801] = { name = "Smoked Desert Dumplings", t = { 1, 325, 345, 365 }, r = { { 20424, 1 }, { 3713, 1 } }, out = { 20452, 1 }, oq = 1 },
    [25659] = { name = "Dirge's Kickin' Chimaerok Chops", t = { 1, 325, 345, 365 }, scroll = 21025, train = 300, sq = 4, r = { { 2692, 1 }, { 9061, 1 }, { 8150, 1 }, { 21024, 1 } }, out = { 21023, 5 }, oq = 1 },
    [25704] = { name = "Smoked Sagefish", t = { 1, 120, 140, 160 }, scroll = 21099, train = 80, scrollPrice = 500, sq = 1, r = { { 21071, 1 }, { 2678, 1 } }, out = { 21072, 1 }, oq = 1 },
    [25954] = { name = "Sagefish Delight", t = { 1, 215, 235, 255 }, scroll = 21219, train = 175, scrollPrice = 5000, sq = 1, r = { { 21153, 1 }, { 2692, 1 } }, out = { 21217, 1 }, oq = 1 },
    [470370] = { name = "Smoked Redgill", t = { 1, 325, 345, 365 }, scroll = 232443, train = 300, gone = true, sq = 1, r = { { 13758, 1 } }, out = { 232438, 1 }, oq = 1 },
    [1225758] = { name = "Prowler Steak", t = { 1, 260, 270, 280 }, scroll = 238645, train = 250, sq = 1, r = { { 12202, 2 }, { 239016, 1 } }, out = { 238637, 2 }, oq = 1 },
    [1225759] = { name = "Filet o' Flank", t = { 1, 260, 270, 280 }, scroll = 238646, train = 250, sq = 1, r = { { 12203, 2 }, { 239016, 1 } }, out = { 238638, 2 }, oq = 1 },
    [1225760] = { name = "Sunrise Omelette", t = { 1, 260, 270, 280 }, scroll = 238647, train = 250, sq = 1, r = { { 12207, 2 }, { 239016, 1 } }, out = { 238639, 2 }, oq = 1 },
    [1225762] = { name = "Specklefin Feast", t = { 1, 290, 300, 310 }, scroll = 238649, train = 280, sq = 1, r = { { 4603, 12 }, { 12184, 4 }, { 6362, 3 }, { 239017, 1 } }, out = { 238641, 1 }, oq = 2 },
    [1225763] = { name = "Grand Lobster Banquet", t = { 1, 290, 300, 310 }, scroll = 239021, train = 280, sq = 1, r = { { 13888, 12 }, { 3712, 4 }, { 3404, 3 }, { 239017, 1 } }, out = { 238642, 1 }, oq = 2 },
    [1229737] = { name = "Basic Campfire", t = { 1, 1, 1, 1 }, basic = true, r = { { 4470, 1 } }, out = { 279981, 1 }, oq = 1 },
    [1247741] = { name = "Spinefin Halibut", t = { 1, 210, 215, 220 }, r = { { 8959, 1 } }, out = { 8957, 1 }, oq = 1 },
    [1249957] = { name = "Peace Tea", t = { 1, 30, 37, 45 }, scroll = 249879, train = 25, sq = 1, r = { { 159, 1 }, { 2447, 2 } }, out = { 249865, 1 }, oq = 1 },
    [1249958] = { name = "Royal Tea", t = { 1, 105, 115, 125 }, scroll = 249880, train = 100, sq = 1, r = { { 1179, 1 }, { 785, 2 } }, out = { 249866, 1 }, oq = 1 },
    [1249959] = { name = "Root Tea", t = { 1, 155, 170, 185 }, scroll = 249881, train = 125, sq = 1, r = { { 1205, 1 }, { 3357, 2 } }, out = { 249867, 1 }, oq = 1 },
    [1249960] = { name = "Triage Tea", t = { 1, 195, 215, 235 }, scroll = 249882, train = 180, sq = 1, r = { { 1708, 1 }, { 3818, 2 } }, out = { 249868, 1 }, oq = 1 },
    [1249961] = { name = "Sunny Tea", t = { 1, 220, 235, 250 }, scroll = 249883, train = 200, sq = 1, r = { { 1645, 1 }, { 8838, 2 } }, out = { 249869, 1 }, oq = 1 },
    [1249962] = { name = "Sage's Tea", t = { 1, 260, 275, 290 }, scroll = 249884, train = 250, sq = 1, r = { { 8766, 1 }, { 13465, 2 } }, out = { 249870, 1 }, oq = 1 },
    [1249963] = { name = "Venomous Smoothie", t = { 1, 30, 37, 45 }, scroll = 249885, train = 25, sq = 1, favor = 30, r = { { 159, 1 }, { 2678, 1 }, { 1475, 1 } }, out = { 249871, 1 }, oq = 1 },
    [1249964] = { name = "Slimy Smoothie", t = { 1, 105, 112, 120 }, scroll = 249886, train = 100, sq = 1, favor = 30, r = { { 1179, 1 }, { 2678, 2 }, { 3174, 1 } }, out = { 249872, 1 }, oq = 1 },
    [1249965] = { name = "Mrrggl Smrrthle", t = { 1, 135, 140, 145 }, scroll = 249887, train = 125, sq = 1, favor = 30, r = { { 1205, 1 }, { 2692, 2 }, { 1468, 1 } }, out = { 249873, 1 }, oq = 1 },
    [1249966] = { name = "Calcified Smoothie", t = { 1, 185, 190, 195 }, scroll = 249888, train = 180, sq = 1, favor = 60, favorRep = 5, r = { { 1708, 1 }, { 2692, 3 }, { 5637, 1 } }, out = { 249874, 1 }, oq = 1 },
    [1249967] = { name = "Spicy Smoothie", t = { 1, 215, 220, 225 }, scroll = 249889, train = 200, sq = 1, favor = 60, favorRep = 5, r = { { 1645, 1 }, { 3713, 3 }, { 4402, 1 } }, out = { 249875, 1 }, oq = 1 },
    [1249968] = { name = "Wicked Smoothie", t = { 1, 255, 262, 270 }, scroll = 249890, train = 250, sq = 1, favor = 90, favorRep = 6, r = { { 8766, 1 }, { 3713, 4 }, { 8146, 1 } }, out = { 249876, 1 }, oq = 1 },
    [1250142] = { name = "Savory Stag Sliders", t = { 1, 230, 237, 245 }, scroll = 250173, train = 225, sq = 1, r = { { 5471, 2 }, { 2692, 3 } }, out = { 250065, 1 }, oq = 1 },
    [1250143] = { name = "Soaring Pamplona", t = { 1, 280, 295, 310 }, scroll = 250174, train = 275, sq = 1, r = { { 3404, 3 }, { 3713, 3 } }, out = { 250066, 1 }, oq = 1 },
    [1250144] = { name = "Bat Hachee", t = { 1, 280, 295, 310 }, scroll = 250175, train = 275, sq = 1, r = { { 12223, 3 }, { 3713, 2 } }, out = { 250067, 1 }, oq = 1 },
    [1250145] = { name = "Savory Turtle Stew", t = { 1, 280, 295, 310 }, scroll = 250176, train = 275, sq = 1, r = { { 3712, 3 }, { 3713, 3 } }, out = { 250068, 1 }, oq = 1 },
    [1250146] = { name = "Flank au Poivre", t = { 1, 285, 300, 315 }, scroll = 250177, train = 275, sq = 1, r = { { 12203, 3 }, { 3713, 3 } }, out = { 250069, 1 }, oq = 1 },
    [1250147] = { name = "Bear Bruscitti", t = { 1, 280, 295, 310 }, scroll = 250178, train = 275, sq = 1, r = { { 3730, 3 }, { 3713, 3 } }, out = { 250070, 1 }, oq = 1 },
    [1250148] = { name = "Steaming Stag Steak", t = { 1, 280, 295, 310 }, scroll = 250179, train = 275, sq = 1, r = { { 5471, 3 }, { 3713, 4 } }, out = { 250071, 1 }, oq = 1 },
    [1250149] = { name = "Swiftstrike Steak", t = { 1, 280, 295, 310 }, scroll = 250180, train = 275, sq = 1, r = { { 12202, 3 }, { 3713, 2 } }, out = { 250072, 1 }, oq = 1 },
    [1250150] = { name = "Raging Raptor Ribs", t = { 1, 280, 295, 310 }, scroll = 250181, train = 180, sq = 1, r = { { 12184, 2 }, { 2692, 3 } }, out = { 250073, 1 }, oq = 1 },
    [1250151] = { name = "Bear Brisket", t = { 1, 200, 210, 220 }, scroll = 250182, train = 175, sq = 1, r = { { 3730, 2 }, { 2692, 3 } }, out = { 250074, 1 }, oq = 1 },
    [1250152] = { name = "Prehistoric Pulled Raptor", t = { 1, 280, 295, 310 }, scroll = 250183, train = 275, sq = 1, r = { { 12184, 3 }, { 3713, 4 } }, out = { 250075, 1 }, oq = 1 },
    [1250153] = { name = "Raptor Rouladen", t = { 1, 230, 237, 245 }, scroll = 250184, train = 225, sq = 1, r = { { 12184, 2 }, { 2692, 4 } }, out = { 250076, 1 }, oq = 1 },
    [1250154] = { name = "Twice-Spiced Raptor Slice", t = { 1, 115, 132, 150 }, scroll = 250185, train = 75, sq = 1, r = { { 12184, 1 }, { 2678, 2 } }, out = { 250077, 1 }, oq = 1 },
    [1250155] = { name = "Giant Scrambled Eggs", t = { 1, 195, 207, 220 }, scroll = 250186, train = 175, sq = 1, r = { { 12207, 2 }, { 2692, 4 } }, out = { 250078, 1 }, oq = 1 },
    [1250156] = { name = "Tasty Raptor Bites", t = { 1, 35, 55, 75 }, scroll = 250187, train = 25, sq = 1, r = { { 3685, 1 }, { 2678, 4 } }, out = { 250079, 1 }, oq = 1 },
    [1250157] = { name = "Breakfast Omelette", t = { 1, 80, 87, 95 }, scroll = 250188, train = 75, sq = 1, r = { { 6889, 1 }, { 2678, 4 } }, out = { 250080, 1 }, oq = 1 },
    [1250158] = { name = "Clam Linguine", t = { 1, 280, 295, 310 }, scroll = 250189, train = 275, sq = 1, r = { { 7974, 3 }, { 3713, 4 } }, out = { 250081, 1 }, oq = 1 },
    [1252566] = { name = "Savory Whimsyfin Delight", t = { 1, 125, 145, 165 }, scroll = 251526, train = 85, sq = 2, r = { { 251524, 1 }, { 2678, 1 } }, out = { 251525, 1 }, oq = 1 },
    [1262978] = { name = "Cookie's Feast", t = { 1, 145, 145, 145 }, scroll = 273102, train = 140, sq = 2, r = { { 12037, 2 }, { 12204, 1 }, { 3713, 1 } }, out = { 279957, 1 }, oq = 1 },
    [1270632] = { name = "Critter Cookie", t = { 1, 80, 82, 85 }, scroll = 263505, train = 70, sq = 1, r = { { 10284, 5 } }, out = { 263507, 1 }, oq = 1 },
    [1270633] = { name = "Skywall Souffle", t = { 1, 30, 37, 45 }, scroll = 263511, train = 25, sq = 1, r = { { 6889, 2 }, { 10284, 1 } }, out = { 263509, 1 }, oq = 1 },
    [1270635] = { name = "Pincer Bites", t = { 1, 40, 47, 55 }, scroll = 263513, train = 35, sq = 1, r = { { 2675, 1 }, { 10284, 1 } }, out = { 263512, 1 }, oq = 1 },
    [1283400] = { name = "Journeyman Campfire", t = { 1, 95, 95, 95 }, scroll = 273087, train = 90, sq = 2, r = { { 11291, 1 } }, out = { 279961, 1 }, oq = 1 },
    [1291341] = { name = "Expert Campfire", t = { 1, 205, 205, 205 }, scroll = 273101, train = 200, sq = 2, r = { { 272941, 1 } }, out = { 279974, 1 }, oq = 1 },
    [1294014] = { name = "Sweetpaw Jam", t = { 1, 280, 282, 285 }, scroll = 274415, train = 275, scrollPrice = 5000, sq = 1, r = { { 249796, 3 }, { 3713, 1 } }, out = { 267341, 1 }, oq = 1 },
    [1295805] = { name = "Briny Seafood Stew", t = { 1, 220, 230, 240 }, scroll = 274972, train = 200, sq = 1, r = { { 730, 2 }, { 12206, 1 }, { 2692, 1 } }, out = { 274971, 1 }, oq = 1 },
    [1295834] = { name = "Plain Ol' Paletusk", t = { 1, 200, 215, 230 }, scroll = 274977, train = 185, scrollPrice = 2000, sq = 1, r = { { 769, 2 }, { 2678, 1 } }, out = { 274976, 1 }, oq = 1 },
    [1319313] = { name = "Plated Armorfish", t = { 1, 245, 250, 255 }, scroll = 286153, train = 225, sq = 1, r = { { 13890, 1 }, { 3713, 1 } }, out = { 286152, 1 }, oq = 1 },
  },
}

-- Herramientas: [categoría] = { objeto, máscara } (un bastón superior cubre a los inferiores)
ES.Data.Tools = ES.Data.Tools or {}
ES.Data.Tools[12] = { item = 9149, mask = 1, family = "stone" }
ES.Data.Tools[14] = { item = 6219, mask = 1, family = "spanner" }
ES.Data.Tools[15] = { item = 10498, mask = 2, family = "adjustor" }
ES.Data.Tools[162] = { item = 5956, mask = 4, family = "hammer" }
ES.Data.Tools[373] = { item = 6218, mask = 1, family = "rod" }
ES.Data.Tools[374] = { item = 6339, mask = 3, family = "rod" }
ES.Data.Tools[375] = { item = 11130, mask = 7, family = "rod" }
ES.Data.Tools[376] = { item = 11145, mask = 15, family = "rod" }
ES.Data.Tools[377] = { item = 16207, mask = 31, family = "rod" }

ES.Data.VendorPrices = ES.Data.VendorPrices or {}
ES.Data.SellPrices = ES.Data.SellPrices or {}
ES.Data.VendorPrices[159] = 5
ES.Data.VendorPrices[1179] = 25
ES.Data.VendorPrices[1205] = 100
ES.Data.VendorPrices[1645] = 400
ES.Data.VendorPrices[1708] = 200
ES.Data.VendorPrices[2596] = 120
ES.Data.VendorPrices[2678] = 2
ES.Data.VendorPrices[2692] = 40
ES.Data.VendorPrices[2894] = 50
ES.Data.VendorPrices[3713] = 160
ES.Data.VendorPrices[4470] = 38
ES.Data.VendorPrices[4536] = 5
ES.Data.VendorPrices[8766] = 800
ES.Data.VendorPrices[10284] = 200
ES.Data.VendorPrices[11291] = 4500
ES.Data.VendorPrices[17196] = 50
ES.Data.VendorPrices[272941] = 200000
ES.Data.SellPrices[159] = 1
ES.Data.SellPrices[723] = 15
ES.Data.SellPrices[724] = 25
ES.Data.SellPrices[729] = 17
ES.Data.SellPrices[730] = 16
ES.Data.SellPrices[731] = 27
ES.Data.SellPrices[733] = 100
ES.Data.SellPrices[769] = 3
ES.Data.SellPrices[785] = 20
ES.Data.SellPrices[787] = 1
ES.Data.SellPrices[1015] = 24
ES.Data.SellPrices[1017] = 100
ES.Data.SellPrices[1080] = 78
ES.Data.SellPrices[1081] = 50
ES.Data.SellPrices[1082] = 150
ES.Data.SellPrices[1179] = 6
ES.Data.SellPrices[1205] = 25
ES.Data.SellPrices[1468] = 28
ES.Data.SellPrices[1475] = 82
ES.Data.SellPrices[1645] = 100
ES.Data.SellPrices[1708] = 50
ES.Data.SellPrices[2251] = 12
ES.Data.SellPrices[2447] = 10
ES.Data.SellPrices[2452] = 15
ES.Data.SellPrices[2596] = 30
ES.Data.SellPrices[2672] = 4
ES.Data.SellPrices[2673] = 10
ES.Data.SellPrices[2674] = 12
ES.Data.SellPrices[2675] = 11
ES.Data.SellPrices[2677] = 15
ES.Data.SellPrices[2678] = 1
ES.Data.SellPrices[2679] = 5
ES.Data.SellPrices[2680] = 10
ES.Data.SellPrices[2681] = 6
ES.Data.SellPrices[2682] = 25
ES.Data.SellPrices[2683] = 25
ES.Data.SellPrices[2684] = 20
ES.Data.SellPrices[2685] = 75
ES.Data.SellPrices[2687] = 25
ES.Data.SellPrices[2692] = 10
ES.Data.SellPrices[2886] = 5
ES.Data.SellPrices[2888] = 10
ES.Data.SellPrices[2894] = 12
ES.Data.SellPrices[2924] = 16
ES.Data.SellPrices[3172] = 18
ES.Data.SellPrices[3173] = 15
ES.Data.SellPrices[3174] = 16
ES.Data.SellPrices[3220] = 40
ES.Data.SellPrices[3357] = 75
ES.Data.SellPrices[3404] = 181
ES.Data.SellPrices[3662] = 25
ES.Data.SellPrices[3663] = 125
ES.Data.SellPrices[3664] = 100
ES.Data.SellPrices[3665] = 150
ES.Data.SellPrices[3666] = 100
ES.Data.SellPrices[3667] = 25
ES.Data.SellPrices[3685] = 71
ES.Data.SellPrices[3712] = 87
ES.Data.SellPrices[3713] = 40
ES.Data.SellPrices[3726] = 125
ES.Data.SellPrices[3727] = 125
ES.Data.SellPrices[3728] = 300
ES.Data.SellPrices[3729] = 300
ES.Data.SellPrices[3730] = 45
ES.Data.SellPrices[3731] = 55
ES.Data.SellPrices[3818] = 125
ES.Data.SellPrices[3821] = 150
ES.Data.SellPrices[4402] = 250
ES.Data.SellPrices[4457] = 300
ES.Data.SellPrices[4470] = 9
ES.Data.SellPrices[4536] = 1
ES.Data.SellPrices[4592] = 1
ES.Data.SellPrices[4593] = 4
ES.Data.SellPrices[4594] = 6
ES.Data.SellPrices[4603] = 4
ES.Data.SellPrices[4655] = 71
ES.Data.SellPrices[5051] = 1
ES.Data.SellPrices[5095] = 3
ES.Data.SellPrices[5465] = 3
ES.Data.SellPrices[5466] = 8
ES.Data.SellPrices[5467] = 7
ES.Data.SellPrices[5468] = 12
ES.Data.SellPrices[5469] = 9
ES.Data.SellPrices[5470] = 28
ES.Data.SellPrices[5471] = 30
ES.Data.SellPrices[5472] = 10
ES.Data.SellPrices[5473] = 10
ES.Data.SellPrices[5474] = 9
ES.Data.SellPrices[5476] = 3
ES.Data.SellPrices[5477] = 18
ES.Data.SellPrices[5478] = 70
ES.Data.SellPrices[5479] = 125
ES.Data.SellPrices[5480] = 95
ES.Data.SellPrices[5503] = 16
ES.Data.SellPrices[5504] = 22
ES.Data.SellPrices[5525] = 20
ES.Data.SellPrices[5526] = 75
ES.Data.SellPrices[5527] = 95
ES.Data.SellPrices[5637] = 75
ES.Data.SellPrices[6038] = 312
ES.Data.SellPrices[6289] = 1
ES.Data.SellPrices[6290] = 1
ES.Data.SellPrices[6291] = 1
ES.Data.SellPrices[6303] = 1
ES.Data.SellPrices[6308] = 2
ES.Data.SellPrices[6316] = 3
ES.Data.SellPrices[6317] = 2
ES.Data.SellPrices[6361] = 2
ES.Data.SellPrices[6362] = 4
ES.Data.SellPrices[6522] = 4
ES.Data.SellPrices[6657] = 5
ES.Data.SellPrices[6887] = 5
ES.Data.SellPrices[6888] = 10
ES.Data.SellPrices[6889] = 4
ES.Data.SellPrices[6890] = 6
ES.Data.SellPrices[7676] = 30
ES.Data.SellPrices[7974] = 50
ES.Data.SellPrices[8146] = 500
ES.Data.SellPrices[8150] = 250
ES.Data.SellPrices[8364] = 6
ES.Data.SellPrices[8365] = 4
ES.Data.SellPrices[8766] = 200
ES.Data.SellPrices[8838] = 60
ES.Data.SellPrices[8957] = 200
ES.Data.SellPrices[8959] = 160
ES.Data.SellPrices[9061] = 250
ES.Data.SellPrices[10284] = 50
ES.Data.SellPrices[10841] = 85
ES.Data.SellPrices[11291] = 1125
ES.Data.SellPrices[12037] = 87
ES.Data.SellPrices[12184] = 87
ES.Data.SellPrices[12202] = 87
ES.Data.SellPrices[12203] = 87
ES.Data.SellPrices[12204] = 112
ES.Data.SellPrices[12205] = 112
ES.Data.SellPrices[12206] = 112
ES.Data.SellPrices[12207] = 150
ES.Data.SellPrices[12208] = 150
ES.Data.SellPrices[12209] = 95
ES.Data.SellPrices[12210] = 300
ES.Data.SellPrices[12212] = 300
ES.Data.SellPrices[12213] = 300
ES.Data.SellPrices[12214] = 300
ES.Data.SellPrices[12215] = 300
ES.Data.SellPrices[12216] = 300
ES.Data.SellPrices[12217] = 300
ES.Data.SellPrices[12218] = 300
ES.Data.SellPrices[12223] = 4
ES.Data.SellPrices[12224] = 10
ES.Data.SellPrices[13465] = 150
ES.Data.SellPrices[13754] = 6
ES.Data.SellPrices[13755] = 7
ES.Data.SellPrices[13756] = 9
ES.Data.SellPrices[13758] = 4
ES.Data.SellPrices[13759] = 10
ES.Data.SellPrices[13760] = 10
ES.Data.SellPrices[13851] = 312
ES.Data.SellPrices[13888] = 12
ES.Data.SellPrices[13889] = 5
ES.Data.SellPrices[13890] = 70
ES.Data.SellPrices[13893] = 15
ES.Data.SellPrices[13927] = 8
ES.Data.SellPrices[13928] = 8
ES.Data.SellPrices[13929] = 10
ES.Data.SellPrices[13930] = 5
ES.Data.SellPrices[13931] = 12
ES.Data.SellPrices[13932] = 12
ES.Data.SellPrices[13933] = 14
ES.Data.SellPrices[13934] = 18
ES.Data.SellPrices[13935] = 10
ES.Data.SellPrices[16766] = 100
ES.Data.SellPrices[17196] = 12
ES.Data.SellPrices[17197] = 10
ES.Data.SellPrices[17198] = 9
ES.Data.SellPrices[17222] = 300
ES.Data.SellPrices[18045] = 300
ES.Data.SellPrices[18254] = 18
ES.Data.SellPrices[18255] = 15
ES.Data.SellPrices[20074] = 300
ES.Data.SellPrices[20424] = 175
ES.Data.SellPrices[20452] = 250
ES.Data.SellPrices[21023] = 250
ES.Data.SellPrices[21071] = 25
ES.Data.SellPrices[21072] = 40
ES.Data.SellPrices[21153] = 125
ES.Data.SellPrices[21217] = 125
ES.Data.SellPrices[232438] = 5
ES.Data.SellPrices[238637] = 250
ES.Data.SellPrices[238638] = 250
ES.Data.SellPrices[238639] = 250
ES.Data.SellPrices[238641] = 250
ES.Data.SellPrices[238642] = 250
ES.Data.SellPrices[249796] = 150
ES.Data.SellPrices[249865] = 1
ES.Data.SellPrices[249866] = 1
ES.Data.SellPrices[249867] = 1
ES.Data.SellPrices[249868] = 1
ES.Data.SellPrices[249869] = 1
ES.Data.SellPrices[249870] = 1
ES.Data.SellPrices[249871] = 1
ES.Data.SellPrices[249872] = 1
ES.Data.SellPrices[249873] = 1
ES.Data.SellPrices[249874] = 1
ES.Data.SellPrices[249875] = 1
ES.Data.SellPrices[249876] = 1
ES.Data.SellPrices[250065] = 150
ES.Data.SellPrices[250066] = 5
ES.Data.SellPrices[250067] = 10
ES.Data.SellPrices[250068] = 6
ES.Data.SellPrices[250069] = 25
ES.Data.SellPrices[250070] = 25
ES.Data.SellPrices[250071] = 10
ES.Data.SellPrices[250072] = 40
ES.Data.SellPrices[250073] = 125
ES.Data.SellPrices[250074] = 125
ES.Data.SellPrices[250075] = 10
ES.Data.SellPrices[250076] = 10
ES.Data.SellPrices[250077] = 9
ES.Data.SellPrices[250078] = 18
ES.Data.SellPrices[250079] = 10
ES.Data.SellPrices[250080] = 6
ES.Data.SellPrices[250081] = 10
ES.Data.SellPrices[251524] = 4
ES.Data.SellPrices[251525] = 5
ES.Data.SellPrices[263509] = 100
ES.Data.SellPrices[263512] = 100
ES.Data.SellPrices[267341] = 200
ES.Data.SellPrices[272941] = 50000
ES.Data.SellPrices[274971] = 12
ES.Data.SellPrices[274976] = 75
ES.Data.SellPrices[286152] = 8

-- Nombre de cada objeto (inglés, del cliente): se muestra mientras el juego no lo ha cargado
ES.Data.ItemNames = ES.Data.ItemNames or {}
ES.Data.ItemNames[159] = "Refreshing Spring Water"
ES.Data.ItemNames[723] = "Goretusk Liver"
ES.Data.ItemNames[724] = "Goretusk Liver Pie"
ES.Data.ItemNames[729] = "Stringy Vulture Meat"
ES.Data.ItemNames[730] = "Murloc Eye"
ES.Data.ItemNames[731] = "Goretusk Snout"
ES.Data.ItemNames[733] = "Westfall Stew"
ES.Data.ItemNames[769] = "Chunk of Boar Meat"
ES.Data.ItemNames[785] = "Mageroyal"
ES.Data.ItemNames[787] = "Slitherskin Mackerel"
ES.Data.ItemNames[1015] = "Lean Wolf Flank"
ES.Data.ItemNames[1017] = "Seasoned Wolf Kabob"
ES.Data.ItemNames[1080] = "Tough Condor Meat"
ES.Data.ItemNames[1081] = "Crisp Spider Meat"
ES.Data.ItemNames[1082] = "Redridge Goulash"
ES.Data.ItemNames[1179] = "Ice Cold Milk"
ES.Data.ItemNames[1205] = "Melon Juice"
ES.Data.ItemNames[1468] = "Murloc Fin"
ES.Data.ItemNames[1475] = "Small Venom Sac"
ES.Data.ItemNames[1645] = "Moonberry Juice"
ES.Data.ItemNames[1708] = "Sweet Nectar"
ES.Data.ItemNames[2251] = "Gooey Spider Leg"
ES.Data.ItemNames[2447] = "Peacebloom"
ES.Data.ItemNames[2452] = "Swiftthistle"
ES.Data.ItemNames[2596] = "Skin of Dwarven Stout"
ES.Data.ItemNames[2672] = "Stringy Wolf Meat"
ES.Data.ItemNames[2673] = "Coyote Meat"
ES.Data.ItemNames[2674] = "Crawler Meat"
ES.Data.ItemNames[2675] = "Crawler Claw"
ES.Data.ItemNames[2677] = "Boar Ribs"
ES.Data.ItemNames[2678] = "Mild Spices"
ES.Data.ItemNames[2679] = "Charred Wolf Meat"
ES.Data.ItemNames[2680] = "Spiced Wolf Meat"
ES.Data.ItemNames[2681] = "Roasted Boar Meat"
ES.Data.ItemNames[2682] = "Cooked Crab Claw"
ES.Data.ItemNames[2683] = "Crab Cake"
ES.Data.ItemNames[2684] = "Coyote Steak"
ES.Data.ItemNames[2685] = "Succulent Pork Ribs"
ES.Data.ItemNames[2687] = "Dry Pork Ribs"
ES.Data.ItemNames[2692] = "Hot Spices"
ES.Data.ItemNames[2886] = "Crag Boar Rib"
ES.Data.ItemNames[2888] = "Beer Basted Boar Ribs"
ES.Data.ItemNames[2894] = "Rhapsody Malt"
ES.Data.ItemNames[2924] = "Crocolisk Meat"
ES.Data.ItemNames[3172] = "Boar Intestines"
ES.Data.ItemNames[3173] = "Bear Meat"
ES.Data.ItemNames[3174] = "Spider Ichor"
ES.Data.ItemNames[3220] = "Blood Sausage"
ES.Data.ItemNames[3357] = "Liferoot"
ES.Data.ItemNames[3404] = "Buzzard Wing"
ES.Data.ItemNames[3662] = "Crocolisk Steak"
ES.Data.ItemNames[3663] = "Murloc Fin Soup"
ES.Data.ItemNames[3664] = "Crocolisk Gumbo"
ES.Data.ItemNames[3665] = "Curiously Tasty Omelet"
ES.Data.ItemNames[3666] = "Gooey Spider Cake"
ES.Data.ItemNames[3667] = "Tender Crocolisk Meat"
ES.Data.ItemNames[3685] = "Raptor Egg"
ES.Data.ItemNames[3712] = "Turtle Meat"
ES.Data.ItemNames[3713] = "Soothing Spices"
ES.Data.ItemNames[3726] = "Big Bear Steak"
ES.Data.ItemNames[3727] = "Hot Lion Chops"
ES.Data.ItemNames[3728] = "Tasty Lion Steak"
ES.Data.ItemNames[3729] = "Soothing Turtle Bisque"
ES.Data.ItemNames[3730] = "Big Bear Meat"
ES.Data.ItemNames[3731] = "Lion Meat"
ES.Data.ItemNames[3818] = "Fadeleaf"
ES.Data.ItemNames[3821] = "Goldthorn"
ES.Data.ItemNames[4402] = "Small Flame Sac"
ES.Data.ItemNames[4457] = "Barbecued Buzzard Wing"
ES.Data.ItemNames[4470] = "Simple Wood"
ES.Data.ItemNames[4536] = "Shiny Red Apple"
ES.Data.ItemNames[4592] = "Longjaw Mud Snapper"
ES.Data.ItemNames[4593] = "Bristle Whisker Catfish"
ES.Data.ItemNames[4594] = "Rockscale Cod"
ES.Data.ItemNames[4603] = "Raw Spotted Yellowtail"
ES.Data.ItemNames[4655] = "Giant Clam Meat"
ES.Data.ItemNames[5051] = "Dig Rat"
ES.Data.ItemNames[5095] = "Rainbow Fin Albacore"
ES.Data.ItemNames[5465] = "Small Spider Leg"
ES.Data.ItemNames[5466] = "Scorpid Stinger"
ES.Data.ItemNames[5467] = "Kodo Meat"
ES.Data.ItemNames[5468] = "Soft Frenzy Flesh"
ES.Data.ItemNames[5469] = "Strider Meat"
ES.Data.ItemNames[5470] = "Thunder Lizard Tail"
ES.Data.ItemNames[5471] = "Stag Meat"
ES.Data.ItemNames[5472] = "Kaldorei Spider Kabob"
ES.Data.ItemNames[5473] = "Scorpid Surprise"
ES.Data.ItemNames[5474] = "Roasted Kodo Meat"
ES.Data.ItemNames[5476] = "Fillet of Frenzy"
ES.Data.ItemNames[5477] = "Strider Stew"
ES.Data.ItemNames[5478] = "Dig Rat Stew"
ES.Data.ItemNames[5479] = "Crispy Lizard Tail"
ES.Data.ItemNames[5480] = "Lean Venison"
ES.Data.ItemNames[5503] = "Clam Meat"
ES.Data.ItemNames[5504] = "Tangy Clam Meat"
ES.Data.ItemNames[5525] = "Boiled Clams"
ES.Data.ItemNames[5526] = "Clam Chowder"
ES.Data.ItemNames[5527] = "Goblin Deviled Clams"
ES.Data.ItemNames[5637] = "Large Fang"
ES.Data.ItemNames[6038] = "Giant Clam Scorcho"
ES.Data.ItemNames[6289] = "Raw Longjaw Mud Snapper"
ES.Data.ItemNames[6290] = "Brilliant Smallfish"
ES.Data.ItemNames[6291] = "Raw Brilliant Smallfish"
ES.Data.ItemNames[6303] = "Raw Slitherskin Mackerel"
ES.Data.ItemNames[6308] = "Raw Bristle Whisker Catfish"
ES.Data.ItemNames[6316] = "Loch Frenzy Delight"
ES.Data.ItemNames[6317] = "Raw Loch Frenzy"
ES.Data.ItemNames[6361] = "Raw Rainbow Fin Albacore"
ES.Data.ItemNames[6362] = "Raw Rockscale Cod"
ES.Data.ItemNames[6522] = "Deviate Fish"
ES.Data.ItemNames[6657] = "Savory Deviate Delight"
ES.Data.ItemNames[6887] = "Spotted Yellowtail"
ES.Data.ItemNames[6888] = "Herb Baked Egg"
ES.Data.ItemNames[6889] = "Small Egg"
ES.Data.ItemNames[6890] = "Smoked Bear Meat"
ES.Data.ItemNames[7676] = "Thistle Tea"
ES.Data.ItemNames[7974] = "Zesty Clam Meat"
ES.Data.ItemNames[8146] = "Wicked Claw"
ES.Data.ItemNames[8150] = "Deeprock Salt"
ES.Data.ItemNames[8364] = "Mithril Head Trout"
ES.Data.ItemNames[8365] = "Raw Mithril Head Trout"
ES.Data.ItemNames[8766] = "Morning Glory Dew"
ES.Data.ItemNames[8838] = "Sungrass"
ES.Data.ItemNames[8957] = "Spinefin Halibut"
ES.Data.ItemNames[8959] = "Raw Spinefin Halibut"
ES.Data.ItemNames[9061] = "Goblin Rocket Fuel"
ES.Data.ItemNames[10284] = "Simple Flour"
ES.Data.ItemNames[10841] = "Goldthorn Tea"
ES.Data.ItemNames[11291] = "Star Wood"
ES.Data.ItemNames[12037] = "Mystery Meat"
ES.Data.ItemNames[12184] = "Raptor Flesh"
ES.Data.ItemNames[12202] = "Tiger Meat"
ES.Data.ItemNames[12203] = "Red Wolf Meat"
ES.Data.ItemNames[12204] = "Heavy Kodo Meat"
ES.Data.ItemNames[12205] = "White Spider Meat"
ES.Data.ItemNames[12206] = "Tender Crab Meat"
ES.Data.ItemNames[12207] = "Giant Egg"
ES.Data.ItemNames[12208] = "Tender Wolf Meat"
ES.Data.ItemNames[12209] = "Lean Wolf Steak"
ES.Data.ItemNames[12210] = "Roast Raptor"
ES.Data.ItemNames[12212] = "Jungle Stew"
ES.Data.ItemNames[12213] = "Carrion Surprise"
ES.Data.ItemNames[12214] = "Mystery Stew"
ES.Data.ItemNames[12215] = "Heavy Kodo Stew"
ES.Data.ItemNames[12216] = "Spiced Chili Crab"
ES.Data.ItemNames[12217] = "Dragonbreath Chili"
ES.Data.ItemNames[12218] = "Monster Omelet"
ES.Data.ItemNames[12223] = "Meaty Bat Wing"
ES.Data.ItemNames[12224] = "Crispy Bat Wing"
ES.Data.ItemNames[13465] = "Mountain Silversage"
ES.Data.ItemNames[13754] = "Raw Glossy Mightfish"
ES.Data.ItemNames[13755] = "Raw Winter Squid"
ES.Data.ItemNames[13756] = "Raw Summer Bass"
ES.Data.ItemNames[13758] = "Raw Redgill"
ES.Data.ItemNames[13759] = "Raw Nightfin Snapper"
ES.Data.ItemNames[13760] = "Raw Sunscale Salmon"
ES.Data.ItemNames[13851] = "Hot Wolf Ribs"
ES.Data.ItemNames[13888] = "Darkclaw Lobster"
ES.Data.ItemNames[13889] = "Raw Whitescale Salmon"
ES.Data.ItemNames[13890] = "Raw Plated Armorfish"
ES.Data.ItemNames[13893] = "Large Raw Mightfish"
ES.Data.ItemNames[13927] = "Cooked Glossy Mightfish"
ES.Data.ItemNames[13928] = "Grilled Squid"
ES.Data.ItemNames[13929] = "Hot Smoked Bass"
ES.Data.ItemNames[13930] = "Filet of Redgill"
ES.Data.ItemNames[13931] = "Nightfin Soup"
ES.Data.ItemNames[13932] = "Poached Sunscale Salmon"
ES.Data.ItemNames[13933] = "Lobster Stew"
ES.Data.ItemNames[13934] = "Mightfish Steak"
ES.Data.ItemNames[13935] = "Baked Salmon"
ES.Data.ItemNames[16766] = "Undermine Clam Chowder"
ES.Data.ItemNames[17194] = "Holiday Spices"
ES.Data.ItemNames[17196] = "Holiday Spirits"
ES.Data.ItemNames[17197] = "Gingerbread Cookie"
ES.Data.ItemNames[17198] = "Egg Nog"
ES.Data.ItemNames[17222] = "Spider Sausage"
ES.Data.ItemNames[18045] = "Tender Wolf Steak"
ES.Data.ItemNames[18254] = "Runn Tum Tuber Surprise"
ES.Data.ItemNames[18255] = "Runn Tum Tuber"
ES.Data.ItemNames[20074] = "Heavy Crocolisk Stew"
ES.Data.ItemNames[20424] = "Sandworm Meat"
ES.Data.ItemNames[20452] = "Smoked Desert Dumplings"
ES.Data.ItemNames[21023] = "Dirge's Kickin' Chimaerok Chops"
ES.Data.ItemNames[21024] = "Chimaerok Tenderloin"
ES.Data.ItemNames[21071] = "Raw Sagefish"
ES.Data.ItemNames[21072] = "Smoked Sagefish"
ES.Data.ItemNames[21153] = "Raw Greater Sagefish"
ES.Data.ItemNames[21217] = "Sagefish Delight"
ES.Data.ItemNames[232438] = "Smoked Redgill"
ES.Data.ItemNames[238637] = "Prowler Steak"
ES.Data.ItemNames[238638] = "Filet o' Flank"
ES.Data.ItemNames[238639] = "Sunrise Omelette"
ES.Data.ItemNames[238641] = "Specklefin Feast"
ES.Data.ItemNames[238642] = "Grand Lobster Banquet"
ES.Data.ItemNames[239016] = "Holy Salts"
ES.Data.ItemNames[239017] = "Exquisite Spices"
ES.Data.ItemNames[249796] = "Hyjal Berries"
ES.Data.ItemNames[249865] = "Peace Tea"
ES.Data.ItemNames[249866] = "Royal Tea"
ES.Data.ItemNames[249867] = "Root Tea"
ES.Data.ItemNames[249868] = "Triage Tea"
ES.Data.ItemNames[249869] = "Sunny Tea"
ES.Data.ItemNames[249870] = "Sage's Tea"
ES.Data.ItemNames[249871] = "Venomous Smoothie"
ES.Data.ItemNames[249872] = "Slimy Smoothie"
ES.Data.ItemNames[249873] = "Mrrggl Smrrthle"
ES.Data.ItemNames[249874] = "Calcified Smoothie"
ES.Data.ItemNames[249875] = "Spicy Smoothie"
ES.Data.ItemNames[249876] = "Wicked Smoothie"
ES.Data.ItemNames[250065] = "Savory Stag Sliders"
ES.Data.ItemNames[250066] = "Soaring Pamplona"
ES.Data.ItemNames[250067] = "Bat Hachee"
ES.Data.ItemNames[250068] = "Savory Turtle Stew"
ES.Data.ItemNames[250069] = "Flank au Poivre"
ES.Data.ItemNames[250070] = "Bear Bruscitti"
ES.Data.ItemNames[250071] = "Steaming Stag Steak"
ES.Data.ItemNames[250072] = "Swiftstrike Steak"
ES.Data.ItemNames[250073] = "Raging Raptor Ribs"
ES.Data.ItemNames[250074] = "Bear Brisket"
ES.Data.ItemNames[250075] = "Prehistoric Pulled Raptor"
ES.Data.ItemNames[250076] = "Raptor Rouladen"
ES.Data.ItemNames[250077] = "Twice-Spiced Raptor Slice"
ES.Data.ItemNames[250078] = "Giant Scrambled Eggs"
ES.Data.ItemNames[250079] = "Tasty Raptor Bites"
ES.Data.ItemNames[250080] = "Breakfast Omelette"
ES.Data.ItemNames[250081] = "Clam Linguine"
ES.Data.ItemNames[251524] = "Whimsyfin"
ES.Data.ItemNames[251525] = "Savory Whimsyfin Delight"
ES.Data.ItemNames[263509] = "Skywall Souffle"
ES.Data.ItemNames[263512] = "Pincer Bites"
ES.Data.ItemNames[267341] = "Sweetpaw Jam"
ES.Data.ItemNames[272941] = "Thick Logs"
ES.Data.ItemNames[274971] = "Briny Seafood Stew"
ES.Data.ItemNames[274976] = "Plain Ol' Paletusk"
ES.Data.ItemNames[279957] = "Cookie's Feast"
ES.Data.ItemNames[279961] = "Journeyman Campfire Kit"
ES.Data.ItemNames[279974] = "Expert Campfire Kit"
ES.Data.ItemNames[279981] = "Basic Campfire Kit"
ES.Data.ItemNames[286152] = "Plated Armorfish"

-- Material -> profesión de recolección que lo consigue (393 Desuello, 182 Herboristería, 186 Minería).
-- Sin uso por ahora: reservado para la vía "Vender en bruto" de Ganar dinero (docs/PLAN.md, G1).
ES.Data.GatheredBy = ES.Data.GatheredBy or {}
ES.Data.GatheredBy[785] = 182
ES.Data.GatheredBy[2447] = 182
ES.Data.GatheredBy[2452] = 182
ES.Data.GatheredBy[3357] = 182
ES.Data.GatheredBy[3818] = 182
ES.Data.GatheredBy[3821] = 182
ES.Data.GatheredBy[8150] = 186
ES.Data.GatheredBy[8838] = 182
ES.Data.GatheredBy[13465] = 182

```

---

## Enchanting

```lua
-- Generado por tools/gen_profession.py (Enchanting). No editar a mano.
-- Datos: cliente de WoW Forever (wago.tools DB2), instructores de CMaNGOS classic-db, vendedores de QuestieDB.
local _, ES = ...
ES.Data = ES.Data or {}

-- t = { naranja, amarilla, verde, gris }; fee/train = precio y habilidad del instructor
-- (sin fee = se aprende de pergamino: de dónde sale, en Data/Sources.lua; scrollPrice = su precio si lo vende un PNJ)
-- rep = { facción, nivel } que pide el pergamino para aprenderla (5 amistoso, 6 honorable, 7 venerado, 8 exaltado)
-- r = { {itemID, cantidad} }; out = { itemID, cantidad }
-- sq / oq = calidad del pergamino / de lo fabricado (0 pobre, 1 común, 2 poco común, 3 raro, 4 épico)
-- faction = bando que puede aprenderla, si solo es de uno
-- bop = lo fabricado se liga al recogerlo: no se puede vender en la AH (sí al vendedor)
-- favor / favorRep = se compra con Merchant's Favor en el campamento de tu bando, y la reputación que pide
-- train ajustado a Forever: nivel de Classic menos lo que Forever bajó la amarilla de esa receta
-- basic = se aprende sola al coger la profesión; trainer = de instructor sin precio conocido
--   (receta nueva de Forever que no está en CMaNGOS: se aprende al ponerse amarilla)
ES.Data.Enchanting = {
  skillLine = 333,
  ranks = { -- { tope, precio, habilidad requerida, nivel de personaje }
    { 150, 500, 50, 10 },
    { 225, 5000, 125, 20 },
    { 300, 50000, 200, 35 },
  },
  -- { PNJ instructor, rangos que enseña: 1 aprendiz (75), 2 oficial (150), 4 experto (225), 8 artesano (300) }
  trainers = { { 1317, 2 }, { 3011, 2 }, { 3345, 2 }, { 3606, 1 }, { 4213, 2 }, { 4616, 2 }, { 5157, 2 }, { 5695, 1 }, { 7949, 2 }, { 11065, 1 }, { 11066, 1 }, { 11067, 1 }, { 11068, 1 }, { 11070, 1 }, { 11071, 1 }, { 11072, 4 }, { 11073, 8 }, { 11074, 4 }, { 251978, 3 }, { 257004, 3 }, { 257020, 3 }, { 266881, 1 } },
  recipes = {
    [7418] = { name = "Enchant Bracer - Inferior Stamina", t = { 1, 20, 22, 25 }, basic = true, r = { { 247786, 1 } }, tool = 373 },
    [7420] = { name = "Enchant Chest - Inferior Stamina", t = { 1, 70, 90, 110 }, fee = 50, train = 15, r = { { 10940, 1 } }, tool = 373 },
    [7421] = { name = "Runed Copper Rod", t = { 1, 5, 7, 10 }, basic = true, r = { { 6217, 1 }, { 247786, 1 } }, out = { 6218, 1 }, oq = 1, bop = true },
    [7426] = { name = "Enchant Chest - Minor Absorption", t = { 1, 90, 110, 130 }, fee = 100, train = 40, r = { { 10938, 1 } }, tool = 373 },
    [7428] = { name = "Enchant Bracer - Minor Deflect", t = { 1, 80, 100, 120 }, basic = true, r = { { 10938, 1 } }, tool = 373 },
    [7443] = { name = "Enchant Chest - Minor Intellect", t = { 1, 80, 100, 120 }, scroll = 6342, train = 20, scrollPrice = 300, sq = 2, r = { { 10938, 1 } }, tool = 373 },
    [7454] = { name = "Enchant Cloak - Minor Resistance", t = { 1, 95, 115, 135 }, fee = 100, train = 45, r = { { 10940, 1 }, { 10938, 1 } }, tool = 373 },
    [7457] = { name = "Enchant Bracer - Minor Stamina", t = { 1, 100, 120, 140 }, fee = 250, train = 50, r = { { 10940, 2 } }, tool = 373 },
    [7745] = { name = "Enchant 2H Weapon - Minor Impact", t = { 1, 130, 150, 170 }, fee = 500, train = 100, r = { { 10940, 1 }, { 10978, 1 } }, tool = 373 },
    [7748] = { name = "Enchant Chest - Lesser Stamina", t = { 1, 105, 125, 145 }, fee = 250, train = 60, r = { { 10940, 1 }, { 10938, 1 } }, tool = 373 },
    [7766] = { name = "Enchant Bracer - Minor Spirit", t = { 1, 105, 125, 145 }, scroll = 6344, train = 60, sq = 2, r = { { 10938, 1 } }, tool = 373 },
    [7771] = { name = "Enchant Cloak - Minor Protection", t = { 1, 110, 130, 150 }, fee = 200, train = 70, r = { { 10940, 2 } }, tool = 373 },
    [7776] = { name = "Enchant Chest - Lesser Intellect", t = { 1, 115, 135, 155 }, scroll = 6346, train = 80, scrollPrice = 400, sq = 2, r = { { 10938, 2 } }, tool = 373 },
    [7779] = { name = "Enchant Bracer - Minor Agility", t = { 1, 115, 135, 155 }, fee = 400, train = 80, r = { { 10940, 1 }, { 10938, 2 } }, tool = 373 },
    [7782] = { name = "Enchant Bracer - Minor Strength", t = { 1, 115, 135, 155 }, scroll = 6347, train = 80, sq = 2, r = { { 10940, 3 } }, tool = 373 },
    [7786] = { name = "Enchant Weapon - Minor Beastslayer", t = { 1, 120, 140, 160 }, scroll = 6348, train = 90, sq = 2, r = { { 10940, 2 }, { 10939, 1 } }, tool = 373 },
    [7788] = { name = "Enchant Weapon - Minor Striking", t = { 1, 120, 140, 160 }, fee = 500, train = 90, r = { { 10940, 1 }, { 10938, 1 }, { 10978, 1 } }, tool = 373 },
    [7793] = { name = "Enchant 2H Weapon - Lesser Intellect", t = { 1, 130, 150, 170 }, scroll = 6349, train = 100, scrollPrice = 500, sq = 1, r = { { 10938, 4 } }, tool = 373 },
    [7795] = { name = "Runed Silver Rod", t = { 1, 130, 150, 170 }, fee = 1000, train = 100, r = { { 6338, 1 }, { 10940, 3 }, { 10938, 4 }, { 1210, 1 } }, out = { 6339, 1 }, oq = 1, bop = true },
    [7857] = { name = "Enchant Chest - Stamina", t = { 1, 145, 165, 185 }, fee = 1000, train = 120, r = { { 10940, 2 }, { 10998, 1 } }, tool = 374 },
    [7859] = { name = "Enchant Bracer - Lesser Spirit", t = { 1, 145, 165, 185 }, scroll = 6375, train = 120, sq = 2, r = { { 10998, 1 } }, tool = 374 },
    [7861] = { name = "Enchant Cloak - Lesser Fire Resistance", t = { 1, 150, 170, 190 }, fee = 1250, train = 125, r = { { 6371, 1 }, { 10998, 1 } }, tool = 374 },
    [7863] = { name = "Enchant Boots - Minor Stamina", t = { 1, 150, 170, 190 }, fee = 1400, train = 125, r = { { 10940, 4 } }, tool = 374 },
    [7867] = { name = "Enchant Boots - Minor Agility", t = { 1, 150, 170, 190 }, scroll = 6377, train = 125, scrollPrice = 1000, sq = 2, r = { { 10940, 3 }, { 10998, 1 } }, tool = 374 },
    [13378] = { name = "Enchant Shield - Minor Stamina", t = { 1, 130, 150, 170 }, fee = 600, train = 105, r = { { 10998, 1 }, { 10940, 1 } }, tool = 373 },
    [13380] = { name = "Enchant 2H Weapon - Lesser Spirit", t = { 1, 135, 155, 175 }, scroll = 11038, train = 110, sq = 2, r = { { 10998, 1 }, { 10940, 3 } }, tool = 373 },
    [13419] = { name = "Enchant Cloak - Minor Agility", t = { 1, 135, 155, 175 }, scroll = 11039, train = 110, scrollPrice = 800, sq = 2, r = { { 10998, 1 } }, tool = 374 },
    [13421] = { name = "Enchant Cloak - Lesser Protection", t = { 1, 140, 160, 180 }, fee = 800, train = 115, r = { { 10940, 3 }, { 10978, 1 } }, tool = 373 },
    [13464] = { name = "Enchant Shield - Lesser Protection", t = { 1, 140, 160, 180 }, scroll = 11081, train = 115, sq = 2, r = { { 10940, 1 }, { 10978, 1 } }, tool = 374 },
    [13485] = { name = "Enchant Shield - Lesser Spirit", t = { 1, 155, 175, 195 }, fee = 1500, train = 130, r = { { 10998, 1 }, { 10940, 2 } }, tool = 374 },
    [13501] = { name = "Enchant Bracer - Lesser Stamina", t = { 1, 155, 175, 195 }, fee = 1500, train = 130, r = { { 11083, 1 } }, tool = 374 },
    [13503] = { name = "Enchant Weapon - Lesser Striking", t = { 1, 165, 185, 205 }, fee = 2000, train = 140, r = { { 11083, 1 }, { 11084, 1 } }, tool = 374 },
    [13522] = { name = "Enchant Cloak - Lesser Shadow Resistance", t = { 1, 160, 180, 200 }, scroll = 11098, train = 135, sq = 2, r = { { 10998, 1 }, { 6048, 1 } }, tool = 374 },
    [13529] = { name = "Enchant 2H Weapon - Lesser Impact", t = { 1, 170, 190, 210 }, fee = 2400, train = 145, r = { { 11083, 1 }, { 11084, 1 } }, tool = 374 },
    [13536] = { name = "Enchant Bracer - Lesser Strength", t = { 1, 165, 185, 205 }, scroll = 11101, train = 140, scrollPrice = 2500, sq = 2, r = { { 11083, 1 } }, tool = 374 },
    [13538] = { name = "Enchant Chest - Lesser Absorption", t = { 1, 165, 185, 205 }, fee = 2500, train = 140, r = { { 10940, 1 }, { 10998, 1 }, { 11084, 1 } }, tool = 374 },
    [13607] = { name = "Enchant Chest - Intellect", t = { 1, 170, 190, 210 }, fee = 2400, train = 145, r = { { 11082, 1 } }, tool = 374 },
    [13612] = { name = "Enchant Gloves - Mining", t = { 1, 170, 190, 210 }, scroll = 11150, train = 145, sq = 2, r = { { 11083, 1 }, { 2772, 1 } }, tool = 374 },
    [13617] = { name = "Enchant Gloves - Herbalism", t = { 1, 170, 190, 210 }, scroll = 11151, train = 145, sq = 2, r = { { 11083, 1 }, { 3356, 1 } }, tool = 374 },
    [13620] = { name = "Enchant Gloves - Fishing", t = { 1, 170, 190, 210 }, scroll = 11152, train = 145, sq = 2, r = { { 11083, 1 }, { 6370, 1 } }, tool = 374 },
    [13622] = { name = "Enchant Bracer - Lesser Intellect", t = { 1, 175, 195, 215 }, fee = 2500, train = 150, r = { { 11082, 1 } }, tool = 374 },
    [13626] = { name = "Enchant Chest - Minor Stats", t = { 1, 175, 195, 215 }, fee = 2500, train = 150, r = { { 10998, 1 }, { 11083, 1 }, { 11084, 1 } }, tool = 374 },
    [13628] = { name = "Runed Golden Rod", t = { 1, 175, 195, 215 }, fee = 2500, train = 150, r = { { 11128, 1 }, { 5500, 1 }, { 11082, 1 }, { 11083, 1 } }, out = { 11130, 1 }, oq = 1, bop = true },
    [13631] = { name = "Enchant Shield - Lesser Stamina", t = { 1, 175, 195, 215 }, fee = 2600, train = 155, r = { { 11134, 1 } }, tool = 375 },
    [13635] = { name = "Enchant Cloak - Defense", t = { 1, 175, 195, 215 }, fee = 2600, train = 155, r = { { 11138, 1 }, { 11083, 1 } }, tool = 375 },
    [13637] = { name = "Enchant Boots - Lesser Agility", t = { 1, 180, 200, 220 }, fee = 2800, train = 160, r = { { 11083, 1 } }, tool = 375 },
    [13640] = { name = "Enchant Chest - Greater Stamina", t = { 1, 180, 200, 220 }, fee = 2700, train = 160, r = { { 11083, 2 } }, tool = 375 },
    [13642] = { name = "Enchant Bracer - Spirit", t = { 1, 185, 205, 225 }, fee = 2800, train = 165, r = { { 11134, 1 } }, tool = 375 },
    [13644] = { name = "Enchant Boots - Lesser Stamina", t = { 1, 190, 210, 230 }, fee = 2800, train = 170, r = { { 11083, 2 } }, tool = 375 },
    [13646] = { name = "Enchant Bracer - Lesser Deflection", t = { 1, 190, 210, 230 }, scroll = 11163, train = 170, scrollPrice = 3000, sq = 2, r = { { 11134, 1 }, { 11083, 1 } }, tool = 375 },
    [13648] = { name = "Enchant Bracer - Stamina", t = { 1, 190, 210, 230 }, fee = 2800, train = 170, r = { { 11083, 3 } }, tool = 375 },
    [13653] = { name = "Enchant Weapon - Lesser Beastslayer", t = { 1, 195, 215, 235 }, scroll = 11164, train = 175, sq = 2, r = { { 5637, 1 }, { 11138, 1 } }, tool = 375 },
    [13655] = { name = "Enchant Weapon - Lesser Elemental Slayer", t = { 1, 195, 215, 235 }, scroll = 11165, train = 175, sq = 2, r = { { 7067, 1 }, { 11138, 1 } }, tool = 375 },
    [13657] = { name = "Enchant Cloak - Fire Resistance", t = { 1, 195, 215, 235 }, fee = 3000, train = 175, r = { { 11134, 1 }, { 7068, 1 } }, tool = 375 },
    [13659] = { name = "Enchant Shield - Spirit", t = { 1, 200, 220, 240 }, fee = 3200, train = 180, r = { { 11134, 1 }, { 11137, 1 } }, tool = 375 },
    [13661] = { name = "Enchant Bracer - Strength", t = { 1, 200, 220, 240 }, fee = 3600, train = 180, r = { { 11137, 1 } }, tool = 375 },
    [13663] = { name = "Enchant Chest - Greater Intellect", t = { 1, 205, 225, 245 }, fee = 3800, train = 185, r = { { 11134, 1 } }, tool = 375 },
    [13687] = { name = "Enchant Boots - Lesser Spirit", t = { 1, 210, 230, 250 }, scroll = 11167, train = 190, sq = 2, r = { { 11134, 2 } }, tool = 375 },
    [13689] = { name = "Enchant Shield - Lesser Block", t = { 1, 215, 235, 255 }, scroll = 11168, train = 195, sq = 2, r = { { 11135, 1 }, { 11137, 1 }, { 11139, 1 } }, tool = 375 },
    [13693] = { name = "Enchant Weapon - Striking", t = { 1, 215, 235, 255 }, fee = 4000, train = 195, r = { { 11135, 1 }, { 11139, 1 } }, tool = 375 },
    [13695] = { name = "Enchant 2H Weapon - Impact", t = { 1, 220, 240, 260 }, fee = 4000, train = 200, r = { { 11137, 2 }, { 11139, 1 } }, tool = 375 },
    [13698] = { name = "Enchant Gloves - Skinning", t = { 1, 220, 240, 260 }, scroll = 11166, train = 200, sq = 2, r = { { 11137, 1 }, { 7392, 1 } }, tool = 375 },
    [13700] = { name = "Enchant Chest - Lesser Stats", t = { 1, 220, 240, 260 }, fee = 4000, train = 200, r = { { 11135, 1 }, { 11137, 1 }, { 11139, 1 } }, tool = 375 },
    [13702] = { name = "Runed Truesilver Rod", t = { 1, 220, 240, 260 }, fee = 4000, train = 200, r = { { 11144, 1 }, { 7971, 1 }, { 11135, 1 }, { 11137, 1 } }, out = { 11145, 1 }, oq = 1, bop = true },
    [13746] = { name = "Enchant Cloak - Greater Defense", t = { 1, 225, 245, 265 }, fee = 4200, train = 205, r = { { 11137, 1 } }, tool = 376 },
    [13794] = { name = "Enchant Cloak - Resistance", t = { 1, 225, 245, 265 }, fee = 4200, train = 205, r = { { 11174, 1 } }, tool = 376 },
    [13815] = { name = "Enchant Gloves - Agility", t = { 1, 230, 250, 270 }, fee = 4400, train = 210, r = { { 11137, 1 } }, tool = 376 },
    [13817] = { name = "Enchant Shield - Stamina", t = { 1, 230, 250, 270 }, scroll = 11202, train = 210, sq = 2, r = { { 11137, 2 } }, tool = 376 },
    [13822] = { name = "Enchant Bracer - Intellect", t = { 1, 230, 250, 270 }, fee = 4400, train = 210, r = { { 11174, 1 } }, tool = 376 },
    [13836] = { name = "Enchant Boots - Stamina", t = { 1, 235, 255, 275 }, fee = 4600, train = 215, r = { { 11137, 2 } }, tool = 376 },
    [13841] = { name = "Enchant Gloves - Advanced Mining", t = { 1, 235, 255, 275 }, scroll = 11203, train = 215, sq = 2, r = { { 11137, 2 }, { 6037, 1 } }, tool = 376 },
    [13846] = { name = "Enchant Bracer - Greater Spirit", t = { 1, 240, 260, 280 }, scroll = 11204, train = 220, sq = 2, r = { { 11174, 1 }, { 11137, 1 } }, tool = 376 },
    [13858] = { name = "Enchant Chest - Superior Stamina", t = { 1, 240, 260, 280 }, fee = 4800, train = 220, r = { { 11137, 3 } }, tool = 376 },
    [13868] = { name = "Enchant Gloves - Advanced Herbalism", t = { 1, 245, 265, 285 }, scroll = 11205, train = 225, sq = 2, r = { { 11137, 2 }, { 8838, 1 } }, tool = 376 },
    [13882] = { name = "Enchant Cloak - Lesser Agility", t = { 1, 245, 265, 285 }, scroll = 11206, train = 225, sq = 2, r = { { 11174, 1 } }, tool = 376 },
    [13887] = { name = "Enchant Gloves - Strength", t = { 1, 245, 265, 285 }, fee = 5000, train = 225, r = { { 11174, 1 }, { 11137, 2 } }, tool = 376 },
    [13890] = { name = "Enchant Boots - Minor Speed", t = { 1, 245, 265, 285 }, fee = 5000, train = 225, r = { { 11177, 1 }, { 7909, 1 }, { 11174, 1 } }, tool = 376 },
    [13898] = { name = "Enchant Weapon - Fiery Weapon", t = { 1, 285, 305, 325 }, scroll = 11207, train = 265, sq = 2, r = { { 11177, 2 }, { 7078, 1 } }, tool = 376 },
    [13905] = { name = "Enchant Shield - Greater Spirit", t = { 1, 250, 270, 290 }, fee = 5400, train = 230, r = { { 11174, 2 }, { 11176, 1 } }, tool = 376 },
    [13915] = { name = "Enchant Weapon - Demonslaying", t = { 1, 250, 270, 290 }, scroll = 11208, train = 230, sq = 2, r = { { 11177, 1 }, { 11176, 1 }, { 9224, 1 } }, tool = 376 },
    [13917] = { name = "Enchant Chest - Superior Intellect", t = { 1, 250, 270, 290 }, fee = 5400, train = 230, r = { { 11175, 1 } }, tool = 376 },
    [13931] = { name = "Enchant Bracer - Deflection", t = { 1, 255, 275, 295 }, scroll = 11223, train = 235, scrollPrice = 5800, sq = 2, r = { { 11174, 2 }, { 11176, 1 } }, tool = 376 },
    [13933] = { name = "Enchant Shield - Frost Resistance", t = { 1, 255, 275, 295 }, scroll = 11224, train = 235, sq = 2, r = { { 11178, 1 }, { 3829, 1 } }, tool = 376 },
    [13935] = { name = "Enchant Boots - Agility", t = { 1, 255, 275, 295 }, fee = 5800, train = 235, r = { { 11175, 1 } }, tool = 376 },
    [13937] = { name = "Enchant 2H Weapon - Greater Impact", t = { 1, 260, 280, 300 }, fee = 6200, train = 240, r = { { 11178, 1 }, { 11176, 1 } }, tool = 376 },
    [13939] = { name = "Enchant Bracer - Greater Strength", t = { 1, 260, 280, 300 }, fee = 6200, train = 240, r = { { 11176, 1 }, { 11174, 2 } }, tool = 376 },
    [13941] = { name = "Enchant Chest - Stats", t = { 1, 265, 285, 305 }, fee = 6200, train = 245, r = { { 11178, 1 }, { 11176, 1 }, { 11175, 1 } }, tool = 376 },
    [13943] = { name = "Enchant Weapon - Greater Striking", t = { 1, 265, 285, 305 }, fee = 6200, train = 245, r = { { 11178, 1 }, { 11175, 1 } }, tool = 376 },
    [13945] = { name = "Enchant Bracer - Greater Stamina", t = { 1, 265, 285, 305 }, scroll = 11225, train = 245, sq = 2, r = { { 11176, 3 } }, tool = 376 },
    [13947] = { name = "Enchant Gloves - Riding Skill", t = { 1, 270, 290, 310 }, scroll = 11226, train = 250, sq = 2, r = { { 11178, 1 }, { 11176, 2 } }, tool = 376 },
    [13948] = { name = "Enchant Gloves - Minor Haste", t = { 1, 270, 290, 310 }, fee = 6500, train = 250, r = { { 11178, 1 }, { 8153, 1 } }, tool = 376 },
    [14293] = { name = "Lesser Magic Wand", t = { 1, 75, 95, 115 }, fee = 50, train = 10, r = { { 4470, 1 }, { 10938, 1 } }, tool = 373, out = { 11287, 1 }, oq = 2 },
    [14807] = { name = "Greater Magic Wand", t = { 1, 110, 130, 150 }, fee = 200, train = 70, r = { { 4470, 1 }, { 10938, 2 } }, tool = 373, out = { 11288, 1 }, oq = 2 },
    [14809] = { name = "Lesser Mystic Wand", t = { 1, 175, 195, 215 }, fee = 2600, train = 155, r = { { 11291, 1 }, { 11134, 1 } }, tool = 375, out = { 11289, 1 }, oq = 2 },
    [14810] = { name = "Greater Mystic Wand", t = { 1, 195, 215, 235 }, fee = 3000, train = 175, r = { { 11291, 1 }, { 11134, 1 }, { 11137, 1 } }, tool = 375, out = { 217287, 1 }, oq = 2 },
    [15596] = { name = "Smoking Heart of the Mountain", t = { 1, 285, 305, 325 }, scroll = 11813, train = 265, sq = 2, r = { { 11382, 1 }, { 7078, 1 }, { 14343, 3 } }, out = { 11811, 1 }, oq = 1 },
    [17180] = { name = "Enchanted Thorium", t = { 1, 250, 255, 260 }, fee = 10000, train = 250, r = { { 12359, 1 }, { 11176, 3 } }, tool = 376, out = { 12655, 1 }, oq = 1 },
    [17181] = { name = "Enchanted Leather", t = { 1, 250, 255, 260 }, fee = 10000, train = 250, r = { { 8170, 1 }, { 16202, 1 } }, tool = 376, out = { 12810, 1 }, oq = 1 },
    [20008] = { name = "Enchant Bracer - Greater Intellect", t = { 1, 275, 295, 315 }, scroll = 16214, train = 255, sq = 2, r = { { 16202, 2 } }, tool = 376 },
    [20009] = { name = "Enchant Bracer - Superior Spirit", t = { 1, 290, 310, 330 }, scroll = 16218, train = 270, sq = 2, r = { { 16202, 2 }, { 11176, 7 } }, tool = 376 },
    [20010] = { name = "Enchant Bracer - Superior Strength", t = { 1, 315, 335, 355 }, scroll = 16246, train = 295, sq = 2, r = { { 16204, 6 }, { 16203, 6 } }, tool = 376 },
    [20011] = { name = "Enchant Bracer - Superior Stamina", t = { 1, 320, 340, 360 }, scroll = 16251, train = 300, sq = 2, r = { { 16204, 15 } }, tool = 376 },
    [20012] = { name = "Enchant Gloves - Greater Agility", t = { 1, 290, 310, 330 }, scroll = 16219, train = 270, sq = 2, r = { { 16202, 2 }, { 16204, 2 } }, tool = 376 },
    [20013] = { name = "Enchant Gloves - Greater Strength", t = { 1, 315, 335, 355 }, scroll = 16244, train = 295, sq = 2, r = { { 16203, 4 }, { 16204, 4 } }, tool = 376 },
    [20014] = { name = "Enchant Cloak - Greater Resistance", t = { 1, 285, 305, 325 }, scroll = 16216, train = 265, sq = 2, r = { { 16202, 1 }, { 7077, 1 }, { 7075, 1 }, { 7079, 1 }, { 7081, 1 }, { 7972, 1 } }, tool = 376 },
    [20015] = { name = "Enchant Cloak - Superior Defense", t = { 1, 305, 325, 345 }, scroll = 16224, train = 285, scrollPrice = 20000, sq = 1, r = { { 16204, 8 } }, tool = 376 },
    [20016] = { name = "Enchant Shield - Superior Spirit", t = { 1, 300, 320, 340 }, scroll = 16222, train = 280, sq = 2, r = { { 16203, 2 }, { 16204, 4 } }, tool = 376 },
    [20017] = { name = "Enchant Shield - Greater Stamina", t = { 1, 285, 305, 325 }, scroll = 16217, train = 265, scrollPrice = 12000, sq = 1, r = { { 11176, 6 } }, tool = 376 },
    [20020] = { name = "Enchant Boots - Greater Stamina", t = { 1, 280, 300, 320 }, scroll = 16215, train = 260, sq = 2, r = { { 11176, 6 } }, tool = 376 },
    [20023] = { name = "Enchant Boots - Greater Agility", t = { 1, 315, 335, 355 }, scroll = 16245, train = 295, sq = 2, r = { { 16203, 8 } }, tool = 376 },
    [20024] = { name = "Enchant Boots - Spirit", t = { 1, 295, 315, 335 }, scroll = 16220, train = 275, sq = 2, r = { { 16203, 2 }, { 16202, 1 } }, tool = 376 },
    [20025] = { name = "Enchant Chest - Greater Stats", t = { 1, 320, 340, 360 }, scroll = 16253, train = 300, sq = 2, r = { { 14344, 4 }, { 16204, 15 }, { 16203, 10 } }, tool = 377 },
    [20026] = { name = "Enchant Chest - Major Stamina", t = { 1, 295, 315, 335 }, scroll = 16221, train = 275, scrollPrice = 16000, sq = 1, r = { { 16204, 6 }, { 14343, 1 } }, tool = 376 },
    [20028] = { name = "Enchant Chest - Major Intellect", t = { 1, 310, 330, 350 }, scroll = 16242, train = 290, sq = 2, r = { { 16203, 3 }, { 14343, 1 } }, tool = 376 },
    [20029] = { name = "Enchant Weapon - Icy Chill", t = { 1, 305, 325, 345 }, scroll = 16223, train = 285, sq = 2, r = { { 14343, 4 }, { 7080, 1 }, { 7082, 1 }, { 13467, 1 } }, tool = 376 },
    [20030] = { name = "Enchant 2H Weapon - Superior Impact", t = { 1, 315, 335, 355 }, scroll = 16247, train = 295, sq = 2, r = { { 14344, 4 }, { 16204, 10 } }, tool = 377 },
    [20031] = { name = "Enchant Weapon - Superior Striking", t = { 1, 320, 340, 360 }, scroll = 16250, train = 300, sq = 2, r = { { 14344, 2 }, { 16203, 10 } }, tool = 377 },
    [20032] = { name = "Enchant Weapon - Lifestealing", t = { 1, 320, 340, 360 }, scroll = 16254, train = 300, sq = 3, r = { { 14344, 6 }, { 12808, 6 }, { 12803, 6 } }, tool = 377 },
    [20033] = { name = "Enchant Weapon - Unholy Weapon", t = { 1, 315, 335, 355 }, scroll = 16248, train = 295, sq = 2, r = { { 14344, 4 }, { 12808, 4 } }, tool = 377 },
    [20034] = { name = "Enchant Weapon - Crusader", t = { 1, 320, 340, 360 }, scroll = 16252, train = 300, sq = 2, r = { { 14344, 4 }, { 12811, 2 } }, tool = 377 },
    [20035] = { name = "Enchant 2H Weapon - Major Spirit", t = { 1, 320, 340, 360 }, scroll = 16255, train = 300, sq = 2, r = { { 16203, 12 }, { 14344, 2 } }, tool = 377 },
    [20036] = { name = "Enchant 2H Weapon - Major Intellect", t = { 1, 320, 340, 360 }, scroll = 16249, train = 300, sq = 2, r = { { 16203, 12 }, { 14344, 2 } }, tool = 377 },
    [20051] = { name = "Runed Arcanite Rod", t = { 1, 310, 330, 350 }, scroll = 16243, train = 290, scrollPrice = 22000, sq = 1, r = { { 16206, 1 }, { 13926, 1 }, { 16204, 10 }, { 16203, 4 }, { 14343, 4 }, { 14344, 2 } }, out = { 16207, 1 }, oq = 1, bop = true },
    [21931] = { name = "Enchant Weapon - Winter's Might", t = { 1, 210, 230, 250 }, scroll = 17725, train = 190, sq = 2, r = { { 11135, 1 }, { 11137, 1 }, { 11139, 1 }, { 3819, 1 } }, tool = 375 },
    [22749] = { name = "Enchant Weapon - Spell Power", t = { 1, 320, 340, 360 }, scroll = 18259, train = 300, sq = 3, r = { { 14344, 4 }, { 16203, 12 }, { 7078, 4 }, { 7080, 4 }, { 7082, 4 }, { 13926, 2 } }, tool = 377 },
    [22750] = { name = "Enchant Weapon - Healing Power", t = { 1, 320, 340, 360 }, scroll = 18260, train = 300, sq = 3, r = { { 14344, 4 }, { 16203, 8 }, { 12803, 6 }, { 7080, 6 }, { 12811, 1 } }, tool = 377 },
    [23799] = { name = "Enchant Weapon - Strength", t = { 1, 310, 330, 350 }, scroll = 19444, train = 290, rep = { 59, 4 }, sq = 1, r = { { 14344, 6 }, { 16203, 6 }, { 16204, 4 }, { 7076, 2 } }, tool = 377 },
    [23800] = { name = "Enchant Weapon - Agility", t = { 1, 310, 330, 350 }, scroll = 19445, train = 290, scrollPrice = 30000, rep = { 576, 5 }, sq = 1, r = { { 14344, 6 }, { 16203, 6 }, { 16204, 4 }, { 7082, 2 } }, tool = 377 },
    [23801] = { name = "Enchant Bracer - Mana Regeneration", t = { 1, 310, 330, 350 }, scroll = 19446, train = 290, scrollPrice = 30000, rep = { 529, 5 }, sq = 1, r = { { 16204, 16 }, { 16203, 4 }, { 7080, 2 } }, tool = 377 },
    [23802] = { name = "Enchant Bracer - Healing Power", t = { 1, 320, 340, 360 }, scroll = 19447, train = 300, scrollPrice = 60000, rep = { 529, 6 }, sq = 1, r = { { 14344, 2 }, { 16204, 20 }, { 16203, 4 }, { 12803, 6 } }, tool = 377 },
    [23803] = { name = "Enchant Weapon - Mighty Spirit", t = { 1, 320, 340, 360 }, scroll = 19448, train = 300, rep = { 59, 5 }, sq = 1, r = { { 14344, 10 }, { 16203, 8 }, { 16204, 15 } }, tool = 377 },
    [23804] = { name = "Enchant Weapon - Mighty Intellect", t = { 1, 320, 340, 360 }, scroll = 19449, train = 300, rep = { 59, 6 }, sq = 1, r = { { 14344, 15 }, { 16203, 12 }, { 16204, 20 } }, tool = 377 },
    [25072] = { name = "Enchant Gloves - Threat", t = { 1, 320, 340, 360 }, scroll = 20726, train = 300, sq = 3, r = { { 20725, 4 }, { 14344, 6 }, { 18512, 8 } }, tool = 377 },
    [25073] = { name = "Enchant Gloves - Shadow Power", t = { 1, 320, 340, 360 }, scroll = 20727, train = 300, sq = 3, r = { { 20725, 3 }, { 14344, 10 }, { 12808, 6 } }, tool = 377 },
    [25074] = { name = "Enchant Gloves - Frost Power", t = { 1, 320, 340, 360 }, scroll = 20728, train = 300, sq = 3, r = { { 20725, 3 }, { 14344, 10 }, { 7080, 4 } }, tool = 377 },
    [25078] = { name = "Enchant Gloves - Fire Power", t = { 1, 320, 340, 360 }, scroll = 20729, train = 300, sq = 3, r = { { 20725, 2 }, { 14344, 10 }, { 7078, 4 } }, tool = 377 },
    [25079] = { name = "Enchant Gloves - Healing Power", t = { 1, 320, 340, 360 }, scroll = 20730, train = 300, sq = 3, r = { { 20725, 3 }, { 14344, 8 }, { 12811, 1 } }, tool = 377 },
    [25080] = { name = "Enchant Gloves - Superior Agility", t = { 1, 320, 340, 360 }, scroll = 20731, train = 300, sq = 3, r = { { 20725, 3 }, { 14344, 8 }, { 7082, 4 } }, tool = 377 },
    [25081] = { name = "Enchant Cloak - Greater Fire Resistance", t = { 1, 320, 340, 360 }, scroll = 229008, train = 300, rep = { 59, 5 }, sq = 1, r = { { 20725, 3 }, { 14344, 8 }, { 7078, 4 } }, tool = 377 },
    [25082] = { name = "Enchant Cloak - Greater Nature Resistance", t = { 1, 320, 340, 360 }, scroll = 229009, train = 300, rep = { 59, 5 }, sq = 1, r = { { 20725, 2 }, { 14344, 8 }, { 12803, 4 } }, tool = 377 },
    [25083] = { name = "Enchant Cloak - Stealth", t = { 1, 320, 340, 360 }, scroll = 20734, train = 300, sq = 3, r = { { 20725, 3 }, { 14344, 8 }, { 13468, 2 } }, tool = 377 },
    [25084] = { name = "Enchant Cloak - Subtlety", t = { 1, 320, 340, 360 }, scroll = 20735, train = 300, sq = 3, r = { { 20725, 4 }, { 14344, 6 }, { 11754, 2 } }, tool = 377 },
    [25086] = { name = "Enchant Cloak - Dodge", t = { 1, 320, 340, 360 }, scroll = 20736, train = 300, sq = 3, r = { { 20725, 3 }, { 14344, 8 }, { 12809, 8 } }, tool = 377 },
    [25124] = { name = "Minor Wizard Oil", t = { 1, 30, 47, 65 }, scroll = 20758, train = 5, scrollPrice = 500, sq = 1, r = { { 10940, 1 }, { 17034, 1 }, { 3371, 1 } }, tool = 373, out = { 20744, 1 }, oq = 1 },
    [25125] = { name = "Minor Mana Oil", t = { 1, 160, 170, 180 }, scroll = 20752, train = 150, scrollPrice = 3000, sq = 1, r = { { 11083, 1 }, { 17034, 2 }, { 3372, 1 } }, tool = 374, out = { 20745, 1 }, oq = 1 },
    [25126] = { name = "Lesser Wizard Oil", t = { 1, 210, 220, 230 }, scroll = 20753, train = 200, scrollPrice = 4000, sq = 1, r = { { 11137, 1 }, { 17035, 2 }, { 3372, 1 } }, tool = 375, out = { 20746, 1 }, oq = 1 },
    [25127] = { name = "Lesser Mana Oil", t = { 1, 260, 270, 280 }, scroll = 20754, train = 250, scrollPrice = 10000, sq = 1, r = { { 11176, 1 }, { 8831, 1 }, { 8925, 1 } }, tool = 376, out = { 20747, 1 }, oq = 1 },
    [25128] = { name = "Wizard Oil", t = { 1, 285, 295, 305 }, scroll = 20755, train = 275, scrollPrice = 20000, sq = 1, r = { { 16204, 3 }, { 4625, 2 }, { 8925, 1 } }, tool = 376, out = { 20750, 1 }, oq = 1 },
    [25129] = { name = "Brilliant Wizard Oil", t = { 1, 310, 320, 330 }, scroll = 20756, train = 300, scrollPrice = 40000, rep = { 270, 5 }, sq = 1, r = { { 14344, 2 }, { 4625, 3 }, { 18256, 1 } }, tool = 377, out = { 20749, 1 }, oq = 1 },
    [25130] = { name = "Brilliant Mana Oil", t = { 1, 310, 320, 330 }, scroll = 20757, train = 300, scrollPrice = 40000, rep = { 270, 4 }, sq = 1, r = { { 14344, 2 }, { 8831, 3 }, { 18256, 1 } }, tool = 377, out = { 20748, 1 }, oq = 1 },
    [27837] = { name = "Enchant 2H Weapon - Agility", t = { 1, 310, 330, 350 }, scroll = 22392, train = 290, scrollPrice = 25000, rep = { 576, 4 }, sq = 1, r = { { 14344, 10 }, { 16203, 6 }, { 16204, 14 }, { 7082, 4 } }, tool = 377 },
    [430409] = { name = "Blackfathom Mana Oil", t = { 1, 100, 110, 120 }, scroll = 211849, train = 90, sq = 1, r = { { 3372, 1 }, { 10939, 1 }, { 10940, 5 } }, tool = 374, out = { 211848, 1 }, oq = 1 },
    [435481] = { name = "Enchant Weapon - Dismantle", t = { 1, 200, 217, 235 }, scroll = 215129, train = 225, gone = true, sq = 4, r = { { 11174, 4 }, { 5637, 2 }, { 11177, 2 } }, tool = 375 },
    [435903] = { name = "Enchant Chest - Retricutioner", t = { 1, 200, 220, 240 }, scroll = 215138, train = 225, gone = true, sq = 4, r = { { 11177, 1 }, { 11176, 2 } }, tool = 375 },
    [439156] = { name = "Sigil of Innovation", t = { 1, 225, 227, 230 }, scroll = 215141, train = 225, gone = true, sq = 4, r = { { 11137, 5 } }, tool = 375, out = { 217308, 1 }, oq = 2, bop = true },
    [446243] = { name = "Sigil of Living Dreams", t = { 1, 250, 255, 260 }, r = { { 11176, 5 } }, tool = 376, out = { 221028, 1 }, oq = 1 },
    [448624] = { name = "Scroll of Spatial Mending", t = { 1, 120, 140, 160 }, scroll = 223163, train = 120, sq = 2, r = { { 4470, 1 }, { 10940, 4 } }, tool = 374, out = { 220792, 1 }, oq = 2 },
    [463866] = { name = "Sigil of Flowing Waters", t = { 1, 305, 312, 320 }, scroll = 228979, train = 290, gone = true, rep = { 749, 6 }, sq = 4, r = { { 16204, 1 } }, tool = 376, out = { 228978, 1 }, oq = 3, bop = true },
    [463869] = { name = "Conductive Shield Coating", t = { 1, 285, 295, 305 }, scroll = 228981, train = 275, sq = 1, r = { { 16204, 2 }, { 4625, 1 }, { 8925, 1 } }, tool = 376, out = { 228980, 1 }, oq = 1 },
    [463871] = { name = "Enchant Shield - Law of Nature", t = { 1, 320, 340, 360 }, scroll = 228982, train = 300, gone = true, rep = { 576, 6 }, sq = 3, r = { { 14344, 4 }, { 16203, 12 }, { 7078, 4 }, { 7080, 4 }, { 7076, 1 }, { 12811, 1 } }, tool = 377 },
    [471400] = { name = "Magnificent Trollshine", t = { 1, 310, 320, 330 }, scroll = 232610, train = 300, gone = true, rep = { 270, 5 }, sq = 1, r = { { 8151, 3 }, { 8152, 3 }, { 14344, 2 }, { 18256, 1 } }, tool = 377, out = { 232611, 1 }, oq = 1 },
    [1213607] = { name = "Scroll: Wrath of the Swarm", t = { 1, 320, 340, 360 }, scroll = 234271, train = 300, sq = 1, r = { { 16203, 1 }, { 14047, 1 } }, tool = 377, out = { 233995, 1 }, oq = 1 },
    [1213622] = { name = "Enchant Gloves - Holy Power", t = { 1, 320, 340, 360 }, scroll = 249536, train = 300, sq = 2, favor = 240, favorRep = 6, r = { { 20725, 2 }, { 14344, 5 }, { 13180, 5 }, { 12735, 2 } }, tool = 377 },
    [1213626] = { name = "Enchant Gloves - Arcane Power", t = { 1, 320, 340, 360 }, scroll = 249534, train = 300, sq = 2, favor = 240, favorRep = 6, r = { { 20725, 2 }, { 14344, 5 }, { 12753, 2 } }, tool = 377 },
    [1217189] = { name = "Enchant Bracer - Spell Power", t = { 1, 320, 340, 360 }, scroll = 235526, train = 310, sq = 1, r = { { 14344, 2 }, { 16204, 20 }, { 16203, 4 }, { 7080, 2 }, { 7078, 2 }, { 7082, 2 } }, tool = 377 },
    [1219577] = { name = "Enchant Off-Hand - Superior Intellect", t = { 1, 320, 340, 360 }, scroll = 274391, train = 300, sq = 3, r = { { 20725, 2 }, { 16204, 18 }, { 7082, 2 } }, tool = 377 },
    [1219578] = { name = "Enchant Off-Hand - Excellent Spirit", t = { 1, 320, 340, 360 }, scroll = 274392, train = 300, sq = 3, r = { { 20725, 2 }, { 16204, 18 }, { 7080, 2 } }, tool = 377 },
    [1219579] = { name = "Enchant Off-Hand - Wisdom", t = { 1, 320, 340, 360 }, scroll = 274393, train = 300, sq = 3, favor = 240, favorRep = 6, r = { { 14344, 6 }, { 16204, 18 }, { 7082, 1 }, { 7080, 1 } }, tool = 377 },
    [1219580] = { name = "Enchant 2H Weapon - Spellblasting", t = { 1, 320, 340, 360 }, scroll = 274394, train = 300, sq = 3, favor = 240, favorRep = 6, r = { { 20725, 3 }, { 16204, 24 }, { 12938, 1 }, { 8831, 6 } }, tool = 377 },
    [1219581] = { name = "Enchant Shield - Excellent Stamina", t = { 1, 320, 340, 360 }, scroll = 274395, train = 300, sq = 3, r = { { 14344, 6 }, { 16204, 18 }, { 7076, 2 } }, tool = 377 },
    [1219587] = { name = "Enchant Cloak - Agility", t = { 1, 320, 340, 360 }, scroll = 274399, train = 300, sq = 3, favor = 240, favorRep = 6, r = { { 16203, 3 }, { 16204, 9 }, { 7078, 1 } }, tool = 377 },
    [1220623] = { name = "Enchant Shield - Critical Strike", t = { 1, 320, 340, 360 }, scroll = 274400, train = 300, sq = 3, r = { { 14344, 5 }, { 16204, 15 }, { 12938, 1 } }, tool = 377 },
    [1220624] = { name = "Enchant Bracer - Greater Spellpower", t = { 1, 320, 340, 360 }, scroll = 274401, train = 300, sq = 3, favor = 240, favorRep = 6, r = { { 16203, 3 }, { 16204, 9 }, { 12808, 12 }, { 8831, 2 } }, tool = 377 },
    [1230643] = { name = "Enchanted Lute", t = { 1, 20, 20, 20 }, fee = 0, train = 20, r = { { 4470, 1 }, { 10940, 1 } }, out = { 279976, 1 }, oq = 1 },
    [1231128] = { name = "Enchant Weapon - Grand Crusader", t = { 1, 305, 307, 310 }, scroll = 241191, train = 280, sq = 3, r = { { 14344, 5 }, { 12811, 2 }, { 20725, 2 }, { 12938, 1 } }, tool = 377 },
    [1231139] = { name = "Enchant 2H Weapon - Grand Arcanist", t = { 1, 305, 307, 310 }, scroll = 241195, train = 280, sq = 3, r = { { 14344, 10 }, { 12811, 4 }, { 20725, 4 }, { 12938, 1 } }, tool = 377 },
    [1231164] = { name = "Enchant Weapon - Grand Sorcerer", t = { 1, 305, 307, 310 }, scroll = 241201, train = 280, sq = 3, r = { { 14344, 6 }, { 12811, 3 }, { 20725, 2 }, { 12938, 1 } }, tool = 377 },
    [1232172] = { name = "Enchant 2H Weapon - Grand Inquisitor", t = { 1, 305, 307, 310 }, scroll = 242361, train = 280, sq = 3, r = { { 14344, 10 }, { 12811, 6 }, { 20725, 4 }, { 12938, 1 } }, tool = 377 },
    [1245320] = { name = "Dust to Motes", t = { 1, 10, 12, 15 }, basic = true, r = { { 10940, 1 } }, tool = 373, out = { 247786, 3 }, oq = 1 },
    [1245321] = { name = "Novice's Practice Wand", t = { 1, 10, 12, 15 }, basic = true, r = { { 4470, 1 }, { 247786, 1 } }, tool = 373, out = { 247789, 1 }, oq = 1 },
    [1248458] = { name = "Enchant Bracer - Minor Intellect", t = { 1, 110, 130, 150 }, scroll = 249474, train = 70, sq = 2, r = { { 10938, 1 } }, tool = 373 },
    [1248459] = { name = "Enchant Bracer - Minor Healing Power", t = { 1, 120, 140, 160 }, scroll = 249475, train = 90, sq = 2, r = { { 10938, 2 } }, tool = 373 },
    [1248460] = { name = "Enchant Bracer - Lesser Agility", t = { 1, 165, 185, 205 }, scroll = 249486, train = 140, scrollPrice = 10000, sq = 2, r = { { 11134, 1 } }, tool = 374 },
    [1248461] = { name = "Twisted Nether Wand", t = { 1, 205, 225, 245 }, scroll = 249487, train = 185, sq = 2, r = { { 11174, 1 }, { 11176, 1 }, { 11291, 1 } }, tool = 375, out = { 249144, 1 }, oq = 2 },
    [1248497] = { name = "Enchant Bracer - Agility", t = { 1, 225, 245, 265 }, scroll = 249488, train = 190, sq = 2, r = { { 11137, 1 } }, tool = 375 },
    [1248498] = { name = "Enchant Bracer - Lesser Healing Power", t = { 1, 225, 245, 265 }, scroll = 249489, train = 205, scrollPrice = 10000, sq = 2, r = { { 11134, 2 } }, tool = 376 },
    [1248500] = { name = "Enchant Bracer - Greater Agility", t = { 1, 260, 280, 300 }, scroll = 249514, train = 240, sq = 2, r = { { 11176, 3 }, { 11174, 1 } }, tool = 376 },
    [1248505] = { name = "Lesser Eternal Wand", t = { 1, 265, 285, 305 }, scroll = 249515, train = 245, sq = 2, r = { { 16202, 1 }, { 11176, 1 }, { 11291, 1 } }, tool = 376, out = { 249232, 1 }, oq = 2 },
    [1248509] = { name = "Dreambough Wand", t = { 1, 235, 255, 275 }, scroll = 249512, train = 215, sq = 2, r = { { 11174, 2 }, { 11137, 1 }, { 11291, 1 } }, tool = 376, out = { 249234, 1 }, oq = 2 },
    [1248510] = { name = "Enchant 2H Weapon - Lesser Agility", t = { 1, 230, 250, 270 }, scroll = 249511, train = 210, sq = 2, r = { { 11137, 2 }, { 11139, 1 }, { 11174, 1 } }, tool = 376 },
    [1248511] = { name = "Enchant 2H Weapon - Lesser Strength", t = { 1, 240, 260, 280 }, scroll = 249513, train = 220, sq = 2, r = { { 11137, 1 }, { 11139, 1 }, { 11174, 2 } }, tool = 376 },
    [1248515] = { name = "Greater Eternal Wand", t = { 1, 285, 295, 305 }, scroll = 249522, train = 275, sq = 2, r = { { 16203, 2 }, { 16204, 1 }, { 11291, 1 } }, tool = 376, out = { 249237, 1 }, oq = 2 },
    [1248528] = { name = "Enchant Gloves - Advanced Skinning", t = { 1, 270, 290, 310 }, scroll = 249516, train = 250, sq = 2, r = { { 11176, 2 }, { 15407, 1 } }, tool = 376 },
    [1248599] = { name = "Enchant Bracer - Superior Agility", t = { 1, 315, 335, 355 }, scroll = 249524, train = 295, sq = 2, r = { { 16204, 3 }, { 16203, 3 }, { 14344, 1 } }, tool = 376 },
    [1248607] = { name = "Enchant 2H Weapon - Mighty Spell Power", t = { 1, 320, 340, 360 }, scroll = 249525, train = 300, sq = 2, favor = 240, favorRep = 6, r = { { 248819, 4 }, { 16203, 6 }, { 7076, 4 }, { 12808, 4 }, { 20725, 4 }, { 248820, 2 } }, tool = 377 },
    [1248636] = { name = "Enchant 2H Weapon - Mighty Healing Power", t = { 1, 320, 340, 360 }, scroll = 249526, train = 300, sq = 2, favor = 240, favorRep = 6, r = { { 248819, 4 }, { 16203, 6 }, { 249726, 4 }, { 249274, 4 }, { 20725, 4 }, { 248820, 4 } }, tool = 377 },
    [1248640] = { name = "Enchant Gloves - Superior Strength", t = { 1, 320, 340, 360 }, scroll = 274398, train = 300, sq = 3, favor = 240, favorRep = 6, r = { { 20725, 4 }, { 16203, 8 }, { 7076, 4 } }, tool = 377 },
    [1248645] = { name = "Enchant Gloves - Natural Power", t = { 1, 320, 340, 360 }, scroll = 249535, train = 300, sq = 2, favor = 240, favorRep = 6, r = { { 20725, 2 }, { 14344, 5 }, { 248822, 4 } }, tool = 377 },
    [1248650] = { name = "Brilliant Wand", t = { 1, 320, 340, 360 }, scroll = 249537, train = 275, sq = 3, favor = 180, favorRep = 6, r = { { 16203, 1 }, { 16204, 3 }, { 14344, 2 }, { 11291, 1 } }, tool = 377, out = { 249385, 1 }, oq = 3, bop = true },
    [1248661] = { name = "Enchant Bracer - Superior Intellect", t = { 1, 320, 340, 360 }, scroll = 249538, train = 300, sq = 2, favor = 240, favorRep = 6, r = { { 16203, 10 } }, tool = 376 },
    [1248665] = { name = "Enchant Bracer - Superior Deflection", t = { 1, 320, 340, 360 }, scroll = 249539, train = 300, sq = 2, favor = 240, favorRep = 6, r = { { 14344, 3 } }, tool = 376 },
    [1248668] = { name = "Enchant 2H Weapon - Strength", t = { 1, 295, 297, 300 }, scroll = 249523, train = 290, sq = 2, r = { { 14344, 8 }, { 16203, 10 }, { 16204, 8 }, { 12363, 4 } }, tool = 377 },
    [1248703] = { name = "Glimmering Staff", t = { 1, 140, 160, 180 }, scroll = 249482, train = 140, sq = 3, favor = 45, r = { { 11084, 4 }, { 10978, 2 }, { 11291, 4 }, { 11082, 1 }, { 10940, 5 }, { 249391, 3 } }, tool = 374, out = { 249392, 1 }, oq = 3, bop = true },
    [1248739] = { name = "Soulstaff", t = { 1, 140, 160, 180 }, scroll = 249483, train = 140, sq = 3, favor = 45, r = { { 11084, 2 }, { 10978, 1 }, { 11291, 4 }, { 11082, 1 }, { 11083, 6 }, { 1210, 2 } }, tool = 374, out = { 249393, 1 }, oq = 3, bop = true },
    [1248745] = { name = "Orb of Mystic Insight", t = { 1, 140, 160, 180 }, scroll = 249484, train = 140, sq = 3, favor = 45, r = { { 10978, 2 }, { 11082, 2 }, { 10940, 5 } }, tool = 374, out = { 249394, 1 }, oq = 3, bop = true },
    [1248748] = { name = "Orb of Souls", t = { 1, 140, 160, 180 }, scroll = 249485, train = 140, sq = 3, favor = 45, r = { { 10978, 2 }, { 11082, 2 }, { 11083, 2 } }, tool = 374, out = { 249395, 1 }, oq = 3, bop = true },
    [1248752] = { name = "Mystic Mushroom", t = { 1, 140, 160, 180 }, scroll = 249476, train = 130, sq = 3, favor = 45, r = { { 10978, 1 }, { 10939, 2 }, { 10940, 5 }, { 4605, 1 } }, tool = 374, out = { 249396, 1 }, oq = 3, bop = true },
    [1248754] = { name = "Tenets of the Silver Hand", t = { 1, 140, 160, 180 }, scroll = 249477, train = 130, sq = 3, favor = 45, r = { { 11084, 1 }, { 10939, 1 }, { 10940, 2 }, { 3013, 5 } }, tool = 374, out = { 249397, 1 }, oq = 3, bop = true },
    [1248755] = { name = "Polished Driftwood Icon", t = { 1, 140, 160, 180 }, scroll = 249478, train = 130, sq = 3, favor = 45, r = { { 11084, 1 }, { 10939, 2 }, { 10940, 3 }, { 4470, 1 } }, tool = 374, out = { 249398, 1 }, oq = 3, bop = true },
    [1248757] = { name = "Enchant Weapon - Insight", t = { 1, 140, 160, 180 }, scroll = 249479, train = 140, sq = 2, favor = 45, r = { { 10940, 10 }, { 11084, 4 }, { 11082, 4 }, { 249391, 4 }, { 249399, 4 } }, tool = 374 },
    [1248760] = { name = "Enchant Weapon - Recovery", t = { 1, 140, 160, 180 }, scroll = 249480, train = 140, sq = 2, favor = 45, r = { { 11083, 6 }, { 11084, 4 }, { 11082, 6 }, { 249391, 4 }, { 2775, 4 } }, tool = 374 },
    [1248805] = { name = "Enchant Weapon - Revelation", t = { 1, 140, 160, 180 }, scroll = 249481, train = 140, sq = 2, favor = 45, r = { { 11083, 8 }, { 11084, 6 }, { 11082, 2 }, { 249409, 4 }, { 249410, 4 } }, tool = 374 },
    [1248974] = { name = "Talons of Wrath", t = { 1, 225, 245, 265 }, scroll = 249493, train = 210, sq = 3, favor = 120, favorRep = 5, r = { { 11178, 2 }, { 11175, 4 }, { 11176, 6 }, { 249430, 2 }, { 249409, 1 }, { 11291, 1 } }, tool = 374, out = { 249441, 1 }, oq = 3, bop = true },
    [1249006] = { name = "Libram of Invocation", t = { 1, 225, 245, 265 }, scroll = 249494, train = 210, sq = 3, favor = 120, favorRep = 5, r = { { 11178, 3 }, { 11175, 3 }, { 11176, 4 }, { 249430, 2 }, { 249409, 1 }, { 2289, 4 } }, tool = 374, out = { 249442, 1 }, oq = 3, bop = true },
    [1249015] = { name = "Totem of Ancestral Protection", t = { 1, 225, 245, 265 }, scroll = 249495, train = 210, sq = 3, favor = 120, favorRep = 5, r = { { 11178, 4 }, { 11175, 2 }, { 11176, 2 }, { 249432, 4 }, { 249410, 2 }, { 11291, 2 } }, tool = 374, out = { 249443, 1 }, oq = 3, bop = true },
    [1249019] = { name = "Enchant Necklace - Strength", t = { 1, 225, 245, 265 }, scroll = 249496, train = 210, sq = 2, favor = 120, favorRep = 5, r = { { 11175, 4 }, { 11178, 4 }, { 11176, 10 }, { 249410, 4 }, { 249425, 4 } }, tool = 376 },
    [1249057] = { name = "Enchant Necklace - Spell Power", t = { 1, 225, 245, 265 }, scroll = 249502, train = 210, sq = 2, favor = 120, favorRep = 5, r = { { 11175, 5 }, { 11178, 3 }, { 11176, 8 }, { 249409, 4 }, { 249430, 4 } }, tool = 376 },
    [1249058] = { name = "Enchant Necklace - Healing Power", t = { 1, 225, 245, 265 }, scroll = 249503, train = 210, sq = 2, favor = 120, favorRep = 5, r = { { 11175, 3 }, { 11178, 5 }, { 11176, 4 }, { 249391, 4 }, { 249424, 4 } }, tool = 376 },
    [1249059] = { name = "Enchant Necklace - Agility", t = { 1, 225, 245, 265 }, scroll = 249504, train = 210, sq = 2, favor = 120, favorRep = 5, r = { { 11175, 2 }, { 11178, 8 }, { 11176, 6 }, { 249410, 4 }, { 249430, 4 } }, tool = 376 },
    [1249060] = { name = "Enchant Necklace - Deflection", t = { 1, 225, 245, 265 }, scroll = 249505, train = 210, sq = 2, favor = 120, favorRep = 5, r = { { 11175, 8 }, { 11178, 2 }, { 11176, 2 }, { 249409, 4 }, { 249430, 4 } }, tool = 376 },
    [1249061] = { name = "Radiant Staff", t = { 1, 225, 245, 265 }, scroll = 249506, train = 220, sq = 3, favor = 120, favorRep = 5, r = { { 11178, 6 }, { 11177, 2 }, { 11291, 4 }, { 11175, 4 }, { 11176, 6 }, { 249409, 2 }, { 249430, 4 } }, tool = 374, out = { 249453, 1 }, oq = 3, bop = true },
    [1249064] = { name = "Dreamstaff", t = { 1, 225, 245, 265 }, scroll = 249507, train = 220, sq = 3, favor = 120, favorRep = 5, r = { { 11178, 4 }, { 11177, 4 }, { 11291, 4 }, { 11175, 6 }, { 11176, 8 }, { 249409, 2 }, { 249430, 4 } }, tool = 374, out = { 249454, 1 }, oq = 3, bop = true },
    [1249069] = { name = "Truesilver Conduit", t = { 1, 225, 245, 265 }, scroll = 249508, train = 220, sq = 3, favor = 120, favorRep = 5, r = { { 11178, 3 }, { 11177, 1 }, { 11291, 2 }, { 11175, 2 }, { 11176, 3 }, { 249409, 1 }, { 249430, 2 } }, tool = 374, out = { 249455, 1 }, oq = 3, bop = true },
    [1249070] = { name = "Twisting Essence Jar", t = { 1, 225, 245, 265 }, scroll = 249509, train = 220, sq = 3, favor = 120, favorRep = 5, r = { { 6037, 4 }, { 11175, 12 }, { 11135, 12 }, { 249409, 1 }, { 249430, 2 } }, tool = 374, out = { 249456, 1 }, oq = 3, bop = true },
    [1249071] = { name = "Enchant Chest - Absorption", t = { 1, 225, 245, 265 }, scroll = 249510, train = 220, sq = 2, favor = 120, favorRep = 5, r = { { 11176, 10 }, { 11175, 4 }, { 11178, 2 } }, tool = 374 },
    [1249107] = { name = "Frozen Heart of the Mountain", t = { 1, 285, 305, 325 }, scroll = 249519, train = 265, sq = 3, r = { { 11382, 1 }, { 12808, 1 }, { 14343, 3 } }, out = { 249469, 1 }, oq = 3, bop = true },
    [1249112] = { name = "Molten Heart of the Mountain", t = { 1, 285, 305, 325 }, scroll = 249520, train = 265, sq = 3, r = { { 11382, 1 }, { 7076, 1 }, { 14343, 3 } }, out = { 249470, 1 }, oq = 3, bop = true },
    [1249114] = { name = "Dormant Heart of the Mountain", t = { 1, 285, 305, 325 }, scroll = 249521, train = 265, sq = 3, r = { { 11382, 1 }, { 7080, 1 }, { 14343, 3 } }, out = { 249473, 1 }, oq = 3, bop = true },
    [1249128] = { name = "Idol of the Dream", t = { 1, 320, 340, 360 }, scroll = 249529, train = 300, sq = 3, favor = 240, favorRep = 6, r = { { 14344, 2 }, { 16203, 4 }, { 16204, 6 }, { 249431, 8 }, { 249430, 4 }, { 249409, 2 }, { 11291, 4 } }, tool = 377, out = { 220606, 1 }, oq = 3, bop = true },
    [1249152] = { name = "Libram of Holy Alacrity", t = { 1, 320, 340, 360 }, scroll = 249530, train = 300, sq = 3, favor = 240, favorRep = 6, r = { { 14344, 4 }, { 16203, 3 }, { 16204, 4 }, { 249431, 8 }, { 249430, 4 }, { 249409, 2 }, { 10308, 4 } }, tool = 377, out = { 228175, 1 }, oq = 3, bop = true },
    [1249154] = { name = "Totem of Thunder", t = { 1, 320, 340, 360 }, scroll = 249532, train = 300, sq = 3, favor = 240, favorRep = 6, r = { { 14344, 1 }, { 16203, 8 }, { 16204, 10 }, { 249431, 8 }, { 249430, 4 }, { 249409, 2 }, { 11291, 4 } }, tool = 377, out = { 228176, 1 }, oq = 3, bop = true },
    [1263056] = { name = "Arcane Salvager", t = { 1, 140, 140, 140 }, scroll = 273103, train = 140, sq = 2, r = { { 11137, 2 }, { 11174, 1 } }, tool = 375, out = { 279985, 1 }, oq = 1 },
    [1294054] = { name = "Enchant Gloves - Lotus Claw", t = { 1, 295, 297, 300 }, scroll = 274424, train = 295, scrollPrice = 5000, sq = 2, r = { { 248822, 1 }, { 14343, 2 }, { 16204, 12 }, { 16202, 4 } }, tool = 377 },
    [1306520] = { name = "Torch of Light", t = { 1, 310, 317, 325 }, scroll = 279295, train = 300, sq = 4, r = { { 274030, 2 }, { 20725, 1 }, { 14344, 6 }, { 16202, 5 } }, out = { 279246, 1 }, oq = 4 },
    [1306521] = { name = "Steadfast Libram", t = { 1, 310, 317, 325 }, scroll = 279296, train = 300, sq = 4, r = { { 274030, 1 }, { 20725, 1 }, { 16203, 2 }, { 16204, 12 } }, out = { 279247, 1 }, oq = 4 },
    [1306522] = { name = "Libram of Infusion", t = { 1, 310, 317, 325 }, scroll = 279297, train = 300, sq = 4, r = { { 274030, 1 }, { 20725, 1 }, { 16203, 2 }, { 16204, 12 } }, out = { 279248, 1 }, oq = 4 },
    [1306523] = { name = "Totem of Urgency", t = { 1, 310, 317, 325 }, scroll = 279298, train = 300, sq = 4, r = { { 274030, 1 }, { 20725, 1 }, { 16203, 2 }, { 16204, 12 } }, out = { 279249, 1 }, oq = 4 },
    [1306524] = { name = "Idol of Swiftness", t = { 1, 310, 317, 325 }, scroll = 279299, train = 300, sq = 4, r = { { 274030, 1 }, { 20725, 1 }, { 16203, 2 }, { 16204, 12 } }, out = { 279250, 1 }, oq = 4 },
    [1306525] = { name = "Idol of the Ursine Twins", t = { 1, 310, 317, 325 }, scroll = 279300, train = 300, sq = 4, r = { { 274030, 1 }, { 20725, 1 }, { 16203, 2 }, { 16204, 12 } }, out = { 279251, 1 }, oq = 4 },
    [1328948] = { name = "Enchant Boots - Speed", t = { 1, 280, 290, 300 }, scroll = 289560, train = 280, scrollPrice = 6200, sq = 2, r = { { 11178, 2 }, { 11176, 8 }, { 11175, 2 }, { 12361, 1 } }, tool = 376 },
    -- Conversión de esencias (clic derecho en la bolsa): no es receta ni da puntos
    [-1] = { name = "Convertir 3 en 1 mayor", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 10938, 3 } }, out = { 10939, 1 } },
    [-2] = { name = "Convertir 1 en 3 menores", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 10939, 1 } }, out = { 10938, 3 } },
    [-3] = { name = "Convertir 3 en 1 mayor", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 10998, 3 } }, out = { 11082, 1 } },
    [-4] = { name = "Convertir 1 en 3 menores", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 11082, 1 } }, out = { 10998, 3 } },
    [-5] = { name = "Convertir 3 en 1 mayor", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 11134, 3 } }, out = { 11135, 1 } },
    [-6] = { name = "Convertir 1 en 3 menores", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 11135, 1 } }, out = { 11134, 3 } },
    [-7] = { name = "Convertir 3 en 1 mayor", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 11174, 3 } }, out = { 11175, 1 } },
    [-8] = { name = "Convertir 1 en 3 menores", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 11175, 1 } }, out = { 11174, 3 } },
    [-9] = { name = "Convertir 3 en 1 mayor", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 16202, 3 } }, out = { 16203, 1 } },
    [-10] = { name = "Convertir 1 en 3 menores", intermediate = true, conversion = true, t = { 1, 1, 1, 1 }, train = 1, r = { { 16203, 1 } }, out = { 16202, 3 } },
  },
}

-- Herramientas: [categoría] = { objeto, máscara } (un bastón superior cubre a los inferiores)
ES.Data.Tools = ES.Data.Tools or {}
ES.Data.Tools[12] = { item = 9149, mask = 1, family = "stone" }
ES.Data.Tools[14] = { item = 6219, mask = 1, family = "spanner" }
ES.Data.Tools[15] = { item = 10498, mask = 2, family = "adjustor" }
ES.Data.Tools[162] = { item = 5956, mask = 4, family = "hammer" }
ES.Data.Tools[373] = { item = 6218, mask = 1, family = "rod" }
ES.Data.Tools[374] = { item = 6339, mask = 3, family = "rod" }
ES.Data.Tools[375] = { item = 11130, mask = 7, family = "rod" }
ES.Data.Tools[376] = { item = 11145, mask = 15, family = "rod" }
ES.Data.Tools[377] = { item = 16207, mask = 31, family = "rod" }

ES.Data.VendorPrices = ES.Data.VendorPrices or {}
ES.Data.SellPrices = ES.Data.SellPrices or {}
ES.Data.VendorPrices[3371] = 4
ES.Data.VendorPrices[3372] = 40
ES.Data.VendorPrices[4470] = 38
ES.Data.VendorPrices[4605] = 25
ES.Data.VendorPrices[6217] = 124
ES.Data.VendorPrices[8925] = 500
ES.Data.VendorPrices[10938] = 800
ES.Data.VendorPrices[10940] = 800
ES.Data.VendorPrices[11291] = 4500
ES.Data.VendorPrices[17034] = 200
ES.Data.VendorPrices[17035] = 400
ES.Data.VendorPrices[18256] = 6000
ES.Data.VendorPrices[247786] = 10
ES.Data.SellPrices[1210] = 250
ES.Data.SellPrices[2289] = 87
ES.Data.SellPrices[2772] = 150
ES.Data.SellPrices[2775] = 75
ES.Data.SellPrices[3013] = 25
ES.Data.SellPrices[3356] = 30
ES.Data.SellPrices[3371] = 1
ES.Data.SellPrices[3372] = 10
ES.Data.SellPrices[3819] = 100
ES.Data.SellPrices[3829] = 150
ES.Data.SellPrices[4470] = 9
ES.Data.SellPrices[4605] = 6
ES.Data.SellPrices[4625] = 250
ES.Data.SellPrices[5500] = 750
ES.Data.SellPrices[5637] = 75
ES.Data.SellPrices[6037] = 1250
ES.Data.SellPrices[6048] = 100
ES.Data.SellPrices[6217] = 24
ES.Data.SellPrices[6218] = 24
ES.Data.SellPrices[6338] = 125
ES.Data.SellPrices[6339] = 24
ES.Data.SellPrices[6370] = 10
ES.Data.SellPrices[6371] = 12
ES.Data.SellPrices[7067] = 400
ES.Data.SellPrices[7068] = 400
ES.Data.SellPrices[7075] = 400
ES.Data.SellPrices[7076] = 400
ES.Data.SellPrices[7077] = 400
ES.Data.SellPrices[7078] = 400
ES.Data.SellPrices[7079] = 400
ES.Data.SellPrices[7080] = 400
ES.Data.SellPrices[7081] = 400
ES.Data.SellPrices[7082] = 400
ES.Data.SellPrices[7392] = 200
ES.Data.SellPrices[7909] = 1000
ES.Data.SellPrices[7971] = 1000
ES.Data.SellPrices[7972] = 400
ES.Data.SellPrices[8151] = 250
ES.Data.SellPrices[8152] = 500
ES.Data.SellPrices[8153] = 5
ES.Data.SellPrices[8170] = 500
ES.Data.SellPrices[8831] = 300
ES.Data.SellPrices[8838] = 60
ES.Data.SellPrices[8925] = 125
ES.Data.SellPrices[9224] = 700
ES.Data.SellPrices[10308] = 112
ES.Data.SellPrices[10938] = 1
ES.Data.SellPrices[10939] = 1
ES.Data.SellPrices[10940] = 1
ES.Data.SellPrices[10978] = 1
ES.Data.SellPrices[10998] = 1
ES.Data.SellPrices[11082] = 1
ES.Data.SellPrices[11083] = 1
ES.Data.SellPrices[11084] = 1
ES.Data.SellPrices[11128] = 500
ES.Data.SellPrices[11130] = 500
ES.Data.SellPrices[11134] = 1
ES.Data.SellPrices[11135] = 1
ES.Data.SellPrices[11137] = 1
ES.Data.SellPrices[11138] = 1
ES.Data.SellPrices[11139] = 1
ES.Data.SellPrices[11144] = 1000
ES.Data.SellPrices[11145] = 1250
ES.Data.SellPrices[11174] = 1
ES.Data.SellPrices[11175] = 1
ES.Data.SellPrices[11176] = 1
ES.Data.SellPrices[11177] = 1
ES.Data.SellPrices[11178] = 1
ES.Data.SellPrices[11287] = 110
ES.Data.SellPrices[11288] = 200
ES.Data.SellPrices[11289] = 450
ES.Data.SellPrices[11291] = 1125
ES.Data.SellPrices[11382] = 750
ES.Data.SellPrices[12359] = 600
ES.Data.SellPrices[12361] = 7000
ES.Data.SellPrices[12363] = 2000
ES.Data.SellPrices[12655] = 500
ES.Data.SellPrices[12803] = 500
ES.Data.SellPrices[12808] = 1000
ES.Data.SellPrices[12809] = 10000
ES.Data.SellPrices[12810] = 500
ES.Data.SellPrices[12811] = 20000
ES.Data.SellPrices[13467] = 250
ES.Data.SellPrices[13468] = 1000
ES.Data.SellPrices[13926] = 10000
ES.Data.SellPrices[14047] = 400
ES.Data.SellPrices[14343] = 1
ES.Data.SellPrices[14344] = 1
ES.Data.SellPrices[15407] = 500
ES.Data.SellPrices[16202] = 1
ES.Data.SellPrices[16203] = 1
ES.Data.SellPrices[16204] = 1
ES.Data.SellPrices[16206] = 1000
ES.Data.SellPrices[16207] = 1250
ES.Data.SellPrices[17034] = 50
ES.Data.SellPrices[17035] = 100
ES.Data.SellPrices[18256] = 1500
ES.Data.SellPrices[18512] = 4000
ES.Data.SellPrices[20725] = 1
ES.Data.SellPrices[20744] = 100
ES.Data.SellPrices[20745] = 500
ES.Data.SellPrices[20746] = 1000
ES.Data.SellPrices[20747] = 1000
ES.Data.SellPrices[20748] = 1000
ES.Data.SellPrices[20749] = 1000
ES.Data.SellPrices[20750] = 1000
ES.Data.SellPrices[217287] = 600
ES.Data.SellPrices[220606] = 11850
ES.Data.SellPrices[220792] = 150
ES.Data.SellPrices[228980] = 400
ES.Data.SellPrices[232611] = 1000
ES.Data.SellPrices[247786] = 1
ES.Data.SellPrices[247789] = 5
ES.Data.SellPrices[248819] = 3000
ES.Data.SellPrices[248820] = 15000
ES.Data.SellPrices[248822] = 1500
ES.Data.SellPrices[249144] = 1000
ES.Data.SellPrices[249232] = 2000
ES.Data.SellPrices[249234] = 1500
ES.Data.SellPrices[249237] = 2500
ES.Data.SellPrices[249274] = 250
ES.Data.SellPrices[249385] = 5263
ES.Data.SellPrices[249391] = 100
ES.Data.SellPrices[249392] = 601
ES.Data.SellPrices[249393] = 601
ES.Data.SellPrices[249394] = 499
ES.Data.SellPrices[249395] = 496
ES.Data.SellPrices[249396] = 499
ES.Data.SellPrices[249397] = 450
ES.Data.SellPrices[249398] = 499
ES.Data.SellPrices[249399] = 30
ES.Data.SellPrices[249409] = 75
ES.Data.SellPrices[249410] = 125
ES.Data.SellPrices[249424] = 95
ES.Data.SellPrices[249425] = 250
ES.Data.SellPrices[249430] = 250
ES.Data.SellPrices[249431] = 375
ES.Data.SellPrices[249432] = 250
ES.Data.SellPrices[249441] = 2001
ES.Data.SellPrices[249442] = 2655
ES.Data.SellPrices[249443] = 4752
ES.Data.SellPrices[249453] = 601
ES.Data.SellPrices[249454] = 601
ES.Data.SellPrices[249455] = 2156
ES.Data.SellPrices[249456] = 2156
ES.Data.SellPrices[249469] = 1500
ES.Data.SellPrices[249470] = 1500
ES.Data.SellPrices[249473] = 1500
ES.Data.SellPrices[249726] = 3000
ES.Data.SellPrices[279246] = 13687
ES.Data.SellPrices[279247] = 18929
ES.Data.SellPrices[279248] = 18929
ES.Data.SellPrices[279249] = 18929
ES.Data.SellPrices[279250] = 18929
ES.Data.SellPrices[279251] = 18929

-- Nombre de cada objeto (inglés, del cliente): se muestra mientras el juego no lo ha cargado
ES.Data.ItemNames = ES.Data.ItemNames or {}
ES.Data.ItemNames[1210] = "Shadowgem"
ES.Data.ItemNames[2289] = "Scroll of Strength II"
ES.Data.ItemNames[2772] = "Iron Ore"
ES.Data.ItemNames[2775] = "Silver Ore"
ES.Data.ItemNames[3013] = "Scroll of Protection"
ES.Data.ItemNames[3356] = "Kingsblood"
ES.Data.ItemNames[3371] = "Empty Vial"
ES.Data.ItemNames[3372] = "Leaded Vial"
ES.Data.ItemNames[3819] = "Wintersbite"
ES.Data.ItemNames[3829] = "Frost Oil"
ES.Data.ItemNames[4470] = "Simple Wood"
ES.Data.ItemNames[4605] = "Red-speckled Mushroom"
ES.Data.ItemNames[4625] = "Firebloom"
ES.Data.ItemNames[5500] = "Iridescent Pearl"
ES.Data.ItemNames[5637] = "Large Fang"
ES.Data.ItemNames[6037] = "Truesilver Bar"
ES.Data.ItemNames[6048] = "Shadow Protection Potion"
ES.Data.ItemNames[6217] = "Copper Rod"
ES.Data.ItemNames[6218] = "Runed Copper Rod"
ES.Data.ItemNames[6338] = "Silver Rod"
ES.Data.ItemNames[6339] = "Runed Silver Rod"
ES.Data.ItemNames[6370] = "Blackmouth Oil"
ES.Data.ItemNames[6371] = "Fire Oil"
ES.Data.ItemNames[7067] = "Elemental Earth"
ES.Data.ItemNames[7068] = "Elemental Fire"
ES.Data.ItemNames[7075] = "Core of Earth"
ES.Data.ItemNames[7076] = "Essence of Earth"
ES.Data.ItemNames[7077] = "Heart of Fire"
ES.Data.ItemNames[7078] = "Essence of Fire"
ES.Data.ItemNames[7079] = "Globe of Water"
ES.Data.ItemNames[7080] = "Essence of Water"
ES.Data.ItemNames[7081] = "Breath of Wind"
ES.Data.ItemNames[7082] = "Essence of Air"
ES.Data.ItemNames[7392] = "Green Whelp Scale"
ES.Data.ItemNames[7909] = "Aquamarine"
ES.Data.ItemNames[7971] = "Black Pearl"
ES.Data.ItemNames[7972] = "Ichor of Undeath"
ES.Data.ItemNames[8151] = "Flask of Mojo"
ES.Data.ItemNames[8152] = "Flask of Big Mojo"
ES.Data.ItemNames[8153] = "Wildvine"
ES.Data.ItemNames[8170] = "Rugged Leather"
ES.Data.ItemNames[8831] = "Purple Lotus"
ES.Data.ItemNames[8838] = "Sungrass"
ES.Data.ItemNames[8925] = "Crystal Vial"
ES.Data.ItemNames[9224] = "Potion of Demon Slaying"
ES.Data.ItemNames[10308] = "Scroll of Intellect IV"
ES.Data.ItemNames[10938] = "Lesser Magic Essence"
ES.Data.ItemNames[10939] = "Greater Magic Essence"
ES.Data.ItemNames[10940] = "Strange Dust"
ES.Data.ItemNames[10978] = "Small Glimmering Shard"
ES.Data.ItemNames[10998] = "Lesser Astral Essence"
ES.Data.ItemNames[11082] = "Greater Astral Essence"
ES.Data.ItemNames[11083] = "Soul Dust"
ES.Data.ItemNames[11084] = "Large Glimmering Shard"
ES.Data.ItemNames[11128] = "Golden Rod"
ES.Data.ItemNames[11130] = "Runed Golden Rod"
ES.Data.ItemNames[11134] = "Lesser Mystic Essence"
ES.Data.ItemNames[11135] = "Greater Mystic Essence"
ES.Data.ItemNames[11137] = "Vision Dust"
ES.Data.ItemNames[11138] = "Small Glowing Shard"
ES.Data.ItemNames[11139] = "Large Glowing Shard"
ES.Data.ItemNames[11144] = "Truesilver Rod"
ES.Data.ItemNames[11145] = "Runed Truesilver Rod"
ES.Data.ItemNames[11174] = "Lesser Nether Essence"
ES.Data.ItemNames[11175] = "Greater Nether Essence"
ES.Data.ItemNames[11176] = "Dream Dust"
ES.Data.ItemNames[11177] = "Small Radiant Shard"
ES.Data.ItemNames[11178] = "Large Radiant Shard"
ES.Data.ItemNames[11287] = "Lesser Magic Wand"
ES.Data.ItemNames[11288] = "Greater Magic Wand"
ES.Data.ItemNames[11289] = "Lesser Mystic Wand"
ES.Data.ItemNames[11291] = "Star Wood"
ES.Data.ItemNames[11382] = "Blood of the Mountain"
ES.Data.ItemNames[11754] = "Black Diamond"
ES.Data.ItemNames[12359] = "Thorium Bar"
ES.Data.ItemNames[12361] = "Blue Sapphire"
ES.Data.ItemNames[12363] = "Arcane Crystal"
ES.Data.ItemNames[12655] = "Enchanted Thorium Bar"
ES.Data.ItemNames[12735] = "Frayed Abomination Stitching"
ES.Data.ItemNames[12753] = "Skin of Shadow"
ES.Data.ItemNames[12803] = "Living Essence"
ES.Data.ItemNames[12808] = "Essence of Undeath"
ES.Data.ItemNames[12809] = "Guardian Stone"
ES.Data.ItemNames[12810] = "Enchanted Leather"
ES.Data.ItemNames[12811] = "Righteous Orb"
ES.Data.ItemNames[12938] = "Blood of Heroes"
ES.Data.ItemNames[13180] = "Stratholme Holy Water"
ES.Data.ItemNames[13467] = "Icecap"
ES.Data.ItemNames[13468] = "Black Lotus"
ES.Data.ItemNames[13926] = "Golden Pearl"
ES.Data.ItemNames[14047] = "Runecloth"
ES.Data.ItemNames[14343] = "Small Brilliant Shard"
ES.Data.ItemNames[14344] = "Large Brilliant Shard"
ES.Data.ItemNames[15407] = "Cured Rugged Hide"
ES.Data.ItemNames[16202] = "Lesser Eternal Essence"
ES.Data.ItemNames[16203] = "Greater Eternal Essence"
ES.Data.ItemNames[16204] = "Illusion Dust"
ES.Data.ItemNames[16206] = "Arcanite Rod"
ES.Data.ItemNames[16207] = "Runed Arcanite Rod"
ES.Data.ItemNames[17034] = "Maple Seed"
ES.Data.ItemNames[17035] = "Stranglethorn Seed"
ES.Data.ItemNames[18256] = "Imbued Vial"
ES.Data.ItemNames[18512] = "Larval Acid"
ES.Data.ItemNames[20725] = "Nexus Crystal"
ES.Data.ItemNames[20744] = "Minor Wizard Oil"
ES.Data.ItemNames[20745] = "Minor Mana Oil"
ES.Data.ItemNames[20746] = "Lesser Wizard Oil"
ES.Data.ItemNames[20747] = "Lesser Mana Oil"
ES.Data.ItemNames[20748] = "Brilliant Mana Oil"
ES.Data.ItemNames[20749] = "Brilliant Wizard Oil"
ES.Data.ItemNames[20750] = "Wizard Oil"
ES.Data.ItemNames[217287] = "Greater Mystic Wand"
ES.Data.ItemNames[217308] = "Enchanted Sigil: Innovation"
ES.Data.ItemNames[220606] = "Idol of the Dream"
ES.Data.ItemNames[220792] = "Scroll of Spatial Mending"
ES.Data.ItemNames[228175] = "Libram of Holy Alacrity"
ES.Data.ItemNames[228176] = "Totem of Thunder"
ES.Data.ItemNames[228978] = "Enchanted Sigil: Flowing Waters"
ES.Data.ItemNames[228980] = "Conductive Shield Coating"
ES.Data.ItemNames[232611] = "Magnificent Trollshine"
ES.Data.ItemNames[247786] = "Mote of Magic"
ES.Data.ItemNames[247789] = "Novice's Practice Wand"
ES.Data.ItemNames[248819] = "Fel Crystal"
ES.Data.ItemNames[248820] = "Torbernite"
ES.Data.ItemNames[248822] = "Death Lotus"
ES.Data.ItemNames[249144] = "Twisted Nether Wand"
ES.Data.ItemNames[249232] = "Lesser Eternal Wand"
ES.Data.ItemNames[249234] = "Dreambough Wand"
ES.Data.ItemNames[249237] = "Greater Eternal Wand"
ES.Data.ItemNames[249274] = "Stranglevine"
ES.Data.ItemNames[249385] = "Brilliant Wand"
ES.Data.ItemNames[249391] = "Pyrite"
ES.Data.ItemNames[249392] = "Glimmering Staff"
ES.Data.ItemNames[249393] = "Soulstaff"
ES.Data.ItemNames[249394] = "Orb of Mystic Insight"
ES.Data.ItemNames[249395] = "Orb of Souls"
ES.Data.ItemNames[249396] = "Mystic Mushroom"
ES.Data.ItemNames[249397] = "Tenets of the Silver Hand"
ES.Data.ItemNames[249398] = "Polished Driftwood Icon"
ES.Data.ItemNames[249399] = "Frilled Lichen"
ES.Data.ItemNames[249409] = "Cerulean Dye"
ES.Data.ItemNames[249410] = "Sulfuric Acid"
ES.Data.ItemNames[249424] = "Rosecap"
ES.Data.ItemNames[249425] = "Bauxite"
ES.Data.ItemNames[249430] = "Magenta Dye"
ES.Data.ItemNames[249431] = "Viridian Dye"
ES.Data.ItemNames[249432] = "Sandpaper"
ES.Data.ItemNames[249441] = "Talons of Wrath"
ES.Data.ItemNames[249442] = "Libram of Invocation"
ES.Data.ItemNames[249443] = "Totem of Ancestral Protection"
ES.Data.ItemNames[249453] = "Radiant Staff"
ES.Data.ItemNames[249454] = "Dreamstaff"
ES.Data.ItemNames[249455] = "Truesilver Conduit"
ES.Data.ItemNames[249456] = "Twisting Essence Jar"
ES.Data.ItemNames[249469] = "Frozen Heart of the Mountain"
ES.Data.ItemNames[249470] = "Molten Heart of the Mountain"
ES.Data.ItemNames[249473] = "Dormant Heart of the Mountain"
ES.Data.ItemNames[249726] = "Azerothium Bar"
ES.Data.ItemNames[274030] = "Malleable Essence of Nature"
ES.Data.ItemNames[279246] = "Torch of Light"
ES.Data.ItemNames[279247] = "Steadfast Libram"
ES.Data.ItemNames[279248] = "Libram of Infusion"
ES.Data.ItemNames[279249] = "Totem of Urgency"
ES.Data.ItemNames[279250] = "Idol of Swiftness"
ES.Data.ItemNames[279251] = "Idol of the Ursine Twins"
ES.Data.ItemNames[279976] = "Enchanted Lute"
ES.Data.ItemNames[279985] = "Arcane Salvager"

-- Material -> profesión de recolección que lo consigue (393 Desuello, 182 Herboristería, 186 Minería).
-- Sin uso por ahora: reservado para la vía "Vender en bruto" de Ganar dinero (docs/PLAN.md, G1).
ES.Data.GatheredBy = ES.Data.GatheredBy or {}
ES.Data.GatheredBy[2772] = 186
ES.Data.GatheredBy[2775] = 186
ES.Data.GatheredBy[3356] = 182
ES.Data.GatheredBy[3819] = 182
ES.Data.GatheredBy[4625] = 182
ES.Data.GatheredBy[7392] = 393
ES.Data.GatheredBy[8153] = 182
ES.Data.GatheredBy[8170] = 393
ES.Data.GatheredBy[8831] = 182
ES.Data.GatheredBy[8838] = 182
ES.Data.GatheredBy[12359] = 186
ES.Data.GatheredBy[12809] = 186
ES.Data.GatheredBy[13467] = 182
ES.Data.GatheredBy[13468] = 182
ES.Data.GatheredBy[248822] = 182
ES.Data.GatheredBy[249274] = 182
ES.Data.GatheredBy[249391] = 186
ES.Data.GatheredBy[249399] = 182
ES.Data.GatheredBy[249424] = 182
ES.Data.GatheredBy[249425] = 186
ES.Data.GatheredBy[249726] = 186

```

---

## Engineering

```lua
-- Generado por tools/gen_profession.py (Engineering). No editar a mano.
-- Datos: cliente de WoW Forever (wago.tools DB2), instructores de CMaNGOS classic-db, vendedores de QuestieDB.
local _, ES = ...
ES.Data = ES.Data or {}

-- t = { naranja, amarilla, verde, gris }; fee/train = precio y habilidad del instructor
-- (sin fee = se aprende de pergamino: de dónde sale, en Data/Sources.lua; scrollPrice = su precio si lo vende un PNJ)
-- rep = { facción, nivel } que pide el pergamino para aprenderla (5 amistoso, 6 honorable, 7 venerado, 8 exaltado)
-- r = { {itemID, cantidad} }; out = { itemID, cantidad }
-- sq / oq = calidad del pergamino / de lo fabricado (0 pobre, 1 común, 2 poco común, 3 raro, 4 épico)
-- faction = bando que puede aprenderla, si solo es de uno
-- bop = lo fabricado se liga al recogerlo: no se puede vender en la AH (sí al vendedor)
-- favor / favorRep = se compra con Merchant's Favor en el campamento de tu bando, y la reputación que pide
-- train ajustado a Forever: nivel de Classic menos lo que Forever bajó la amarilla de esa receta
-- basic = se aprende sola al coger la profesión; trainer = de instructor sin precio conocido
--   (receta nueva de Forever que no está en CMaNGOS: se aprende al ponerse amarilla)
ES.Data.Engineering = {
  skillLine = 202,
  ranks = { -- { tope, precio, habilidad requerida, nivel de personaje }
    { 150, 450, 50, 10 },
    { 225, 4500, 125, 20 },
    { 300, 45000, 200, 35 },
  },
  -- { PNJ instructor, rangos que enseña: 1 aprendiz (75), 2 oficial (150), 4 experto (225), 8 artesano (300) }
  trainers = { { 1676, 2 }, { 1702, 1 }, { 2857, 1 }, { 3290, 1 }, { 3412, 2 }, { 3494, 1 }, { 4586, 1 }, { 5174, 4 }, { 5518, 2 }, { 8736, 8 }, { 10993, 1 }, { 11017, 4 }, { 11025, 1 }, { 11026, 1 }, { 11028, 1 }, { 11029, 2 }, { 11031, 2 }, { 11037, 1 }, { 249235, 8 }, { 251684, 1 } },
  recipes = {
    [3918] = { name = "Rough Blasting Powder", t = { 1, 20, 30, 40 }, basic = true, r = { { 2835, 1 } }, out = { 4357, 1 }, oq = 1 },
    [3919] = { name = "Rough Dynamite", t = { 1, 30, 45, 60 }, basic = true, r = { { 4357, 1 }, { 2589, 1 } }, out = { 4358, 2 }, oq = 1 },
    [3920] = { name = "Crafted Light Shot", t = { 1, 30, 45, 60 }, basic = true, r = { { 4357, 1 }, { 2840, 1 } }, out = { 8067, 200 }, oq = 1 },
    [3922] = { name = "Handful of Copper Bolts", t = { 1, 45, 52, 60 }, fee = 115, train = 30, r = { { 2840, 1 } }, tool = 162, out = { 4359, 1 }, oq = 1 },
    [3923] = { name = "Rough Copper Bomb", t = { 1, 60, 75, 90 }, fee = 130, train = 30, r = { { 2840, 1 }, { 4359, 1 }, { 4357, 2 }, { 2589, 1 } }, tool = 162, out = { 4360, 2 }, oq = 1 },
    [3924] = { name = "Copper Tube", t = { 1, 80, 95, 110 }, fee = 150, train = 50, r = { { 2840, 2 }, { 2880, 1 } }, tool = 162, out = { 4361, 1 }, oq = 1 },
    [3925] = { name = "Rough Boomstick", t = { 1, 80, 95, 110 }, fee = 150, train = 50, r = { { 4361, 1 }, { 4359, 1 }, { 4399, 1 } }, tool = 162, out = { 4362, 1 }, oq = 2 },
    [3926] = { name = "Copper Modulator", t = { 1, 95, 110, 125 }, fee = 225, train = 65, r = { { 4359, 2 }, { 2840, 1 }, { 2589, 2 } }, tool = 162, tool2 = 14, out = { 4363, 1 }, oq = 1 },
    [3928] = { name = "Mechanical Squirrel", t = { 1, 105, 120, 135 }, scroll = 4408, train = 75, sq = 2, r = { { 4363, 1 }, { 4359, 1 }, { 2840, 1 }, { 774, 2 } }, tool = 162, tool2 = 14, out = { 4401, 1 }, oq = 1 },
    [3929] = { name = "Coarse Blasting Powder", t = { 1, 85, 90, 95 }, fee = 250, train = 75, r = { { 2836, 1 } }, out = { 4364, 1 }, oq = 1 },
    [3930] = { name = "Crafted Heavy Shot", t = { 1, 85, 90, 95 }, fee = 250, train = 75, r = { { 4364, 1 }, { 2840, 1 } }, out = { 8068, 200 }, oq = 1 },
    [3931] = { name = "Coarse Dynamite", t = { 1, 90, 97, 105 }, fee = 250, train = 75, r = { { 4364, 3 }, { 2589, 1 } }, out = { 4365, 2 }, oq = 1 },
    [3932] = { name = "Target Dummy", t = { 1, 115, 130, 145 }, fee = 300, train = 85, r = { { 4363, 1 }, { 4359, 2 }, { 2841, 1 }, { 2592, 1 } }, tool = 162, tool2 = 14, out = { 4366, 1 }, oq = 1 },
    [3933] = { name = "Small Seaforium Charge", t = { 1, 130, 145, 160 }, scroll = 4409, train = 100, sq = 2, r = { { 4364, 2 }, { 4363, 1 }, { 2318, 1 }, { 159, 1 } }, out = { 4367, 1 }, oq = 1 },
    [3934] = { name = "Flying Tiger Goggles", t = { 1, 130, 145, 160 }, fee = 400, train = 100, r = { { 2318, 6 }, { 818, 2 } }, tool2 = 14, out = { 4368, 1 }, oq = 2 },
    [3936] = { name = "Deadly Blunderbuss", t = { 1, 130, 142, 155 }, fee = 420, train = 105, r = { { 4361, 2 }, { 4359, 4 }, { 4399, 1 }, { 2319, 2 } }, tool = 162, tool2 = 14, out = { 4369, 1 }, oq = 2 },
    [3937] = { name = "Large Copper Bomb", t = { 1, 105, 130, 155 }, fee = 450, train = 105, r = { { 2840, 3 }, { 4364, 4 }, { 4404, 1 } }, tool = 162, out = { 4370, 3 }, oq = 1 },
    [3938] = { name = "Bronze Tube", t = { 1, 105, 130, 155 }, fee = 450, train = 105, r = { { 2841, 2 }, { 2880, 1 } }, tool = 162, out = { 4371, 1 }, oq = 1 },
    [3939] = { name = "Lovingly Crafted Boomstick", t = { 1, 145, 157, 170 }, scroll = 13309, train = 120, scrollPrice = 1000, sq = 1, r = { { 4371, 2 }, { 4359, 2 }, { 4400, 1 }, { 1206, 3 } }, tool = 162, tool2 = 14, out = { 4372, 1 }, oq = 2 },
    [3940] = { name = "Shadow Goggles", t = { 1, 145, 157, 170 }, scroll = 4410, train = 120, sq = 2, r = { { 2319, 4 }, { 1210, 2 } }, out = { 4373, 1 }, oq = 2 },
    [3941] = { name = "Small Bronze Bomb", t = { 1, 120, 145, 170 }, fee = 500, train = 120, r = { { 4364, 4 }, { 2841, 2 }, { 4404, 1 }, { 2592, 1 } }, tool = 162, out = { 4374, 2 }, oq = 1 },
    [3942] = { name = "Whirring Bronze Gizmo", t = { 1, 125, 150, 175 }, fee = 500, train = 125, r = { { 2841, 2 }, { 2592, 1 } }, tool = 162, tool2 = 14, out = { 4375, 1 }, oq = 1 },
    [3944] = { name = "Flame Deflector", t = { 1, 125, 150, 175 }, scroll = 4411, train = 125, sq = 2, r = { { 4375, 1 }, { 4402, 1 } }, tool = 162, tool2 = 14, out = { 4376, 1 }, oq = 1 },
    [3945] = { name = "Heavy Blasting Powder", t = { 1, 125, 135, 145 }, fee = 500, train = 125, r = { { 2838, 1 } }, out = { 4377, 1 }, oq = 1 },
    [3946] = { name = "Heavy Dynamite", t = { 1, 125, 135, 145 }, fee = 500, train = 125, r = { { 4377, 2 }, { 2592, 1 } }, out = { 4378, 3 }, oq = 1 },
    [3947] = { name = "Crafted Solid Shot", t = { 1, 125, 135, 145 }, fee = 300, train = 125, r = { { 4377, 1 }, { 2841, 1 } }, out = { 8069, 200 }, oq = 1 },
    [3949] = { name = "Silver-plated Shotgun", t = { 1, 155, 167, 180 }, fee = 550, train = 130, r = { { 4371, 2 }, { 4375, 2 }, { 4400, 1 }, { 2842, 3 } }, out = { 4379, 1 }, oq = 2 },
    [3950] = { name = "Big Bronze Bomb", t = { 1, 140, 165, 190 }, fee = 600, train = 140, r = { { 4377, 2 }, { 2841, 3 }, { 4404, 1 } }, tool = 162, tool2 = 14, out = { 4380, 3 }, oq = 1 },
    [3952] = { name = "Minor Recombobulator", t = { 1, 165, 177, 190 }, scroll = 14639, train = 140, scrollPrice = 1500, sq = 1, r = { { 4371, 1 }, { 4375, 2 }, { 2319, 2 }, { 1206, 1 } }, out = { 4381, 1 }, oq = 2 },
    [3953] = { name = "Bronze Framework", t = { 1, 145, 170, 195 }, fee = 600, train = 145, r = { { 2841, 2 }, { 2319, 1 }, { 2592, 1 } }, out = { 4382, 1 }, oq = 1 },
    [3954] = { name = "Moonsight Rifle", t = { 1, 170, 182, 195 }, scroll = 4412, train = 145, sq = 2, r = { { 4371, 3 }, { 4375, 3 }, { 4400, 1 }, { 1705, 2 } }, tool = 162, tool2 = 14, out = { 4383, 1 }, oq = 2 },
    [3955] = { name = "Explosive Sheep", t = { 1, 175, 187, 200 }, fee = 750, train = 150, r = { { 4382, 1 }, { 4375, 1 }, { 4377, 2 }, { 2592, 2 } }, tool = 162, tool2 = 14, out = { 4384, 1 }, oq = 1 },
    [3956] = { name = "Green Tinted Goggles", t = { 1, 175, 187, 200 }, fee = 750, train = 150, r = { { 2319, 4 }, { 1206, 2 }, { 4368, 1 } }, tool2 = 14, out = { 4385, 1 }, oq = 2 },
    [3957] = { name = "Ice Deflector", t = { 1, 175, 185, 195 }, scroll = 13308, train = 155, scrollPrice = 1800, sq = 1, r = { { 4375, 1 }, { 3829, 1 } }, tool = 162, tool2 = 14, out = { 4386, 1 }, oq = 1 },
    [3958] = { name = "Iron Strut", t = { 1, 160, 170, 180 }, fee = 800, train = 160, r = { { 3575, 2 } }, tool = 162, out = { 4387, 1 }, oq = 1 },
    [3959] = { name = "Discombobulator Ray", t = { 1, 180, 190, 200 }, scroll = 4413, train = 160, sq = 2, r = { { 4375, 3 }, { 4306, 2 }, { 1529, 1 }, { 4371, 1 } }, tool = 162, tool2 = 14, out = { 4388, 1 }, oq = 1 },
    [3960] = { name = "Portable Bronze Mortar", t = { 1, 185, 195, 205 }, scroll = 4414, train = 165, sq = 2, r = { { 4371, 4 }, { 4387, 1 }, { 4377, 4 }, { 2319, 4 } }, tool = 162, tool2 = 14, out = { 4403, 1 }, oq = 1 },
    [3961] = { name = "Gyrochronatom", t = { 1, 170, 190, 210 }, fee = 900, train = 170, r = { { 3575, 1 }, { 10558, 1 } }, tool = 162, tool2 = 14, out = { 4389, 1 }, oq = 1 },
    [3962] = { name = "Iron Grenade", t = { 1, 175, 195, 215 }, fee = 1000, train = 175, r = { { 3575, 1 }, { 4377, 1 }, { 4306, 1 } }, tool = 162, out = { 4390, 3 }, oq = 1 },
    [3963] = { name = "Compact Harvest Reaper Kit", t = { 1, 175, 195, 215 }, fee = 1000, train = 175, r = { { 4387, 2 }, { 4382, 1 }, { 4389, 2 }, { 4234, 4 } }, tool = 162, tool2 = 14, out = { 4391, 1 }, oq = 1 },
    [3965] = { name = "Advanced Target Dummy", t = { 1, 185, 205, 225 }, fee = 1200, train = 185, r = { { 4387, 1 }, { 4382, 1 }, { 4389, 1 }, { 4234, 4 } }, tool = 162, tool2 = 14, out = { 4392, 1 }, oq = 1 },
    [3966] = { name = "Craftsman's Monocle", t = { 1, 205, 215, 225 }, scroll = 4415, train = 185, sq = 3, r = { { 4234, 6 }, { 3864, 2 } }, tool = 14, tool2 = 15, out = { 4393, 1 }, oq = 2 },
    [3967] = { name = "Big Iron Bomb", t = { 1, 190, 210, 230 }, fee = 1400, train = 190, r = { { 3575, 3 }, { 4377, 3 }, { 4404, 1 } }, tool = 162, tool2 = 14, out = { 4394, 2 }, oq = 1 },
    [3968] = { name = "Goblin Land Mine", t = { 1, 215, 225, 235 }, scroll = 4416, train = 195, sq = 2, r = { { 4377, 3 }, { 3575, 2 }, { 4389, 1 } }, tool = 162, tool2 = 14, out = { 4395, 1 }, oq = 1 },
    [3969] = { name = "Mechanical Dragonling", t = { 1, 220, 230, 240 }, scroll = 13311, train = 200, scrollPrice = 10000, sq = 1, r = { { 4382, 1 }, { 4387, 4 }, { 4389, 4 }, { 3864, 2 }, { 7191, 1 } }, tool = 162, tool2 = 14, out = { 4396, 1 }, oq = 1 },
    [3971] = { name = "Gnomish Cloaking Device", t = { 1, 220, 230, 240 }, scroll = 7742, train = 200, scrollPrice = 2400, sq = 1, r = { { 4389, 4 }, { 1529, 2 }, { 1705, 2 }, { 3864, 2 }, { 7191, 1 } }, tool = 162, tool2 = 14, out = { 4397, 1 }, oq = 1 },
    [3972] = { name = "Large Seaforium Charge", t = { 1, 200, 220, 240 }, scroll = 4417, train = 200, sq = 2, r = { { 10505, 2 }, { 4234, 2 }, { 159, 1 } }, out = { 4398, 1 }, oq = 1 },
    [3973] = { name = "Silver Contact", t = { 1, 110, 125, 140 }, fee = 300, train = 90, r = { { 2842, 1 } }, out = { 4404, 5 }, oq = 1 },
    [3977] = { name = "Crude Scope", t = { 1, 90, 105, 120 }, fee = 200, train = 60, r = { { 4361, 1 }, { 774, 1 }, { 4359, 1 } }, tool = 14, out = { 4405, 1 }, oq = 1 },
    [3978] = { name = "Standard Scope", t = { 1, 135, 147, 160 }, fee = 475, train = 110, r = { { 4371, 1 }, { 1206, 1 } }, tool = 14, out = { 4406, 1 }, oq = 1 },
    [3979] = { name = "Accurate Scope", t = { 1, 200, 210, 220 }, scroll = 13310, train = 180, scrollPrice = 2000, sq = 1, r = { { 4371, 1 }, { 1529, 1 }, { 3864, 1 } }, tool = 14, tool2 = 15, out = { 4407, 1 }, oq = 1 },
    [6458] = { name = "Ornate Spyglass", t = { 1, 160, 172, 185 }, fee = 400, train = 135, r = { { 4371, 2 }, { 4375, 2 }, { 4363, 1 }, { 1206, 1 } }, out = { 5507, 1 }, oq = 1 },
    [7430] = { name = "Arclight Spanner", t = { 1, 70, 80, 90 }, fee = 150, train = 50, r = { { 2840, 6 } }, tool = 162, out = { 6219, 1 }, oq = 1 },
    [8243] = { name = "Flash Bomb", t = { 1, 185, 205, 225 }, scroll = 6672, train = 185, sq = 2, r = { { 4611, 1 }, { 4377, 1 }, { 4306, 1 } }, out = { 4852, 1 }, oq = 1 },
    [8334] = { name = "Practice Lock", t = { 1, 115, 122, 130 }, fee = 300, train = 100, r = { { 2841, 1 }, { 4359, 2 }, { 2880, 1 } }, tool = 162, out = { 6712, 1 }, oq = 1 },
    [8339] = { name = "EZ-Thro Dynamite", t = { 1, 115, 122, 130 }, scroll = 6716, train = 100, sq = 2, r = { { 4364, 3 }, { 2589, 1 }, { 260794, 1 } }, out = { 6714, 2 }, oq = 1 },
    [8895] = { name = "Goblin Rocket Boots", t = { 1, 245, 255, 265 }, fee = 2200, train = 225, spec = "Goblin", tr = { 8126, 8738, 260562 }, r = { { 10026, 1 }, { 10559, 2 }, { 4234, 4 }, { 9061, 2 }, { 10560, 1 } }, tool = 162, tool2 = 14, out = { 7189, 1 }, oq = 2 },
    [9269] = { name = "Gnomish Universal Remote", t = { 1, 150, 162, 175 }, scroll = 7560, train = 125, scrollPrice = 1200, sq = 1, r = { { 2841, 6 }, { 4375, 1 }, { 814, 2 }, { 818, 1 }, { 774, 1 } }, tool = 162, tool2 = 14, out = { 7506, 1 }, oq = 2 },
    [9271] = { name = "Aquadynamic Fish Attractor", t = { 1, 150, 160, 170 }, fee = 500, train = 150, r = { { 2841, 2 }, { 6530, 1 }, { 4364, 1 } }, out = { 6533, 3 }, oq = 1 },
    [9273] = { name = "Goblin Jumper Cables", t = { 1, 160, 180, 200 }, scroll = 7561, train = 165, scrollPrice = 2000, sq = 1, r = { { 3575, 6 }, { 4375, 2 }, { 814, 2 }, { 4306, 2 }, { 1210, 2 }, { 7191, 1 } }, out = { 7148, 1 }, oq = 1 },
    [12584] = { name = "Gold Power Core", t = { 1, 150, 170, 190 }, fee = 1000, train = 150, r = { { 3577, 1 } }, tool = 162, tool2 = 14, out = { 10558, 3 }, oq = 1 },
    [12585] = { name = "Solid Blasting Powder", t = { 1, 175, 185, 195 }, fee = 1000, train = 175, r = { { 7912, 2 } }, out = { 10505, 1 }, oq = 1 },
    [12586] = { name = "Solid Dynamite", t = { 1, 175, 185, 195 }, fee = 1000, train = 175, r = { { 10505, 1 }, { 4306, 1 } }, out = { 10507, 2 }, oq = 1 },
    [12587] = { name = "Bright-Eye Goggles", t = { 1, 195, 205, 215 }, scroll = 10601, train = 175, sq = 2, r = { { 4234, 6 }, { 3864, 2 } }, tool = 14, tool2 = 15, out = { 10499, 1 }, oq = 2 },
    [12589] = { name = "Mithril Tube", t = { 1, 195, 215, 235 }, fee = 1300, train = 195, r = { { 3860, 3 } }, tool = 162, out = { 10559, 1 }, oq = 1 },
    [12590] = { name = "Gyromatic Micro-Adjustor", t = { 1, 175, 195, 215 }, fee = 1000, train = 175, r = { { 3859, 4 } }, tool = 162, out = { 10498, 1 }, oq = 1 },
    [12591] = { name = "Unstable Trigger", t = { 1, 200, 220, 240 }, fee = 1500, train = 200, r = { { 3860, 1 }, { 4338, 1 }, { 10505, 1 } }, tool = 162, tool2 = 14, out = { 10560, 1 }, oq = 1 },
    [12594] = { name = "Fire Goggles", t = { 1, 225, 235, 245 }, fee = 1600, train = 205, r = { { 4385, 1 }, { 3864, 2 }, { 7068, 2 }, { 4234, 4 } }, tool = 14, tool2 = 15, out = { 10500, 1 }, oq = 2 },
    [12595] = { name = "Mithril Blunderbuss", t = { 1, 225, 235, 245 }, fee = 1600, train = 205, r = { { 10559, 1 }, { 10560, 1 }, { 4400, 1 }, { 3860, 4 }, { 7068, 2 } }, tool = 162, tool2 = 14, out = { 10508, 1 }, oq = 2 },
    [12596] = { name = "Hi-Impact Mithril Slugs", t = { 1, 210, 230, 250 }, fee = 1700, train = 210, r = { { 3860, 1 }, { 10505, 1 } }, tool = 162, out = { 10512, 200 }, oq = 2 },
    [12597] = { name = "Deadly Scope", t = { 1, 230, 240, 250 }, scroll = 10602, train = 210, scrollPrice = 3000, sq = 1, r = { { 10559, 1 }, { 7909, 2 }, { 4304, 2 } }, tool = 162, tool2 = 14, out = { 10546, 1 }, oq = 1 },
    [12599] = { name = "Mithril Casing", t = { 1, 215, 235, 255 }, fee = 1800, train = 215, r = { { 3860, 3 } }, tool = 162, tool2 = 14, out = { 10561, 1 }, oq = 1 },
    [12603] = { name = "Mithril Frag Bomb", t = { 1, 215, 235, 255 }, fee = 1800, train = 215, r = { { 10561, 1 }, { 10560, 1 }, { 10505, 1 } }, tool = 162, tool2 = 14, out = { 10514, 3 }, oq = 1 },
    [12607] = { name = "Catseye Ultra Goggles", t = { 1, 240, 250, 260 }, scroll = 10603, train = 220, sq = 2, r = { { 4304, 4 }, { 7909, 2 }, { 10592, 1 } }, tool = 14, tool2 = 15, out = { 10501, 1 }, oq = 2 },
    [12614] = { name = "Mithril Heavy-bore Rifle", t = { 1, 240, 250, 260 }, scroll = 10604, train = 220, sq = 2, r = { { 10559, 2 }, { 10560, 1 }, { 4400, 1 }, { 3860, 6 }, { 3864, 2 } }, tool = 162, tool2 = 14, out = { 10510, 1 }, oq = 2 },
    [12615] = { name = "Spellpower Goggles Xtreme", t = { 1, 245, 255, 265 }, scroll = 10605, train = 225, sq = 3, r = { { 4304, 4 }, { 7910, 2 } }, tool = 14, tool2 = 15, out = { 10502, 1 }, oq = 2 },
    [12616] = { name = "Parachute Cloak", t = { 1, 245, 255, 265 }, scroll = 10606, train = 225, sq = 2, r = { { 4339, 4 }, { 10285, 2 }, { 10560, 1 }, { 10505, 4 } }, tool = 14, tool2 = 15, out = { 10518, 1 }, oq = 2 },
    [12617] = { name = "Deepdive Helmet", t = { 1, 250, 260, 270 }, scroll = 10607, train = 230, scrollPrice = 3600, sq = 1, r = { { 3860, 8 }, { 10561, 1 }, { 6037, 1 }, { 818, 4 }, { 774, 4 } }, tool = 162, tool2 = 14, out = { 10506, 1 }, oq = 2 },
    [12618] = { name = "Rose Colored Goggles", t = { 1, 250, 260, 270 }, fee = 2200, train = 230, r = { { 4304, 6 }, { 7910, 2 } }, tool = 14, tool2 = 15, out = { 10503, 1 }, oq = 2 },
    [12619] = { name = "Hi-Explosive Bomb", t = { 1, 235, 255, 275 }, fee = 2400, train = 235, r = { { 10561, 2 }, { 10560, 1 }, { 10505, 2 } }, tool = 162, tool2 = 14, out = { 10562, 4 }, oq = 1 },
    [12620] = { name = "Sniper Scope", t = { 1, 260, 270, 280 }, scroll = 10608, train = 240, sq = 3, r = { { 10559, 1 }, { 7910, 1 }, { 6037, 2 } }, tool = 162, tool2 = 14, out = { 10548, 1 }, oq = 1 },
    [12621] = { name = "Mithril Gyro-Shot", t = { 1, 245, 265, 285 }, fee = 2800, train = 245, r = { { 3860, 2 }, { 10505, 2 } }, tool = 162, out = { 10513, 200 }, oq = 2 },
    [12622] = { name = "Green Lens", t = { 1, 265, 275, 285 }, fee = 2800, train = 245, r = { { 4304, 8 }, { 1529, 3 }, { 7909, 3 }, { 10286, 2 }, { 8153, 2 } }, tool = 14, tool2 = 15, out = { 10504, 1 }, oq = 3 },
    [12624] = { name = "Mithril Mechanical Dragonling", t = { 1, 270, 280, 290 }, scroll = 10609, train = 250, scrollPrice = 4000, sq = 1, r = { { 3860, 14 }, { 7077, 4 }, { 6037, 4 }, { 9060, 2 }, { 9061, 2 }, { 7910, 2 } }, tool = 162, tool2 = 14, out = { 10576, 1 }, oq = 1 },
    [12716] = { name = "Goblin Mortar", t = { 1, 225, 235, 245 }, r = { { 10559, 2 }, { 3860, 4 }, { 10505, 5 }, { 10558, 1 }, { 7068, 1 } }, tool = 162, tool2 = 14, out = { 10577, 1 }, oq = 1 },
    [12717] = { name = "Goblin Mining Helmet", t = { 1, 225, 235, 245 }, fee = 1500, train = 205, spec = "Goblin", tr = { 8126, 8738, 260562 }, r = { { 3860, 8 }, { 3864, 1 }, { 7067, 4 } }, tool = 162, tool2 = 14, out = { 10542, 1 }, oq = 2, bop = true },
    [12718] = { name = "Goblin Construction Helmet", t = { 1, 225, 235, 245 }, fee = 1500, train = 205, spec = "Goblin", tr = { 8126, 8738, 260562 }, r = { { 3860, 8 }, { 3864, 1 }, { 7068, 4 } }, tool = 162, tool2 = 14, out = { 10543, 1 }, oq = 2, bop = true },
    [12719] = { name = "Explosive Arrow", t = { 1, 210, 230, 250 }, r = { { 3030, 100 }, { 10505, 2 }, { 3860, 2 } }, tool = 14, tool2 = 15, out = { 10579, 100 }, oq = 3 },
    [12720] = { name = "Goblin \"Boom\" Box", t = { 1, 235, 245, 255 }, r = { { 10561, 1 }, { 10505, 2 }, { 10558, 1 }, { 3860, 2 } }, tool = 162, tool2 = 14, out = { 10580, 1 }, oq = 1 },
    [12722] = { name = "Goblin Radio", t = { 1, 240, 250, 260 }, r = { { 10561, 1 }, { 3860, 2 }, { 4389, 1 }, { 10560, 1 } }, tool = 162, tool2 = 14, out = { 10585, 1 }, oq = 1 },
    [12754] = { name = "The Big One", t = { 1, 235, 255, 275 }, fee = 2600, train = 235, spec = "Goblin", tr = { 8126, 8738, 260562 }, r = { { 10561, 1 }, { 9061, 1 }, { 10507, 6 }, { 10560, 1 } }, tool = 162, tool2 = 14, out = { 10586, 2 }, oq = 1 },
    [12755] = { name = "Goblin Bomb Dispenser", t = { 1, 230, 250, 270 }, fee = 2400, train = 230, spec = "Goblin", tr = { 8126, 8738, 260562 }, r = { { 10561, 2 }, { 10505, 4 }, { 6037, 6 }, { 10560, 1 }, { 4407, 2 } }, tool = 162, tool2 = 14, out = { 10587, 1 }, oq = 1, bop = true },
    [12758] = { name = "Goblin Rocket Helmet", t = { 1, 265, 275, 285 }, fee = 3000, train = 245, spec = "Goblin", tr = { 8126, 8738, 260562 }, r = { { 10543, 1 }, { 9061, 4 }, { 3860, 4 }, { 10560, 1 } }, tool = 162, tool2 = 14, out = { 10588, 1 }, oq = 2 },
    [12759] = { name = "Gnomish Death Ray", t = { 1, 260, 270, 280 }, fee = 2800, train = 240, spec = "Gnomish", tr = { 7406, 7944 }, r = { { 10559, 2 }, { 10560, 1 }, { 12808, 1 }, { 7972, 4 }, { 9060, 1 } }, tool = 162, tool2 = 14, out = { 10645, 1 }, oq = 1, bop = true },
    [12760] = { name = "Goblin Sapper Charge", t = { 1, 205, 225, 245 }, fee = 1500, train = 205, spec = "Goblin", tr = { 8126, 8738, 260562 }, r = { { 4338, 1 }, { 10505, 3 }, { 10560, 1 } }, out = { 10646, 1 }, oq = 1 },
    [12897] = { name = "Gnomish Goggles", t = { 1, 230, 240, 250 }, fee = 1500, train = 210, spec = "Gnomish", tr = { 7406, 7944 }, r = { { 10500, 1 }, { 10559, 1 }, { 10558, 2 }, { 8151, 2 }, { 4234, 2 } }, tool = 14, tool2 = 15, out = { 10545, 1 }, oq = 2, bop = true },
    [12899] = { name = "Gnomish Shrink Ray", t = { 1, 225, 235, 245 }, fee = 1500, train = 205, spec = "Gnomish", tr = { 7406, 7944 }, r = { { 10559, 1 }, { 10560, 1 }, { 3860, 4 }, { 8151, 4 }, { 1529, 2 } }, tool = 162, tool2 = 14, out = { 10716, 1 }, oq = 1 },
    [12900] = { name = "Mobile Alarm", t = { 1, 205, 225, 245 }, r = { { 10559, 1 }, { 10560, 1 }, { 3860, 4 } }, tool = 162, tool2 = 14, out = { 10719, 1 }, oq = 1 },
    [12902] = { name = "Gnomish Net-o-Matic Projector", t = { 1, 230, 240, 250 }, fee = 1800, train = 210, spec = "Gnomish", tr = { 7406, 7944 }, r = { { 10559, 1 }, { 10285, 2 }, { 4337, 4 }, { 10505, 2 }, { 3860, 4 } }, tool = 162, tool2 = 14, out = { 10720, 1 }, oq = 1 },
    [12903] = { name = "Gnomish Harm Prevention Belt", t = { 1, 235, 245, 255 }, fee = 2000, train = 215, spec = "Gnomish", tr = { 7406, 7944 }, r = { { 7387, 1 }, { 3860, 4 }, { 6037, 2 }, { 10560, 1 }, { 7909, 2 } }, tool = 162, tool2 = 14, out = { 10721, 1 }, oq = 2 },
    [12904] = { name = "Gnomish Ham Radio", t = { 1, 240, 250, 260 }, r = { { 10561, 1 }, { 3860, 2 }, { 4389, 1 }, { 10560, 1 } }, tool = 162, tool2 = 14, out = { 10723, 1 }, oq = 1 },
    [12905] = { name = "Gnomish Rocket Boots", t = { 1, 245, 255, 265 }, fee = 2200, train = 225, spec = "Gnomish", tr = { 7406, 7944 }, r = { { 10026, 1 }, { 10559, 2 }, { 4234, 4 }, { 10505, 8 }, { 4389, 4 } }, tool = 162, tool2 = 14, out = { 10724, 1 }, oq = 2 },
    [12906] = { name = "Gnomish Battle Chicken", t = { 1, 250, 260, 270 }, fee = 2400, train = 230, spec = "Gnomish", tr = { 7406, 7944 }, r = { { 10561, 1 }, { 6037, 6 }, { 3860, 6 }, { 9060, 2 }, { 10558, 1 }, { 1529, 2 } }, tool = 162, tool2 = 14, out = { 10725, 1 }, oq = 1, bop = true },
    [12907] = { name = "Gnomish Mind Control Cap", t = { 1, 255, 265, 275 }, fee = 2600, train = 235, spec = "Gnomish", tr = { 7406, 7944 }, r = { { 3860, 10 }, { 6037, 4 }, { 10558, 1 }, { 7910, 2 }, { 4338, 4 } }, tool = 162, tool2 = 14, out = { 10726, 1 }, oq = 2 },
    [12908] = { name = "Goblin Dragon Gun", t = { 1, 260, 270, 280 }, fee = 2800, train = 240, spec = "Goblin", tr = { 8126, 8738, 260562 }, r = { { 10559, 2 }, { 9061, 4 }, { 3860, 6 }, { 6037, 6 }, { 10560, 1 } }, tool = 162, tool2 = 14, out = { 10727, 1 }, oq = 1, bop = true },
    [15255] = { name = "Mechanical Repair Kit", t = { 1, 200, 220, 240 }, fee = 1500, train = 200, r = { { 3860, 1 }, { 4338, 1 }, { 10505, 1 } }, tool = 162, tool2 = 14, out = { 11590, 1 }, oq = 1 },
    [15628] = { name = "Pet Bombling", t = { 1, 205, 207, 210 }, scroll = 11828, train = 205, sq = 2, r = { { 4394, 1 }, { 7077, 1 }, { 7191, 1 }, { 3860, 6 } }, tool = 162, tool2 = 14, out = { 11825, 1 }, oq = 1 },
    [19567] = { name = "Salt Shaker", t = { 1, 270, 280, 290 }, fee = 4000, train = 250, r = { { 10561, 1 }, { 12359, 6 }, { 10558, 1 }, { 10560, 4 } }, tool = 162, out = { 15846, 1 }, oq = 1 },
    [19788] = { name = "Dense Blasting Powder", t = { 1, 250, 255, 260 }, fee = 4000, train = 250, r = { { 12365, 2 } }, out = { 15992, 1 }, oq = 1 },
    [19790] = { name = "Thorium Grenade", t = { 1, 280, 290, 300 }, scroll = 16041, train = 260, scrollPrice = 12000, sq = 1, r = { { 15994, 1 }, { 12359, 3 }, { 15992, 3 }, { 14047, 3 } }, tool = 162, out = { 15993, 3 }, oq = 1 },
    [19791] = { name = "Thorium Widget", t = { 1, 280, 290, 300 }, scroll = 16042, train = 260, scrollPrice = 12000, sq = 1, r = { { 12359, 3 }, { 14047, 1 } }, tool = 162, tool2 = 14, out = { 15994, 1 }, oq = 1 },
    [19792] = { name = "Thorium Rifle", t = { 1, 280, 290, 300 }, scroll = 16043, train = 260, sq = 2, r = { { 10559, 2 }, { 10561, 2 }, { 15994, 2 }, { 12359, 4 }, { 10546, 1 } }, tool = 162, tool2 = 14, out = { 15995, 1 }, oq = 2 },
    [19793] = { name = "Lifelike Mechanical Toad", t = { 1, 285, 295, 305 }, scroll = 16044, train = 265, sq = 2, r = { { 12803, 1 }, { 15994, 4 }, { 10558, 1 }, { 8170, 1 } }, tool = 162, tool2 = 14, out = { 15996, 1 }, oq = 1 },
    [19794] = { name = "Spellpower Goggles Xtreme Plus", t = { 1, 290, 300, 310 }, scroll = 16045, train = 270, sq = 2, r = { { 10502, 1 }, { 7910, 4 }, { 12810, 2 }, { 14047, 8 } }, tool = 14, tool2 = 15, out = { 15999, 1 }, oq = 2 },
    [19795] = { name = "Thorium Tube", t = { 1, 295, 305, 315 }, scroll = 16047, train = 275, scrollPrice = 16000, sq = 1, r = { { 12359, 6 } }, tool = 162, tool2 = 14, out = { 16000, 1 }, oq = 1 },
    [19796] = { name = "Dark Iron Rifle", t = { 1, 295, 305, 315 }, scroll = 16048, train = 275, sq = 2, r = { { 16000, 2 }, { 11371, 6 }, { 10546, 2 }, { 12361, 2 }, { 12799, 2 }, { 8170, 4 } }, tool = 162, tool2 = 14, out = { 16004, 1 }, oq = 3 },
    [19799] = { name = "Dark Iron Bomb", t = { 1, 305, 315, 325 }, scroll = 16049, train = 285, sq = 2, r = { { 15994, 2 }, { 11371, 1 }, { 15992, 3 }, { 14047, 3 } }, tool = 162, out = { 16005, 3 }, oq = 1 },
    [19800] = { name = "Thorium Shells", t = { 1, 305, 315, 325 }, scroll = 16051, train = 285, sq = 2, r = { { 12359, 2 }, { 15992, 1 } }, tool = 162, out = { 15997, 200 }, oq = 2 },
    [19814] = { name = "Masterwork Target Dummy", t = { 1, 295, 305, 315 }, scroll = 16046, train = 275, scrollPrice = 16000, sq = 1, r = { { 10561, 1 }, { 16000, 1 }, { 15994, 2 }, { 6037, 1 }, { 8170, 2 }, { 14047, 4 } }, tool = 162, tool2 = 14, out = { 16023, 1 }, oq = 1 },
    [19815] = { name = "Delicate Arcanite Converter", t = { 1, 305, 315, 325 }, scroll = 16050, train = 285, scrollPrice = 20000, sq = 1, r = { { 12360, 1 }, { 14227, 1 } }, tool = 162, tool2 = 14, out = { 16006, 1 }, oq = 1 },
    [19819] = { name = "Voice Amplification Modulator", t = { 1, 310, 320, 330 }, scroll = 16052, train = 290, sq = 2, r = { { 16006, 2 }, { 10558, 1 }, { 15994, 1 }, { 12799, 1 } }, tool = 162, tool2 = 14, out = { 16009, 1 }, oq = 2 },
    [19825] = { name = "Master Engineer's Goggles", t = { 1, 310, 320, 330 }, scroll = 16053, train = 290, sq = 2, r = { { 10500, 1 }, { 12364, 2 }, { 12810, 4 } }, tool = 14, tool2 = 15, out = { 16008, 1 }, oq = 2 },
    [19830] = { name = "Arcanite Dragonling", t = { 1, 320, 330, 340 }, scroll = 16054, train = 300, sq = 2, r = { { 10576, 1 }, { 16006, 8 }, { 12655, 10 }, { 15994, 6 }, { 10558, 4 }, { 12810, 6 } }, tool = 162, tool2 = 14, out = { 16022, 1 }, oq = 3 },
    [19831] = { name = "Arcane Bomb", t = { 1, 320, 330, 340 }, scroll = 16055, train = 300, sq = 2, r = { { 16006, 1 }, { 12359, 3 }, { 14047, 1 } }, tool = 162, out = { 16040, 3 }, oq = 1 },
    [19833] = { name = "Flawless Arcanite Rifle", t = { 1, 320, 330, 340 }, scroll = 16056, train = 300, sq = 2, r = { { 12360, 10 }, { 16000, 2 }, { 7078, 2 }, { 7076, 2 }, { 12800, 2 }, { 12810, 2 } }, tool = 162, tool2 = 14, out = { 16007, 1 }, oq = 3 },
    [21940] = { name = "Snowmaster 9000", t = { 1, 190, 210, 230 }, scroll = 17720, train = 190, sq = 2, r = { { 3860, 8 }, { 4389, 4 }, { 17202, 4 }, { 3829, 1 } }, tool = 162, tool2 = 14, out = { 17716, 1 }, oq = 1 },
    [22704] = { name = "Field Repair Bot 74A", t = { 1, 320, 330, 340 }, scroll = 18235, train = 300, sq = 1, r = { { 12359, 12 }, { 8170, 4 }, { 7191, 1 }, { 7067, 2 }, { 7068, 1 } }, tool = 162, tool2 = 14, out = { 18232, 1 }, oq = 1 },
    [22793] = { name = "Biznicks 247x128 Accurascope", t = { 1, 320, 330, 340 }, scroll = 18290, train = 300, sq = 3, r = { { 17011, 2 }, { 7076, 2 }, { 16006, 4 }, { 11371, 6 }, { 16000, 1 } }, tool = 162, tool2 = 14, out = { 18283, 1 }, oq = 3 },
    [22795] = { name = "Core Marksman Rifle", t = { 1, 320, 330, 340 }, scroll = 18292, train = 300, sq = 3, r = { { 17010, 4 }, { 17011, 2 }, { 12360, 6 }, { 16006, 2 }, { 16000, 2 } }, tool = 162, tool2 = 14, out = { 18282, 1 }, oq = 4 },
    [22797] = { name = "Force Reactive Disk", t = { 1, 320, 330, 340 }, scroll = 18291, train = 300, sq = 3, r = { { 12360, 6 }, { 16006, 2 }, { 7082, 8 }, { 12803, 12 }, { 7076, 8 } }, tool = 162, tool2 = 14, out = { 18168, 1 }, oq = 4 },
    [23066] = { name = "Red Firework", t = { 1, 150, 162, 175 }, scroll = 18647, train = 150, scrollPrice = 1800, sq = 1, r = { { 4377, 1 }, { 4234, 1 } }, out = { 9318, 3 }, oq = 1 },
    [23067] = { name = "Blue Firework", t = { 1, 150, 162, 175 }, scroll = 18649, train = 150, scrollPrice = 1800, sq = 1, r = { { 4377, 1 }, { 4234, 1 } }, out = { 9312, 3 }, oq = 1 },
    [23068] = { name = "Green Firework", t = { 1, 150, 162, 175 }, scroll = 18648, train = 150, scrollPrice = 1800, sq = 1, r = { { 4377, 1 }, { 4234, 1 } }, out = { 9313, 3 }, oq = 1 },
    [23069] = { name = "EZ-Thro Dynamite II", t = { 1, 200, 210, 220 }, scroll = 18650, train = 200, scrollPrice = 5000, sq = 1, r = { { 10505, 1 }, { 4306, 1 }, { 260801, 1 } }, out = { 18588, 1 }, oq = 1 },
    [23070] = { name = "Dense Dynamite", t = { 1, 250, 260, 270 }, fee = 5000, train = 250, r = { { 15992, 2 }, { 14047, 3 } }, out = { 18641, 2 }, oq = 1 },
    [23071] = { name = "Truesilver Transformer", t = { 1, 270, 275, 280 }, scroll = 18651, train = 260, scrollPrice = 12000, sq = 1, r = { { 6037, 2 }, { 7067, 2 }, { 7069, 1 } }, tool = 162, tool2 = 14, out = { 18631, 1 }, oq = 1 },
    [23077] = { name = "Gyrofreeze Ice Reflector", t = { 1, 280, 290, 300 }, scroll = 18652, train = 260, scrollPrice = 12000, sq = 1, r = { { 15994, 6 }, { 18631, 2 }, { 12361, 2 }, { 7078, 4 }, { 3829, 2 }, { 13467, 4 } }, tool = 162, tool2 = 14, out = { 18634, 1 }, oq = 3 },
    [23078] = { name = "Goblin Jumper Cables XL", t = { 1, 285, 295, 305 }, scroll = 18653, train = 265, sq = 2, r = { { 15994, 2 }, { 18631, 2 }, { 7191, 2 }, { 14227, 2 }, { 7910, 2 } }, out = { 18587, 1 }, oq = 1 },
    [23079] = { name = "Major Recombobulator", t = { 1, 285, 290, 295 }, scroll = 18655, train = 275, sq = 2, r = { { 16000, 2 }, { 18631, 1 }, { 14047, 2 } }, out = { 18637, 1 }, oq = 2 },
    [23080] = { name = "Powerful Seaforium Charge", t = { 1, 275, 285, 295 }, scroll = 18656, train = 275, scrollPrice = 16000, sq = 1, r = { { 15994, 2 }, { 15992, 3 }, { 8170, 2 }, { 159, 1 } }, out = { 18594, 1 }, oq = 1 },
    [23081] = { name = "Hyper-Radiant Flame Reflector", t = { 1, 310, 320, 330 }, scroll = 18657, train = 290, sq = 2, r = { { 11371, 4 }, { 18631, 3 }, { 7080, 6 }, { 7910, 4 }, { 12800, 2 } }, tool = 162, tool2 = 14, out = { 18638, 1 }, oq = 3 },
    [23082] = { name = "Ultra-Flash Shadow Reflector", t = { 1, 320, 330, 340 }, scroll = 18658, train = 300, sq = 2, r = { { 11371, 8 }, { 18631, 4 }, { 12803, 6 }, { 12808, 4 }, { 12800, 2 }, { 12799, 2 } }, tool = 162, tool2 = 14, out = { 18639, 1 }, oq = 3 },
    [23096] = { name = "Alarm-O-Bot", t = { 1, 275, 280, 285 }, scroll = 18654, train = 265, sq = 2, r = { { 12359, 4 }, { 15994, 2 }, { 8170, 4 }, { 7910, 1 }, { 7191, 1 } }, tool = 162, tool2 = 14, out = { 18645, 1 }, oq = 1 },
    [23129] = { name = "World Enlarger", t = { 1, 260, 265, 270 }, scroll = 18661, train = 260, sq = 2, r = { { 10561, 1 }, { 15994, 2 }, { 10558, 1 }, { 10560, 1 }, { 3864, 1 } }, tool = 162, out = { 18660, 1 }, oq = 2 },
    [23486] = { name = "Dimensional Ripper - Everlook", t = { 1, 285, 295, 305 }, r = { { 3860, 10 }, { 18631, 1 }, { 7077, 4 }, { 7910, 2 }, { 10586, 1 } }, tool = 162, tool2 = 14, out = { 18984, 1 }, oq = 2 },
    [23489] = { name = "Ultrasafe Transporter - Gadgetzan", t = { 1, 285, 295, 305 }, r = { { 3860, 12 }, { 18631, 2 }, { 7075, 4 }, { 7079, 2 }, { 7909, 4 }, { 9060, 1 } }, tool = 162, tool2 = 14, out = { 18986, 1 }, oq = 2 },
    [23507] = { name = "Snake Burst Firework", t = { 1, 250, 260, 270 }, scroll = 19027, train = 250, scrollPrice = 5000, sq = 1, r = { { 15992, 2 }, { 14047, 2 }, { 8150, 1 } }, out = { 19026, 4 }, oq = 1 },
    [24356] = { name = "Bloodvine Goggles", t = { 1, 320, 330, 340 }, scroll = 20000, train = 300, scrollPrice = 120000, rep = { 270, 5 }, sq = 1, r = { { 19726, 4 }, { 19774, 5 }, { 16006, 2 }, { 12804, 8 }, { 12810, 4 } }, tool = 15, tool2 = 14, out = { 19999, 1 }, oq = 3 },
    [24357] = { name = "Bloodvine Lens", t = { 1, 320, 330, 340 }, scroll = 20001, train = 300, scrollPrice = 50000, rep = { 270, 4 }, sq = 1, r = { { 19726, 5 }, { 19774, 5 }, { 16006, 1 }, { 12804, 8 }, { 12810, 4 } }, tool = 15, tool2 = 14, out = { 19998, 1 }, oq = 3 },
    [26011] = { name = "Tranquil Mechanical Yeti", t = { 1, 320, 330, 340 }, r = { { 15407, 1 }, { 15994, 4 }, { 7079, 2 }, { 18631, 2 }, { 10558, 1 } }, tool = 162, tool2 = 14, out = { 21277, 1 }, oq = 1 },
    [26416] = { name = "Small Blue Rocket", t = { 1, 125, 137, 150 }, scroll = 21724, train = 125, sq = 2, r = { { 4364, 1 }, { 2319, 1 } }, out = { 21558, 5 }, oq = 1 },
    [26417] = { name = "Small Green Rocket", t = { 1, 125, 137, 150 }, scroll = 21725, train = 125, sq = 2, r = { { 4364, 1 }, { 2319, 1 } }, out = { 21559, 5 }, oq = 1 },
    [26418] = { name = "Small Red Rocket", t = { 1, 125, 137, 150 }, scroll = 21726, train = 125, sq = 2, r = { { 4364, 1 }, { 2319, 1 } }, out = { 21557, 5 }, oq = 1 },
    [26420] = { name = "Large Blue Rocket", t = { 1, 175, 187, 200 }, scroll = 21727, train = 175, sq = 2, r = { { 4377, 1 }, { 4234, 1 } }, out = { 21589, 5 }, oq = 1 },
    [26421] = { name = "Large Green Rocket", t = { 1, 175, 187, 200 }, scroll = 21728, train = 175, sq = 2, r = { { 4377, 1 }, { 4234, 1 } }, out = { 21590, 5 }, oq = 1 },
    [26422] = { name = "Large Red Rocket", t = { 1, 175, 187, 200 }, scroll = 21729, train = 175, sq = 2, r = { { 4377, 1 }, { 4234, 1 } }, out = { 21592, 5 }, oq = 1 },
    [26423] = { name = "Blue Rocket Cluster", t = { 1, 225, 237, 250 }, scroll = 21730, train = 225, sq = 2, r = { { 10505, 1 }, { 4304, 1 } }, out = { 21571, 5 }, oq = 1 },
    [26424] = { name = "Green Rocket Cluster", t = { 1, 225, 237, 250 }, scroll = 21731, train = 225, sq = 2, r = { { 10505, 1 }, { 4304, 1 } }, out = { 21574, 5 }, oq = 1 },
    [26425] = { name = "Red Rocket Cluster", t = { 1, 225, 237, 250 }, scroll = 21732, train = 225, sq = 2, r = { { 10505, 1 }, { 4304, 1 } }, out = { 21576, 5 }, oq = 1 },
    [26426] = { name = "Large Blue Rocket Cluster", t = { 1, 275, 280, 285 }, scroll = 21733, train = 275, sq = 2, r = { { 15992, 1 }, { 8170, 1 } }, out = { 21714, 5 }, oq = 1 },
    [26427] = { name = "Large Green Rocket Cluster", t = { 1, 275, 280, 285 }, scroll = 21734, train = 275, sq = 2, r = { { 15992, 1 }, { 8170, 1 } }, out = { 21716, 5 }, oq = 1 },
    [26428] = { name = "Large Red Rocket Cluster", t = { 1, 275, 280, 285 }, scroll = 21735, train = 275, sq = 2, r = { { 15992, 1 }, { 8170, 1 } }, out = { 21718, 5 }, oq = 1 },
    [26442] = { name = "Firework Launcher", t = { 1, 245, 255, 265 }, scroll = 21738, train = 225, sq = 2, r = { { 9060, 2 }, { 9061, 2 }, { 10560, 2 }, { 10561, 1 } }, out = { 21569, 1 }, oq = 1 },
    [26443] = { name = "Firework Cluster Launcher", t = { 1, 295, 305, 315 }, scroll = 21737, train = 275, sq = 2, r = { { 9060, 3 }, { 9061, 3 }, { 18631, 1 }, { 10561, 1 } }, out = { 21570, 1 }, oq = 1 },
    [28327] = { name = "Steam Tonk Controller", t = { 1, 295, 305, 315 }, scroll = 22729, train = 275, sq = 1, r = { { 15994, 2 }, { 10561, 1 }, { 10558, 1 } }, tool = 162, tool2 = 14, out = { 22728, 1 }, oq = 2 },
    [424641] = { name = "Shredder Autosalvage Unit", t = { 1, 135, 140, 145 }, scroll = 210178, train = 135, sq = 2, r = { { 4382, 1 }, { 4375, 2 }, { 4234, 1 } }, tool = 162, tool2 = 14, out = { 210147, 1 }, oq = 1 },
    [431362] = { name = "Soul Vessel", t = { 1, 205, 210, 215 }, scroll = 212230, train = 205, gone = true, sq = 3, r = { { 1210, 4 }, { 9262, 1 }, { 16583, 1 } }, tool = 14, out = { 211427, 1 }, oq = 3 },
    [435956] = { name = "Polished Truesilver Gears", t = { 1, 200, 210, 220 }, scroll = 215429, train = 200, sq = 3, r = { { 6037, 1 }, { 213381, 5 } }, tool = 162, out = { 213383, 1 }, oq = 3 },
    [435958] = { name = "Whirling Truesilver Gearwall", t = { 1, 225, 232, 240 }, scroll = 215153, train = 225, sq = 4, r = { { 213376, 3 }, { 213383, 5 }, { 213369, 2 }, { 10561, 2 }, { 4389, 2 }, { 3860, 15 } }, tool = 162, out = { 213390, 1 }, oq = 1 },
    [435960] = { name = "Hyperconductive Goldwap", t = { 1, 225, 230, 235 }, scroll = 215156, train = 225, sq = 4, r = { { 213383, 3 }, { 213379, 3 }, { 213369, 1 }, { 3577, 10 } }, tool = 14, out = { 215115, 1 }, oq = 1 },
    [435964] = { name = "High-Yield Radiation Bomb", t = { 1, 225, 230, 235 }, scroll = 215431, train = 225, sq = 4, r = { { 10505, 1 }, { 215430, 1 }, { 3860, 2 } }, tool = 162, out = { 215127, 3 }, oq = 1 },
    [435966] = { name = "Ez-Thro Radiation Bomb", t = { 1, 225, 230, 235 }, scroll = 215432, train = 225, sq = 4, r = { { 10505, 2 }, { 215430, 1 }, { 3860, 2 } }, tool = 162, out = { 215168, 3 }, oq = 1 },
    [461710] = { name = "Fiery Core Sharpshooter Rifle", t = { 1, 320, 330, 340 }, scroll = 228304, train = 310, sq = 1, r = { { 17010, 4 }, { 17011, 2 }, { 12360, 6 }, { 16006, 2 }, { 16000, 2 } }, tool = 162, tool2 = 14, out = { 227849, 1 }, oq = 1 },
    [1213573] = { name = "Arcane Megabomb", t = { 1, 315, 322, 330 }, scroll = 234261, train = 305, sq = 1, r = { { 16006, 1 }, { 20725, 1 }, { 14047, 1 } }, out = { 233984, 5 }, oq = 1 },
    [1213646] = { name = "Obsidian Blasting Powder", t = { 1, 315, 322, 330 }, scroll = 234280, train = 305, sq = 1, r = { { 22202, 2 } }, out = { 234005, 1 }, oq = 1 },
    [1221012] = { name = "Creepy Censor Sensors", t = { 1, 275, 277, 280 }, scroll = 236872, train = 250, sq = 2, r = { { 8170, 8 }, { 12800, 2 } }, tool = 14, out = { 236871, 1 }, oq = 1 },
    [1226206] = { name = "Tinkerbox", t = { 1, 260, 270, 280 }, scroll = 250400, train = 250, sq = 1, r = { { 10561, 1 }, { 10558, 2 } }, tool = 14, tool2 = 15, out = { 238737, 1 }, oq = 1 },
    [1228088] = { name = "Pop-Up Shrub", t = { 1, 255, 257, 260 }, scroll = 239222, train = 250, sq = 3, r = { { 15994, 1 }, { 10560, 1 }, { 4382, 1 } }, tool = 14, tool2 = 15, out = { 237023, 1 }, oq = 1 },
    [1230656] = { name = "Reagent Bot", t = { 1, 20, 20, 20 }, fee = 0, train = 20, r = { { 4359, 1 }, { 4361, 1 } }, out = { 279950, 1 }, oq = 1 },
    [1249634] = { name = "Sandpaper", t = { 1, 130, 142, 155 }, fee = 500, train = 120, tr = { 5174, 8736, 11017, 249235 }, r = { { 249425, 2 }, { 2996, 1 } }, out = { 249432, 1 }, oq = 2 },
    [1263034] = { name = "Repair Bot", t = { 1, 140, 140, 140 }, scroll = 273092, train = 140, sq = 2, r = { { 4375, 2 }, { 4371, 1 }, { 4234, 1 } }, tool2 = 14, out = { 279949, 1 }, oq = 1 },
    [1266893] = { name = "SAF-T Tabs", t = { 1, 25, 27, 30 }, scroll = 264201, train = 25, sq = 1, favor = 45, r = { { 2570, 1 }, { 249409, 1 } }, out = { 260784, 1 }, oq = 1 },
    [1266905] = { name = "SAF-T Dynamite", t = { 1, 25, 30, 35 }, scroll = 264202, train = 25, sq = 1, favor = 45, r = { { 4357, 2 }, { 2589, 1 } }, out = { 260792, 1 }, oq = 1 },
    [1266906] = { name = "SAF-T Copper Bomb", t = { 1, 55, 60, 65 }, scroll = 264203, train = 55, sq = 1, favor = 45, r = { { 2840, 1 }, { 4359, 1 }, { 4357, 2 }, { 2570, 1 }, { 260784, 2 } }, tool = 162, out = { 260793, 1 }, oq = 1 },
    [1266907] = { name = "EZ-Thro Wrap", t = { 1, 100, 102, 105 }, scroll = 264204, train = 100, sq = 1, favor = 45, r = { { 2592, 1 }, { 249410, 1 } }, out = { 260794, 1 }, oq = 1 },
    [1266908] = { name = "EZ-Thro Copper Bomb XL", t = { 1, 130, 155, 180 }, scroll = 264205, train = 130, sq = 1, favor = 45, r = { { 2840, 3 }, { 4364, 4 }, { 4404, 1 }, { 260794, 1 } }, tool = 162, out = { 260795, 1 }, oq = 1 },
    [1266909] = { name = "No Slip SAF-T Padding", t = { 1, 145, 147, 150 }, scroll = 264206, train = 145, sq = 1, favor = 45, r = { { 4234, 1 }, { 249430, 1 } }, out = { 260796, 1 }, oq = 1 },
    [1266910] = { name = "SAF-T Bronze Bomb", t = { 1, 145, 170, 195 }, scroll = 264207, train = 145, sq = 1, r = { { 4364, 4 }, { 2841, 2 }, { 4404, 1 }, { 2592, 1 }, { 260796, 1 } }, tool = 162, out = { 260797, 1 }, oq = 1 },
    [1266911] = { name = "SAF-T Jumbo Dynamite", t = { 1, 150, 160, 170 }, scroll = 264208, train = 150, sq = 1, r = { { 4377, 2 }, { 2592, 1 }, { 260796, 1 } }, out = { 260798, 1 }, oq = 1 },
    [1266912] = { name = "SAF-T Bell", t = { 1, 175, 177, 180 }, scroll = 264209, train = 175, sq = 1, favor = 180, favorRep = 5, r = { { 2841, 2 }, { 249432, 1 } }, tool = 162, out = { 260799, 1 }, oq = 1 },
    [1266913] = { name = "Shafety Sheep", t = { 1, 200, 212, 225 }, scroll = 264210, train = 175, sq = 1, r = { { 4382, 1 }, { 4375, 1 }, { 4377, 2 }, { 2592, 2 }, { 260799, 1 } }, tool = 162, tool2 = 14, out = { 260800, 1 }, oq = 1 },
    [1266914] = { name = "EZ-Thro Fireproof Fuse", t = { 1, 190, 192, 195 }, scroll = 264211, train = 190, sq = 1, favor = 180, favorRep = 5, r = { { 4404, 1 }, { 249428, 1 } }, tool = 162, tool2 = 14, out = { 260801, 1 }, oq = 1 },
    [1266915] = { name = "EZ-Thro Bronze Mortar", t = { 1, 210, 220, 230 }, scroll = 264212, train = 190, sq = 1, r = { { 4371, 4 }, { 4387, 1 }, { 4377, 4 }, { 2319, 4 }, { 260801, 1 } }, tool = 162, tool2 = 14, out = { 260802, 1 }, oq = 1 },
    [1266916] = { name = "EZ-Thro Grenade", t = { 1, 200, 220, 240 }, scroll = 264213, train = 200, sq = 1, r = { { 3575, 1 }, { 4377, 1 }, { 4306, 1 }, { 260801, 1 } }, tool = 162, tool2 = 14, out = { 260803, 1 }, oq = 1 },
    [1266917] = { name = "SAF-T Casing", t = { 1, 215, 217, 220 }, scroll = 264214, train = 215, sq = 1, r = { { 10561, 1 }, { 4234, 1 } }, tool = 162, out = { 260804, 1 }, oq = 1 },
    [1266918] = { name = "SAF-T Bomb", t = { 1, 215, 230, 245 }, scroll = 264215, train = 215, sq = 1, r = { { 3575, 3 }, { 4377, 3 }, { 4404, 1 }, { 260804, 1 } }, tool = 162, tool2 = 14, out = { 260805, 1 }, oq = 1 },
    [1266919] = { name = "Emergency Field Cloak", t = { 1, 245, 255, 265 }, scroll = 264216, train = 225, sq = 1, favor = 270, favorRep = 6, r = { { 4397, 1 }, { 260804, 1 } }, tool = 162, tool2 = 14, out = { 260806, 1 }, oq = 1, bop = true },
    [1266920] = { name = "Compact Critter Carrier", t = { 1, 230, 232, 235 }, scroll = 264217, train = 225, sq = 1, favor = 270, favorRep = 6, r = { { 4234, 10 }, { 10559, 10 }, { 11175, 2 }, { 10558, 1 } }, tool = 162, tool2 = 14, out = { 260807, 1 }, oq = 1 },
    [1266921] = { name = "EZ-Thro Tru-Trigger", t = { 1, 240, 242, 245 }, scroll = 264218, train = 240, sq = 1, r = { { 6037, 1 }, { 249431, 1 } }, tool = 162, tool2 = 14, out = { 260808, 1 }, oq = 1 },
    [1266922] = { name = "Tru-Trigger Frag Bomb", t = { 1, 240, 260, 280 }, scroll = 264219, train = 240, sq = 1, r = { { 10561, 1 }, { 10560, 1 }, { 10505, 1 }, { 260808, 1 } }, out = { 260809, 1 }, oq = 1 },
    [1266923] = { name = "SAF-T Disposable Parachute", t = { 1, 270, 280, 290 }, scroll = 264220, train = 250, sq = 1, favor = 270, favorRep = 6, r = { { 10518, 1 }, { 260804, 1 } }, tool = 14, tool2 = 15, out = { 260810, 1 }, oq = 1 },
    [1266924] = { name = "Gnomish Army Knife", t = { 1, 250, 252, 255 }, scroll = 264221, train = 250, scrollPrice = 6250, sq = 1, r = { { 10561, 1 }, { 10558, 1 }, { 15994, 2 } }, tool = 162, tool2 = 14, out = { 260811, 1 }, oq = 1 },
    [1266925] = { name = "Loot-A-Rang", t = { 1, 275, 277, 280 }, scroll = 264222, train = 275, scrollPrice = 6875, sq = 1, r = { { 12359, 5 }, { 16203, 5 } }, tool = 14, tool2 = 15, out = { 260812, 1 }, oq = 3 },
    [1266926] = { name = "SAF-T Tube", t = { 1, 275, 277, 280 }, scroll = 264223, train = 275, sq = 1, r = { { 12359, 1 }, { 249726, 1 } }, tool = 162, tool2 = 14, out = { 260813, 1 }, oq = 1 },
    [1266927] = { name = "SAF-T Clever Dynamite", t = { 1, 275, 285, 295 }, scroll = 264224, train = 275, sq = 1, r = { { 15992, 2 }, { 14047, 3 }, { 260813, 1 } }, tool = 162, out = { 260814, 1 }, oq = 1 },
    [1266928] = { name = "EZ-Thro Shell", t = { 1, 285, 287, 290 }, scroll = 264225, train = 285, sq = 1, r = { { 12359, 2 }, { 249429, 1 } }, tool = 162, out = { 260815, 1 }, oq = 1 },
    [1266929] = { name = "EZ-Thro Thorium Grenade", t = { 1, 285, 295, 305 }, scroll = 264226, train = 285, sq = 1, r = { { 15994, 1 }, { 12359, 3 }, { 15992, 3 }, { 14047, 3 }, { 260815, 1 } }, tool = 162, out = { 260816, 1 }, oq = 1 },
    [1266930] = { name = "EZ-Thro Dark Bomb", t = { 1, 320, 330, 340 }, scroll = 264227, train = 300, sq = 1, r = { { 15994, 2 }, { 11371, 1 }, { 15992, 3 }, { 14047, 3 }, { 260815, 1 } }, tool = 162, out = { 260817, 1 }, oq = 1 },
    [1266931] = { name = "EZ-Thro Mana Bomb", t = { 1, 320, 330, 340 }, scroll = 264228, train = 300, sq = 1, r = { { 16006, 1 }, { 12359, 3 }, { 14047, 1 }, { 260815, 1 } }, tool = 162, out = { 260818, 1 }, oq = 1 },
    [1266932] = { name = "EZ-Thro Field Transporter: Gadgetzan", t = { 1, 320, 330, 340 }, scroll = 264229, train = 300, sq = 1, r = { { 18986, 1 }, { 260815, 1 } }, tool = 162, tool2 = 14, out = { 260819, 1 }, oq = 2 },
    [1266933] = { name = "SAF-T Emergency Ripper: Everlook", t = { 1, 320, 330, 340 }, scroll = 264230, train = 300, sq = 1, r = { { 18984, 1 }, { 260813, 2 } }, tool = 162, tool2 = 14, out = { 260820, 1 }, oq = 2 },
    [1266934] = { name = "EZ and SAF Field Transporter: Mt. Hyjal", t = { 1, 320, 330, 340 }, scroll = 264231, train = 300, sq = 1, r = { { 260823, 1 }, { 260815, 1 }, { 260813, 1 } }, tool = 162, tool2 = 14, out = { 260821, 1 }, oq = 2 },
    [1266935] = { name = "Ultrasafe Rechargeable Battery", t = { 1, 320, 330, 340 }, scroll = 264232, train = 300, sq = 1, favor = 360, favorRep = 6, r = { { 249410, 2 }, { 249426, 1 }, { 249431, 1 }, { 12359, 3 }, { 3860, 1 }, { 248822, 1 } }, tool = 14, tool2 = 15, out = { 260822, 1 }, oq = 2 },
    [1266936] = { name = "Dimensional Transporter - Mt. Hyjal", t = { 1, 320, 330, 340 }, scroll = 264233, train = 300, scrollPrice = 100000, sq = 1, r = { { 3860, 10 }, { 18631, 1 }, { 7075, 4 }, { 7082, 4 }, { 251290, 2 } }, tool = 162, tool2 = 14, out = { 260823, 1 }, oq = 2 },
    [1266937] = { name = "Gnomish Poultryizer", t = { 1, 320, 330, 340 }, scroll = 264234, train = 300, sq = 1, favor = 360, favorRep = 6, r = { { 16204, 10 }, { 14344, 2 }, { 249726, 2 }, { 251290, 2 } }, tool = 14, tool2 = 15, out = { 260824, 1 }, oq = 3, bop = true },
    [1266938] = { name = "Ultralight Goblin Glider", t = { 1, 320, 330, 340 }, scroll = 264235, train = 300, sq = 1, favor = 360, favorRep = 6, r = { { 249431, 2 }, { 249726, 2 }, { 249429, 8 }, { 12359, 8 } }, tool = 14, tool2 = 15, out = { 260825, 1 }, oq = 2 },
    [1266939] = { name = "Gnomish Weather Machine", t = { 1, 320, 330, 340 }, scroll = 264236, train = 300, sq = 1, r = { { 7076, 2 }, { 7078, 2 }, { 7082, 2 }, { 7080, 2 }, { 248822, 2 } }, tool = 14, tool2 = 15, out = { 260826, 1 }, oq = 2 },
    [1266940] = { name = "Stealthman 52", t = { 1, 320, 330, 340 }, scroll = 264237, train = 300, sq = 1, favor = 360, favorRep = 6, r = { { 7082, 6 }, { 16204, 6 }, { 248820, 2 }, { 251290, 2 }, { 248823, 4 } }, tool = 14, tool2 = 15, out = { 260827, 1 }, oq = 2 },
    [1286792] = { name = "Centaur Banner Deployment Device", t = { 1, 190, 197, 205 }, scroll = 269901, train = 190, scrollPrice = 3000, sq = 2, r = { { 4387, 6 }, { 4389, 2 }, { 10558, 4 }, { 4234, 30 } }, tool = 14, tool2 = 15, out = { 269900, 1 }, oq = 2 },
    [1286796] = { name = "Hoof-Shaped Foot Pedal", t = { 1, 150, 155, 160 }, scroll = 269903, train = 140, scrollPrice = 3000, sq = 2, r = { { 4387, 3 }, { 4382, 2 }, { 4389, 1 }, { 10558, 1 }, { 4234, 4 } }, tool = 14, tool2 = 15, out = { 269902, 1 }, oq = 1 },
    [1293088] = { name = "9-60 Battery Pack", t = { 1, 125, 135, 145 }, scroll = 274049, train = 125, sq = 1, r = { { 249409, 1 }, { 249391, 1 }, { 3575, 1 } }, tool = 14, tool2 = 15, out = { 274048, 1 }, oq = 1 },
    [1293849] = { name = "Swiftfeather Arrow", t = { 1, 310, 315, 320 }, scroll = 274389, train = 300, sq = 4, r = { { 251291, 8 }, { 17056, 5 }, { 7069, 1 } }, out = { 274387, 200 }, oq = 4 },
    [1293850] = { name = "Swiftstrike Shot", t = { 1, 310, 315, 320 }, scroll = 274390, train = 300, sq = 4, r = { { 251291, 8 }, { 12365, 8 }, { 7067, 1 } }, out = { 274388, 200 }, oq = 4 },
    [1302161] = { name = "Harvester Override Signalcaster", t = { 1, 65, 72, 80 }, scroll = 277470, train = 65, sq = 1, r = { { 255007, 4 }, { 4363, 2 }, { 4405, 1 } }, tool = 162, tool2 = 14, out = { 277132, 1 }, oq = 2, bop = true },
    [1306546] = { name = "SAF-T Ultra Precision Scope", t = { 1, 310, 317, 325 }, scroll = 279321, train = 300, sq = 4, r = { { 251290, 1 }, { 251291, 12 } }, tool = 14, tool2 = 15, out = { 279272, 1 }, oq = 3 },
    [1306547] = { name = "Hyper Deluxe Sniper Rifle Mk XVII", t = { 1, 310, 317, 325 }, scroll = 279322, train = 300, sq = 4, r = { { 274030, 4 }, { 251290, 2 }, { 251291, 10 }, { 12800, 1 } }, tool = 14, tool2 = 15, out = { 279273, 1 }, oq = 4 },
    [1308178] = { name = "Whimsical Waistwrap", t = { 1, 180, 182, 185 }, scroll = 280321, train = 175, sq = 2, favor = 180, favorRep = 5, r = { { 4382, 2 }, { 4375, 1 }, { 4305, 2 } }, tool = 14, tool2 = 15, out = { 280306, 1 }, oq = 2, bop = true },
    [1308179] = { name = "Gizmo Girdle", t = { 1, 180, 182, 185 }, scroll = 280322, train = 175, sq = 2, favor = 180, favorRep = 5, r = { { 4375, 2 }, { 4382, 1 }, { 2319, 4 } }, tool = 14, tool2 = 15, out = { 280307, 1 }, oq = 2, bop = true },
    [1308180] = { name = "Clanking Cord", t = { 1, 180, 182, 185 }, scroll = 280323, train = 175, sq = 2, favor = 180, favorRep = 5, r = { { 4371, 2 }, { 4363, 1 }, { 2319, 4 } }, tool = 14, tool2 = 15, out = { 280308, 1 }, oq = 2, bop = true },
    [1308182] = { name = "Serrated Strap", t = { 1, 180, 182, 185 }, scroll = 280324, train = 175, sq = 2, r = { { 4363, 2 }, { 4371, 1 }, { 3575, 1 } }, tool = 14, tool2 = 15, out = { 280309, 1 }, oq = 1 },
    [1308183] = { name = "Floppy Goggles", t = { 1, 205, 207, 210 }, scroll = 280325, train = 200, sq = 2, favor = 180, favorRep = 5, r = { { 5507, 1 }, { 4389, 1 }, { 4339, 4 } }, tool = 14, tool2 = 15, out = { 280310, 1 }, oq = 2, bop = true },
    [1308184] = { name = "Bent Goggles", t = { 1, 205, 207, 210 }, scroll = 280326, train = 200, sq = 2, favor = 180, favorRep = 5, r = { { 5507, 1 }, { 4389, 1 }, { 4234, 8 } }, tool = 14, tool2 = 15, out = { 280311, 1 }, oq = 2, bop = true },
    [1308185] = { name = "Stuckbutton Goggles", t = { 1, 205, 207, 210 }, scroll = 280327, train = 200, sq = 2, favor = 180, favorRep = 5, r = { { 5507, 1 }, { 4389, 1 }, { 4234, 8 } }, tool = 14, tool2 = 15, out = { 280312, 1 }, oq = 2, bop = true },
    [1308186] = { name = "Dented Goggles", t = { 1, 205, 207, 210 }, scroll = 280328, train = 200, sq = 2, favor = 180, favorRep = 5, r = { { 5507, 1 }, { 4389, 1 }, { 3860, 2 } }, tool = 14, tool2 = 15, out = { 280313, 1 }, oq = 2, bop = true },
    [1317270] = { name = "Unsanctified Grenade", t = { 1, 280, 290, 300 }, scroll = 284870, train = 260, sq = 1, r = { { 18631, 1 }, { 12655, 2 }, { 15992, 3 }, { 14047, 2 } }, tool = 162, out = { 284869, 3 }, oq = 1 },
    [1317958] = { name = "Satchel of Copper Bombs", t = { 1, 90, 92, 95 }, scroll = 285285, train = 85, sq = 2, favor = 45, r = { { 4360, 20 }, { 2318, 6 }, { 4359, 4 } }, out = { 285275, 1 }, oq = 2, bop = true },
    [1317959] = { name = "Satchel of Bronze Bombs", t = { 1, 170, 172, 175 }, scroll = 285286, train = 165, sq = 2, favor = 180, favorRep = 5, r = { { 4380, 20 }, { 2319, 6 }, { 4375, 1 } }, out = { 285276, 1 }, oq = 2, bop = true },
    [1317960] = { name = "Satchel of Iron Bombs", t = { 1, 235, 237, 240 }, scroll = 285287, train = 230, sq = 2, favor = 270, favorRep = 6, r = { { 4394, 20 }, { 4304, 6 }, { 4389, 1 } }, out = { 285277, 1 }, oq = 2, bop = true },
    [1317961] = { name = "Satchel of Dark Iron Bombs", t = { 1, 290, 292, 295 }, scroll = 285288, train = 285, sq = 2, favor = 270, favorRep = 6, r = { { 16005, 20 }, { 8170, 6 }, { 10560, 1 } }, out = { 285278, 1 }, oq = 2, bop = true },
    [1319154] = { name = "Small Purple Rocket", t = { 1, 125, 137, 150 }, scroll = 286076, train = 125, sq = 2, r = { { 4364, 1 }, { 2319, 1 } }, out = { 21560, 5 }, oq = 1 },
    [1319155] = { name = "Small White Rocket", t = { 1, 125, 137, 150 }, scroll = 286077, train = 125, sq = 2, r = { { 4364, 1 }, { 2319, 1 } }, out = { 21561, 5 }, oq = 1 },
    [1319156] = { name = "Small Yellow Rocket", t = { 1, 125, 137, 150 }, scroll = 286078, train = 125, sq = 2, r = { { 4364, 1 }, { 2319, 1 } }, out = { 21562, 5 }, oq = 1 },
    [1319157] = { name = "Large Purple Rocket", t = { 1, 175, 187, 200 }, scroll = 286079, train = 175, sq = 2, r = { { 4377, 1 }, { 4234, 1 } }, out = { 21591, 5 }, oq = 1 },
    [1319158] = { name = "Large White Rocket", t = { 1, 175, 187, 200 }, scroll = 286080, train = 175, sq = 2, r = { { 4377, 1 }, { 4234, 1 } }, out = { 21593, 5 }, oq = 1 },
    [1319159] = { name = "Large Yellow Rocket", t = { 1, 175, 187, 200 }, scroll = 286081, train = 175, sq = 2, r = { { 4377, 1 }, { 4234, 1 } }, out = { 21595, 5 }, oq = 1 },
    [1319160] = { name = "Purple Rocket Cluster", t = { 1, 225, 237, 250 }, scroll = 286082, train = 225, sq = 2, r = { { 10505, 1 }, { 4304, 1 } }, out = { 21575, 5 }, oq = 1 },
    [1319161] = { name = "White Rocket Cluster", t = { 1, 225, 237, 250 }, scroll = 286083, train = 225, sq = 2, r = { { 10505, 1 }, { 4304, 1 } }, out = { 21577, 5 }, oq = 1 },
    [1319162] = { name = "Yellow Rocket Cluster", t = { 1, 225, 237, 250 }, scroll = 286084, train = 225, sq = 2, r = { { 10505, 1 }, { 4304, 1 } }, out = { 21578, 5 }, oq = 1 },
    [1319163] = { name = "Large Purple Rocket Cluster", t = { 1, 275, 280, 285 }, scroll = 286085, train = 275, sq = 2, r = { { 15992, 1 }, { 8170, 1 } }, out = { 21717, 5 }, oq = 1 },
    [1319164] = { name = "Large White Rocket Cluster", t = { 1, 275, 280, 285 }, scroll = 286086, train = 275, sq = 2, r = { { 15992, 1 }, { 8170, 1 } }, out = { 21719, 5 }, oq = 1 },
    [1319165] = { name = "Large Yellow Rocket Cluster", t = { 1, 275, 280, 285 }, scroll = 286087, train = 275, sq = 2, r = { { 15992, 1 }, { 8170, 1 } }, out = { 21720, 5 }, oq = 1 },
  },
}

-- Herramientas: [categoría] = { objeto, máscara } (un bastón superior cubre a los inferiores)
ES.Data.Tools = ES.Data.Tools or {}
ES.Data.Tools[12] = { item = 9149, mask = 1, family = "stone" }
ES.Data.Tools[14] = { item = 6219, mask = 1, family = "spanner" }
ES.Data.Tools[15] = { item = 10498, mask = 2, family = "adjustor" }
ES.Data.Tools[162] = { item = 5956, mask = 4, family = "hammer" }
ES.Data.Tools[373] = { item = 6218, mask = 1, family = "rod" }
ES.Data.Tools[374] = { item = 6339, mask = 3, family = "rod" }
ES.Data.Tools[375] = { item = 11130, mask = 7, family = "rod" }
ES.Data.Tools[376] = { item = 11145, mask = 15, family = "rod" }
ES.Data.Tools[377] = { item = 16207, mask = 31, family = "rod" }

ES.Data.VendorPrices = ES.Data.VendorPrices or {}
ES.Data.SellPrices = ES.Data.SellPrices or {}
ES.Data.VendorPrices[159] = 5
ES.Data.VendorPrices[2880] = 100
ES.Data.VendorPrices[3030] = 2
ES.Data.VendorPrices[4371] = 800
ES.Data.VendorPrices[4389] = 3000
ES.Data.VendorPrices[4399] = 200
ES.Data.VendorPrices[4400] = 2000
ES.Data.VendorPrices[5956] = 18
ES.Data.VendorPrices[6219] = 721
ES.Data.VendorPrices[6530] = 100
ES.Data.VendorPrices[16583] = 10000
ES.Data.SellPrices[159] = 1
ES.Data.SellPrices[774] = 15
ES.Data.SellPrices[814] = 25
ES.Data.SellPrices[818] = 100
ES.Data.SellPrices[1206] = 400
ES.Data.SellPrices[1210] = 250
ES.Data.SellPrices[1529] = 700
ES.Data.SellPrices[1705] = 600
ES.Data.SellPrices[2318] = 15
ES.Data.SellPrices[2319] = 50
ES.Data.SellPrices[2570] = 11
ES.Data.SellPrices[2589] = 13
ES.Data.SellPrices[2592] = 33
ES.Data.SellPrices[2835] = 2
ES.Data.SellPrices[2836] = 15
ES.Data.SellPrices[2838] = 60
ES.Data.SellPrices[2840] = 10
ES.Data.SellPrices[2841] = 50
ES.Data.SellPrices[2842] = 100
ES.Data.SellPrices[2880] = 25
ES.Data.SellPrices[2996] = 40
ES.Data.SellPrices[3575] = 200
ES.Data.SellPrices[3577] = 600
ES.Data.SellPrices[3829] = 150
ES.Data.SellPrices[3859] = 60
ES.Data.SellPrices[3860] = 400
ES.Data.SellPrices[3864] = 800
ES.Data.SellPrices[4234] = 150
ES.Data.SellPrices[4304] = 300
ES.Data.SellPrices[4305] = 600
ES.Data.SellPrices[4306] = 150
ES.Data.SellPrices[4337] = 750
ES.Data.SellPrices[4338] = 250
ES.Data.SellPrices[4339] = 1250
ES.Data.SellPrices[4357] = 4
ES.Data.SellPrices[4358] = 30
ES.Data.SellPrices[4359] = 12
ES.Data.SellPrices[4360] = 60
ES.Data.SellPrices[4361] = 120
ES.Data.SellPrices[4362] = 187
ES.Data.SellPrices[4363] = 50
ES.Data.SellPrices[4364] = 12
ES.Data.SellPrices[4365] = 75
ES.Data.SellPrices[4366] = 75
ES.Data.SellPrices[4367] = 150
ES.Data.SellPrices[4368] = 408
ES.Data.SellPrices[4369] = 790
ES.Data.SellPrices[4370] = 175
ES.Data.SellPrices[4371] = 200
ES.Data.SellPrices[4372] = 1800
ES.Data.SellPrices[4373] = 722
ES.Data.SellPrices[4374] = 200
ES.Data.SellPrices[4375] = 115
ES.Data.SellPrices[4376] = 200
ES.Data.SellPrices[4377] = 150
ES.Data.SellPrices[4378] = 350
ES.Data.SellPrices[4379] = 2357
ES.Data.SellPrices[4380] = 500
ES.Data.SellPrices[4381] = 600
ES.Data.SellPrices[4382] = 600
ES.Data.SellPrices[4383] = 3183
ES.Data.SellPrices[4384] = 1000
ES.Data.SellPrices[4385] = 1410
ES.Data.SellPrices[4386] = 175
ES.Data.SellPrices[4387] = 400
ES.Data.SellPrices[4388] = 1000
ES.Data.SellPrices[4389] = 750
ES.Data.SellPrices[4390] = 125
ES.Data.SellPrices[4391] = 4000
ES.Data.SellPrices[4392] = 2500
ES.Data.SellPrices[4393] = 2632
ES.Data.SellPrices[4394] = 750
ES.Data.SellPrices[4395] = 1600
ES.Data.SellPrices[4396] = 6000
ES.Data.SellPrices[4397] = 5000
ES.Data.SellPrices[4398] = 900
ES.Data.SellPrices[4399] = 50
ES.Data.SellPrices[4400] = 500
ES.Data.SellPrices[4401] = 100
ES.Data.SellPrices[4402] = 250
ES.Data.SellPrices[4403] = 2000
ES.Data.SellPrices[4404] = 25
ES.Data.SellPrices[4405] = 125
ES.Data.SellPrices[4406] = 600
ES.Data.SellPrices[4407] = 1200
ES.Data.SellPrices[4611] = 50
ES.Data.SellPrices[4852] = 300
ES.Data.SellPrices[5507] = 600
ES.Data.SellPrices[5956] = 3
ES.Data.SellPrices[6037] = 1250
ES.Data.SellPrices[6219] = 144
ES.Data.SellPrices[6530] = 25
ES.Data.SellPrices[6533] = 62
ES.Data.SellPrices[6712] = 12
ES.Data.SellPrices[6714] = 75
ES.Data.SellPrices[7067] = 400
ES.Data.SellPrices[7068] = 400
ES.Data.SellPrices[7069] = 400
ES.Data.SellPrices[7075] = 400
ES.Data.SellPrices[7076] = 400
ES.Data.SellPrices[7077] = 400
ES.Data.SellPrices[7078] = 400
ES.Data.SellPrices[7079] = 400
ES.Data.SellPrices[7080] = 400
ES.Data.SellPrices[7082] = 400
ES.Data.SellPrices[7148] = 21
ES.Data.SellPrices[7189] = 4712
ES.Data.SellPrices[7387] = 2587
ES.Data.SellPrices[7506] = 500
ES.Data.SellPrices[7909] = 1000
ES.Data.SellPrices[7910] = 5000
ES.Data.SellPrices[7912] = 100
ES.Data.SellPrices[7972] = 400
ES.Data.SellPrices[8150] = 250
ES.Data.SellPrices[8151] = 250
ES.Data.SellPrices[8153] = 5
ES.Data.SellPrices[8170] = 500
ES.Data.SellPrices[9060] = 1000
ES.Data.SellPrices[9061] = 250
ES.Data.SellPrices[9262] = 1000
ES.Data.SellPrices[9312] = 5
ES.Data.SellPrices[9313] = 5
ES.Data.SellPrices[9318] = 5
ES.Data.SellPrices[10026] = 5459
ES.Data.SellPrices[10285] = 1000
ES.Data.SellPrices[10286] = 400
ES.Data.SellPrices[10498] = 16
ES.Data.SellPrices[10499] = 2105
ES.Data.SellPrices[10500] = 3478
ES.Data.SellPrices[10501] = 4398
ES.Data.SellPrices[10502] = 4088
ES.Data.SellPrices[10503] = 5169
ES.Data.SellPrices[10504] = 7770
ES.Data.SellPrices[10505] = 250
ES.Data.SellPrices[10506] = 5227
ES.Data.SellPrices[10507] = 350
ES.Data.SellPrices[10508] = 8958
ES.Data.SellPrices[10510] = 11369
ES.Data.SellPrices[10512] = 2
ES.Data.SellPrices[10513] = 5
ES.Data.SellPrices[10514] = 750
ES.Data.SellPrices[10518] = 4696
ES.Data.SellPrices[10542] = 5255
ES.Data.SellPrices[10543] = 3517
ES.Data.SellPrices[10545] = 3929
ES.Data.SellPrices[10546] = 1500
ES.Data.SellPrices[10548] = 2500
ES.Data.SellPrices[10558] = 250
ES.Data.SellPrices[10559] = 750
ES.Data.SellPrices[10560] = 1000
ES.Data.SellPrices[10561] = 1000
ES.Data.SellPrices[10562] = 750
ES.Data.SellPrices[10576] = 6000
ES.Data.SellPrices[10577] = 2000
ES.Data.SellPrices[10586] = 750
ES.Data.SellPrices[10587] = 1500
ES.Data.SellPrices[10588] = 5834
ES.Data.SellPrices[10592] = 150
ES.Data.SellPrices[10645] = 750
ES.Data.SellPrices[10646] = 500
ES.Data.SellPrices[10716] = 750
ES.Data.SellPrices[10719] = 1500
ES.Data.SellPrices[10720] = 750
ES.Data.SellPrices[10721] = 3317
ES.Data.SellPrices[10724] = 4697
ES.Data.SellPrices[10725] = 1500
ES.Data.SellPrices[10726] = 5520
ES.Data.SellPrices[10727] = 2000
ES.Data.SellPrices[11175] = 1
ES.Data.SellPrices[11371] = 600
ES.Data.SellPrices[11590] = 250
ES.Data.SellPrices[11825] = 2500
ES.Data.SellPrices[12359] = 600
ES.Data.SellPrices[12360] = 5000
ES.Data.SellPrices[12361] = 7000
ES.Data.SellPrices[12364] = 10000
ES.Data.SellPrices[12365] = 250
ES.Data.SellPrices[12655] = 500
ES.Data.SellPrices[12799] = 7000
ES.Data.SellPrices[12800] = 10000
ES.Data.SellPrices[12803] = 500
ES.Data.SellPrices[12804] = 2000
ES.Data.SellPrices[12808] = 1000
ES.Data.SellPrices[12810] = 500
ES.Data.SellPrices[13467] = 250
ES.Data.SellPrices[14047] = 400
ES.Data.SellPrices[14227] = 2500
ES.Data.SellPrices[14344] = 1
ES.Data.SellPrices[15407] = 500
ES.Data.SellPrices[15846] = 7500
ES.Data.SellPrices[15992] = 250
ES.Data.SellPrices[15993] = 1500
ES.Data.SellPrices[15994] = 2500
ES.Data.SellPrices[15995] = 19739
ES.Data.SellPrices[15996] = 2500
ES.Data.SellPrices[15997] = 10
ES.Data.SellPrices[15999] = 9002
ES.Data.SellPrices[16000] = 3750
ES.Data.SellPrices[16004] = 29152
ES.Data.SellPrices[16005] = 1250
ES.Data.SellPrices[16006] = 10000
ES.Data.SellPrices[16007] = 40625
ES.Data.SellPrices[16008] = 11739
ES.Data.SellPrices[16009] = 5930
ES.Data.SellPrices[16022] = 40000
ES.Data.SellPrices[16023] = 10000
ES.Data.SellPrices[16040] = 4000
ES.Data.SellPrices[16203] = 1
ES.Data.SellPrices[16204] = 1
ES.Data.SellPrices[16583] = 2500
ES.Data.SellPrices[17010] = 2000
ES.Data.SellPrices[17011] = 2000
ES.Data.SellPrices[17056] = 7
ES.Data.SellPrices[17716] = 7500
ES.Data.SellPrices[18168] = 56416
ES.Data.SellPrices[18232] = 10000
ES.Data.SellPrices[18282] = 66347
ES.Data.SellPrices[18283] = 25000
ES.Data.SellPrices[18587] = 2000
ES.Data.SellPrices[18588] = 200
ES.Data.SellPrices[18594] = 3000
ES.Data.SellPrices[18631] = 3000
ES.Data.SellPrices[18634] = 12500
ES.Data.SellPrices[18637] = 600
ES.Data.SellPrices[18638] = 12500
ES.Data.SellPrices[18639] = 12500
ES.Data.SellPrices[18641] = 500
ES.Data.SellPrices[18645] = 1500
ES.Data.SellPrices[18660] = 7500
ES.Data.SellPrices[18984] = 5000
ES.Data.SellPrices[18986] = 5000
ES.Data.SellPrices[19026] = 250
ES.Data.SellPrices[19726] = 500
ES.Data.SellPrices[19774] = 5000
ES.Data.SellPrices[19998] = 23211
ES.Data.SellPrices[19999] = 18639
ES.Data.SellPrices[20725] = 1
ES.Data.SellPrices[21277] = 1250
ES.Data.SellPrices[21557] = 6
ES.Data.SellPrices[21558] = 6
ES.Data.SellPrices[21559] = 6
ES.Data.SellPrices[21560] = 2
ES.Data.SellPrices[21561] = 6
ES.Data.SellPrices[21562] = 6
ES.Data.SellPrices[21571] = 25
ES.Data.SellPrices[21574] = 25
ES.Data.SellPrices[21575] = 25
ES.Data.SellPrices[21576] = 25
ES.Data.SellPrices[21577] = 25
ES.Data.SellPrices[21578] = 25
ES.Data.SellPrices[21589] = 12
ES.Data.SellPrices[21590] = 12
ES.Data.SellPrices[21591] = 12
ES.Data.SellPrices[21592] = 12
ES.Data.SellPrices[21593] = 12
ES.Data.SellPrices[21595] = 12
ES.Data.SellPrices[21714] = 50
ES.Data.SellPrices[21716] = 50
ES.Data.SellPrices[21717] = 50
ES.Data.SellPrices[21718] = 50
ES.Data.SellPrices[21719] = 50
ES.Data.SellPrices[21720] = 50
ES.Data.SellPrices[22202] = 2500
ES.Data.SellPrices[22728] = 5000
ES.Data.SellPrices[213369] = 280
ES.Data.SellPrices[213379] = 280
ES.Data.SellPrices[215430] = 250
ES.Data.SellPrices[248820] = 15000
ES.Data.SellPrices[248822] = 1500
ES.Data.SellPrices[248823] = 150
ES.Data.SellPrices[249391] = 100
ES.Data.SellPrices[249409] = 75
ES.Data.SellPrices[249410] = 125
ES.Data.SellPrices[249425] = 250
ES.Data.SellPrices[249426] = 375
ES.Data.SellPrices[249428] = 250
ES.Data.SellPrices[249429] = 375
ES.Data.SellPrices[249430] = 250
ES.Data.SellPrices[249431] = 375
ES.Data.SellPrices[249432] = 250
ES.Data.SellPrices[249726] = 3000
ES.Data.SellPrices[251290] = 5000
ES.Data.SellPrices[251291] = 1500
ES.Data.SellPrices[255007] = 22
ES.Data.SellPrices[260784] = 4
ES.Data.SellPrices[260792] = 75
ES.Data.SellPrices[260793] = 60
ES.Data.SellPrices[260794] = 150
ES.Data.SellPrices[260795] = 175
ES.Data.SellPrices[260796] = 200
ES.Data.SellPrices[260797] = 200
ES.Data.SellPrices[260798] = 350
ES.Data.SellPrices[260799] = 250
ES.Data.SellPrices[260800] = 1000
ES.Data.SellPrices[260801] = 300
ES.Data.SellPrices[260802] = 2000
ES.Data.SellPrices[260803] = 350
ES.Data.SellPrices[260804] = 1000
ES.Data.SellPrices[260805] = 750
ES.Data.SellPrices[260806] = 5000
ES.Data.SellPrices[260807] = 200
ES.Data.SellPrices[260808] = 1100
ES.Data.SellPrices[260809] = 750
ES.Data.SellPrices[260810] = 4696
ES.Data.SellPrices[260811] = 1000
ES.Data.SellPrices[260812] = 2000
ES.Data.SellPrices[260813] = 1500
ES.Data.SellPrices[260814] = 500
ES.Data.SellPrices[260815] = 2000
ES.Data.SellPrices[260816] = 1500
ES.Data.SellPrices[260817] = 1250
ES.Data.SellPrices[260818] = 4000
ES.Data.SellPrices[260819] = 5000
ES.Data.SellPrices[260820] = 5000
ES.Data.SellPrices[260821] = 5000
ES.Data.SellPrices[260822] = 2500
ES.Data.SellPrices[260823] = 5000
ES.Data.SellPrices[260824] = 5000
ES.Data.SellPrices[260826] = 5000
ES.Data.SellPrices[260827] = 5000
ES.Data.SellPrices[269900] = 500
ES.Data.SellPrices[269902] = 100
ES.Data.SellPrices[277132] = 200
ES.Data.SellPrices[279272] = 25000
ES.Data.SellPrices[279273] = 66347
ES.Data.SellPrices[280306] = 1710
ES.Data.SellPrices[280307] = 1716
ES.Data.SellPrices[280308] = 1033
ES.Data.SellPrices[280310] = 4987
ES.Data.SellPrices[280311] = 3764
ES.Data.SellPrices[280312] = 3784
ES.Data.SellPrices[280313] = 2201
ES.Data.SellPrices[284869] = 1500
ES.Data.SellPrices[285275] = 821
ES.Data.SellPrices[285276] = 4484
ES.Data.SellPrices[285277] = 13124
ES.Data.SellPrices[285278] = 26602

-- Nombre de cada objeto (inglés, del cliente): se muestra mientras el juego no lo ha cargado
ES.Data.ItemNames = ES.Data.ItemNames or {}
ES.Data.ItemNames[159] = "Refreshing Spring Water"
ES.Data.ItemNames[774] = "Malachite"
ES.Data.ItemNames[814] = "Flask of Oil"
ES.Data.ItemNames[818] = "Tigerseye"
ES.Data.ItemNames[1206] = "Moss Agate"
ES.Data.ItemNames[1210] = "Shadowgem"
ES.Data.ItemNames[1529] = "Jade"
ES.Data.ItemNames[1705] = "Lesser Moonstone"
ES.Data.ItemNames[2318] = "Light Leather"
ES.Data.ItemNames[2319] = "Medium Leather"
ES.Data.ItemNames[2570] = "Linen Cloak"
ES.Data.ItemNames[2589] = "Linen Cloth"
ES.Data.ItemNames[2592] = "Wool Cloth"
ES.Data.ItemNames[2835] = "Rough Stone"
ES.Data.ItemNames[2836] = "Coarse Stone"
ES.Data.ItemNames[2838] = "Heavy Stone"
ES.Data.ItemNames[2840] = "Copper Bar"
ES.Data.ItemNames[2841] = "Bronze Bar"
ES.Data.ItemNames[2842] = "Silver Bar"
ES.Data.ItemNames[2880] = "Weak Flux"
ES.Data.ItemNames[2996] = "Bolt of Linen Cloth"
ES.Data.ItemNames[3030] = "Razor Arrow"
ES.Data.ItemNames[3575] = "Iron Bar"
ES.Data.ItemNames[3577] = "Gold Bar"
ES.Data.ItemNames[3829] = "Frost Oil"
ES.Data.ItemNames[3859] = "Steel Bar"
ES.Data.ItemNames[3860] = "Mithril Bar"
ES.Data.ItemNames[3864] = "Citrine"
ES.Data.ItemNames[4234] = "Heavy Leather"
ES.Data.ItemNames[4304] = "Thick Leather"
ES.Data.ItemNames[4305] = "Bolt of Silk Cloth"
ES.Data.ItemNames[4306] = "Silk Cloth"
ES.Data.ItemNames[4337] = "Thick Spider's Silk"
ES.Data.ItemNames[4338] = "Mageweave Cloth"
ES.Data.ItemNames[4339] = "Bolt of Mageweave"
ES.Data.ItemNames[4357] = "Rough Blasting Powder"
ES.Data.ItemNames[4358] = "Rough Dynamite"
ES.Data.ItemNames[4359] = "Handful of Copper Bolts"
ES.Data.ItemNames[4360] = "Rough Copper Bomb"
ES.Data.ItemNames[4361] = "Copper Tube"
ES.Data.ItemNames[4362] = "Rough Boomstick"
ES.Data.ItemNames[4363] = "Copper Modulator"
ES.Data.ItemNames[4364] = "Coarse Blasting Powder"
ES.Data.ItemNames[4365] = "Coarse Dynamite"
ES.Data.ItemNames[4366] = "Target Dummy"
ES.Data.ItemNames[4367] = "Small Seaforium Charge"
ES.Data.ItemNames[4368] = "Flying Tiger Goggles"
ES.Data.ItemNames[4369] = "Deadly Blunderbuss"
ES.Data.ItemNames[4370] = "Large Copper Bomb"
ES.Data.ItemNames[4371] = "Bronze Tube"
ES.Data.ItemNames[4372] = "Lovingly Crafted Boomstick"
ES.Data.ItemNames[4373] = "Shadow Goggles"
ES.Data.ItemNames[4374] = "Small Bronze Bomb"
ES.Data.ItemNames[4375] = "Whirring Bronze Gizmo"
ES.Data.ItemNames[4376] = "Flame Deflector"
ES.Data.ItemNames[4377] = "Heavy Blasting Powder"
ES.Data.ItemNames[4378] = "Heavy Dynamite"
ES.Data.ItemNames[4379] = "Silver-plated Shotgun"
ES.Data.ItemNames[4380] = "Big Bronze Bomb"
ES.Data.ItemNames[4381] = "Minor Recombobulator"
ES.Data.ItemNames[4382] = "Bronze Framework"
ES.Data.ItemNames[4383] = "Moonsight Rifle"
ES.Data.ItemNames[4384] = "Explosive Sheep"
ES.Data.ItemNames[4385] = "Green Tinted Goggles"
ES.Data.ItemNames[4386] = "Ice Deflector"
ES.Data.ItemNames[4387] = "Iron Strut"
ES.Data.ItemNames[4388] = "Discombobulator Ray"
ES.Data.ItemNames[4389] = "Gyrochronatom"
ES.Data.ItemNames[4390] = "Iron Grenade"
ES.Data.ItemNames[4391] = "Compact Harvest Reaper Kit"
ES.Data.ItemNames[4392] = "Advanced Target Dummy"
ES.Data.ItemNames[4393] = "Craftsman's Monocle"
ES.Data.ItemNames[4394] = "Big Iron Bomb"
ES.Data.ItemNames[4395] = "Goblin Land Mine"
ES.Data.ItemNames[4396] = "Mechanical Dragonling"
ES.Data.ItemNames[4397] = "Gnomish Cloaking Device"
ES.Data.ItemNames[4398] = "Large Seaforium Charge"
ES.Data.ItemNames[4399] = "Wooden Stock"
ES.Data.ItemNames[4400] = "Heavy Stock"
ES.Data.ItemNames[4401] = "Mechanical Squirrel Box"
ES.Data.ItemNames[4402] = "Small Flame Sac"
ES.Data.ItemNames[4403] = "Portable Bronze Mortar"
ES.Data.ItemNames[4404] = "Silver Contact"
ES.Data.ItemNames[4405] = "Crude Scope"
ES.Data.ItemNames[4406] = "Standard Scope"
ES.Data.ItemNames[4407] = "Accurate Scope"
ES.Data.ItemNames[4611] = "Blue Pearl"
ES.Data.ItemNames[4852] = "Flash Bomb"
ES.Data.ItemNames[5507] = "Ornate Spyglass"
ES.Data.ItemNames[5956] = "Blacksmith Hammer"
ES.Data.ItemNames[6037] = "Truesilver Bar"
ES.Data.ItemNames[6219] = "Arclight Spanner"
ES.Data.ItemNames[6530] = "Nightcrawlers"
ES.Data.ItemNames[6533] = "Aquadynamic Fish Attractor"
ES.Data.ItemNames[6712] = "Practice Lock"
ES.Data.ItemNames[6714] = "Ez-Thro Dynamite"
ES.Data.ItemNames[7067] = "Elemental Earth"
ES.Data.ItemNames[7068] = "Elemental Fire"
ES.Data.ItemNames[7069] = "Elemental Air"
ES.Data.ItemNames[7075] = "Core of Earth"
ES.Data.ItemNames[7076] = "Essence of Earth"
ES.Data.ItemNames[7077] = "Heart of Fire"
ES.Data.ItemNames[7078] = "Essence of Fire"
ES.Data.ItemNames[7079] = "Globe of Water"
ES.Data.ItemNames[7080] = "Essence of Water"
ES.Data.ItemNames[7082] = "Essence of Air"
ES.Data.ItemNames[7148] = "Goblin Jumper Cables"
ES.Data.ItemNames[7189] = "Goblin Rocket Boots"
ES.Data.ItemNames[7191] = "Fused Wiring"
ES.Data.ItemNames[7387] = "Dusky Belt"
ES.Data.ItemNames[7506] = "Gnomish Universal Remote"
ES.Data.ItemNames[7909] = "Aquamarine"
ES.Data.ItemNames[7910] = "Star Ruby"
ES.Data.ItemNames[7912] = "Solid Stone"
ES.Data.ItemNames[7972] = "Ichor of Undeath"
ES.Data.ItemNames[8067] = "Crafted Light Shot"
ES.Data.ItemNames[8068] = "Crafted Heavy Shot"
ES.Data.ItemNames[8069] = "Crafted Solid Shot"
ES.Data.ItemNames[8150] = "Deeprock Salt"
ES.Data.ItemNames[8151] = "Flask of Mojo"
ES.Data.ItemNames[8153] = "Wildvine"
ES.Data.ItemNames[8170] = "Rugged Leather"
ES.Data.ItemNames[9060] = "Inlaid Mithril Cylinder"
ES.Data.ItemNames[9061] = "Goblin Rocket Fuel"
ES.Data.ItemNames[9262] = "Black Vitriol"
ES.Data.ItemNames[9312] = "Blue Firework"
ES.Data.ItemNames[9313] = "Green Firework"
ES.Data.ItemNames[9318] = "Red Firework"
ES.Data.ItemNames[10026] = "Black Mageweave Boots"
ES.Data.ItemNames[10285] = "Shadow Silk"
ES.Data.ItemNames[10286] = "Heart of the Wild"
ES.Data.ItemNames[10498] = "Gyromatic Micro-Adjustor"
ES.Data.ItemNames[10499] = "Bright-Eye Goggles"
ES.Data.ItemNames[10500] = "Fire Goggles"
ES.Data.ItemNames[10501] = "Catseye Ultra Goggles"
ES.Data.ItemNames[10502] = "Spellpower Goggles Xtreme"
ES.Data.ItemNames[10503] = "Rose Colored Goggles"
ES.Data.ItemNames[10504] = "Green Lens"
ES.Data.ItemNames[10505] = "Solid Blasting Powder"
ES.Data.ItemNames[10506] = "Deepdive Helmet"
ES.Data.ItemNames[10507] = "Solid Dynamite"
ES.Data.ItemNames[10508] = "Mithril Blunderbuss"
ES.Data.ItemNames[10510] = "Mithril Heavy-bore Rifle"
ES.Data.ItemNames[10512] = "Hi-Impact Mithril Slugs"
ES.Data.ItemNames[10513] = "Mithril Gyro-Shot"
ES.Data.ItemNames[10514] = "Mithril Frag Bomb"
ES.Data.ItemNames[10518] = "Parachute Cloak"
ES.Data.ItemNames[10542] = "Goblin Mining Helmet"
ES.Data.ItemNames[10543] = "Goblin Construction Helmet"
ES.Data.ItemNames[10545] = "Gnomish Goggles"
ES.Data.ItemNames[10546] = "Deadly Scope"
ES.Data.ItemNames[10548] = "Sniper Scope"
ES.Data.ItemNames[10558] = "Gold Power Core"
ES.Data.ItemNames[10559] = "Mithril Tube"
ES.Data.ItemNames[10560] = "Unstable Trigger"
ES.Data.ItemNames[10561] = "Mithril Casing"
ES.Data.ItemNames[10562] = "Hi-Explosive Bomb"
ES.Data.ItemNames[10576] = "Mithril Mechanical Dragonling"
ES.Data.ItemNames[10577] = "Goblin Mortar"
ES.Data.ItemNames[10579] = "Explosive Arrow"
ES.Data.ItemNames[10586] = "The Big One"
ES.Data.ItemNames[10587] = "Goblin Bomb Dispenser"
ES.Data.ItemNames[10588] = "Goblin Rocket Helmet"
ES.Data.ItemNames[10592] = "Catseye Draught"
ES.Data.ItemNames[10645] = "Gnomish Death Ray"
ES.Data.ItemNames[10646] = "Goblin Sapper Charge"
ES.Data.ItemNames[10716] = "Gnomish Shrink Ray"
ES.Data.ItemNames[10719] = "Mobile Alarm"
ES.Data.ItemNames[10720] = "Gnomish Net-o-Matic Projector"
ES.Data.ItemNames[10721] = "Gnomish Harm Prevention Belt"
ES.Data.ItemNames[10724] = "Gnomish Rocket Boots"
ES.Data.ItemNames[10725] = "Gnomish Battle Chicken"
ES.Data.ItemNames[10726] = "Gnomish Mind Control Cap"
ES.Data.ItemNames[10727] = "Goblin Dragon Gun"
ES.Data.ItemNames[11175] = "Greater Nether Essence"
ES.Data.ItemNames[11371] = "Dark Iron Bar"
ES.Data.ItemNames[11590] = "Mechanical Repair Kit"
ES.Data.ItemNames[11825] = "Pet Bombling"
ES.Data.ItemNames[12359] = "Thorium Bar"
ES.Data.ItemNames[12360] = "Arcanite Bar"
ES.Data.ItemNames[12361] = "Blue Sapphire"
ES.Data.ItemNames[12364] = "Huge Emerald"
ES.Data.ItemNames[12365] = "Dense Stone"
ES.Data.ItemNames[12655] = "Enchanted Thorium Bar"
ES.Data.ItemNames[12799] = "Large Opal"
ES.Data.ItemNames[12800] = "Azerothian Diamond"
ES.Data.ItemNames[12803] = "Living Essence"
ES.Data.ItemNames[12804] = "Powerful Mojo"
ES.Data.ItemNames[12808] = "Essence of Undeath"
ES.Data.ItemNames[12810] = "Enchanted Leather"
ES.Data.ItemNames[13467] = "Icecap"
ES.Data.ItemNames[14047] = "Runecloth"
ES.Data.ItemNames[14227] = "Ironweb Spider Silk"
ES.Data.ItemNames[14344] = "Large Brilliant Shard"
ES.Data.ItemNames[15407] = "Cured Rugged Hide"
ES.Data.ItemNames[15846] = "Salt Shaker"
ES.Data.ItemNames[15992] = "Dense Blasting Powder"
ES.Data.ItemNames[15993] = "Thorium Grenade"
ES.Data.ItemNames[15994] = "Thorium Widget"
ES.Data.ItemNames[15995] = "Thorium Rifle"
ES.Data.ItemNames[15996] = "Lifelike Mechanical Toad"
ES.Data.ItemNames[15997] = "Thorium Shells"
ES.Data.ItemNames[15999] = "Spellpower Goggles Xtreme Plus"
ES.Data.ItemNames[16000] = "Thorium Tube"
ES.Data.ItemNames[16004] = "Dark Iron Rifle"
ES.Data.ItemNames[16005] = "Dark Iron Bomb"
ES.Data.ItemNames[16006] = "Delicate Arcanite Converter"
ES.Data.ItemNames[16007] = "Flawless Arcanite Rifle"
ES.Data.ItemNames[16008] = "Master Engineer's Goggles"
ES.Data.ItemNames[16009] = "Voice Amplification Modulator"
ES.Data.ItemNames[16022] = "Arcanite Dragonling"
ES.Data.ItemNames[16023] = "Masterwork Target Dummy"
ES.Data.ItemNames[16040] = "Arcane Bomb"
ES.Data.ItemNames[16203] = "Greater Eternal Essence"
ES.Data.ItemNames[16204] = "Illusion Dust"
ES.Data.ItemNames[16583] = "Demonic Figurine"
ES.Data.ItemNames[17010] = "Fiery Core"
ES.Data.ItemNames[17011] = "Lava Core"
ES.Data.ItemNames[17056] = "Light Feather"
ES.Data.ItemNames[17202] = "Snowball"
ES.Data.ItemNames[17716] = "Snowmaster 9000"
ES.Data.ItemNames[18168] = "Force Reactive Disk"
ES.Data.ItemNames[18232] = "Field Repair Bot 74A"
ES.Data.ItemNames[18282] = "Core Marksman Rifle"
ES.Data.ItemNames[18283] = "Biznicks 247x128 Accurascope"
ES.Data.ItemNames[18587] = "Goblin Jumper Cables XL"
ES.Data.ItemNames[18588] = "Ez-Thro Dynamite II"
ES.Data.ItemNames[18594] = "Powerful Seaforium Charge"
ES.Data.ItemNames[18631] = "Truesilver Transformer"
ES.Data.ItemNames[18634] = "Gyrofreeze Ice Reflector"
ES.Data.ItemNames[18637] = "Major Recombobulator"
ES.Data.ItemNames[18638] = "Hyper-Radiant Flame Reflector"
ES.Data.ItemNames[18639] = "Ultra-Flash Shadow Reflector"
ES.Data.ItemNames[18641] = "Dense Dynamite"
ES.Data.ItemNames[18645] = "Gnomish Alarm-O-Bot"
ES.Data.ItemNames[18660] = "World Enlarger"
ES.Data.ItemNames[18984] = "Dimensional Ripper - Everlook"
ES.Data.ItemNames[18986] = "Ultrasafe Transporter: Gadgetzan"
ES.Data.ItemNames[19026] = "Snake Burst Firework"
ES.Data.ItemNames[19726] = "Bloodvine"
ES.Data.ItemNames[19774] = "Souldarite"
ES.Data.ItemNames[19998] = "Bloodvine Lens"
ES.Data.ItemNames[19999] = "Bloodvine Goggles"
ES.Data.ItemNames[20725] = "Nexus Crystal"
ES.Data.ItemNames[21277] = "Tranquil Mechanical Yeti"
ES.Data.ItemNames[21557] = "Small Red Rocket"
ES.Data.ItemNames[21558] = "Small Blue Rocket"
ES.Data.ItemNames[21559] = "Small Green Rocket"
ES.Data.ItemNames[21560] = "Small Purple Rocket"
ES.Data.ItemNames[21561] = "Small White Rocket"
ES.Data.ItemNames[21562] = "Small Yellow Rocket"
ES.Data.ItemNames[21569] = "Firework Launcher"
ES.Data.ItemNames[21570] = "Cluster Launcher"
ES.Data.ItemNames[21571] = "Blue Rocket Cluster"
ES.Data.ItemNames[21574] = "Green Rocket Cluster"
ES.Data.ItemNames[21575] = "Purple Rocket Cluster"
ES.Data.ItemNames[21576] = "Red Rocket Cluster"
ES.Data.ItemNames[21577] = "White Rocket Cluster"
ES.Data.ItemNames[21578] = "Yellow Rocket Cluster"
ES.Data.ItemNames[21589] = "Large Blue Rocket"
ES.Data.ItemNames[21590] = "Large Green Rocket"
ES.Data.ItemNames[21591] = "Large Purple Rocket"
ES.Data.ItemNames[21592] = "Large Red Rocket"
ES.Data.ItemNames[21593] = "Large White Rocket"
ES.Data.ItemNames[21595] = "Large Yellow Rocket"
ES.Data.ItemNames[21714] = "Large Blue Rocket Cluster"
ES.Data.ItemNames[21716] = "Large Green Rocket Cluster"
ES.Data.ItemNames[21717] = "Large Purple Rocket Cluster"
ES.Data.ItemNames[21718] = "Large Red Rocket Cluster"
ES.Data.ItemNames[21719] = "Large White Rocket Cluster"
ES.Data.ItemNames[21720] = "Large Yellow Rocket Cluster"
ES.Data.ItemNames[22202] = "Small Obsidian Shard"
ES.Data.ItemNames[22728] = "Steam Tonk Controller"
ES.Data.ItemNames[210147] = "Shredder Autosalvage Unit"
ES.Data.ItemNames[211427] = "Soul Vessel"
ES.Data.ItemNames[213369] = "Faintly Glowing Leather"
ES.Data.ItemNames[213376] = "Low-Background Truesilver Plates"
ES.Data.ItemNames[213379] = "Hyperconductive Arcano-Filament"
ES.Data.ItemNames[213381] = "Pile of Tarnished Gears"
ES.Data.ItemNames[213383] = "Polished Truesilver Gears"
ES.Data.ItemNames[215430] = "Gnomeregan Fallout"
ES.Data.ItemNames[237023] = "Pop-Up Shrub"
ES.Data.ItemNames[248820] = "Torbernite"
ES.Data.ItemNames[248822] = "Death Lotus"
ES.Data.ItemNames[248823] = "Marefoil"
ES.Data.ItemNames[249391] = "Pyrite"
ES.Data.ItemNames[249409] = "Cerulean Dye"
ES.Data.ItemNames[249410] = "Sulfuric Acid"
ES.Data.ItemNames[249425] = "Bauxite"
ES.Data.ItemNames[249426] = "Pitchblende"
ES.Data.ItemNames[249428] = "Pristine Hide"
ES.Data.ItemNames[249429] = "Pristine Scale"
ES.Data.ItemNames[249430] = "Magenta Dye"
ES.Data.ItemNames[249431] = "Viridian Dye"
ES.Data.ItemNames[249432] = "Sandpaper"
ES.Data.ItemNames[249726] = "Azerothium Bar"
ES.Data.ItemNames[251290] = "Legionite Bar"
ES.Data.ItemNames[251291] = "Heavy Thorium Bar"
ES.Data.ItemNames[255007] = "Golem Isospring"
ES.Data.ItemNames[260784] = "SAF-T Tabs"
ES.Data.ItemNames[260792] = "SAF-T Dynamite"
ES.Data.ItemNames[260793] = "SAF-T Copper Bomb"
ES.Data.ItemNames[260794] = "EZ-Thro Wrap"
ES.Data.ItemNames[260795] = "EZ-Thro Copper Bomb XL"
ES.Data.ItemNames[260796] = "No Slip SAF-T Padding"
ES.Data.ItemNames[260797] = "SAF-T Bronze Bomb"
ES.Data.ItemNames[260798] = "SAF-T Jumbo Dynamite"
ES.Data.ItemNames[260799] = "SAF-T Bell"
ES.Data.ItemNames[260800] = "Shafety Sheep"
ES.Data.ItemNames[260801] = "EZ-Thro Fireproof Fuse"
ES.Data.ItemNames[260802] = "EZ-Thro Bronze Mortar"
ES.Data.ItemNames[260803] = "EZ-Thro Grenade"
ES.Data.ItemNames[260804] = "SAF-T Casing"
ES.Data.ItemNames[260805] = "SAF-T Bomb"
ES.Data.ItemNames[260806] = "Emergency Field Cloak"
ES.Data.ItemNames[260807] = "Compact Critter Carrier"
ES.Data.ItemNames[260808] = "EZ-Thro Tru-Trigger"
ES.Data.ItemNames[260809] = "Tru-Trigger Frag Bomb"
ES.Data.ItemNames[260810] = "SAF-T Disposable Parachute"
ES.Data.ItemNames[260811] = "Gnomish Army Knife"
ES.Data.ItemNames[260812] = "Loot-A-Rang"
ES.Data.ItemNames[260813] = "SAF-T Tube"
ES.Data.ItemNames[260814] = "SAF-T Clever Dynamite"
ES.Data.ItemNames[260815] = "EZ-Thro Shell"
ES.Data.ItemNames[260816] = "EZ-Thro Thorium Grenade"
ES.Data.ItemNames[260817] = "EZ-Thro Dark Bomb"
ES.Data.ItemNames[260818] = "EZ-Thro Mana Bomb"
ES.Data.ItemNames[260819] = "EZ-Thro Field Transporter: Gadgetzan"
ES.Data.ItemNames[260820] = "SAF-T Emergency Ripper: Everlook"
ES.Data.ItemNames[260821] = "EZ and SAF Field Transporter: Mt. Hyjal"
ES.Data.ItemNames[260822] = "Ultrasafe Rechargeable Battery"
ES.Data.ItemNames[260823] = "Dimensional Transporter - Mt. Hyjal"
ES.Data.ItemNames[260824] = "Gnomish Poultryizer"
ES.Data.ItemNames[260825] = "Ultralight Goblin Glider"
ES.Data.ItemNames[260826] = "Gnomish Weather Machine NYI"
ES.Data.ItemNames[260827] = "Stealthman 52"
ES.Data.ItemNames[269900] = "Centaur Banner Deployment Device"
ES.Data.ItemNames[269902] = "Hoof-Shaped Foot Pedal"
ES.Data.ItemNames[274030] = "Malleable Essence of Nature"
ES.Data.ItemNames[274387] = "Swiftfeather Arrow"
ES.Data.ItemNames[274388] = "Swiftstrike Shot"
ES.Data.ItemNames[277132] = "Harvester Override Signalcaster"
ES.Data.ItemNames[279272] = "SAF-T Ultra Precision Scope"
ES.Data.ItemNames[279273] = "Hyper Deluxe Sniper Rifle Mk XVII"
ES.Data.ItemNames[279949] = "Repair Bot"
ES.Data.ItemNames[279950] = "Reagent Bot"
ES.Data.ItemNames[280306] = "Whimsical Waistwrap"
ES.Data.ItemNames[280307] = "Gizmo Girdle"
ES.Data.ItemNames[280308] = "Clanking Cord"
ES.Data.ItemNames[280310] = "Floppy Goggles"
ES.Data.ItemNames[280311] = "Bent Goggles"
ES.Data.ItemNames[280312] = "Stuckbutton Goggles"
ES.Data.ItemNames[280313] = "Dented Goggles"
ES.Data.ItemNames[284869] = "Unsanctified Grenade"
ES.Data.ItemNames[285275] = "Satchel of Copper Bombs"
ES.Data.ItemNames[285276] = "Satchel of Bronze Bombs"
ES.Data.ItemNames[285277] = "Satchel of Iron Bombs"
ES.Data.ItemNames[285278] = "Satchel of Dark Iron Bombs"

-- Material -> profesión de recolección que lo consigue (393 Desuello, 182 Herboristería, 186 Minería).
-- Sin uso por ahora: reservado para la vía "Vender en bruto" de Ganar dinero (docs/PLAN.md, G1).
ES.Data.GatheredBy = ES.Data.GatheredBy or {}
ES.Data.GatheredBy[2318] = 393
ES.Data.GatheredBy[2319] = 393
ES.Data.GatheredBy[2835] = 186
ES.Data.GatheredBy[2836] = 186
ES.Data.GatheredBy[2838] = 186
ES.Data.GatheredBy[2840] = 186
ES.Data.GatheredBy[2841] = 186
ES.Data.GatheredBy[2842] = 186
ES.Data.GatheredBy[3575] = 186
ES.Data.GatheredBy[3859] = 186
ES.Data.GatheredBy[3860] = 186
ES.Data.GatheredBy[4234] = 393
ES.Data.GatheredBy[4304] = 393
ES.Data.GatheredBy[7912] = 186
ES.Data.GatheredBy[8150] = 186
ES.Data.GatheredBy[8153] = 182
ES.Data.GatheredBy[8170] = 393
ES.Data.GatheredBy[11371] = 186
ES.Data.GatheredBy[12359] = 186
ES.Data.GatheredBy[12365] = 186
ES.Data.GatheredBy[13467] = 182
ES.Data.GatheredBy[19726] = 182
ES.Data.GatheredBy[22202] = 186
ES.Data.GatheredBy[248822] = 182
ES.Data.GatheredBy[248823] = 182
ES.Data.GatheredBy[249391] = 186
ES.Data.GatheredBy[249425] = 186
ES.Data.GatheredBy[249426] = 186
ES.Data.GatheredBy[249428] = 393
ES.Data.GatheredBy[249429] = 393
ES.Data.GatheredBy[249726] = 186
ES.Data.GatheredBy[251291] = 186

```

---

## FirstAid

```lua
-- Generado por tools/gen_profession.py (FirstAid). No editar a mano.
-- Datos: cliente de WoW Forever (wago.tools DB2), instructores de CMaNGOS classic-db, vendedores de QuestieDB.
local _, ES = ...
ES.Data = ES.Data or {}

-- t = { naranja, amarilla, verde, gris }; fee/train = precio y habilidad del instructor
-- (sin fee = se aprende de pergamino: de dónde sale, en Data/Sources.lua; scrollPrice = su precio si lo vende un PNJ)
-- rep = { facción, nivel } que pide el pergamino para aprenderla (5 amistoso, 6 honorable, 7 venerado, 8 exaltado)
-- r = { {itemID, cantidad} }; out = { itemID, cantidad }
-- sq / oq = calidad del pergamino / de lo fabricado (0 pobre, 1 común, 2 poco común, 3 raro, 4 épico)
-- faction = bando que puede aprenderla, si solo es de uno
-- bop = lo fabricado se liga al recogerlo: no se puede vender en la AH (sí al vendedor)
-- favor / favorRep = se compra con Merchant's Favor en el campamento de tu bando, y la reputación que pide
-- train ajustado a Forever: nivel de Classic menos lo que Forever bajó la amarilla de esa receta
-- basic = se aprende sola al coger la profesión; trainer = de instructor sin precio conocido
--   (receta nueva de Forever que no está en CMaNGOS: se aprende al ponerse amarilla)
ES.Data.FirstAid = {
  skillLine = 129,
  ranks = { -- { tope, precio, habilidad requerida, nivel de personaje }
    { 150, 500, 50, 0 },
    { 225, 10000, 125, 35 },
    { 300, 0, 225, 35 },
  },
  -- { PNJ instructor, rangos que enseña: 1 aprendiz (75), 2 oficial (150), 4 experto (225), 8 artesano (300) }
  trainers = { { 2326, 3 }, { 2327, 3 }, { 2329, 3 }, { 2798, 3 }, { 3181, 3 }, { 3373, 3 }, { 4211, 3 }, { 4591, 3 }, { 5150, 3 }, { 5759, 3 }, { 5939, 3 }, { 5943, 3 }, { 6094, 3 }, { 251977, 3 } },
  recipes = {
    [3275] = { name = "Linen Bandage", t = { 1, 30, 45, 60 }, basic = true, r = { { 2589, 1 } }, out = { 1251, 1 }, oq = 1 },
    [3276] = { name = "Heavy Linen Bandage", t = { 1, 50, 75, 100 }, fee = 100, train = 40, r = { { 2589, 2 } }, out = { 2581, 1 }, oq = 1 },
    [3277] = { name = "Wool Bandage", t = { 1, 80, 115, 150 }, fee = 250, train = 80, r = { { 2592, 1 } }, out = { 3530, 1 }, oq = 1 },
    [3278] = { name = "Heavy Wool Bandage", t = { 1, 115, 150, 185 }, fee = 1000, train = 115, r = { { 2592, 2 } }, out = { 3531, 1 }, oq = 1 },
    [7928] = { name = "Silk Bandage", t = { 1, 150, 180, 210 }, fee = 5000, train = 150, r = { { 4306, 1 } }, out = { 6450, 1 }, oq = 1 },
    [7929] = { name = "Heavy Silk Bandage", t = { 1, 180, 210, 240 }, scroll = 16112, train = 180, scrollPrice = 2200, sq = 1, r = { { 4306, 2 } }, out = { 6451, 1 }, oq = 1 },
    [7934] = { name = "Anti-Venom", t = { 1, 80, 115, 150 }, fee = 250, train = 80, r = { { 1475, 1 } }, out = { 6452, 3 }, oq = 1 },
    [7935] = { name = "Strong Anti-Venom", t = { 1, 130, 165, 200 }, scroll = 6454, train = 130, sq = 2, r = { { 1288, 1 } }, out = { 6453, 3 }, oq = 1 },
    [10840] = { name = "Mageweave Bandage", t = { 1, 210, 240, 270 }, scroll = 16113, train = 210, scrollPrice = 5000, sq = 1, r = { { 4338, 1 } }, out = { 8544, 1 }, oq = 1 },
    [10841] = { name = "Heavy Mageweave Bandage", t = { 1, 240, 270, 300 }, gone = true, r = { { 4338, 2 } }, out = { 8545, 1 }, oq = 1 },
    [18629] = { name = "Runecloth Bandage", t = { 1, 260, 290, 320 }, gone = true, r = { { 14047, 1 } }, out = { 14529, 1 }, oq = 1 },
    [18630] = { name = "Heavy Runecloth Bandage", t = { 1, 290, 320, 350 }, gone = true, r = { { 14047, 2 } }, out = { 14530, 1 }, oq = 1 },
    [23787] = { name = "Powerful Anti-Venom", t = { 1, 300, 330, 360 }, scroll = 19442, train = 300, scrollPrice = 100000, rep = { 529, 5 }, sq = 1, r = { { 19441, 1 } }, out = { 19440, 3 }, oq = 1 },
    [30021] = { name = "Crystal Infused Bandage", t = { 1, 300, 330, 360 }, scroll = 23689, train = 290, sq = 1, r = { { 23567, 1 }, { 14047, 10 } }, out = { 23684, 4 }, oq = 1 },
    [470349] = { name = "Dense Runecloth Bandage", t = { 1, 315, 327, 340 }, scroll = 232434, train = 300, gone = true, sq = 1, r = { { 14530, 2 } }, out = { 232433, 1 }, oq = 1 },
    [1230117] = { name = "First Aid Kit", t = { 1, 20, 20, 20 }, fee = 100, train = 20, r = { { 1251, 3 }, { 159, 1 } }, out = { 279968, 1 }, oq = 1 },
    [1244431] = { name = "Minor Healing Potion", t = { 1, 55, 75, 95 }, fee = 100, train = 1, r = { { 3371, 1 }, { 2678, 1 }, { 2447, 1 } }, out = { 118, 1 }, oq = 1 },
    [1244432] = { name = "Lesser Healing Potion", t = { 1, 85, 105, 125 }, fee = 150, train = 55, r = { { 3371, 1 }, { 2678, 2 }, { 2450, 1 } }, out = { 858, 1 }, oq = 1 },
    [1244433] = { name = "Healing Potion", t = { 1, 135, 155, 175 }, fee = 800, train = 110, r = { { 3372, 1 }, { 2692, 1 }, { 2453, 1 } }, out = { 929, 1 }, oq = 1 },
    [1244434] = { name = "Greater Healing Potion", t = { 1, 175, 195, 215 }, scroll = 255723, train = 155, sq = 2, r = { { 3372, 1 }, { 2692, 3 }, { 3357, 1 } }, out = { 1710, 1 }, oq = 1 },
    [1244435] = { name = "Superior Healing Potion", t = { 1, 230, 250, 270 }, scroll = 255725, train = 215, sq = 2, r = { { 8925, 1 }, { 3713, 1 }, { 8838, 1 } }, out = { 3928, 1 }, oq = 1 },
    [1244436] = { name = "Major Healing Potion", t = { 1, 290, 310, 330 }, scroll = 255729, train = 275, scrollPrice = 80000, sq = 2, r = { { 8925, 1 }, { 3713, 3 }, { 13464, 1 } }, out = { 13446, 1 }, oq = 1 },
    [1259341] = { name = "Potent Anti-Venom", t = { 1, 230, 260, 290 }, scroll = 255728, train = 215, sq = 2, r = { { 255645, 1 } }, out = { 255715, 3 }, oq = 1 },
    [1259342] = { name = "Simple Poultice", t = { 1, 90, 125, 160 }, fee = 250, train = 90, r = { { 3174, 1 }, { 2678, 1 }, { 2723, 1 } }, out = { 255716, 3 }, oq = 1 },
    [1259343] = { name = "Clever Poultice", t = { 1, 160, 190, 220 }, scroll = 255724, train = 140, sq = 2, r = { { 1468, 1 }, { 3713, 1 }, { 2686, 1 } }, out = { 255717, 3 }, oq = 1 },
    [1259344] = { name = "Superior Poultice", t = { 1, 225, 255, 285 }, scroll = 255727, train = 210, sq = 2, r = { { 7070, 1 }, { 2692, 1 }, { 2596, 1 } }, out = { 255718, 3 }, oq = 1 },
    [1259345] = { name = "Powerful Poultice", t = { 1, 295, 325, 355 }, scroll = 255731, train = 280, sq = 2, r = { { 7080, 1 }, { 2692, 1 }, { 2594, 1 } }, out = { 255719, 3 }, oq = 1 },
    [1259347] = { name = "Woolen Tourniquet", t = { 1, 120, 155, 190 }, fee = 1200, train = 120, r = { { 2592, 2 }, { 2321, 2 } }, out = { 255720, 1 }, oq = 1 },
    [1259348] = { name = "Leather Tourniquet", t = { 1, 220, 250, 280 }, scroll = 255726, train = 200, sq = 2, r = { { 4304, 2 }, { 4291, 2 } }, out = { 255721, 1 }, oq = 1 },
    [1259349] = { name = "Surgical Tourniquet", t = { 1, 280, 310, 340 }, scroll = 255730, train = 265, sq = 2, r = { { 8170, 2 }, { 14047, 2 }, { 8343, 2 } }, out = { 255722, 1 }, oq = 1 },
    [1262996] = { name = "Toxin Study", t = { 1, 140, 140, 140 }, scroll = 273105, train = 140, sq = 2, r = { { 6452, 1 }, { 8544, 2 }, { 4470, 2 } }, out = { 279940, 1 }, oq = 1 },
  },
}

-- Herramientas: [categoría] = { objeto, máscara } (un bastón superior cubre a los inferiores)
ES.Data.Tools = ES.Data.Tools or {}
ES.Data.Tools[12] = { item = 9149, mask = 1, family = "stone" }
ES.Data.Tools[14] = { item = 6219, mask = 1, family = "spanner" }
ES.Data.Tools[15] = { item = 10498, mask = 2, family = "adjustor" }
ES.Data.Tools[162] = { item = 5956, mask = 4, family = "hammer" }
ES.Data.Tools[373] = { item = 6218, mask = 1, family = "rod" }
ES.Data.Tools[374] = { item = 6339, mask = 3, family = "rod" }
ES.Data.Tools[375] = { item = 11130, mask = 7, family = "rod" }
ES.Data.Tools[376] = { item = 11145, mask = 15, family = "rod" }
ES.Data.Tools[377] = { item = 16207, mask = 31, family = "rod" }

ES.Data.VendorPrices = ES.Data.VendorPrices or {}
ES.Data.SellPrices = ES.Data.SellPrices or {}
ES.Data.VendorPrices[159] = 5
ES.Data.VendorPrices[2321] = 100
ES.Data.VendorPrices[2594] = 1500
ES.Data.VendorPrices[2596] = 120
ES.Data.VendorPrices[2678] = 2
ES.Data.VendorPrices[2686] = 50
ES.Data.VendorPrices[2692] = 40
ES.Data.VendorPrices[2723] = 50
ES.Data.VendorPrices[3371] = 4
ES.Data.VendorPrices[3372] = 40
ES.Data.VendorPrices[3713] = 160
ES.Data.VendorPrices[4291] = 500
ES.Data.VendorPrices[4470] = 38
ES.Data.VendorPrices[8343] = 2000
ES.Data.VendorPrices[8925] = 500
ES.Data.SellPrices[118] = 5
ES.Data.SellPrices[159] = 1
ES.Data.SellPrices[858] = 25
ES.Data.SellPrices[929] = 75
ES.Data.SellPrices[1251] = 10
ES.Data.SellPrices[1288] = 185
ES.Data.SellPrices[1468] = 28
ES.Data.SellPrices[1475] = 82
ES.Data.SellPrices[1710] = 125
ES.Data.SellPrices[2321] = 25
ES.Data.SellPrices[2447] = 10
ES.Data.SellPrices[2450] = 25
ES.Data.SellPrices[2453] = 25
ES.Data.SellPrices[2581] = 20
ES.Data.SellPrices[2589] = 13
ES.Data.SellPrices[2592] = 33
ES.Data.SellPrices[2594] = 375
ES.Data.SellPrices[2596] = 30
ES.Data.SellPrices[2678] = 1
ES.Data.SellPrices[2686] = 12
ES.Data.SellPrices[2692] = 10
ES.Data.SellPrices[2723] = 12
ES.Data.SellPrices[3174] = 16
ES.Data.SellPrices[3357] = 75
ES.Data.SellPrices[3371] = 1
ES.Data.SellPrices[3372] = 10
ES.Data.SellPrices[3530] = 28
ES.Data.SellPrices[3531] = 57
ES.Data.SellPrices[3713] = 40
ES.Data.SellPrices[3928] = 250
ES.Data.SellPrices[4291] = 125
ES.Data.SellPrices[4304] = 300
ES.Data.SellPrices[4306] = 150
ES.Data.SellPrices[4338] = 250
ES.Data.SellPrices[4470] = 9
ES.Data.SellPrices[6450] = 200
ES.Data.SellPrices[6451] = 400
ES.Data.SellPrices[6452] = 28
ES.Data.SellPrices[6453] = 62
ES.Data.SellPrices[7070] = 400
ES.Data.SellPrices[7080] = 400
ES.Data.SellPrices[8170] = 500
ES.Data.SellPrices[8343] = 500
ES.Data.SellPrices[8544] = 400
ES.Data.SellPrices[8545] = 600
ES.Data.SellPrices[8838] = 60
ES.Data.SellPrices[8925] = 125
ES.Data.SellPrices[13446] = 1000
ES.Data.SellPrices[13464] = 100
ES.Data.SellPrices[14047] = 400
ES.Data.SellPrices[14529] = 500
ES.Data.SellPrices[14530] = 1000
ES.Data.SellPrices[19440] = 500
ES.Data.SellPrices[19441] = 1500
ES.Data.SellPrices[23684] = 1500
ES.Data.SellPrices[232433] = 2000
ES.Data.SellPrices[255645] = 370
ES.Data.SellPrices[255715] = 125
ES.Data.SellPrices[255716] = 28
ES.Data.SellPrices[255717] = 62
ES.Data.SellPrices[255718] = 125
ES.Data.SellPrices[255719] = 500
ES.Data.SellPrices[255720] = 50
ES.Data.SellPrices[255721] = 125
ES.Data.SellPrices[255722] = 500

-- Nombre de cada objeto (inglés, del cliente): se muestra mientras el juego no lo ha cargado
ES.Data.ItemNames = ES.Data.ItemNames or {}
ES.Data.ItemNames[118] = "Minor Healing Potion"
ES.Data.ItemNames[159] = "Refreshing Spring Water"
ES.Data.ItemNames[858] = "Lesser Healing Potion"
ES.Data.ItemNames[929] = "Healing Potion"
ES.Data.ItemNames[1251] = "Linen Bandage"
ES.Data.ItemNames[1288] = "Large Venom Sac"
ES.Data.ItemNames[1468] = "Murloc Fin"
ES.Data.ItemNames[1475] = "Small Venom Sac"
ES.Data.ItemNames[1710] = "Greater Healing Potion"
ES.Data.ItemNames[2321] = "Fine Thread"
ES.Data.ItemNames[2447] = "Peacebloom"
ES.Data.ItemNames[2450] = "Briarthorn"
ES.Data.ItemNames[2453] = "Bruiseweed"
ES.Data.ItemNames[2581] = "Heavy Linen Bandage"
ES.Data.ItemNames[2589] = "Linen Cloth"
ES.Data.ItemNames[2592] = "Wool Cloth"
ES.Data.ItemNames[2594] = "Flagon of Dwarven Honeymead"
ES.Data.ItemNames[2596] = "Skin of Dwarven Stout"
ES.Data.ItemNames[2678] = "Mild Spices"
ES.Data.ItemNames[2686] = "Thunder Ale"
ES.Data.ItemNames[2692] = "Hot Spices"
ES.Data.ItemNames[2723] = "Bottle of Dalaran Noir"
ES.Data.ItemNames[3174] = "Spider Ichor"
ES.Data.ItemNames[3357] = "Liferoot"
ES.Data.ItemNames[3371] = "Empty Vial"
ES.Data.ItemNames[3372] = "Leaded Vial"
ES.Data.ItemNames[3530] = "Wool Bandage"
ES.Data.ItemNames[3531] = "Heavy Wool Bandage"
ES.Data.ItemNames[3713] = "Soothing Spices"
ES.Data.ItemNames[3928] = "Superior Healing Potion"
ES.Data.ItemNames[4291] = "Silken Thread"
ES.Data.ItemNames[4304] = "Thick Leather"
ES.Data.ItemNames[4306] = "Silk Cloth"
ES.Data.ItemNames[4338] = "Mageweave Cloth"
ES.Data.ItemNames[4470] = "Simple Wood"
ES.Data.ItemNames[6450] = "Silk Bandage"
ES.Data.ItemNames[6451] = "Heavy Silk Bandage"
ES.Data.ItemNames[6452] = "Anti-Venom"
ES.Data.ItemNames[6453] = "Strong Anti-Venom"
ES.Data.ItemNames[7070] = "Elemental Water"
ES.Data.ItemNames[7080] = "Essence of Water"
ES.Data.ItemNames[8170] = "Rugged Leather"
ES.Data.ItemNames[8343] = "Heavy Silken Thread"
ES.Data.ItemNames[8544] = "Mageweave Bandage"
ES.Data.ItemNames[8545] = "Heavy Mageweave Bandage"
ES.Data.ItemNames[8838] = "Sungrass"
ES.Data.ItemNames[8925] = "Crystal Vial"
ES.Data.ItemNames[13446] = "Major Healing Potion"
ES.Data.ItemNames[13464] = "Golden Sansam"
ES.Data.ItemNames[14047] = "Runecloth"
ES.Data.ItemNames[14529] = "Runecloth Bandage"
ES.Data.ItemNames[14530] = "Heavy Runecloth Bandage"
ES.Data.ItemNames[19440] = "Powerful Anti-Venom"
ES.Data.ItemNames[19441] = "Huge Venom Sac"
ES.Data.ItemNames[23567] = "DEPRECATED ITEM"
ES.Data.ItemNames[23684] = "Crystal Infused Bandage"
ES.Data.ItemNames[232433] = "Dense Runecloth Bandage"
ES.Data.ItemNames[255645] = "Swollen Venom Sac"
ES.Data.ItemNames[255715] = "Potent Anti-Venom"
ES.Data.ItemNames[255716] = "Simple Poultice"
ES.Data.ItemNames[255717] = "Clever Poultice"
ES.Data.ItemNames[255718] = "Superior Poultice"
ES.Data.ItemNames[255719] = "Powerful Poultice"
ES.Data.ItemNames[255720] = "Woolen Tourniquet"
ES.Data.ItemNames[255721] = "Leather Tourniquet"
ES.Data.ItemNames[255722] = "Surgical Tourniquet"
ES.Data.ItemNames[279940] = "Toxin Study"
ES.Data.ItemNames[279968] = "First Aid Kit"

-- Material -> profesión de recolección que lo consigue (393 Desuello, 182 Herboristería, 186 Minería).
-- Sin uso por ahora: reservado para la vía "Vender en bruto" de Ganar dinero (docs/PLAN.md, G1).
ES.Data.GatheredBy = ES.Data.GatheredBy or {}
ES.Data.GatheredBy[2447] = 182
ES.Data.GatheredBy[2450] = 182
ES.Data.GatheredBy[2453] = 182
ES.Data.GatheredBy[3357] = 182
ES.Data.GatheredBy[4304] = 393
ES.Data.GatheredBy[8170] = 393
ES.Data.GatheredBy[8838] = 182
ES.Data.GatheredBy[13464] = 182

```

---

## Leatherworking

```lua
-- Generado por tools/gen_profession.py (Leatherworking). No editar a mano.
-- Datos: cliente de WoW Forever (wago.tools DB2), instructores de CMaNGOS classic-db, vendedores de QuestieDB.
local _, ES = ...
ES.Data = ES.Data or {}

-- t = { naranja, amarilla, verde, gris }; fee/train = precio y habilidad del instructor
-- (sin fee = se aprende de pergamino: de dónde sale, en Data/Sources.lua; scrollPrice = su precio si lo vende un PNJ)
-- rep = { facción, nivel } que pide el pergamino para aprenderla (5 amistoso, 6 honorable, 7 venerado, 8 exaltado)
-- r = { {itemID, cantidad} }; out = { itemID, cantidad }
-- sq / oq = calidad del pergamino / de lo fabricado (0 pobre, 1 común, 2 poco común, 3 raro, 4 épico)
-- faction = bando que puede aprenderla, si solo es de uno
-- bop = lo fabricado se liga al recogerlo: no se puede vender en la AH (sí al vendedor)
-- favor / favorRep = se compra con Merchant's Favor en el campamento de tu bando, y la reputación que pide
-- train ajustado a Forever: nivel de Classic menos lo que Forever bajó la amarilla de esa receta
-- basic = se aprende sola al coger la profesión; trainer = de instructor sin precio conocido
--   (receta nueva de Forever que no está en CMaNGOS: se aprende al ponerse amarilla)
ES.Data.Leatherworking = {
  skillLine = 165,
  ranks = { -- { tope, precio, habilidad requerida, nivel de personaje }
    { 150, 500, 50, 10 },
    { 225, 5000, 125, 20 },
    { 300, 50000, 200, 35 },
  },
  -- { PNJ instructor, rangos que enseña: 1 aprendiz (75), 2 oficial (150), 4 experto (225), 8 artesano (300) }
  trainers = { { 223, 1 }, { 1385, 2 }, { 1466, 1 }, { 1632, 1 }, { 3007, 4 }, { 3008, 1 }, { 3069, 1 }, { 3365, 2 }, { 3549, 1 }, { 3605, 1 }, { 3703, 2 }, { 3967, 2 }, { 4212, 4 }, { 4588, 2 }, { 5127, 2 }, { 5564, 2 }, { 5784, 1 }, { 5811, 1 }, { 11081, 2 }, { 11083, 1 }, { 11084, 2 }, { 11096, 1 }, { 11098, 8 }, { 251993, 3 }, { 252376, 3 } },
  recipes = {
    [2149] = { name = "Handstitched Leather Boots", t = { 1, 40, 55, 70 }, basic = true, r = { { 2318, 2 }, { 2320, 1 } }, out = { 2302, 1 }, oq = 1 },
    [2152] = { name = "Light Armor Kit", t = { 1, 30, 45, 60 }, basic = true, r = { { 2318, 1 } }, out = { 2304, 1 }, oq = 1 },
    [2153] = { name = "Handstitched Leather Pants", t = { 1, 45, 60, 75 }, fee = 50, train = 15, r = { { 2318, 4 }, { 2320, 1 } }, out = { 2303, 1 }, oq = 2 },
    [2158] = { name = "Fine Leather Boots", t = { 1, 95, 110, 125 }, scroll = 2406, train = 65, sq = 2, r = { { 2318, 7 }, { 2320, 2 } }, out = { 2307, 1 }, oq = 2 },
    [2159] = { name = "Fine Leather Cloak", t = { 1, 70, 85, 100 }, fee = 250, train = 50, r = { { 2318, 10 }, { 2321, 2 } }, out = { 2308, 1 }, oq = 2 },
    [2160] = { name = "Embossed Leather Vest", t = { 1, 65, 80, 95 }, fee = 100, train = 35, r = { { 2318, 8 }, { 2320, 4 } }, out = { 2300, 1 }, oq = 2 },
    [2161] = { name = "Embossed Leather Boots", t = { 1, 80, 95, 110 }, fee = 100, train = 50, r = { { 2318, 8 }, { 2320, 5 } }, out = { 2309, 1 }, oq = 2 },
    [2162] = { name = "Embossed Leather Cloak", t = { 1, 70, 85, 100 }, fee = 100, train = 40, r = { { 2318, 5 }, { 2320, 2 } }, out = { 2310, 1 }, oq = 2 },
    [2163] = { name = "White Leather Jerkin", t = { 1, 70, 85, 100 }, scroll = 2407, train = 40, sq = 2, r = { { 2318, 8 }, { 2320, 2 }, { 2324, 1 } }, out = { 2311, 1 }, oq = 2 },
    [2164] = { name = "Fine Leather Gloves", t = { 1, 80, 95, 110 }, scroll = 2408, train = 50, sq = 2, r = { { 4231, 1 }, { 2318, 4 }, { 2320, 2 } }, out = { 2312, 1 }, oq = 2 },
    [2165] = { name = "Medium Armor Kit", t = { 1, 90, 97, 105 }, fee = 250, train = 75, r = { { 2319, 4 }, { 2320, 1 } }, out = { 2313, 1 }, oq = 1 },
    [2166] = { name = "Toughened Leather Armor", t = { 1, 120, 132, 145 }, fee = 450, train = 95, r = { { 2319, 10 }, { 4231, 2 }, { 2321, 2 } }, out = { 2314, 1 }, oq = 2 },
    [2167] = { name = "Gray Leather Boots", t = { 1, 100, 112, 125 }, fee = 350, train = 75, r = { { 2319, 4 }, { 2321, 2 }, { 4340, 1 } }, out = { 2315, 1 }, oq = 2 },
    [2168] = { name = "Dark Leather Cloak", t = { 1, 110, 122, 135 }, fee = 350, train = 85, r = { { 2319, 8 }, { 2321, 1 }, { 4340, 1 } }, out = { 2316, 1 }, oq = 2 },
    [2169] = { name = "Dark Leather Tunic", t = { 1, 100, 112, 125 }, scroll = 2409, train = 75, sq = 2, r = { { 2319, 6 }, { 2321, 1 }, { 4340, 1 } }, out = { 2317, 1 }, oq = 2 },
    [2881] = { name = "Light Leather", t = { 1, 20, 30, 40 }, basic = true, r = { { 2934, 3 } }, out = { 2318, 1 }, oq = 1 },
    [3753] = { name = "Handstitched Leather Belt", t = { 1, 55, 70, 85 }, fee = 75, train = 25, r = { { 2318, 6 }, { 2320, 1 } }, out = { 4237, 1 }, oq = 2 },
    [3756] = { name = "Embossed Leather Gloves", t = { 1, 70, 85, 100 }, fee = 150, train = 40, r = { { 2318, 3 }, { 2320, 2 } }, out = { 4239, 1 }, oq = 2 },
    [3759] = { name = "Embossed Leather Pants", t = { 1, 80, 95, 110 }, fee = 200, train = 50, r = { { 4231, 1 }, { 2318, 6 }, { 2320, 2 } }, out = { 4242, 1 }, oq = 2 },
    [3760] = { name = "Hillman's Cloak", t = { 1, 145, 155, 165 }, fee = 600, train = 125, r = { { 4234, 5 }, { 2321, 2 } }, out = { 3719, 1 }, oq = 2 },
    [3761] = { name = "Fine Leather Tunic", t = { 1, 90, 105, 120 }, fee = 350, train = 60, r = { { 4231, 3 }, { 2318, 6 }, { 2320, 4 } }, out = { 4243, 1 }, oq = 2 },
    [3762] = { name = "Hillman's Leather Vest", t = { 1, 100, 112, 125 }, scroll = 4293, train = 75, sq = 2, r = { { 4243, 1 }, { 4231, 2 }, { 2320, 2 } }, out = { 4244, 1 }, oq = 2 },
    [3763] = { name = "Fine Leather Belt", t = { 1, 85, 100, 115 }, fee = 300, train = 55, r = { { 2318, 6 }, { 2320, 2 } }, out = { 4246, 1 }, oq = 2 },
    [3764] = { name = "Hillman's Leather Gloves", t = { 1, 145, 157, 170 }, fee = 500, train = 120, r = { { 2319, 14 }, { 2321, 4 } }, out = { 4247, 1 }, oq = 2 },
    [3765] = { name = "Dark Leather Gloves", t = { 1, 140, 152, 165 }, scroll = 7360, train = 95, sq = 2, r = { { 2312, 1 }, { 4233, 1 }, { 2321, 1 }, { 4340, 1 } }, out = { 4248, 1 }, oq = 2 },
    [3766] = { name = "Dark Leather Belt", t = { 1, 125, 137, 150 }, fee = 400, train = 100, r = { { 4246, 1 }, { 4233, 1 }, { 2321, 2 }, { 4340, 1 } }, out = { 4249, 1 }, oq = 2 },
    [3767] = { name = "Hillman's Belt", t = { 1, 125, 137, 150 }, scroll = 4294, train = 95, sq = 2, r = { { 2319, 8 }, { 3383, 1 }, { 2321, 2 } }, out = { 4250, 1 }, oq = 2 },
    [3768] = { name = "Hillman's Shoulders", t = { 1, 130, 142, 155 }, fee = 500, train = 105, r = { { 4233, 1 }, { 2319, 4 }, { 2321, 1 } }, out = { 4251, 1 }, oq = 2 },
    [3769] = { name = "Dark Leather Shoulders", t = { 1, 140, 152, 165 }, scroll = 4296, train = 115, sq = 2, r = { { 2319, 12 }, { 3390, 1 }, { 4340, 1 }, { 2321, 2 } }, out = { 4252, 1 }, oq = 2 },
    [3770] = { name = "Toughened Leather Gloves", t = { 1, 135, 147, 160 }, fee = 500, train = 110, r = { { 2319, 4 }, { 4233, 2 }, { 3389, 2 }, { 3182, 2 }, { 2321, 2 } }, out = { 4253, 1 }, oq = 3 },
    [3771] = { name = "Barbaric Gloves", t = { 1, 150, 160, 170 }, scroll = 4297, train = 125, sq = 2, r = { { 4234, 6 }, { 5637, 2 }, { 2321, 1 } }, out = { 4254, 1 }, oq = 2 },
    [3772] = { name = "Green Leather Armor", t = { 1, 150, 160, 170 }, scroll = 7613, train = 130, scrollPrice = 2000, sq = 1, r = { { 4234, 9 }, { 2605, 2 }, { 2321, 4 } }, out = { 4255, 1 }, oq = 2 },
    [3773] = { name = "Guardian Armor", t = { 1, 170, 180, 190 }, scroll = 4299, train = 150, sq = 2, r = { { 4236, 2 }, { 4234, 12 }, { 3824, 1 }, { 2321, 2 } }, out = { 4256, 1 }, oq = 2 },
    [3774] = { name = "Green Leather Belt", t = { 1, 155, 165, 175 }, fee = 1000, train = 135, tr = { 3007, 4212, 11098 }, r = { { 4236, 1 }, { 4234, 5 }, { 2321, 1 }, { 2605, 1 }, { 7071, 1 } }, out = { 4257, 1 }, oq = 2 },
    [3775] = { name = "Guardian Belt", t = { 1, 165, 175, 185 }, scroll = 4298, train = 145, sq = 3, r = { { 4236, 2 }, { 4234, 4 }, { 2321, 1 }, { 7071, 1 } }, out = { 4258, 1 }, oq = 2 },
    [3776] = { name = "Green Leather Bracers", t = { 1, 175, 185, 195 }, fee = 1200, train = 155, r = { { 4236, 2 }, { 4234, 6 }, { 2605, 1 }, { 2321, 1 } }, out = { 4259, 1 }, oq = 2 },
    [3777] = { name = "Guardian Leather Bracers", t = { 1, 190, 200, 210 }, scroll = 4300, train = 170, sq = 2, r = { { 4234, 6 }, { 4236, 2 }, { 4291, 1 } }, out = { 4260, 1 }, oq = 2 },
    [3778] = { name = "Gem-studded Leather Belt", t = { 1, 180, 190, 200 }, scroll = 14635, train = 160, scrollPrice = 3000, sq = 1, r = { { 4236, 4 }, { 5500, 2 }, { 1529, 2 }, { 3864, 1 }, { 2321, 1 } }, out = { 4262, 1 }, oq = 3 },
    [3779] = { name = "Barbaric Belt", t = { 1, 195, 205, 215 }, scroll = 4301, train = 175, sq = 3, r = { { 4234, 6 }, { 4236, 2 }, { 4096, 2 }, { 5633, 1 }, { 4291, 1 }, { 7071, 1 } }, out = { 4264, 1 }, oq = 2 },
    [3780] = { name = "Heavy Armor Kit", t = { 1, 145, 155, 165 }, fee = 750, train = 125, r = { { 4234, 5 }, { 2321, 1 } }, out = { 4265, 1 }, oq = 1 },
    [3816] = { name = "Cured Light Hide", t = { 1, 50, 60, 70 }, fee = 50, train = 30, r = { { 783, 1 }, { 4289, 1 } }, out = { 4231, 1 }, oq = 1 },
    [3817] = { name = "Cured Medium Hide", t = { 1, 90, 97, 105 }, fee = 200, train = 75, r = { { 4232, 1 }, { 4289, 1 } }, out = { 4233, 1 }, oq = 1 },
    [3818] = { name = "Cured Heavy Hide", t = { 1, 135, 140, 145 }, fee = 500, train = 125, r = { { 4235, 1 }, { 4289, 3 } }, out = { 4236, 1 }, oq = 1 },
    [4096] = { name = "Raptor Hide Harness", t = { 1, 160, 170, 180 }, scroll = 13287, train = 140, scrollPrice = 2500, sq = 2, r = { { 4461, 6 }, { 4234, 4 }, { 2321, 2 } }, out = { 4455, 1 }, oq = 2 },
    [4097] = { name = "Raptor Hide Belt", t = { 1, 160, 170, 180 }, scroll = 13288, train = 140, scrollPrice = 2500, sq = 2, r = { { 4461, 4 }, { 4234, 4 }, { 2321, 2 } }, out = { 4456, 1 }, oq = 2 },
    [5244] = { name = "Kodo Hide Bag", t = { 1, 65, 80, 95 }, scroll = 5083, train = 35, sq = 2, r = { { 5082, 3 }, { 2318, 4 }, { 2320, 1 } }, out = { 5081, 1 }, oq = 1 },
    [6661] = { name = "Barbaric Harness", t = { 1, 185, 195, 205 }, fee = 1800, train = 165, r = { { 4234, 14 }, { 2321, 2 }, { 7071, 1 } }, out = { 5739, 1 }, oq = 2 },
    [6702] = { name = "Murloc Scale Belt", t = { 1, 95, 110, 125 }, scroll = 5786, train = 65, scrollPrice = 550, sq = 1, r = { { 5784, 8 }, { 2318, 6 }, { 2321, 1 } }, out = { 5780, 1 }, oq = 2 },
    [6703] = { name = "Murloc Scale Breastplate", t = { 1, 100, 115, 130 }, scroll = 5787, train = 70, scrollPrice = 600, sq = 1, r = { { 5784, 12 }, { 4231, 1 }, { 2318, 8 }, { 2321, 1 } }, out = { 5781, 1 }, oq = 2 },
    [6704] = { name = "Thick Murloc Armor", t = { 1, 165, 175, 185 }, scroll = 5788, train = 145, scrollPrice = 650, sq = 2, r = { { 5785, 12 }, { 4236, 1 }, { 4234, 10 }, { 2321, 3 } }, out = { 5782, 1 }, oq = 2 },
    [6705] = { name = "Murloc Scale Bracers", t = { 1, 185, 195, 205 }, scroll = 5789, train = 165, scrollPrice = 2800, sq = 2, r = { { 5785, 16 }, { 4236, 1 }, { 4234, 14 }, { 4291, 1 } }, out = { 5783, 1 }, oq = 2 },
    [7126] = { name = "Handstitched Leather Vest", t = { 1, 40, 55, 70 }, basic = true, r = { { 2318, 3 }, { 2320, 1 } }, out = { 5957, 1 }, oq = 2 },
    [7133] = { name = "Fine Leather Pants", t = { 1, 105, 117, 130 }, scroll = 5972, train = 80, sq = 2, r = { { 2319, 8 }, { 2997, 1 }, { 2321, 1 } }, out = { 5958, 1 }, oq = 2 },
    [7135] = { name = "Dark Leather Pants", t = { 1, 115, 127, 140 }, fee = 400, train = 90, r = { { 2319, 12 }, { 4340, 1 }, { 2321, 1 } }, out = { 5961, 1 }, oq = 2 },
    [7147] = { name = "Guardian Pants", t = { 1, 155, 165, 175 }, fee = 1000, train = 135, tr = { 3007, 4212, 11098 }, r = { { 4234, 12 }, { 4305, 2 }, { 2321, 2 } }, out = { 5962, 1 }, oq = 2 },
    [7149] = { name = "Barbaric Leggings", t = { 1, 165, 175, 185 }, scroll = 5973, train = 145, scrollPrice = 650, sq = 1, r = { { 4234, 10 }, { 2321, 2 }, { 1206, 1 } }, out = { 5963, 1 }, oq = 2 },
    [7151] = { name = "Barbaric Shoulders", t = { 1, 170, 180, 190 }, fee = 1200, train = 150, tr = { 3007, 4212, 11098 }, r = { { 4234, 8 }, { 4236, 1 }, { 2321, 2 } }, out = { 5964, 1 }, oq = 2 },
    [7153] = { name = "Guardian Cloak", t = { 1, 180, 190, 200 }, scroll = 5974, train = 160, sq = 2, r = { { 4234, 14 }, { 4305, 2 }, { 4291, 2 } }, out = { 5965, 1 }, oq = 2 },
    [7156] = { name = "Guardian Gloves", t = { 1, 185, 195, 205 }, fee = 2400, train = 165, r = { { 4234, 4 }, { 4236, 1 }, { 4291, 1 } }, out = { 5966, 1 }, oq = 2 },
    [7953] = { name = "Deviate Scale Cloak", t = { 1, 95, 110, 125 }, scroll = 6474, train = 65, scrollPrice = 550, sq = 1, r = { { 6470, 8 }, { 4231, 1 }, { 2321, 1 } }, out = { 6466, 1 }, oq = 2 },
    [7954] = { name = "Deviate Scale Gloves", t = { 1, 105, 117, 130 }, scroll = 6475, train = 80, scrollPrice = 1500, sq = 1, r = { { 6471, 2 }, { 6470, 6 }, { 2321, 2 } }, out = { 6467, 1 }, oq = 2 },
    [7955] = { name = "Deviate Scale Belt", t = { 1, 115, 127, 140 }, scroll = 6476, train = 90, sq = 2, r = { { 6471, 10 }, { 6470, 10 }, { 2321, 2 } }, out = { 6468, 1 }, oq = 3 },
    [8322] = { name = "Moonglow Vest", t = { 1, 90, 105, 120 }, scroll = 6710, train = 65, sq = 2, r = { { 2318, 6 }, { 4231, 1 }, { 2320, 4 }, { 5498, 1 } }, out = { 6709, 1 }, oq = 2 },
    [9058] = { name = "Handstitched Leather Cloak", t = { 1, 40, 55, 70 }, basic = true, r = { { 2318, 2 }, { 2320, 1 } }, out = { 7276, 1 }, oq = 1 },
    [9059] = { name = "Handstitched Leather Bracers", t = { 1, 40, 55, 70 }, basic = true, r = { { 2318, 2 }, { 2320, 3 } }, out = { 7277, 1 }, oq = 1 },
    [9060] = { name = "Light Leather Quiver", t = { 1, 55, 70, 85 }, fee = 100, train = 25, r = { { 2318, 4 }, { 2320, 2 } }, out = { 7278, 1 }, oq = 1 },
    [9062] = { name = "Small Leather Ammo Pouch", t = { 1, 55, 70, 85 }, fee = 100, train = 25, r = { { 2318, 3 }, { 2320, 4 } }, out = { 7279, 1 }, oq = 1 },
    [9064] = { name = "Rugged Leather Pants", t = { 1, 60, 75, 90 }, scroll = 7288, train = 30, sq = 2, r = { { 2318, 5 }, { 2320, 5 } }, out = { 7280, 1 }, oq = 2 },
    [9065] = { name = "Light Leather Bracers", t = { 1, 75, 90, 105 }, fee = 150, train = 45, r = { { 2318, 6 }, { 2320, 4 } }, out = { 7281, 1 }, oq = 2 },
    [9068] = { name = "Light Leather Pants", t = { 1, 100, 115, 130 }, fee = 400, train = 70, r = { { 2318, 10 }, { 4231, 1 }, { 2321, 1 } }, out = { 7282, 1 }, oq = 2 },
    [9070] = { name = "Black Whelp Cloak", t = { 1, 100, 112, 125 }, scroll = 7289, train = 75, scrollPrice = 650, sq = 1, r = { { 7286, 12 }, { 2319, 4 }, { 2321, 1 } }, out = { 7283, 1 }, oq = 2 },
    [9072] = { name = "Red Whelp Gloves", t = { 1, 120, 132, 145 }, scroll = 7290, train = 95, scrollPrice = 1600, sq = 1, r = { { 7287, 6 }, { 2319, 4 }, { 2321, 1 } }, out = { 7284, 1 }, oq = 2 },
    [9074] = { name = "Nimble Leather Gloves", t = { 1, 120, 132, 145 }, fee = 500, train = 95, r = { { 2457, 1 }, { 2319, 6 }, { 2321, 1 } }, out = { 7285, 1 }, oq = 2 },
    [9145] = { name = "Fletcher's Gloves", t = { 1, 125, 137, 150 }, fee = 500, train = 100, r = { { 2319, 8 }, { 5116, 4 }, { 2321, 2 } }, out = { 7348, 1 }, oq = 2 },
    [9146] = { name = "Herbalist's Gloves", t = { 1, 135, 147, 160 }, scroll = 7361, train = 110, scrollPrice = 1800, sq = 2, r = { { 2319, 8 }, { 3356, 4 }, { 2321, 2 } }, out = { 7349, 1 }, oq = 2 },
    [9147] = { name = "Earthen Leather Shoulders", t = { 1, 135, 147, 160 }, scroll = 7362, train = 110, scrollPrice = 2000, sq = 1, r = { { 2319, 6 }, { 7067, 1 }, { 2321, 2 } }, out = { 7352, 1 }, oq = 2 },
    [9148] = { name = "Pilferer's Gloves", t = { 1, 140, 152, 165 }, scroll = 7363, train = 115, sq = 2, r = { { 2319, 10 }, { 5373, 2 }, { 2321, 2 } }, out = { 7358, 1 }, oq = 2 },
    [9149] = { name = "Heavy Earthen Gloves", t = { 1, 145, 157, 170 }, scroll = 7364, train = 120, sq = 2, r = { { 2319, 12 }, { 7067, 2 }, { 2997, 2 }, { 2321, 2 } }, out = { 7359, 1 }, oq = 2 },
    [9193] = { name = "Heavy Quiver", t = { 1, 145, 155, 165 }, fee = 500, train = 125, r = { { 4234, 8 }, { 2321, 2 } }, out = { 7371, 1 }, oq = 2 },
    [9194] = { name = "Heavy Leather Ammo Pouch", t = { 1, 145, 155, 165 }, fee = 500, train = 125, r = { { 4234, 8 }, { 2321, 2 } }, out = { 7372, 1 }, oq = 2 },
    [9195] = { name = "Dusky Leather Leggings", t = { 1, 160, 170, 180 }, scroll = 7449, train = 140, sq = 2, r = { { 4234, 10 }, { 2325, 1 }, { 2321, 2 } }, out = { 7373, 1 }, oq = 2 },
    [9196] = { name = "Dusky Leather Armor", t = { 1, 170, 180, 190 }, fee = 1500, train = 150, tr = { 3007, 4212, 11098 }, r = { { 4234, 10 }, { 3824, 1 }, { 2321, 2 } }, out = { 7374, 1 }, oq = 2 },
    [9197] = { name = "Green Whelp Armor", t = { 1, 170, 180, 190 }, scroll = 7450, train = 150, sq = 2, r = { { 7392, 4 }, { 4234, 10 }, { 2321, 2 } }, out = { 7375, 1 }, oq = 2 },
    [9198] = { name = "Frost Leather Cloak", t = { 1, 175, 185, 195 }, fee = 2000, train = 155, r = { { 4234, 6 }, { 7067, 2 }, { 7070, 2 }, { 2321, 2 } }, out = { 7377, 1 }, oq = 2 },
    [9201] = { name = "Dusky Bracers", t = { 1, 180, 190, 200 }, fee = 2000, train = 160, r = { { 4234, 16 }, { 2325, 1 }, { 4291, 2 } }, out = { 7378, 1 }, oq = 2 },
    [9202] = { name = "Green Whelp Bracers", t = { 1, 185, 195, 205 }, scroll = 7451, train = 165, scrollPrice = 2800, sq = 2, r = { { 7392, 6 }, { 4234, 8 }, { 4291, 2 } }, out = { 7386, 1 }, oq = 2 },
    [9206] = { name = "Dusky Belt", t = { 1, 190, 200, 210 }, fee = 2500, train = 170, r = { { 4234, 10 }, { 4305, 2 }, { 2325, 2 }, { 7071, 1 } }, out = { 7387, 1 }, oq = 2 },
    [9207] = { name = "Dusky Boots", t = { 1, 195, 205, 215 }, scroll = 7452, train = 175, sq = 3, r = { { 4234, 8 }, { 7428, 2 }, { 3824, 1 }, { 4291, 2 } }, out = { 7390, 1 }, oq = 2 },
    [9208] = { name = "Swift Boots", t = { 1, 195, 205, 215 }, scroll = 7453, train = 175, sq = 2, r = { { 4234, 10 }, { 2459, 2 }, { 4337, 2 }, { 4291, 1 } }, out = { 7391, 1 }, oq = 2 },
    [10487] = { name = "Thick Armor Kit", t = { 1, 195, 205, 215 }, fee = 2000, train = 175, r = { { 4304, 5 }, { 4291, 1 } }, out = { 8173, 1 }, oq = 1 },
    [10490] = { name = "Comfortable Leather Hat", t = { 1, 195, 205, 215 }, scroll = 8384, train = 175, sq = 3, r = { { 4234, 12 }, { 4236, 2 }, { 4291, 2 } }, out = { 8174, 1 }, oq = 2 },
    [10499] = { name = "Nightscape Tunic", t = { 1, 200, 210, 220 }, fee = 3000, train = 180, r = { { 4304, 7 }, { 4291, 2 } }, out = { 8175, 1 }, oq = 2 },
    [10507] = { name = "Nightscape Headband", t = { 1, 200, 210, 220 }, fee = 3000, train = 180, r = { { 4304, 5 }, { 4291, 2 } }, out = { 8176, 1 }, oq = 2 },
    [10509] = { name = "Turtle Scale Gloves", t = { 1, 200, 210, 220 }, scroll = 8385, train = 180, scrollPrice = 3500, sq = 1, r = { { 4304, 6 }, { 8167, 8 }, { 8343, 1 } }, out = { 8187, 1 }, oq = 2 },
    [10511] = { name = "Turtle Scale Breastplate", t = { 1, 205, 215, 225 }, fee = 3000, train = 185, r = { { 4304, 6 }, { 8167, 12 }, { 8343, 1 } }, out = { 8189, 1 }, oq = 2 },
    [10516] = { name = "Nightscape Shoulders", t = { 1, 205, 215, 225 }, scroll = 8409, train = 185, scrollPrice = 4000, sq = 2, r = { { 4304, 8 }, { 4338, 6 }, { 4291, 3 } }, out = { 8192, 1 }, oq = 2 },
    [10518] = { name = "Turtle Scale Bracers", t = { 1, 205, 215, 225 }, fee = 3500, train = 185, r = { { 4304, 8 }, { 8167, 12 }, { 8343, 1 } }, out = { 8198, 1 }, oq = 2 },
    [10520] = { name = "Big Voodoo Robe", t = { 1, 210, 220, 230 }, scroll = 8386, train = 190, sq = 2, r = { { 4304, 10 }, { 8151, 4 }, { 8343, 1 } }, out = { 8200, 1 }, oq = 2 },
    [10525] = { name = "Tough Scorpid Breastplate", t = { 1, 215, 225, 235 }, scroll = 8395, train = 195, sq = 2, r = { { 4304, 12 }, { 8154, 12 }, { 4291, 4 } }, out = { 8203, 1 }, oq = 2 },
    [10529] = { name = "Wild Leather Shoulders", t = { 1, 215, 225, 235 }, scroll = 8403, train = 195, sq = 2, r = { { 4304, 10 }, { 8153, 1 }, { 8172, 1 } }, out = { 8210, 1 }, oq = 2 },
    [10531] = { name = "Big Voodoo Mask", t = { 1, 215, 225, 235 }, scroll = 8387, train = 195, sq = 2, r = { { 4304, 8 }, { 8151, 6 }, { 8343, 1 } }, out = { 8201, 1 }, oq = 2 },
    [10533] = { name = "Tough Scorpid Bracers", t = { 1, 215, 225, 235 }, scroll = 8397, train = 195, sq = 2, r = { { 4304, 10 }, { 8154, 4 }, { 4291, 2 } }, out = { 8205, 1 }, oq = 2 },
    [10542] = { name = "Tough Scorpid Gloves", t = { 1, 220, 230, 240 }, scroll = 8398, train = 200, sq = 2, r = { { 4304, 6 }, { 8154, 8 }, { 4291, 2 } }, out = { 8204, 1 }, oq = 2 },
    [10544] = { name = "Wild Leather Vest", t = { 1, 220, 230, 240 }, scroll = 8404, train = 200, sq = 2, r = { { 4304, 12 }, { 8153, 2 }, { 8172, 1 } }, out = { 8211, 1 }, oq = 2 },
    [10546] = { name = "Wild Leather Helmet", t = { 1, 220, 230, 240 }, scroll = 8405, train = 200, sq = 2, r = { { 4304, 10 }, { 8153, 2 }, { 8172, 1 } }, out = { 8214, 1 }, oq = 2 },
    [10548] = { name = "Nightscape Pants", t = { 1, 225, 235, 245 }, fee = 4000, train = 205, tr = { 11098 }, r = { { 4304, 14 }, { 4291, 4 } }, out = { 8193, 1 }, oq = 2 },
    [10550] = { name = "Nightscape Cloak", t = { 1, 225, 235, 245 }, scroll = 8388, train = 205, sq = 2, r = { { 4304, 12 }, { 4291, 4 } }, out = { 8195, 1 }, oq = 2 },
    [10552] = { name = "Turtle Scale Helm", t = { 1, 225, 235, 245 }, fee = 4000, train = 205, tr = { 11098 }, r = { { 4304, 14 }, { 8167, 24 }, { 8343, 1 } }, out = { 8191, 1 }, oq = 2 },
    [10554] = { name = "Tough Scorpid Boots", t = { 1, 230, 240, 250 }, scroll = 8399, train = 210, sq = 2, r = { { 4304, 12 }, { 8154, 12 }, { 4291, 6 } }, out = { 8209, 1 }, oq = 2 },
    [10556] = { name = "Turtle Scale Leggings", t = { 1, 230, 240, 250 }, fee = 4500, train = 210, tr = { 11098 }, r = { { 4304, 14 }, { 8167, 28 }, { 8343, 1 } }, out = { 8185, 1 }, oq = 2 },
    [10558] = { name = "Nightscape Boots", t = { 1, 230, 240, 250 }, fee = 4500, train = 210, tr = { 11098 }, r = { { 4304, 16 }, { 8343, 2 } }, out = { 8197, 1 }, oq = 2 },
    [10560] = { name = "Big Voodoo Pants", t = { 1, 230, 240, 250 }, scroll = 8389, train = 215, sq = 2, r = { { 4304, 10 }, { 8152, 6 }, { 8343, 2 } }, out = { 8202, 1 }, oq = 2 },
    [10562] = { name = "Big Voodoo Cloak", t = { 1, 235, 245, 255 }, scroll = 8390, train = 215, sq = 2, r = { { 4304, 14 }, { 8152, 4 }, { 8343, 2 } }, out = { 8216, 1 }, oq = 2 },
    [10564] = { name = "Tough Scorpid Shoulders", t = { 1, 235, 245, 255 }, scroll = 8400, train = 215, sq = 2, r = { { 4304, 12 }, { 8154, 16 }, { 8343, 2 } }, out = { 8207, 1 }, oq = 2 },
    [10566] = { name = "Wild Leather Boots", t = { 1, 240, 250, 260 }, scroll = 8406, train = 220, sq = 2, r = { { 4304, 14 }, { 8153, 4 }, { 8172, 2 } }, out = { 8213, 1 }, oq = 2 },
    [10568] = { name = "Tough Scorpid Leggings", t = { 1, 240, 250, 260 }, scroll = 8401, train = 220, sq = 2, r = { { 4304, 14 }, { 8154, 8 }, { 8343, 2 } }, out = { 8206, 1 }, oq = 2 },
    [10570] = { name = "Tough Scorpid Helm", t = { 1, 245, 255, 265 }, scroll = 8402, train = 225, sq = 2, r = { { 4304, 10 }, { 8154, 20 }, { 8343, 2 } }, out = { 8208, 1 }, oq = 2 },
    [10572] = { name = "Wild Leather Leggings", t = { 1, 245, 255, 265 }, scroll = 8407, train = 225, sq = 2, r = { { 4304, 16 }, { 8153, 2 }, { 8172, 2 } }, out = { 8212, 1 }, oq = 2 },
    [10574] = { name = "Wild Leather Cloak", t = { 1, 245, 255, 265 }, scroll = 8408, train = 225, sq = 2, r = { { 4304, 16 }, { 8153, 2 }, { 8172, 2 } }, out = { 8215, 1 }, oq = 2 },
    [10619] = { name = "Dragonscale Gauntlets", t = { 1, 220, 230, 240 }, fee = 9000, train = 225, spec = "Dragonscale", tr = { 7867 }, r = { { 4304, 24 }, { 8165, 12 }, { 8343, 4 }, { 8172, 2 } }, out = { 8347, 1 }, oq = 3 },
    [10621] = { name = "Wolfshead Helm", t = { 1, 220, 230, 240 }, gone = true, r = { { 4304, 18 }, { 8368, 2 }, { 8146, 8 }, { 8343, 4 }, { 8172, 2 } }, out = { 8345, 1 }, oq = 3 },
    [10630] = { name = "Gauntlets of the Sea", t = { 1, 225, 235, 245 }, gone = true, r = { { 4304, 20 }, { 7079, 8 }, { 7075, 2 }, { 8172, 1 }, { 8343, 4 } }, out = { 8346, 1 }, oq = 3 },
    [10632] = { name = "Helm of Fire", t = { 1, 245, 255, 265 }, gone = true, r = { { 4304, 40 }, { 7077, 8 }, { 7075, 4 }, { 8172, 2 }, { 8343, 4 } }, out = { 8348, 1 }, oq = 3 },
    [10647] = { name = "Feathered Breastplate", t = { 1, 245, 255, 265 }, gone = true, r = { { 4304, 40 }, { 8168, 40 }, { 7971, 2 }, { 8172, 4 }, { 8343, 4 } }, out = { 8349, 1 }, oq = 3 },
    [10650] = { name = "Dragonscale Breastplate", t = { 1, 250, 260, 270 }, fee = 9000, train = 255, spec = "Dragonscale", tr = { 7867 }, r = { { 4304, 40 }, { 8165, 30 }, { 8343, 4 }, { 8172, 4 } }, out = { 8367, 1 }, oq = 3 },
    [14930] = { name = "Quickdraw Quiver", t = { 1, 220, 230, 240 }, fee = 3600, train = 200, r = { { 4304, 12 }, { 8172, 1 }, { 8949, 1 }, { 4291, 4 } }, out = { 8217, 1 }, oq = 2 },
    [14932] = { name = "Thick Leather Ammo Pouch", t = { 1, 220, 230, 240 }, fee = 3600, train = 200, r = { { 4304, 10 }, { 8172, 1 }, { 8951, 1 }, { 4291, 6 } }, out = { 8218, 1 }, oq = 2 },
    [16650] = { name = "Wildthorn Mail", t = { 1, 265, 275, 285 }, scroll = 12691, train = 245, sq = 2, r = { { 8170, 40 }, { 12810, 2 }, { 12803, 4 }, { 8153, 4 }, { 12364, 1 }, { 14341, 1 } }, out = { 12624, 1 }, oq = 3 },
    [16661] = { name = "Storm Gauntlets", t = { 1, 290, 300, 310 }, scroll = 12703, train = 270, scrollPrice = 40000, sq = 3, r = { { 8170, 20 }, { 12810, 4 }, { 7080, 4 }, { 12361, 4 }, { 14341, 1 } }, out = { 12632, 1 }, oq = 3 },
    [16728] = { name = "Helm of the Great Chief", t = { 1, 290, 300, 310 }, scroll = 12716, train = 290, sq = 3, r = { { 8170, 40 }, { 12810, 4 }, { 8168, 60 }, { 12799, 6 }, { 12364, 2 }, { 14341, 1 } }, out = { 12636, 1 }, oq = 3 },
    [16746] = { name = "Invulnerable Mail", t = { 1, 295, 302, 310 }, scroll = 12728, train = 295, sq = 4, r = { { 249427, 20 }, { 12810, 30 }, { 12364, 6 }, { 12800, 6 }, { 249429, 10 }, { 14341, 2 } }, out = { 12641, 1 }, oq = 4 },
    [19047] = { name = "Cured Rugged Hide", t = { 1, 225, 230, 235 }, fee = 5000, train = 225, tr = { 11098 }, r = { { 8171, 1 }, { 15409, 1 } }, out = { 15407, 2 }, oq = 1 },
    [19048] = { name = "Heavy Scorpid Bracers", t = { 1, 250, 260, 270 }, scroll = 15724, train = 255, scrollPrice = 12000, sq = 1, r = { { 8170, 4 }, { 15408, 4 }, { 14341, 1 } }, out = { 15077, 1 }, oq = 2 },
    [19049] = { name = "Wicked Leather Gauntlets", t = { 1, 255, 265, 275 }, scroll = 15725, train = 235, scrollPrice = 12000, sq = 1, r = { { 8170, 8 }, { 2325, 1 }, { 14341, 1 } }, out = { 15083, 1 }, oq = 2 },
    [19050] = { name = "Green Dragonscale Breastplate", t = { 1, 255, 265, 275 }, scroll = 15726, train = 235, scrollPrice = 12000, sq = 1, r = { { 8170, 20 }, { 15412, 25 }, { 14341, 2 } }, out = { 15045, 1 }, oq = 3 },
    [19051] = { name = "Heavy Scorpid Vest", t = { 1, 260, 270, 280 }, scroll = 15727, train = 240, sq = 2, r = { { 8170, 6 }, { 15408, 6 }, { 14341, 1 } }, out = { 15076, 1 }, oq = 2 },
    [19052] = { name = "Wicked Leather Bracers", t = { 1, 260, 270, 280 }, scroll = 15728, train = 240, sq = 2, r = { { 8170, 8 }, { 2325, 1 }, { 14341, 1 } }, out = { 15084, 1 }, oq = 2 },
    [19053] = { name = "Chimeric Gloves", t = { 1, 260, 270, 280 }, scroll = 15729, train = 240, scrollPrice = 12000, sq = 1, r = { { 8170, 6 }, { 15423, 6 }, { 14341, 1 } }, out = { 15074, 1 }, oq = 2 },
    [19054] = { name = "Red Dragonscale Breastplate", t = { 1, 310, 320, 330 }, scroll = 15730, train = 290, sq = 3, r = { { 8170, 40 }, { 15414, 30 }, { 14341, 1 } }, out = { 15047, 1 }, oq = 3 },
    [19055] = { name = "Runic Leather Gauntlets", t = { 1, 265, 275, 285 }, scroll = 15731, train = 245, sq = 2, r = { { 8170, 10 }, { 14047, 6 }, { 14341, 1 } }, out = { 15091, 1 }, oq = 2 },
    [19058] = { name = "Rugged Armor Kit", t = { 1, 225, 235, 245 }, fee = 5000, train = 225, tr = { 11098 }, r = { { 8170, 5 } }, out = { 15564, 1 }, oq = 1 },
    [19059] = { name = "Volcanic Leggings", t = { 1, 265, 275, 285 }, scroll = 15732, train = 245, sq = 2, r = { { 8170, 6 }, { 7078, 1 }, { 7075, 1 }, { 14341, 1 } }, out = { 15054, 1 }, oq = 2 },
    [19060] = { name = "Green Dragonscale Leggings", t = { 1, 265, 275, 285 }, scroll = 15733, train = 245, sq = 3, r = { { 8170, 20 }, { 15412, 25 }, { 14341, 1 } }, out = { 15046, 1 }, oq = 3 },
    [19061] = { name = "Living Shoulders", t = { 1, 265, 275, 285 }, scroll = 15734, train = 245, scrollPrice = 14000, sq = 1, r = { { 8170, 12 }, { 12803, 4 }, { 14341, 1 } }, out = { 15061, 1 }, oq = 3 },
    [19062] = { name = "Ironfeather Shoulders", t = { 1, 265, 275, 285 }, scroll = 15735, train = 245, scrollPrice = 14000, sq = 1, r = { { 8170, 24 }, { 15420, 80 }, { 1529, 2 }, { 14341, 1 } }, out = { 15067, 1 }, oq = 3 },
    [19063] = { name = "Chimeric Boots", t = { 1, 270, 280, 290 }, scroll = 15737, train = 250, sq = 2, r = { { 8170, 4 }, { 15423, 8 }, { 14341, 1 } }, out = { 15073, 1 }, oq = 2 },
    [19064] = { name = "Heavy Scorpid Gauntlets", t = { 1, 270, 280, 290 }, scroll = 15738, train = 250, sq = 2, r = { { 8170, 6 }, { 15408, 8 }, { 14341, 1 } }, out = { 15078, 1 }, oq = 2 },
    [19065] = { name = "Runic Leather Bracers", t = { 1, 270, 280, 290 }, scroll = 15739, train = 250, sq = 2, r = { { 8170, 6 }, { 7971, 1 }, { 14047, 6 }, { 14341, 1 } }, out = { 15092, 1 }, oq = 2 },
    [19066] = { name = "Frostsaber Boots", t = { 1, 270, 280, 290 }, scroll = 15740, train = 250, scrollPrice = 16000, sq = 1, r = { { 8170, 4 }, { 15422, 6 }, { 14341, 1 } }, out = { 15071, 1 }, oq = 2 },
    [19067] = { name = "Stormshroud Pants", t = { 1, 270, 280, 290 }, scroll = 15741, train = 250, scrollPrice = 16000, sq = 1, r = { { 8170, 16 }, { 7080, 2 }, { 7082, 2 }, { 14341, 1 } }, out = { 15057, 1 }, oq = 3 },
    [19068] = { name = "Warbear Harness", t = { 1, 270, 280, 290 }, scroll = 20253, train = 250, scrollPrice = 16000, rep = { 576, 4 }, sq = 1, r = { { 8170, 28 }, { 15419, 12 }, { 14341, 1 } }, out = { 15064, 1 }, oq = 3 },
    [19070] = { name = "Heavy Scorpid Belt", t = { 1, 275, 285, 295 }, scroll = 15743, train = 255, sq = 2, r = { { 8170, 6 }, { 15408, 8 }, { 14341, 1 } }, out = { 15082, 1 }, oq = 2 },
    [19071] = { name = "Wicked Leather Headband", t = { 1, 275, 285, 295 }, scroll = 15744, train = 255, sq = 2, r = { { 8170, 12 }, { 2325, 1 }, { 14341, 1 } }, out = { 15086, 1 }, oq = 2 },
    [19072] = { name = "Runic Leather Belt", t = { 1, 275, 285, 295 }, scroll = 15745, train = 255, sq = 2, r = { { 8170, 12 }, { 14047, 10 }, { 14341, 1 } }, out = { 15093, 1 }, oq = 2 },
    [19073] = { name = "Chimeric Leggings", t = { 1, 275, 285, 295 }, scroll = 15746, train = 255, sq = 2, r = { { 8170, 8 }, { 15423, 8 }, { 14341, 1 } }, out = { 15072, 1 }, oq = 2 },
    [19074] = { name = "Frostsaber Leggings", t = { 1, 280, 290, 300 }, scroll = 15747, train = 260, sq = 2, r = { { 8170, 6 }, { 15422, 8 }, { 14341, 1 } }, out = { 15069, 1 }, oq = 2 },
    [19075] = { name = "Heavy Scorpid Leggings", t = { 1, 280, 290, 300 }, scroll = 15748, train = 260, sq = 2, r = { { 8170, 8 }, { 15408, 12 }, { 14341, 1 } }, out = { 15079, 1 }, oq = 2 },
    [19076] = { name = "Volcanic Breastplate", t = { 1, 280, 290, 300 }, scroll = 15749, train = 260, sq = 2, r = { { 8170, 8 }, { 7078, 1 }, { 7076, 1 }, { 14341, 1 } }, out = { 15053, 1 }, oq = 2 },
    [19077] = { name = "Blue Dragonscale Breastplate", t = { 1, 280, 290, 300 }, scroll = 15751, train = 260, scrollPrice = 20000, sq = 1, r = { { 8170, 28 }, { 15415, 30 }, { 15407, 1 }, { 14341, 1 } }, out = { 15048, 1 }, oq = 3 },
    [19078] = { name = "Living Leggings", t = { 1, 280, 290, 300 }, scroll = 15752, train = 260, sq = 3, r = { { 8170, 16 }, { 12803, 6 }, { 15407, 1 }, { 14341, 1 } }, out = { 15060, 1 }, oq = 3 },
    [19079] = { name = "Stormshroud Armor", t = { 1, 280, 290, 300 }, scroll = 15753, train = 260, sq = 3, r = { { 8170, 16 }, { 7080, 3 }, { 7082, 3 }, { 15407, 1 }, { 14341, 1 } }, out = { 15056, 1 }, oq = 3 },
    [19080] = { name = "Warbear Woolies", t = { 1, 280, 290, 300 }, scroll = 20254, train = 260, scrollPrice = 20000, rep = { 576, 4 }, sq = 1, r = { { 8170, 24 }, { 15419, 14 }, { 14341, 1 } }, out = { 15065, 1 }, oq = 3 },
    [19081] = { name = "Chimeric Vest", t = { 1, 285, 295, 305 }, scroll = 15755, train = 265, sq = 2, r = { { 8170, 10 }, { 15423, 10 }, { 14341, 1 } }, out = { 15075, 1 }, oq = 2 },
    [19082] = { name = "Runic Leather Headband", t = { 1, 285, 295, 305 }, scroll = 15756, train = 265, scrollPrice = 22000, sq = 1, r = { { 8170, 14 }, { 14047, 10 }, { 14341, 1 } }, out = { 15094, 1 }, oq = 2 },
    [19083] = { name = "Wicked Leather Pants", t = { 1, 285, 295, 305 }, scroll = 15757, train = 265, sq = 2, r = { { 8170, 16 }, { 15407, 1 }, { 2325, 3 }, { 14341, 1 } }, out = { 15087, 1 }, oq = 2 },
    [19084] = { name = "Devilsaur Gauntlets", t = { 1, 285, 295, 305 }, scroll = 15758, train = 265, scrollPrice = 22000, sq = 1, r = { { 8170, 30 }, { 15417, 8 }, { 14341, 1 } }, out = { 15063, 1 }, oq = 3 },
    [19085] = { name = "Black Dragonscale Breastplate", t = { 1, 285, 295, 305 }, scroll = 15759, train = 265, sq = 1, r = { { 8170, 40 }, { 15416, 60 }, { 15407, 1 }, { 14341, 2 } }, out = { 15050, 1 }, oq = 3 },
    [19086] = { name = "Ironfeather Breastplate", t = { 1, 285, 295, 305 }, scroll = 15760, train = 265, sq = 3, r = { { 8170, 40 }, { 15420, 120 }, { 1529, 1 }, { 15407, 1 }, { 14341, 1 } }, out = { 15066, 1 }, oq = 3 },
    [19087] = { name = "Frostsaber Gloves", t = { 1, 290, 300, 310 }, scroll = 15761, train = 270, sq = 2, r = { { 8170, 6 }, { 15422, 10 }, { 14341, 1 } }, out = { 15070, 1 }, oq = 2 },
    [19088] = { name = "Heavy Scorpid Helm", t = { 1, 290, 300, 310 }, scroll = 15762, train = 270, scrollPrice = 25000, sq = 1, r = { { 8170, 8 }, { 15408, 12 }, { 15407, 1 }, { 14341, 1 } }, out = { 15080, 1 }, oq = 2 },
    [19089] = { name = "Blue Dragonscale Shoulders", t = { 1, 290, 300, 310 }, scroll = 15763, train = 270, sq = 3, r = { { 8170, 28 }, { 15415, 30 }, { 12810, 2 }, { 15407, 1 }, { 14341, 1 } }, out = { 15049, 1 }, oq = 3 },
    [19090] = { name = "Stormshroud Shoulders", t = { 1, 290, 300, 310 }, scroll = 15764, train = 270, sq = 3, r = { { 8170, 12 }, { 7080, 3 }, { 7082, 3 }, { 12810, 2 }, { 14341, 1 } }, out = { 15058, 1 }, oq = 3 },
    [19091] = { name = "Runic Leather Pants", t = { 1, 295, 305, 315 }, scroll = 15765, train = 275, sq = 2, r = { { 8170, 18 }, { 14047, 12 }, { 12810, 2 }, { 14341, 1 } }, out = { 15095, 1 }, oq = 2 },
    [19092] = { name = "Wicked Leather Belt", t = { 1, 295, 305, 315 }, scroll = 15768, train = 275, sq = 2, r = { { 8170, 14 }, { 2325, 2 }, { 14341, 2 } }, out = { 15088, 1 }, oq = 2 },
    [19093] = { name = "Onyxia Scale Cloak", t = { 1, 320, 330, 340 }, scroll = 15769, train = 310, sq = 1, r = { { 15410, 1 }, { 14044, 1 }, { 14341, 1 } }, out = { 15138, 1 }, oq = 3 },
    [19094] = { name = "Black Dragonscale Shoulders", t = { 1, 310, 320, 330 }, scroll = 15770, train = 270, sq = 3, r = { { 8170, 44 }, { 15416, 45 }, { 12810, 2 }, { 15407, 1 }, { 14341, 1 } }, out = { 15051, 1 }, oq = 3 },
    [19095] = { name = "Living Breastplate", t = { 1, 310, 320, 330 }, scroll = 15771, train = 290, sq = 3, r = { { 8170, 16 }, { 12803, 8 }, { 14342, 2 }, { 15407, 1 }, { 14341, 2 } }, out = { 15059, 1 }, oq = 3 },
    [19097] = { name = "Devilsaur Leggings", t = { 1, 310, 320, 330 }, scroll = 15772, train = 290, sq = 3, r = { { 8170, 30 }, { 15417, 14 }, { 15407, 1 }, { 14341, 1 } }, out = { 15062, 1 }, oq = 3 },
    [19098] = { name = "Wicked Leather Armor", t = { 1, 300, 310, 320 }, scroll = 15773, train = 280, sq = 2, r = { { 8170, 20 }, { 15407, 2 }, { 14256, 6 }, { 2325, 4 }, { 14341, 2 } }, out = { 15085, 1 }, oq = 2 },
    [19100] = { name = "Heavy Scorpid Shoulders", t = { 1, 300, 310, 320 }, scroll = 15774, train = 280, sq = 2, r = { { 8170, 14 }, { 15408, 14 }, { 15407, 1 }, { 14341, 2 } }, out = { 15081, 1 }, oq = 2 },
    [19101] = { name = "Volcanic Shoulders", t = { 1, 300, 310, 320 }, scroll = 15775, train = 280, sq = 2, r = { { 8170, 10 }, { 7078, 1 }, { 7076, 1 }, { 14341, 2 } }, out = { 15055, 1 }, oq = 2 },
    [19102] = { name = "Runic Leather Armor", t = { 1, 305, 315, 325 }, scroll = 15776, train = 285, sq = 2, r = { { 8170, 22 }, { 12810, 4 }, { 14047, 16 }, { 15407, 1 }, { 14341, 2 } }, out = { 15090, 1 }, oq = 2 },
    [19103] = { name = "Runic Leather Shoulders", t = { 1, 305, 315, 325 }, scroll = 15777, train = 285, sq = 2, r = { { 8170, 16 }, { 12810, 4 }, { 14047, 18 }, { 15407, 1 }, { 14341, 2 } }, out = { 15096, 1 }, oq = 2 },
    [19104] = { name = "Frostsaber Tunic", t = { 1, 310, 320, 330 }, scroll = 15779, train = 290, sq = 2, r = { { 8170, 12 }, { 15422, 12 }, { 15407, 1 }, { 14341, 2 } }, out = { 15068, 1 }, oq = 2 },
    [19106] = { name = "Onyxia Scale Breastplate", t = { 1, 320, 330, 340 }, scroll = 15780, train = 310, sq = 1, r = { { 8170, 40 }, { 15410, 12 }, { 15416, 60 }, { 14341, 2 } }, out = { 15141, 1 }, oq = 4 },
    [19107] = { name = "Black Dragonscale Leggings", t = { 1, 310, 320, 330 }, scroll = 15781, train = 290, sq = 3, r = { { 8170, 40 }, { 15416, 60 }, { 12810, 4 }, { 15407, 1 }, { 14341, 2 } }, out = { 15052, 1 }, oq = 3 },
    [20648] = { name = "Medium Leather", t = { 1, 75, 80, 85 }, fee = 500, train = 75, r = { { 2318, 4 } }, out = { 2319, 1 }, oq = 1 },
    [20649] = { name = "Heavy Leather", t = { 1, 125, 130, 135 }, fee = 1000, train = 125, r = { { 2319, 5 } }, out = { 4234, 1 }, oq = 1 },
    [20650] = { name = "Thick Leather", t = { 1, 175, 177, 180 }, fee = 4000, train = 175, r = { { 4234, 6 } }, out = { 4304, 1 }, oq = 1 },
    [20853] = { name = "Corehound Boots", t = { 1, 315, 325, 335 }, scroll = 17022, train = 295, rep = { 59, 4 }, sq = 1, r = { { 17012, 20 }, { 17010, 6 }, { 17011, 2 }, { 14341, 2 } }, out = { 16982, 1 }, oq = 4 },
    [20854] = { name = "Molten Helm", t = { 1, 320, 330, 340 }, scroll = 17023, train = 300, rep = { 59, 4 }, sq = 1, r = { { 17012, 15 }, { 17010, 3 }, { 17011, 6 }, { 14341, 2 } }, out = { 16983, 1 }, oq = 4 },
    [20855] = { name = "Black Dragonscale Boots", t = { 1, 320, 330, 340 }, scroll = 17025, train = 300, rep = { 59, 5 }, sq = 1, r = { { 12810, 6 }, { 15416, 30 }, { 17010, 4 }, { 17011, 3 }, { 14341, 2 } }, out = { 16984, 1 }, oq = 4 },
    [21943] = { name = "Gloves of the Greatfather", t = { 1, 185, 195, 205 }, scroll = 17722, train = 165, sq = 2, r = { { 4234, 8 }, { 7067, 4 }, { 4291, 1 } }, out = { 17721, 1 }, oq = 2 },
    [22711] = { name = "Shadowskin Gloves", t = { 1, 185, 195, 205 }, scroll = 18239, train = 175, scrollPrice = 3500, sq = 1, r = { { 4304, 6 }, { 7428, 8 }, { 7971, 2 }, { 4236, 2 }, { 1210, 4 }, { 8343, 1 } }, out = { 18238, 1 }, oq = 3 },
    [22727] = { name = "Core Armor Kit", t = { 1, 320, 330, 340 }, scroll = 18252, train = 300, sq = 3, r = { { 17012, 3 }, { 14341, 2 } }, out = { 18251, 1 }, oq = 3 },
    [22815] = { name = "Gordok Ogre Suit", t = { 1, 285, 290, 295 }, r = { { 8170, 4 }, { 14048, 2 }, { 18240, 1 }, { 14341, 1 } }, out = { 18258, 1 }, oq = 2 },
    [22921] = { name = "Girdle of Insight", t = { 1, 310, 320, 330 }, scroll = 18514, train = 290, sq = 3, r = { { 8170, 12 }, { 12804, 12 }, { 15407, 2 }, { 14341, 4 } }, out = { 18504, 1 }, oq = 3 },
    [22922] = { name = "Mongoose Boots", t = { 1, 310, 320, 330 }, scroll = 18515, train = 290, sq = 3, r = { { 8170, 12 }, { 7082, 6 }, { 11754, 4 }, { 15407, 2 }, { 14341, 4 } }, out = { 18506, 1 }, oq = 3 },
    [22923] = { name = "Swift Flight Bracers", t = { 1, 310, 320, 330 }, scroll = 18516, train = 290, sq = 3, r = { { 8170, 12 }, { 18512, 8 }, { 15420, 60 }, { 15407, 4 }, { 14341, 4 } }, out = { 18508, 1 }, oq = 3 },
    [22926] = { name = "Chromatic Cloak", t = { 1, 320, 330, 340 }, scroll = 18517, train = 300, sq = 4, r = { { 8170, 30 }, { 12607, 12 }, { 15416, 30 }, { 15414, 30 }, { 15407, 5 }, { 14341, 8 } }, out = { 18509, 1 }, oq = 4 },
    [22927] = { name = "Hide of the Wild", t = { 1, 320, 330, 340 }, scroll = 18518, train = 300, sq = 4, r = { { 8170, 30 }, { 12803, 12 }, { 7080, 10 }, { 18512, 8 }, { 15407, 3 }, { 14341, 8 } }, out = { 18510, 1 }, oq = 4 },
    [22928] = { name = "Shifting Cloak", t = { 1, 320, 330, 340 }, scroll = 18519, train = 300, sq = 4, r = { { 8170, 30 }, { 7082, 12 }, { 12753, 4 }, { 12809, 8 }, { 15407, 4 }, { 14341, 8 } }, out = { 18511, 1 }, oq = 4 },
    [23190] = { name = "Heavy Leather Ball", t = { 1, 125, 130, 135 }, scroll = 18731, train = 125, scrollPrice = 2000, sq = 1, r = { { 4234, 2 }, { 2321, 1 } }, out = { 18662, 1 }, oq = 1 },
    [23399] = { name = "Barbaric Bracers", t = { 1, 155, 165, 175 }, scroll = 18949, train = 130, scrollPrice = 2000, sq = 1, r = { { 4234, 8 }, { 4236, 2 }, { 5498, 4 }, { 4461, 1 }, { 5637, 4 } }, out = { 18948, 1 }, oq = 3 },
    [23628] = { name = "Heavy Timbermaw Belt", t = { 1, 285, 295, 305 }, scroll = 19202, train = 265, scrollPrice = 22000, rep = { 576, 5 }, sq = 1, r = { { 8170, 12 }, { 7076, 3 }, { 12803, 3 }, { 14341, 1 } }, out = { 19043, 1 }, oq = 3 },
    [23629] = { name = "Heavy Timbermaw Boots", t = { 1, 300, 310, 320 }, scroll = 19204, train = 295, scrollPrice = 40000, rep = { 576, 6 }, sq = 1, r = { { 8170, 20 }, { 7076, 6 }, { 12803, 6 }, { 14341, 1 } }, out = { 19048, 1 }, oq = 3 },
    [23703] = { name = "Might of the Timbermaw", t = { 1, 285, 295, 305 }, scroll = 19326, train = 265, scrollPrice = 22000, rep = { 576, 5 }, sq = 1, r = { { 8170, 30 }, { 12804, 2 }, { 12803, 4 }, { 15407, 2 }, { 14341, 2 } }, out = { 19044, 1 }, oq = 3 },
    [23704] = { name = "Timbermaw Brawlers", t = { 1, 315, 325, 335 }, scroll = 19327, train = 295, scrollPrice = 40000, rep = { 576, 6 }, sq = 1, r = { { 12810, 8 }, { 12804, 6 }, { 12803, 6 }, { 15407, 2 }, { 14227, 2 } }, out = { 19049, 1 }, oq = 3 },
    [23705] = { name = "Dawn Treaders", t = { 1, 285, 295, 305 }, scroll = 19328, train = 265, scrollPrice = 22000, rep = { 529, 5 }, sq = 1, r = { { 8170, 30 }, { 12809, 2 }, { 7080, 4 }, { 15407, 2 }, { 14341, 2 } }, out = { 19052, 1 }, oq = 3 },
    [23706] = { name = "Golden Mantle of the Dawn", t = { 1, 315, 325, 335 }, scroll = 19329, train = 295, scrollPrice = 40000, rep = { 529, 6 }, sq = 1, r = { { 12810, 8 }, { 12803, 4 }, { 12809, 4 }, { 15407, 2 }, { 14341, 2 } }, out = { 19058, 1 }, oq = 3 },
    [23707] = { name = "Lava Belt", t = { 1, 320, 330, 340 }, scroll = 19330, train = 300, rep = { 59, 5 }, sq = 1, r = { { 17011, 5 }, { 15407, 4 }, { 14227, 4 } }, out = { 19149, 1 }, oq = 4 },
    [23708] = { name = "Chromatic Gauntlets", t = { 1, 320, 330, 340 }, scroll = 19331, train = 300, rep = { 59, 6 }, sq = 1, r = { { 17010, 5 }, { 17011, 2 }, { 17012, 4 }, { 12607, 4 }, { 15407, 4 }, { 14227, 4 } }, out = { 19157, 1 }, oq = 4 },
    [23709] = { name = "Corehound Belt", t = { 1, 320, 330, 340 }, scroll = 19332, train = 300, rep = { 59, 6 }, sq = 1, r = { { 17010, 8 }, { 17012, 12 }, { 12810, 10 }, { 15407, 4 }, { 14227, 4 } }, out = { 19162, 1 }, oq = 4 },
    [23710] = { name = "Molten Belt", t = { 1, 320, 330, 340 }, scroll = 19333, train = 300, rep = { 59, 6 }, sq = 1, r = { { 17010, 2 }, { 17011, 7 }, { 7076, 6 }, { 15407, 4 }, { 14227, 4 } }, out = { 19163, 1 }, oq = 4 },
    [24121] = { name = "Primal Batskin Jerkin", t = { 1, 320, 330, 340 }, scroll = 19769, train = 300, scrollPrice = 50000, rep = { 270, 6 }, sq = 1, r = { { 19767, 14 }, { 15407, 5 }, { 12803, 4 }, { 14341, 4 } }, out = { 19685, 1 }, oq = 3 },
    [24122] = { name = "Primal Batskin Gloves", t = { 1, 320, 330, 340 }, scroll = 19770, train = 300, scrollPrice = 50000, rep = { 270, 5 }, sq = 1, r = { { 19767, 10 }, { 15407, 4 }, { 12803, 4 }, { 14341, 3 } }, out = { 19686, 1 }, oq = 3 },
    [24123] = { name = "Primal Batskin Bracers", t = { 1, 320, 330, 340 }, scroll = 19771, train = 300, scrollPrice = 50000, rep = { 270, 4 }, sq = 1, r = { { 19767, 8 }, { 15407, 3 }, { 12803, 4 }, { 14341, 3 } }, out = { 19687, 1 }, oq = 3 },
    [24124] = { name = "Blood Tiger Breastplate", t = { 1, 320, 330, 340 }, scroll = 19772, train = 300, scrollPrice = 50000, rep = { 270, 6 }, sq = 1, r = { { 19768, 35 }, { 19726, 2 }, { 15407, 3 }, { 14341, 3 } }, out = { 19688, 1 }, oq = 3 },
    [24125] = { name = "Blood Tiger Shoulders", t = { 1, 320, 330, 340 }, scroll = 19773, train = 300, scrollPrice = 50000, rep = { 270, 5 }, sq = 1, r = { { 19768, 25 }, { 19726, 2 }, { 15407, 3 }, { 14341, 3 } }, out = { 19689, 1 }, oq = 3 },
    [24654] = { name = "Blue Dragonscale Leggings", t = { 1, 310, 320, 330 }, fee = 45000, train = 300, spec = "Dragonscale", tr = { 7867 }, r = { { 8170, 28 }, { 15415, 36 }, { 15407, 2 }, { 14341, 2 } }, out = { 20295, 1 }, oq = 3 },
    [24655] = { name = "Green Dragonscale Gauntlets", t = { 1, 275, 285, 295 }, fee = 27000, train = 280, spec = "Dragonscale", tr = { 7867 }, r = { { 8170, 20 }, { 15412, 30 }, { 15407, 1 }, { 14341, 2 } }, out = { 20296, 1 }, oq = 3 },
    [24703] = { name = "Dreamscale Breastplate", t = { 1, 320, 330, 340 }, scroll = 20382, train = 310, gone = true, sq = 1, r = { { 12810, 12 }, { 20381, 6 }, { 12803, 4 }, { 15407, 4 }, { 14227, 6 } }, out = { 20380, 1 }, oq = 4 },
    [24846] = { name = "Spitfire Bracers", t = { 1, 310, 320, 330 }, scroll = 20506, train = 300, gone = true, sq = 1, r = { { 20500, 1 }, { 20498, 20 }, { 7078, 2 } }, out = { 20481, 1 }, oq = 3 },
    [24847] = { name = "Spitfire Gauntlets", t = { 1, 305, 315, 325 }, scroll = 20507, train = 295, gone = true, sq = 1, r = { { 20500, 2 }, { 20498, 30 }, { 7078, 2 }, { 15407, 1 } }, out = { 20480, 1 }, oq = 3 },
    [24848] = { name = "Spitfire Breastplate", t = { 1, 310, 320, 330 }, scroll = 20508, train = 300, gone = true, sq = 1, r = { { 20500, 3 }, { 20498, 40 }, { 7078, 2 }, { 15407, 2 } }, out = { 20479, 1 }, oq = 3 },
    [24849] = { name = "Sandstalker Bracers", t = { 1, 310, 320, 330 }, scroll = 20509, train = 300, gone = true, sq = 1, r = { { 20501, 1 }, { 20498, 20 }, { 18512, 2 } }, out = { 20476, 1 }, oq = 3 },
    [24850] = { name = "Sandstalker Gauntlets", t = { 1, 310, 320, 330 }, scroll = 20510, train = 300, gone = true, sq = 1, r = { { 20501, 2 }, { 20498, 30 }, { 18512, 2 }, { 15407, 1 } }, out = { 20477, 1 }, oq = 3 },
    [24851] = { name = "Sandstalker Breastplate", t = { 1, 310, 320, 330 }, scroll = 20511, train = 300, gone = true, sq = 1, r = { { 20501, 3 }, { 20498, 40 }, { 18512, 2 }, { 15407, 2 } }, out = { 20478, 1 }, oq = 3 },
    [24940] = { name = "Black Whelp Tunic", t = { 1, 100, 112, 125 }, scroll = 20576, train = 75, scrollPrice = 1400, sq = 1, r = { { 2319, 8 }, { 7286, 8 }, { 4231, 1 }, { 2321, 2 } }, out = { 20575, 1 }, oq = 2 },
    [26279] = { name = "Stormshroud Gloves", t = { 1, 310, 320, 330 }, scroll = 21548, train = 290, sq = 3, r = { { 12810, 6 }, { 7080, 4 }, { 7082, 4 }, { 15407, 2 }, { 14227, 2 } }, out = { 21278, 1 }, oq = 3 },
    [28219] = { name = "Polar Tunic", t = { 1, 320, 330, 340 }, scroll = 22692, train = 310, sq = 1, r = { { 22682, 7 }, { 12810, 16 }, { 7080, 2 }, { 15407, 4 }, { 14227, 4 } }, out = { 22661, 1 }, oq = 4 },
    [28220] = { name = "Polar Gloves", t = { 1, 320, 330, 340 }, scroll = 22694, train = 310, sq = 1, r = { { 22682, 5 }, { 12810, 12 }, { 7080, 2 }, { 15407, 3 }, { 14227, 4 } }, out = { 22662, 1 }, oq = 4 },
    [28221] = { name = "Polar Bracers", t = { 1, 320, 330, 340 }, scroll = 22695, train = 310, sq = 1, r = { { 22682, 4 }, { 12810, 12 }, { 7080, 2 }, { 15407, 2 }, { 14227, 4 } }, out = { 22663, 1 }, oq = 4 },
    [28222] = { name = "Icy Scale Breastplate", t = { 1, 320, 330, 340 }, scroll = 22696, train = 310, sq = 1, r = { { 22682, 7 }, { 15408, 24 }, { 7080, 2 }, { 15407, 4 }, { 14227, 4 } }, out = { 22664, 1 }, oq = 4 },
    [28223] = { name = "Icy Scale Gauntlets", t = { 1, 320, 330, 340 }, scroll = 22697, train = 310, sq = 1, r = { { 22682, 5 }, { 15408, 16 }, { 7080, 2 }, { 15407, 3 }, { 14227, 4 } }, out = { 22666, 1 }, oq = 4 },
    [28224] = { name = "Icy Scale Bracers", t = { 1, 320, 330, 340 }, scroll = 22698, train = 310, sq = 1, r = { { 22682, 4 }, { 15408, 16 }, { 7080, 2 }, { 15407, 2 }, { 14227, 4 } }, out = { 22665, 1 }, oq = 4 },
    [28472] = { name = "Bramblewood Helm", t = { 1, 320, 330, 340 }, scroll = 22771, train = 310, gone = true, sq = 1, r = { { 12810, 12 }, { 19726, 2 }, { 12803, 2 }, { 15407, 2 } }, out = { 22759, 1 }, oq = 3 },
    [28473] = { name = "Bramblewood Boots", t = { 1, 320, 330, 340 }, scroll = 22770, train = 310, gone = true, sq = 1, r = { { 12810, 6 }, { 18512, 2 }, { 12803, 2 }, { 15407, 2 } }, out = { 22760, 1 }, oq = 3 },
    [28474] = { name = "Bramblewood Belt", t = { 1, 320, 330, 340 }, scroll = 22769, train = 310, gone = true, sq = 1, r = { { 12810, 4 }, { 12803, 2 }, { 15407, 1 } }, out = { 22761, 1 }, oq = 3 },
    [435819] = { name = "Faintly Glowing Leather", t = { 1, 200, 210, 220 }, scroll = 215367, train = 200, gone = true, sq = 3, r = { { 8172, 1 }, { 213370, 5 } }, out = { 213369, 1 }, oq = 3 },
    [435904] = { name = "Glowing Gneuro-Linked Cowl", t = { 1, 225, 230, 235 }, scroll = 215152, train = 225, gone = true, sq = 4, r = { { 213379, 1 }, { 8172, 5 }, { 4291, 2 }, { 213369, 5 } }, out = { 215166, 1 }, oq = 1 },
    [461645] = { name = "Honed Blue Dragonscale Shoulders", t = { 1, 315, 325, 335 }, scroll = 227899, train = 295, sq = 3, r = { { 8170, 28 }, { 15415, 30 }, { 12810, 2 }, { 15407, 1 }, { 14341, 1 } }, out = { 227873, 1 }, oq = 1 },
    [461649] = { name = "Living Green Dragonscale Leggings", t = { 1, 290, 300, 310 }, scroll = 227900, train = 270, sq = 3, r = { { 8170, 20 }, { 15412, 25 }, { 14341, 1 } }, out = { 227877, 1 }, oq = 1 },
    [461653] = { name = "Brilliant Chromatic Cloak", t = { 1, 320, 330, 340 }, scroll = 227910, train = 300, sq = 4, r = { { 8170, 30 }, { 12607, 12 }, { 15416, 30 }, { 15414, 30 }, { 15407, 5 }, { 14341, 8 } }, out = { 227869, 1 }, oq = 1 },
    [461655] = { name = "Hardened Black Dragonscale Breastplate", t = { 1, 310, 320, 330 }, scroll = 227902, train = 290, gone = true, sq = 1, r = { { 8170, 40 }, { 15416, 60 }, { 15407, 1 }, { 14341, 2 } }, out = { 227851, 1 }, oq = 1 },
    [461657] = { name = "Hardened Black Dragonscale Leggings", t = { 1, 320, 330, 340 }, scroll = 227903, train = 300, sq = 3, r = { { 8170, 40 }, { 15416, 60 }, { 12810, 4 }, { 15407, 1 }, { 14341, 2 } }, out = { 227852, 1 }, oq = 1 },
    [461659] = { name = "Hardened Black Dragonscale Shoulders", t = { 1, 320, 330, 340 }, scroll = 227904, train = 300, sq = 3, r = { { 8170, 44 }, { 15416, 45 }, { 12810, 2 }, { 15407, 1 }, { 14341, 1 } }, out = { 227853, 1 }, oq = 1 },
    [461661] = { name = "Masterwork Volcanic Breastplate", t = { 1, 305, 315, 325 }, scroll = 227906, train = 285, sq = 2, r = { { 8170, 8 }, { 7078, 1 }, { 7076, 1 }, { 14341, 1 } }, out = { 227868, 1 }, oq = 1 },
    [461663] = { name = "Masterwork Volcanic Shoulders", t = { 1, 320, 330, 340 }, scroll = 227907, train = 300, sq = 2, r = { { 8170, 10 }, { 7078, 1 }, { 7076, 1 }, { 14341, 2 } }, out = { 227866, 1 }, oq = 1 },
    [461665] = { name = "Masterwork Volcanic Leggings", t = { 1, 290, 300, 310 }, scroll = 227908, train = 270, sq = 2, r = { { 8170, 6 }, { 7078, 1 }, { 7075, 1 }, { 14341, 1 } }, out = { 227867, 1 }, oq = 1 },
    [461673] = { name = "Honed Blue Dragonscale Breastplate", t = { 1, 305, 315, 325 }, scroll = 227898, train = 285, gone = true, sq = 1, r = { { 8170, 28 }, { 15415, 30 }, { 15407, 1 }, { 14341, 1 } }, out = { 227875, 1 }, oq = 1 },
    [461677] = { name = "Living Green Dragonscale Gauntlets", t = { 1, 300, 310, 320 }, scroll = 228251, train = 270, sq = 3, r = { { 8170, 20 }, { 15412, 25 }, { 14341, 1 } }, out = { 227878, 1 }, oq = 1 },
    [461690] = { name = "Mastercrafted Shifting Cloak", t = { 1, 320, 330, 340 }, scroll = 228276, train = 300, sq = 4, r = { { 8170, 30 }, { 7082, 12 }, { 12753, 4 }, { 12809, 8 }, { 15407, 4 }, { 14341, 8 } }, out = { 227854, 1 }, oq = 1 },
    [461692] = { name = "Synthetic Gordok Ogre Suit", t = { 1, 285, 290, 295 }, scroll = 228115, train = 275, sq = 1, r = { { 8170, 4 }, { 14048, 2 }, { 18240, 1 }, { 14341, 1 } }, out = { 227855, 1 }, oq = 1 },
    [461706] = { name = "Swift Flight Vambraces", t = { 1, 320, 330, 340 }, scroll = 228301, train = 300, sq = 3, r = { { 8170, 12 }, { 18512, 8 }, { 15420, 60 }, { 15407, 4 }, { 14341, 4 } }, out = { 227883, 1 }, oq = 1 },
    [461720] = { name = "Living Green Dragonscale Breastplate", t = { 1, 280, 290, 300 }, scroll = 228309, train = 260, gone = true, sq = 1, r = { { 8170, 20 }, { 15412, 25 }, { 14341, 2 } }, out = { 227879, 1 }, oq = 1 },
    [461722] = { name = "Devilcore Gauntlets", t = { 1, 310, 320, 330 }, scroll = 228119, train = 290, sq = 3, r = { { 8170, 30 }, { 15417, 8 }, { 14341, 1 }, { 7078, 8 } }, out = { 227848, 1 }, oq = 1 },
    [461724] = { name = "Devilcore Leggings", t = { 1, 320, 330, 340 }, scroll = 228120, train = 300, sq = 3, r = { { 8170, 30 }, { 15417, 20 }, { 15407, 1 }, { 14341, 1 }, { 7078, 10 } }, out = { 227847, 1 }, oq = 1 },
    [461754] = { name = "Girdle of Arcane Insight", t = { 1, 320, 330, 340 }, scroll = 228319, train = 300, sq = 3, r = { { 8170, 12 }, { 12804, 12 }, { 15407, 2 }, { 14341, 4 } }, out = { 227882, 1 }, oq = 1 },
    [462227] = { name = "Honed Blue Dragonscale Leggings", t = { 1, 320, 330, 340 }, r = { { 8170, 28 }, { 15415, 36 }, { 15407, 2 }, { 14341, 2 } }, out = { 227874, 1 }, oq = 1 },
    [1214303] = { name = "Dreamscale Kilt", t = { 1, 320, 330, 340 }, scroll = 234481, train = 310, sq = 1, r = { { 12810, 12 }, { 20381, 6 }, { 12803, 4 }, { 15407, 4 }, { 14227, 6 } }, out = { 234482, 1 }, oq = 1 },
    [1224615] = { name = "Scarlet Infiltrator's Bandana", t = { 1, 285, 295, 305 }, scroll = 238306, train = 280, sq = 3, r = { { 12938, 1 }, { 12811, 2 }, { 8170, 12 } }, out = { 238272, 1 }, oq = 1 },
    [1224616] = { name = "Scarlet Infiltrator's Shoulderpads", t = { 1, 285, 295, 305 }, scroll = 238307, train = 280, sq = 3, r = { { 12811, 1 }, { 8170, 10 } }, out = { 238273, 1 }, oq = 1 },
    [1224617] = { name = "Scarlet Infiltrator's Vest", t = { 1, 285, 295, 305 }, scroll = 238308, train = 280, sq = 3, r = { { 12938, 1 }, { 12811, 1 }, { 8170, 12 } }, out = { 238274, 1 }, oq = 1 },
    [1224618] = { name = "Scarlet Infiltrator's Bracers", t = { 1, 260, 282, 305 }, scroll = 238309, train = 250, sq = 3, r = { { 8170, 8 } }, out = { 238275, 1 }, oq = 1 },
    [1224619] = { name = "Scarlet Infiltrator's Gloves", t = { 1, 270, 287, 305 }, scroll = 238310, train = 260, sq = 3, r = { { 12811, 1 }, { 8170, 10 } }, out = { 238276, 1 }, oq = 1 },
    [1224620] = { name = "Scarlet Infiltrator's Belt", t = { 1, 260, 282, 305 }, scroll = 238311, train = 250, sq = 3, r = { { 12811, 1 }, { 8170, 10 } }, out = { 238277, 1 }, oq = 1 },
    [1224621] = { name = "Scarlet Infiltrator's Trousers", t = { 1, 280, 292, 305 }, scroll = 238312, train = 270, sq = 3, r = { { 12938, 1 }, { 12811, 1 }, { 8170, 12 } }, out = { 238278, 1 }, oq = 1 },
    [1224622] = { name = "Scarlet Infiltrator's Shoes", t = { 1, 270, 287, 305 }, scroll = 238313, train = 260, sq = 3, r = { { 12811, 1 }, { 8170, 10 } }, out = { 238279, 1 }, oq = 1 },
    [1224623] = { name = "Scarlet Huntsman's Coif", t = { 1, 285, 295, 305 }, scroll = 238314, train = 280, sq = 3, r = { { 12938, 1 }, { 12811, 2 }, { 15408, 12 } }, out = { 238280, 1 }, oq = 1 },
    [1224624] = { name = "Scarlet Huntsman's Pauldrons", t = { 1, 285, 295, 305 }, scroll = 238315, train = 280, sq = 3, r = { { 12811, 1 }, { 15408, 10 } }, out = { 238281, 1 }, oq = 1 },
    [1224625] = { name = "Scarlet Huntsman's Chain", t = { 1, 285, 295, 305 }, scroll = 238316, train = 280, sq = 3, r = { { 12938, 1 }, { 12811, 1 }, { 15408, 12 } }, out = { 238282, 1 }, oq = 1 },
    [1224626] = { name = "Scarlet Huntsman's Wristguards", t = { 1, 260, 282, 305 }, scroll = 238317, train = 250, sq = 3, r = { { 15408, 8 } }, out = { 238283, 1 }, oq = 1 },
    [1224627] = { name = "Scarlet Huntsman's Handguards", t = { 1, 270, 287, 305 }, scroll = 238318, train = 260, sq = 3, r = { { 12811, 1 }, { 15408, 10 } }, out = { 238284, 1 }, oq = 1 },
    [1224628] = { name = "Scarlet Huntsman's Clasp", t = { 1, 260, 282, 305 }, scroll = 238319, train = 250, sq = 3, r = { { 12811, 1 }, { 15408, 10 } }, out = { 238285, 1 }, oq = 1 },
    [1224629] = { name = "Scarlet Huntsman's Legguards", t = { 1, 280, 292, 305 }, scroll = 238320, train = 270, sq = 3, r = { { 12938, 1 }, { 12811, 1 }, { 15408, 12 } }, out = { 238286, 1 }, oq = 1 },
    [1224630] = { name = "Scarlet Huntsman's Boots", t = { 1, 270, 287, 305 }, scroll = 238321, train = 260, sq = 3, r = { { 12811, 1 }, { 15408, 10 } }, out = { 238287, 1 }, oq = 1 },
    [1226689] = { name = "Scarlet Quiver", t = { 1, 280, 285, 290 }, scroll = 238927, train = 275, sq = 2, r = { { 12811, 1 }, { 8170, 24 }, { 15407, 2 } }, out = { 238925, 1 }, oq = 1 },
    [1226690] = { name = "Scarlet Ammo Pouch", t = { 1, 280, 285, 290 }, scroll = 238928, train = 275, sq = 2, r = { { 12811, 1 }, { 15408, 24 }, { 15407, 2 } }, out = { 238926, 1 }, oq = 1 },
    [1229432] = { name = "Camp Tent", t = { 1, 20, 20, 20 }, fee = 0, train = 20, r = { { 2318, 5 } }, out = { 279978, 1 }, oq = 1 },
    [1254965] = { name = "Forceful Rugged Armor Kit", t = { 1, 235, 245, 255 }, scroll = 252942, train = 235, scrollPrice = 5500, sq = 2, r = { { 15564, 1 }, { 11176, 2 }, { 9206, 2 }, { 249429, 1 }, { 248824, 1 } }, out = { 252488, 1 }, oq = 2 },
    [1254966] = { name = "Mystic Rugged Armor Kit", t = { 1, 235, 245, 255 }, scroll = 252941, train = 235, sq = 2, favor = 90, favorRep = 6, r = { { 15564, 1 }, { 11176, 2 }, { 13444, 2 }, { 249429, 1 }, { 248824, 1 } }, out = { 252487, 1 }, oq = 2 },
    [1254967] = { name = "Pristine Scorpid Leggings", t = { 1, 320, 330, 340 }, scroll = 252940, train = 300, sq = 4, r = { { 8170, 20 }, { 15408, 40 }, { 12810, 12 }, { 15407, 4 }, { 249429, 10 }, { 14341, 2 }, { 248825, 20 } }, out = { 252606, 1 }, oq = 4 },
    [1254968] = { name = "Black Dragonscale Helm", t = { 1, 320, 330, 340 }, scroll = 252939, train = 300, sq = 4, r = { { 8170, 20 }, { 15416, 40 }, { 12810, 12 }, { 15407, 4 }, { 249429, 10 }, { 14341, 2 }, { 248825, 20 } }, out = { 252605, 1 }, oq = 4 },
    [1254969] = { name = "Blue Dragonscale Helm", t = { 1, 320, 330, 340 }, scroll = 252938, train = 300, sq = 4, r = { { 8170, 20 }, { 15415, 40 }, { 12810, 12 }, { 15407, 6 }, { 249429, 10 }, { 14341, 2 }, { 248825, 20 } }, out = { 252604, 1 }, oq = 4 },
    [1254970] = { name = "Red Dragonscale Leggings", t = { 1, 320, 330, 340 }, scroll = 252937, train = 300, sq = 4, r = { { 8170, 20 }, { 15414, 40 }, { 12810, 12 }, { 15407, 4 }, { 249429, 10 }, { 14341, 2 }, { 248825, 20 } }, out = { 252603, 1 }, oq = 4 },
    [1254971] = { name = "Charged Scorpid Boots", t = { 1, 300, 310, 320 }, scroll = 252936, train = 280, sq = 2, r = { { 8170, 12 }, { 15408, 14 }, { 14341, 1 }, { 7069, 2 } }, out = { 252602, 1 }, oq = 2 },
    [1254972] = { name = "Supple Scorpid Sabatons", t = { 1, 300, 310, 320 }, scroll = 252935, train = 280, sq = 2, r = { { 8170, 20 }, { 15408, 10 }, { 14341, 1 } }, out = { 252601, 1 }, oq = 2 },
    [1254973] = { name = "Charged Scorpid Leggings", t = { 1, 290, 300, 310 }, scroll = 252934, train = 270, sq = 2, r = { { 8170, 12 }, { 15408, 14 }, { 14341, 1 }, { 7069, 2 } }, out = { 252600, 1 }, oq = 2 },
    [1254974] = { name = "Supple Scorpid Vest", t = { 1, 290, 300, 310 }, scroll = 252933, train = 270, scrollPrice = 100000, sq = 2, r = { { 8170, 20 }, { 15408, 10 }, { 14341, 1 } }, out = { 252599, 1 }, oq = 2 },
    [1254975] = { name = "Charged Scorpid Vest", t = { 1, 280, 290, 300 }, scroll = 252932, train = 260, sq = 2, r = { { 8170, 6 }, { 15408, 12 }, { 14341, 1 }, { 7069, 2 } }, out = { 252598, 1 }, oq = 2 },
    [1254976] = { name = "Supple Scorpid Helm", t = { 1, 280, 290, 300 }, scroll = 252931, train = 260, sq = 2, r = { { 8170, 11 }, { 15408, 10 }, { 14341, 1 } }, out = { 252597, 1 }, oq = 2 },
    [1254977] = { name = "Charged Scorpid Gauntlets", t = { 1, 275, 285, 295 }, scroll = 252930, train = 255, sq = 2, r = { { 8170, 4 }, { 15408, 8 }, { 14341, 1 }, { 7069, 2 } }, out = { 252596, 1 }, oq = 2 },
    [1254978] = { name = "Supple Scorpid Belt", t = { 1, 275, 285, 295 }, scroll = 252929, train = 255, sq = 2, r = { { 8170, 9 }, { 15408, 6 }, { 14341, 1 } }, out = { 252595, 1 }, oq = 2 },
    [1254979] = { name = "Heavy Scorpid Boots", t = { 1, 275, 285, 295 }, scroll = 252928, train = 255, sq = 2, r = { { 8170, 6 }, { 15408, 8 }, { 14341, 1 } }, out = { 252594, 1 }, oq = 2 },
    [1254980] = { name = "Charged Scorpid Bracers", t = { 1, 275, 285, 295 }, scroll = 252927, train = 255, sq = 2, r = { { 8170, 2 }, { 15408, 4 }, { 14341, 1 }, { 7069, 2 } }, out = { 252593, 1 }, oq = 2 },
    [1254981] = { name = "Supple Scorpid Shoulders", t = { 1, 275, 285, 295 }, scroll = 252926, train = 255, sq = 2, r = { { 8170, 9 }, { 15408, 6 }, { 14341, 1 } }, out = { 252592, 1 }, oq = 2 },
    [1254982] = { name = "Mender's Mail Belt", t = { 1, 270, 280, 290 }, scroll = 252925, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 8170, 12 }, { 8172, 4 }, { 249428, 10 }, { 8343, 2 }, { 5500, 8 }, { 249427, 5 } }, out = { 252591, 1 }, oq = 3, bop = true },
    [1254983] = { name = "Skirmisher's Mail Belt", t = { 1, 270, 280, 290 }, scroll = 252924, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 8170, 12 }, { 8172, 4 }, { 249428, 10 }, { 8343, 2 }, { 3864, 8 }, { 249427, 5 } }, out = { 252590, 1 }, oq = 3, bop = true },
    [1254984] = { name = "Skycaller's Mail Belt", t = { 1, 270, 280, 290 }, scroll = 252923, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 8170, 12 }, { 8172, 4 }, { 249428, 10 }, { 8343, 2 }, { 7070, 8 }, { 249427, 5 } }, out = { 252589, 1 }, oq = 3, bop = true },
    [1254985] = { name = "Stalker's Mail Belt", t = { 1, 270, 280, 290 }, scroll = 252922, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 8170, 12 }, { 8172, 4 }, { 249428, 10 }, { 8343, 2 }, { 7069, 8 }, { 249427, 5 } }, out = { 252588, 1 }, oq = 3, bop = true },
    [1254990] = { name = "Charged Scorpid Shoulders", t = { 1, 270, 280, 290 }, scroll = 252917, train = 250, sq = 2, r = { { 8170, 4 }, { 15408, 8 }, { 14341, 1 }, { 7069, 2 } }, out = { 252583, 1 }, oq = 2 },
    [1254991] = { name = "Supple Scorpid Bracers", t = { 1, 270, 280, 290 }, scroll = 252916, train = 250, sq = 2, r = { { 8170, 7 }, { 15408, 2 }, { 14341, 1 } }, out = { 252582, 1 }, oq = 2 },
    [1254992] = { name = "Charged Scorpid Helm", t = { 1, 260, 270, 280 }, scroll = 252915, train = 240, sq = 2, r = { { 8170, 4 }, { 15408, 6 }, { 14341, 1 }, { 7069, 2 } }, out = { 252581, 1 }, oq = 2 },
    [1254993] = { name = "Supple Scorpid Leggings", t = { 1, 260, 270, 280 }, scroll = 252914, train = 240, sq = 2, r = { { 8170, 9 }, { 15408, 4 }, { 14341, 1 } }, out = { 252580, 1 }, oq = 2 },
    [1254994] = { name = "Mender's Mail Sabatons", t = { 1, 255, 265, 275 }, scroll = 252913, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 16 }, { 8172, 2 }, { 249428, 8 }, { 8343, 2 }, { 5500, 6 }, { 249427, 4 } }, out = { 252579, 1 }, oq = 3, bop = true },
    [1254995] = { name = "Skirmisher's Mail Sabatons", t = { 1, 255, 265, 275 }, scroll = 252912, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 16 }, { 8172, 2 }, { 249428, 8 }, { 8343, 2 }, { 3864, 6 }, { 249427, 4 } }, out = { 252578, 1 }, oq = 3, bop = true },
    [1254996] = { name = "Skycaller's Mail Sabatons", t = { 1, 255, 265, 275 }, scroll = 252911, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 16 }, { 8172, 2 }, { 249428, 8 }, { 8343, 2 }, { 7070, 6 }, { 249427, 4 } }, out = { 252577, 1 }, oq = 3, bop = true },
    [1254997] = { name = "Stalker's Mail Sabatons", t = { 1, 255, 265, 275 }, scroll = 252910, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 16 }, { 8172, 2 }, { 249428, 8 }, { 8343, 2 }, { 7069, 6 }, { 249427, 4 } }, out = { 252576, 1 }, oq = 3, bop = true },
    [1254998] = { name = "Charged Scorpid Belt", t = { 1, 250, 260, 270 }, scroll = 252909, train = 230, sq = 2, r = { { 8170, 6 }, { 15408, 6 }, { 14341, 1 } }, out = { 252575, 1 }, oq = 2 },
    [1254999] = { name = "Supple Scorpid Boots", t = { 1, 250, 260, 270 }, scroll = 252908, train = 230, sq = 2, r = { { 8170, 12 }, { 15408, 4 }, { 14341, 1 } }, out = { 252574, 1 }, oq = 2 },
    [1255000] = { name = "Mender's Mail Bracers", t = { 1, 220, 230, 240 }, scroll = 252907, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 12 }, { 4236, 4 }, { 249428, 6 }, { 8343, 2 }, { 5500, 4 }, { 249427, 3 } }, out = { 252573, 1 }, oq = 3, bop = true },
    [1255001] = { name = "Skirmisher's Mail Bracers", t = { 1, 220, 230, 240 }, scroll = 252906, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 12 }, { 4236, 4 }, { 249428, 6 }, { 8343, 2 }, { 3864, 4 }, { 249427, 3 } }, out = { 252572, 1 }, oq = 3, bop = true },
    [1255002] = { name = "Skycaller's Mail Bracers", t = { 1, 220, 230, 240 }, scroll = 252905, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 12 }, { 4236, 4 }, { 249428, 6 }, { 8343, 2 }, { 7070, 4 }, { 249427, 3 } }, out = { 252571, 1 }, oq = 3, bop = true },
    [1255003] = { name = "Stalker's Mail Bracers", t = { 1, 220, 230, 240 }, scroll = 252904, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 12 }, { 4236, 4 }, { 249428, 6 }, { 8343, 2 }, { 7069, 4 }, { 249427, 3 } }, out = { 252570, 1 }, oq = 3, bop = true },
    [1255004] = { name = "Mender's Mail Shoulders", t = { 1, 220, 230, 240 }, scroll = 252903, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 4304, 10 }, { 4236, 3 }, { 249428, 4 }, { 4291, 2 }, { 5500, 3 }, { 249427, 2 } }, out = { 252569, 1 }, oq = 3, bop = true },
    [1255005] = { name = "Skirmisher's Mail Shoulders", t = { 1, 220, 230, 240 }, scroll = 252902, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 4304, 10 }, { 4236, 3 }, { 249428, 4 }, { 4291, 2 }, { 3864, 3 }, { 249427, 2 } }, out = { 252568, 1 }, oq = 3, bop = true },
    [1255006] = { name = "Skycaller's Mail Shoulders", t = { 1, 220, 230, 240 }, scroll = 252901, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 4304, 10 }, { 4236, 3 }, { 249428, 4 }, { 4291, 2 }, { 7070, 3 }, { 249427, 2 } }, out = { 252567, 1 }, oq = 3, bop = true },
    [1255007] = { name = "Stalker's Mail Shoulders", t = { 1, 220, 230, 240 }, scroll = 252900, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 4304, 10 }, { 4236, 3 }, { 249428, 4 }, { 4291, 2 }, { 7069, 3 }, { 249427, 2 } }, out = { 252566, 1 }, oq = 3, bop = true },
    [1255012] = { name = "Ironfeather Leggings", t = { 1, 320, 330, 340 }, scroll = 252895, train = 300, sq = 4, r = { { 8170, 20 }, { 15420, 120 }, { 1529, 4 }, { 15407, 2 }, { 14341, 4 }, { 249429, 10 }, { 248825, 20 } }, out = { 252486, 1 }, oq = 4 },
    [1255013] = { name = "Warbear Helm", t = { 1, 320, 330, 340 }, scroll = 252894, train = 300, sq = 4, r = { { 8170, 20 }, { 15419, 20 }, { 14341, 4 }, { 15407, 2 }, { 249429, 10 }, { 248825, 20 } }, out = { 252485, 1 }, oq = 4 },
    [1255014] = { name = "Timbermaw Tunic", t = { 1, 320, 330, 340 }, scroll = 252893, train = 300, sq = 4, r = { { 12810, 6 }, { 12804, 20 }, { 12803, 20 }, { 249429, 10 }, { 15407, 4 }, { 14341, 10 }, { 248825, 20 } }, out = { 252484, 1 }, oq = 4 },
    [1255015] = { name = "Dawn Armor", t = { 1, 320, 330, 340 }, scroll = 252892, train = 300, sq = 4, r = { { 12810, 6 }, { 12809, 10 }, { 7080, 20 }, { 249429, 10 }, { 15407, 4 }, { 14341, 10 }, { 248825, 20 } }, out = { 252483, 1 }, oq = 4 },
    [1255016] = { name = "Living Crown", t = { 1, 320, 330, 340 }, scroll = 252891, train = 300, sq = 4, r = { { 8170, 20 }, { 12803, 20 }, { 7080, 20 }, { 249429, 10 }, { 15407, 4 }, { 14341, 10 }, { 248825, 20 } }, out = { 252561, 1 }, oq = 4 },
    [1255017] = { name = "Blue Suede Hat", t = { 1, 300, 310, 320 }, scroll = 252890, train = 280, sq = 2, r = { { 8170, 16 }, { 14341, 1 }, { 6260, 4 } }, out = { 252482, 1 }, oq = 2 },
    [1255018] = { name = "Tooled Leather Pants", t = { 1, 300, 310, 320 }, scroll = 252889, train = 280, sq = 2, r = { { 8170, 18 }, { 14341, 1 }, { 6261, 1 }, { 15407, 1 } }, out = { 252560, 1 }, oq = 2 },
    [1255019] = { name = "Blue Suede Bracers", t = { 1, 295, 305, 315 }, scroll = 252888, train = 275, sq = 2, r = { { 8170, 10 }, { 14341, 1 }, { 6260, 1 } }, out = { 252559, 1 }, oq = 2 },
    [1255020] = { name = "Tooled Leather Epaulets", t = { 1, 295, 305, 315 }, scroll = 252887, train = 275, sq = 2, r = { { 8170, 12 }, { 14341, 1 }, { 6261, 1 }, { 15407, 1 } }, out = { 252558, 1 }, oq = 2 },
    [1255021] = { name = "Blue Suede Belt", t = { 1, 290, 300, 310 }, scroll = 252886, train = 270, sq = 2, r = { { 8170, 14 }, { 14341, 1 }, { 6260, 2 } }, out = { 252481, 1 }, oq = 2 },
    [1255022] = { name = "Tooled Leather Bracers", t = { 1, 290, 300, 310 }, scroll = 252885, train = 270, sq = 2, r = { { 8170, 10 }, { 14341, 1 }, { 6261, 1 } }, out = { 252557, 1 }, oq = 2 },
    [1255023] = { name = "Wicked Leather Shoulders", t = { 1, 290, 300, 310 }, scroll = 252884, train = 270, sq = 2, r = { { 8170, 12 }, { 14341, 1 }, { 2325, 1 }, { 15407, 1 } }, out = { 252556, 1 }, oq = 2 },
    [1255024] = { name = "Blue Suede Armor", t = { 1, 285, 295, 305 }, scroll = 252883, train = 265, sq = 2, r = { { 8170, 14 }, { 15407, 2 }, { 14341, 2 }, { 6260, 4 }, { 15415, 6 } }, out = { 252480, 1 }, oq = 2 },
    [1255025] = { name = "Tooled Leather Crown", t = { 1, 285, 295, 305 }, scroll = 252882, train = 265, sq = 2, r = { { 8170, 14 }, { 14341, 1 }, { 6261, 1 } }, out = { 252555, 1 }, oq = 2 },
    [1255026] = { name = "Blue Suede Shoulders", t = { 1, 280, 290, 300 }, scroll = 252881, train = 260, sq = 2, r = { { 8170, 10 }, { 14341, 1 }, { 6260, 2 } }, out = { 252554, 1 }, oq = 2 },
    [1255027] = { name = "Tooled Leather Gauntlets", t = { 1, 280, 290, 300 }, scroll = 252880, train = 260, sq = 2, r = { { 8170, 10 }, { 14341, 1 }, { 6261, 1 } }, out = { 252553, 1 }, oq = 2 },
    [1255028] = { name = "Wicked Leather Boots", t = { 1, 280, 290, 300 }, scroll = 252879, train = 260, sq = 2, r = { { 8170, 10 }, { 14341, 1 }, { 2325, 1 } }, out = { 252479, 1 }, oq = 2 },
    [1255029] = { name = "Blue Suede Pants", t = { 1, 275, 285, 295 }, scroll = 252878, train = 255, sq = 2, r = { { 8170, 14 }, { 14341, 1 }, { 6260, 3 }, { 15407, 1 } }, out = { 252478, 1 }, oq = 2 },
    [1255030] = { name = "Tooled Leather Armor", t = { 1, 275, 285, 295 }, scroll = 252877, train = 255, scrollPrice = 100000, sq = 2, r = { { 8170, 16 }, { 14341, 1 }, { 6261, 3 }, { 15407, 2 }, { 13423, 6 } }, out = { 252552, 1 }, oq = 2 },
    [1255031] = { name = "Mender's Leather Waistguard", t = { 1, 270, 280, 290 }, scroll = 252876, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 8170, 12 }, { 8172, 4 }, { 249428, 10 }, { 8343, 2 }, { 5500, 8 }, { 249427, 5 } }, out = { 252477, 1 }, oq = 3, bop = true },
    [1255032] = { name = "Skycaller's Leather Waistguard", t = { 1, 270, 280, 290 }, scroll = 252875, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 8170, 12 }, { 8172, 4 }, { 249428, 10 }, { 8343, 2 }, { 7070, 8 }, { 249427, 5 } }, out = { 252476, 1 }, oq = 3, bop = true },
    [1255033] = { name = "Warden's Leather Waistguard", t = { 1, 270, 280, 290 }, scroll = 252874, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 8170, 12 }, { 8172, 4 }, { 249428, 10 }, { 8343, 2 }, { 7067, 8 }, { 249427, 5 } }, out = { 252475, 1 }, oq = 3, bop = true },
    [1255034] = { name = "Skulker's Leather Waistguard", t = { 1, 270, 280, 290 }, scroll = 252873, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 8170, 12 }, { 8172, 4 }, { 249428, 10 }, { 8343, 2 }, { 3182, 8 }, { 249427, 5 } }, out = { 252474, 1 }, oq = 3, bop = true },
    [1255035] = { name = "Prowler's Leather Waistguard", t = { 1, 270, 280, 290 }, scroll = 252872, train = 250, sq = 3, favor = 90, favorRep = 6, r = { { 8170, 12 }, { 8172, 4 }, { 249428, 10 }, { 8343, 2 }, { 1529, 8 }, { 249427, 5 } }, out = { 252473, 1 }, oq = 3, bop = true },
    [1255041] = { name = "Blue Suede Gloves", t = { 1, 260, 270, 280 }, scroll = 252866, train = 240, sq = 2, r = { { 8170, 8 }, { 14341, 1 }, { 6260, 1 } }, out = { 252546, 1 }, oq = 2 },
    [1255042] = { name = "Tooled Leather Boots", t = { 1, 260, 270, 280 }, scroll = 252865, train = 240, sq = 2, r = { { 8170, 8 }, { 14341, 1 }, { 6261, 1 } }, out = { 252545, 1 }, oq = 2 },
    [1255043] = { name = "Mender's Leather Boots", t = { 1, 255, 265, 275 }, scroll = 252864, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 16 }, { 8172, 2 }, { 249428, 8 }, { 8343, 2 }, { 5500, 6 }, { 249427, 4 } }, out = { 252472, 1 }, oq = 3, bop = true },
    [1255044] = { name = "Skycaller's Leather Boots", t = { 1, 255, 265, 275 }, scroll = 252863, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 16 }, { 8172, 2 }, { 249428, 8 }, { 8343, 2 }, { 7070, 6 }, { 249427, 4 } }, out = { 252471, 1 }, oq = 3, bop = true },
    [1255045] = { name = "Warden's Leather Boots", t = { 1, 255, 265, 275 }, scroll = 252862, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 16 }, { 8172, 2 }, { 249428, 8 }, { 8343, 2 }, { 7067, 6 }, { 249427, 4 } }, out = { 252470, 1 }, oq = 3, bop = true },
    [1255046] = { name = "Skulker's Leather Boots", t = { 1, 255, 265, 275 }, scroll = 252861, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 16 }, { 8172, 2 }, { 249428, 8 }, { 8343, 2 }, { 3182, 6 }, { 249427, 4 } }, out = { 252469, 1 }, oq = 3, bop = true },
    [1255047] = { name = "Prowler's Leather Boots", t = { 1, 255, 265, 275 }, scroll = 252860, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 16 }, { 8172, 2 }, { 249428, 8 }, { 8343, 2 }, { 1529, 6 }, { 249427, 4 } }, out = { 252468, 1 }, oq = 3, bop = true },
    [1255048] = { name = "Blue Suede Shoes", t = { 1, 255, 265, 275 }, scroll = 252859, train = 235, sq = 2, r = { { 8170, 8 }, { 14341, 1 }, { 6260, 1 } }, out = { 252467, 1 }, oq = 2 },
    [1255049] = { name = "Tooled Leather Belt", t = { 1, 255, 265, 275 }, scroll = 252858, train = 235, sq = 2, r = { { 8170, 8 }, { 14341, 1 }, { 6261, 1 } }, out = { 252544, 1 }, oq = 2 },
    [1255050] = { name = "Mender's Leather Bracers", t = { 1, 245, 255, 265 }, scroll = 252857, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 12 }, { 4236, 4 }, { 249428, 6 }, { 8343, 2 }, { 5500, 4 }, { 249427, 3 } }, out = { 252543, 1 }, oq = 3, bop = true },
    [1255051] = { name = "Skycaller's Leather Bracers", t = { 1, 245, 255, 265 }, scroll = 252856, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 12 }, { 4236, 4 }, { 249428, 6 }, { 8343, 2 }, { 7070, 4 }, { 249427, 3 } }, out = { 252542, 1 }, oq = 3, bop = true },
    [1255052] = { name = "Warden's Leather Bracers", t = { 1, 245, 255, 265 }, scroll = 252855, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 12 }, { 4236, 4 }, { 249428, 6 }, { 8343, 2 }, { 7067, 4 }, { 249427, 3 } }, out = { 252541, 1 }, oq = 3, bop = true },
    [1255053] = { name = "Skulker's Leather Bracers", t = { 1, 245, 255, 265 }, scroll = 252854, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 12 }, { 4236, 4 }, { 249428, 6 }, { 8343, 2 }, { 3182, 4 }, { 249427, 3 } }, out = { 252540, 1 }, oq = 3, bop = true },
    [1255054] = { name = "Prowler's Leather Bracers", t = { 1, 245, 255, 265 }, scroll = 252853, train = 225, sq = 3, favor = 90, favorRep = 6, r = { { 4304, 12 }, { 4236, 4 }, { 249428, 6 }, { 8343, 2 }, { 1529, 4 }, { 249427, 3 } }, out = { 252539, 1 }, oq = 3, bop = true },
    [1255055] = { name = "Mender's Leather Shoulders", t = { 1, 230, 240, 250 }, scroll = 252852, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 4304, 10 }, { 4236, 3 }, { 249428, 4 }, { 4291, 2 }, { 5500, 3 }, { 249427, 2 } }, out = { 252538, 1 }, oq = 3, bop = true },
    [1255056] = { name = "Skycaller's Leather Shoulders", t = { 1, 230, 240, 250 }, scroll = 252851, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 4304, 10 }, { 4236, 3 }, { 249428, 4 }, { 4291, 2 }, { 7070, 3 }, { 249427, 2 } }, out = { 252537, 1 }, oq = 3, bop = true },
    [1255057] = { name = "Warden's Leather Shoulders", t = { 1, 230, 240, 250 }, scroll = 252850, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 4304, 10 }, { 4236, 3 }, { 249428, 4 }, { 4291, 2 }, { 7067, 3 }, { 249427, 2 } }, out = { 252536, 1 }, oq = 3, bop = true },
    [1255058] = { name = "Skulker's Leather Shoulders", t = { 1, 230, 240, 250 }, scroll = 252849, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 4304, 10 }, { 4236, 3 }, { 249428, 4 }, { 4291, 2 }, { 3182, 3 }, { 249427, 2 } }, out = { 252535, 1 }, oq = 3, bop = true },
    [1255059] = { name = "Prowler's Leather Shoulders", t = { 1, 230, 240, 250 }, scroll = 252848, train = 210, sq = 3, favor = 60, favorRep = 5, r = { { 4304, 10 }, { 4236, 3 }, { 249428, 4 }, { 4291, 2 }, { 1529, 3 }, { 249427, 2 } }, out = { 252534, 1 }, oq = 3, bop = true },
    [1255065] = { name = "Mender's Leather Gloves", t = { 1, 195, 205, 215 }, scroll = 252842, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 4234, 16 }, { 4236, 2 }, { 249428, 2 }, { 4291, 2 }, { 5500, 2 }, { 249427, 1 } }, out = { 252530, 1 }, oq = 3, bop = true },
    [1255066] = { name = "Skycaller's Leather Gloves", t = { 1, 195, 205, 215 }, scroll = 252841, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 4234, 16 }, { 4236, 2 }, { 249428, 2 }, { 4291, 2 }, { 7070, 2 }, { 249427, 1 } }, out = { 252529, 1 }, oq = 3, bop = true },
    [1255067] = { name = "Skirmisher's Leather Gloves", t = { 1, 195, 205, 215 }, scroll = 252840, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 4234, 16 }, { 4236, 2 }, { 249428, 2 }, { 4291, 2 }, { 3864, 2 }, { 249427, 1 } }, out = { 252528, 1 }, oq = 3, bop = true },
    [1255068] = { name = "Warden's Leather Gloves", t = { 1, 195, 205, 215 }, scroll = 252839, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 4234, 16 }, { 4236, 2 }, { 249428, 2 }, { 4291, 2 }, { 7067, 2 }, { 249427, 1 } }, out = { 252527, 1 }, oq = 3, bop = true },
    [1255069] = { name = "Stalker's Leather Gloves", t = { 1, 195, 205, 215 }, scroll = 252838, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 4234, 16 }, { 4236, 2 }, { 249428, 2 }, { 4291, 2 }, { 7069, 2 }, { 249427, 1 } }, out = { 252526, 1 }, oq = 3, bop = true },
    [1255070] = { name = "Skulker's Leather Gloves", t = { 1, 195, 205, 215 }, scroll = 252837, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 4234, 16 }, { 4236, 2 }, { 249428, 2 }, { 4291, 2 }, { 3182, 2 }, { 249427, 1 } }, out = { 252525, 1 }, oq = 3, bop = true },
    [1255071] = { name = "Prowler's Leather Gloves", t = { 1, 195, 205, 215 }, scroll = 252836, train = 175, sq = 3, favor = 60, favorRep = 5, r = { { 4234, 16 }, { 4236, 2 }, { 249428, 2 }, { 4291, 2 }, { 1529, 2 }, { 249427, 1 } }, out = { 252524, 1 }, oq = 3, bop = true },
    [1255073] = { name = "Forceful Thick Armor Kit", t = { 1, 205, 215, 225 }, scroll = 252834, train = 185, sq = 2, favor = 60, favorRep = 5, r = { { 8173, 1 }, { 11137, 2 }, { 3391, 2 } }, out = { 252463, 1 }, oq = 2 },
    [1255074] = { name = "Mystic Thick Armor Kit", t = { 1, 205, 215, 225 }, scroll = 252833, train = 185, scrollPrice = 3500, sq = 2, r = { { 8173, 1 }, { 11137, 2 }, { 3827, 2 } }, out = { 252462, 1 }, oq = 2 },
    [1255082] = { name = "Wisdom's Leather Leggings", t = { 1, 150, 160, 170 }, scroll = 252825, train = 125, sq = 3, favor = 30, r = { { 2319, 12 }, { 4233, 4 }, { 249427, 8 }, { 2321, 3 }, { 5498, 8 } }, out = { 252519, 1 }, oq = 3, bop = true },
    [1255083] = { name = "Stormrider's Leather Kilt", t = { 1, 150, 160, 170 }, scroll = 252824, train = 125, sq = 3, favor = 30, r = { { 2319, 12 }, { 4233, 4 }, { 249427, 8 }, { 2321, 3 }, { 249409, 8 } }, out = { 252518, 1 }, oq = 3, bop = true },
    [1255084] = { name = "Totemic Leather Leggings", t = { 1, 150, 160, 170 }, scroll = 252823, train = 125, sq = 3, favor = 30, r = { { 2319, 12 }, { 4233, 4 }, { 249427, 8 }, { 2321, 3 }, { 249410, 8 } }, out = { 252458, 1 }, oq = 3, bop = true },
    [1255085] = { name = "Defender's Leather Kilt", t = { 1, 150, 160, 170 }, scroll = 252822, train = 125, sq = 3, favor = 30, r = { { 2319, 12 }, { 4233, 4 }, { 249427, 8 }, { 2321, 3 }, { 2458, 8 } }, out = { 252457, 1 }, oq = 3, bop = true },
    [1255086] = { name = "Trapper's Leather Legguards", t = { 1, 150, 160, 170 }, scroll = 252821, train = 125, sq = 3, favor = 30, r = { { 2319, 12 }, { 4233, 4 }, { 249427, 8 }, { 2321, 3 }, { 6470, 8 } }, out = { 252517, 1 }, oq = 3, bop = true },
    [1255087] = { name = "Brawler's Leather Legguards", t = { 1, 150, 160, 170 }, scroll = 252820, train = 125, sq = 3, favor = 30, r = { { 2319, 12 }, { 4233, 4 }, { 249427, 8 }, { 2321, 3 }, { 1210, 8 } }, out = { 252516, 1 }, oq = 3, bop = true },
    [1255095] = { name = "Forceful Heavy Armor Kit", t = { 1, 155, 165, 175 }, scroll = 252812, train = 135, scrollPrice = 2000, sq = 2, r = { { 4265, 1 }, { 11083, 2 }, { 6662, 2 } }, out = { 252453, 1 }, oq = 2 },
    [1255096] = { name = "Mystic Heavy Armor Kit", t = { 1, 155, 165, 175 }, scroll = 252811, train = 135, scrollPrice = 2000, sq = 2, r = { { 4265, 1 }, { 11083, 2 }, { 3385, 2 } }, out = { 252452, 1 }, oq = 2 },
    [1255097] = { name = "Wisdom's Leather Tunic", t = { 1, 135, 147, 160 }, scroll = 252810, train = 110, sq = 3, favor = 30, r = { { 2319, 10 }, { 4233, 3 }, { 249427, 6 }, { 2321, 3 }, { 5498, 6 } }, out = { 252511, 1 }, oq = 3, bop = true },
    [1255098] = { name = "Stormrider's Leather Tunic", t = { 1, 135, 147, 160 }, scroll = 252809, train = 110, sq = 3, favor = 30, r = { { 2319, 10 }, { 4233, 3 }, { 249427, 6 }, { 2321, 3 }, { 249409, 6 } }, out = { 252510, 1 }, oq = 3, bop = true },
    [1255099] = { name = "Totemic Leather Tunic", t = { 1, 135, 147, 160 }, scroll = 252808, train = 110, sq = 3, favor = 30, r = { { 2319, 10 }, { 4233, 3 }, { 249427, 6 }, { 2321, 3 }, { 249410, 6 } }, out = { 252451, 1 }, oq = 3, bop = true },
    [1255100] = { name = "Defender's Leather Tunic", t = { 1, 135, 147, 160 }, scroll = 252807, train = 110, sq = 3, favor = 30, r = { { 2319, 10 }, { 4233, 3 }, { 249427, 6 }, { 2321, 3 }, { 2458, 6 } }, out = { 252450, 1 }, oq = 3, bop = true },
    [1255101] = { name = "Trapper's Leather Tunic", t = { 1, 135, 147, 160 }, scroll = 252806, train = 110, sq = 3, favor = 30, r = { { 2319, 10 }, { 4233, 3 }, { 249427, 6 }, { 2321, 3 }, { 6470, 6 } }, out = { 252509, 1 }, oq = 3, bop = true },
    [1255102] = { name = "Brawler's Leather Tunic", t = { 1, 135, 147, 160 }, scroll = 252805, train = 110, sq = 3, favor = 30, r = { { 2319, 10 }, { 4233, 3 }, { 249427, 6 }, { 2321, 3 }, { 1210, 6 } }, out = { 252508, 1 }, oq = 3, bop = true },
    [1255103] = { name = "Hillman's Leather Boots", t = { 1, 135, 147, 160 }, scroll = 252804, train = 110, sq = 2, r = { { 4233, 1 }, { 2319, 6 }, { 2321, 1 } }, out = { 252449, 1 }, oq = 2 },
    [1255104] = { name = "Wisdom's Leather Hood", t = { 1, 125, 137, 150 }, scroll = 252803, train = 100, sq = 3, favor = 30, r = { { 2319, 8 }, { 4233, 2 }, { 249427, 4 }, { 2321, 2 }, { 5498, 4 } }, out = { 252507, 1 }, oq = 3, bop = true },
    [1255105] = { name = "Stormrider's Leather Hood", t = { 1, 125, 137, 150 }, scroll = 252802, train = 100, sq = 3, favor = 30, r = { { 2319, 8 }, { 4233, 2 }, { 249427, 4 }, { 2321, 2 }, { 249409, 4 } }, out = { 252506, 1 }, oq = 3, bop = true },
    [1255106] = { name = "Totemic Leather Hood", t = { 1, 125, 137, 150 }, scroll = 252801, train = 100, sq = 3, favor = 30, r = { { 2319, 8 }, { 4233, 2 }, { 249427, 4 }, { 2321, 2 }, { 249410, 4 } }, out = { 252448, 1 }, oq = 3, bop = true },
    [1255107] = { name = "Defender's Leather Hood", t = { 1, 125, 137, 150 }, scroll = 252800, train = 100, sq = 3, favor = 30, r = { { 2319, 8 }, { 4233, 2 }, { 249427, 4 }, { 2321, 2 }, { 2458, 4 } }, out = { 252447, 1 }, oq = 3, bop = true },
    [1255108] = { name = "Trapper's Leather Hood", t = { 1, 125, 137, 150 }, scroll = 252799, train = 100, sq = 3, favor = 30, r = { { 2319, 8 }, { 4233, 2 }, { 249427, 4 }, { 2321, 2 }, { 6470, 4 } }, out = { 252505, 1 }, oq = 3, bop = true },
    [1255109] = { name = "Brawler's Leather Hood", t = { 1, 125, 137, 150 }, scroll = 252798, train = 100, sq = 3, favor = 30, r = { { 2319, 8 }, { 4233, 2 }, { 249427, 4 }, { 2321, 2 }, { 1210, 4 } }, out = { 252504, 1 }, oq = 3, bop = true },
    [1255116] = { name = "Wisdom's Leather Boots", t = { 1, 110, 122, 135 }, scroll = 252791, train = 85, sq = 3, favor = 30, r = { { 2318, 14 }, { 4231, 4 }, { 249427, 3 }, { 2321, 1 }, { 5498, 3 } }, out = { 252444, 1 }, oq = 3, bop = true },
    [1255117] = { name = "Stormrider's Leather Boots", t = { 1, 110, 122, 135 }, scroll = 252790, train = 85, sq = 3, favor = 30, r = { { 2318, 14 }, { 4231, 4 }, { 249427, 3 }, { 2321, 1 }, { 249409, 3 } }, out = { 252443, 1 }, oq = 3, bop = true },
    [1255118] = { name = "Totemic Leather Boots", t = { 1, 110, 122, 135 }, scroll = 252789, train = 85, sq = 3, favor = 30, r = { { 2318, 14 }, { 4231, 4 }, { 249427, 3 }, { 2321, 1 }, { 249410, 3 } }, out = { 252442, 1 }, oq = 3, bop = true },
    [1255119] = { name = "Defender's Leather Boots", t = { 1, 110, 122, 135 }, scroll = 252788, train = 85, sq = 3, favor = 30, r = { { 2318, 14 }, { 4231, 4 }, { 249427, 3 }, { 2321, 1 }, { 2458, 3 } }, out = { 252441, 1 }, oq = 3, bop = true },
    [1255120] = { name = "Trapper's Leather Boots", t = { 1, 110, 122, 135 }, scroll = 252787, train = 85, sq = 3, favor = 30, r = { { 2318, 14 }, { 4231, 4 }, { 249427, 3 }, { 2321, 1 }, { 6470, 3 } }, out = { 252440, 1 }, oq = 3, bop = true },
    [1255121] = { name = "Brawler's Leather Boots", t = { 1, 110, 122, 135 }, scroll = 252786, train = 85, sq = 3, favor = 30, r = { { 2318, 14 }, { 4231, 4 }, { 249427, 3 }, { 2321, 1 }, { 1210, 3 } }, out = { 252439, 1 }, oq = 3, bop = true },
    [1255123] = { name = "Forceful Medium Armor Kit", t = { 1, 95, 102, 110 }, scroll = 252784, train = 80, scrollPrice = 500, sq = 2, r = { { 2313, 1 }, { 10940, 2 }, { 2454, 2 } }, out = { 252437, 1 }, oq = 2 },
    [1255124] = { name = "Mystic Medium Armor Kit", t = { 1, 95, 102, 110 }, scroll = 252783, train = 80, scrollPrice = 500, sq = 2, r = { { 2313, 1 }, { 10940, 2 }, { 2455, 2 } }, out = { 252436, 1 }, oq = 2 },
    [1255125] = { name = "Wisdom's Leather Gloves", t = { 1, 100, 112, 125 }, scroll = 252782, train = 75, sq = 3, favor = 30, r = { { 2318, 12 }, { 4231, 3 }, { 249427, 2 }, { 2321, 1 }, { 5498, 2 } }, out = { 252499, 1 }, oq = 3, bop = true },
    [1255126] = { name = "Stormrider's Leather Gloves", t = { 1, 100, 112, 125 }, scroll = 252781, train = 75, sq = 3, favor = 30, r = { { 2318, 12 }, { 4231, 3 }, { 249427, 2 }, { 2321, 1 }, { 249409, 2 } }, out = { 252498, 1 }, oq = 3, bop = true },
    [1255127] = { name = "Totemic Leather Gloves", t = { 1, 100, 112, 125 }, scroll = 252780, train = 75, sq = 3, favor = 30, r = { { 2318, 12 }, { 4231, 3 }, { 249427, 2 }, { 2321, 1 }, { 249410, 2 } }, out = { 252497, 1 }, oq = 3, bop = true },
    [1255128] = { name = "Defender's Leather Gloves", t = { 1, 100, 112, 125 }, scroll = 252779, train = 75, sq = 3, favor = 30, r = { { 2318, 12 }, { 4231, 3 }, { 249427, 2 }, { 2321, 1 }, { 2458, 2 } }, out = { 252496, 1 }, oq = 3, bop = true },
    [1255129] = { name = "Trapper's Leather Gloves", t = { 1, 100, 112, 125 }, scroll = 252778, train = 75, sq = 3, favor = 30, r = { { 2318, 12 }, { 4231, 3 }, { 249427, 2 }, { 2321, 1 }, { 6470, 2 } }, out = { 252495, 1 }, oq = 3, bop = true },
    [1255130] = { name = "Brawler's Leather Gloves", t = { 1, 100, 112, 125 }, scroll = 252777, train = 75, sq = 3, favor = 30, r = { { 2318, 12 }, { 4231, 3 }, { 249427, 2 }, { 2321, 1 }, { 1210, 2 } }, out = { 252494, 1 }, oq = 3, bop = true },
    [1255137] = { name = "Wisdom's Leather Belt", t = { 1, 90, 105, 120 }, scroll = 252770, train = 60, sq = 3, favor = 30, r = { { 2318, 10 }, { 4231, 2 }, { 249427, 2 }, { 2320, 1 }, { 5498, 1 } }, out = { 252433, 1 }, oq = 3, bop = true },
    [1255138] = { name = "Stormrider's Leather Belt", t = { 1, 90, 105, 120 }, scroll = 252769, train = 60, sq = 3, favor = 30, r = { { 2318, 10 }, { 4231, 2 }, { 249427, 2 }, { 2320, 1 }, { 249409, 1 } }, out = { 252432, 1 }, oq = 3, bop = true },
    [1255139] = { name = "Totemic Leather Belt", t = { 1, 90, 105, 120 }, scroll = 252768, train = 60, sq = 3, favor = 30, r = { { 2318, 10 }, { 4231, 2 }, { 249427, 2 }, { 2320, 1 }, { 249410, 1 } }, out = { 252431, 1 }, oq = 3, bop = true },
    [1255140] = { name = "Defender's Leather Belt", t = { 1, 90, 105, 120 }, scroll = 252767, train = 60, sq = 3, favor = 30, r = { { 2318, 10 }, { 4231, 2 }, { 249427, 2 }, { 2320, 1 }, { 2458, 1 } }, out = { 252430, 1 }, oq = 3, bop = true },
    [1255141] = { name = "Trapper's Leather Belt", t = { 1, 90, 105, 120 }, scroll = 252766, train = 60, sq = 3, favor = 30, r = { { 2318, 10 }, { 4231, 2 }, { 249427, 2 }, { 2320, 1 }, { 6470, 1 } }, out = { 252429, 1 }, oq = 3, bop = true },
    [1255142] = { name = "Brawler's Leather Belt", t = { 1, 90, 105, 120 }, scroll = 252765, train = 60, sq = 3, favor = 30, r = { { 2318, 10 }, { 4231, 2 }, { 249427, 2 }, { 2320, 1 }, { 1210, 1 } }, out = { 252428, 1 }, oq = 3, bop = true },
    [1263031] = { name = "Tanning Rack", t = { 1, 125, 125, 125 }, scroll = 273096, train = 125, sq = 2, r = { { 2319, 5 }, { 2321, 3 }, { 4470, 2 } }, out = { 279941, 1 }, oq = 1 },
    [1292920] = { name = "Grovekeeper Trousers", t = { 1, 320, 325, 330 }, scroll = 273952, train = 300, sq = 4, r = { { 274030, 5 }, { 15407, 4 }, { 248825, 24 }, { 14341, 8 } }, out = { 273884, 1 }, oq = 1 },
    [1292921] = { name = "Grovekeeper Grips", t = { 1, 320, 325, 330 }, scroll = 273953, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273885, 1 }, oq = 1 },
    [1292923] = { name = "Grovekeeper Shoulderpads", t = { 1, 320, 325, 330 }, scroll = 273954, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273886, 1 }, oq = 1 },
    [1292924] = { name = "Grovekeeper Stompers", t = { 1, 320, 325, 330 }, scroll = 273955, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273887, 1 }, oq = 1 },
    [1292925] = { name = "Grovekeeper Kilt", t = { 1, 320, 325, 330 }, scroll = 273956, train = 300, sq = 4, r = { { 274030, 5 }, { 15407, 4 }, { 248825, 24 }, { 14341, 8 } }, out = { 273888, 1 }, oq = 1 },
    [1292926] = { name = "Grovekeeper Mitts", t = { 1, 320, 325, 330 }, scroll = 273957, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273889, 1 }, oq = 1 },
    [1292927] = { name = "Grovekeeper Mantle", t = { 1, 320, 325, 330 }, scroll = 273958, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273890, 1 }, oq = 1 },
    [1292928] = { name = "Grovekeeper Sandals", t = { 1, 320, 325, 330 }, scroll = 273959, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273891, 1 }, oq = 1 },
    [1292929] = { name = "Grovekeeper Legguards", t = { 1, 320, 325, 330 }, scroll = 273960, train = 300, sq = 4, r = { { 274030, 5 }, { 15407, 4 }, { 248825, 24 }, { 14341, 8 } }, out = { 273892, 1 }, oq = 1 },
    [1292930] = { name = "Grovekeeper Handguards", t = { 1, 320, 325, 330 }, scroll = 273961, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273893, 1 }, oq = 1 },
    [1292931] = { name = "Grovekeeper Pauldrons", t = { 1, 320, 325, 330 }, scroll = 273962, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273894, 1 }, oq = 1 },
    [1292932] = { name = "Grovekeeper Boots", t = { 1, 320, 325, 330 }, scroll = 273963, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273895, 1 }, oq = 1 },
    [1292933] = { name = "Grovekeeper Leggings", t = { 1, 320, 325, 330 }, scroll = 273964, train = 300, sq = 4, r = { { 274030, 5 }, { 15407, 4 }, { 248825, 24 }, { 14341, 8 } }, out = { 273896, 1 }, oq = 1 },
    [1292934] = { name = "Grovekeeper Gauntlets", t = { 1, 320, 325, 330 }, scroll = 273965, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273897, 1 }, oq = 1 },
    [1292935] = { name = "Grovekeeper Spaulders", t = { 1, 320, 325, 330 }, scroll = 273966, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273898, 1 }, oq = 1 },
    [1292936] = { name = "Grovekeeper Treads", t = { 1, 320, 325, 330 }, scroll = 273967, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273899, 1 }, oq = 1 },
    [1292937] = { name = "Wildstalker's Legguards", t = { 1, 320, 325, 330 }, scroll = 273968, train = 300, sq = 4, r = { { 274030, 5 }, { 15407, 4 }, { 248825, 24 }, { 14341, 8 } }, out = { 273900, 1 }, oq = 1 },
    [1292938] = { name = "Wildstalker's Gauntlets", t = { 1, 320, 325, 330 }, scroll = 273969, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273901, 1 }, oq = 1 },
    [1292939] = { name = "Wildstalker's Spaulders", t = { 1, 320, 325, 330 }, scroll = 273970, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273902, 1 }, oq = 1 },
    [1292940] = { name = "Wildstalker's Greaves", t = { 1, 320, 325, 330 }, scroll = 273971, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273903, 1 }, oq = 1 },
    [1292965] = { name = "Grimstitch Pants", t = { 1, 320, 325, 330 }, scroll = 273996, train = 300, sq = 4, r = { { 274030, 5 }, { 15407, 4 }, { 248825, 24 }, { 14341, 8 } }, out = { 273928, 1 }, oq = 1 },
    [1292966] = { name = "Grimstitch Gloves", t = { 1, 320, 325, 330 }, scroll = 273997, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273929, 1 }, oq = 1 },
    [1292967] = { name = "Grimstitch Spaulders", t = { 1, 320, 325, 330 }, scroll = 273998, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273930, 1 }, oq = 1 },
    [1292968] = { name = "Grimstitch Boots", t = { 1, 320, 325, 330 }, scroll = 273999, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273931, 1 }, oq = 1 },
    [1292969] = { name = "Spiritcaller Leggings", t = { 1, 320, 325, 330 }, scroll = 274000, train = 300, sq = 4, r = { { 274030, 5 }, { 15407, 4 }, { 248825, 24 }, { 14341, 8 } }, out = { 273932, 1 }, oq = 1 },
    [1292970] = { name = "Spiritcaller Grips", t = { 1, 320, 325, 330 }, scroll = 274001, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273933, 1 }, oq = 1 },
    [1292971] = { name = "Spiritcaller Spaulders", t = { 1, 320, 325, 330 }, scroll = 274002, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273934, 1 }, oq = 1 },
    [1292972] = { name = "Spiritcaller Treads", t = { 1, 320, 325, 330 }, scroll = 274003, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273935, 1 }, oq = 1 },
    [1292973] = { name = "Spiritcaller Pants", t = { 1, 320, 325, 330 }, scroll = 274004, train = 300, sq = 4, r = { { 274030, 5 }, { 15407, 4 }, { 248825, 24 }, { 14341, 8 } }, out = { 273936, 1 }, oq = 1 },
    [1292974] = { name = "Spiritcaller Gauntlets", t = { 1, 320, 325, 330 }, scroll = 274005, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273937, 1 }, oq = 1 },
    [1292975] = { name = "Spiritcaller Epaulets", t = { 1, 320, 325, 330 }, scroll = 274006, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273938, 1 }, oq = 1 },
    [1292976] = { name = "Spiritcaller Greaves", t = { 1, 320, 325, 330 }, scroll = 274007, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 273939, 1 }, oq = 1 },
    [1297126] = { name = "Bileblister Claws", t = { 1, 290, 292, 295 }, scroll = 275586, train = 285, rep = { 609, 4 }, sq = 3, r = { { 8170, 12 }, { 12810, 3 }, { 7082, 3 }, { 14341, 6 } }, out = { 275610, 1 }, oq = 3 },
    [1297127] = { name = "Bileblister Girdle", t = { 1, 295, 297, 300 }, scroll = 275587, train = 290, rep = { 609, 5 }, sq = 3, r = { { 8170, 18 }, { 12810, 3 }, { 7082, 3 }, { 14341, 6 } }, out = { 275611, 1 }, oq = 3 },
    [1297128] = { name = "Bileblister Boots", t = { 1, 295, 297, 300 }, scroll = 275588, train = 295, rep = { 609, 5 }, sq = 3, r = { { 8170, 15 }, { 12810, 3 }, { 7082, 3 }, { 14341, 6 } }, out = { 275612, 1 }, oq = 3 },
    [1297129] = { name = "Hivethrasher's Claws", t = { 1, 290, 292, 295 }, scroll = 275589, train = 285, rep = { 609, 4 }, sq = 3, r = { { 8170, 12 }, { 12810, 3 }, { 7076, 3 }, { 14341, 6 } }, out = { 275613, 1 }, oq = 3 },
    [1297130] = { name = "Hivethrasher's Girdle", t = { 1, 295, 297, 300 }, scroll = 275590, train = 290, rep = { 609, 5 }, sq = 3, r = { { 8170, 18 }, { 12810, 3 }, { 7076, 3 }, { 14341, 6 } }, out = { 275614, 1 }, oq = 3 },
    [1297131] = { name = "Hivethrasher's Boots", t = { 1, 295, 297, 300 }, scroll = 275591, train = 295, rep = { 609, 5 }, sq = 3, r = { { 8170, 15 }, { 12810, 3 }, { 7076, 3 }, { 14341, 6 } }, out = { 275615, 1 }, oq = 3 },
    [1297132] = { name = "Scalegut Clenchers", t = { 1, 290, 292, 295 }, scroll = 275592, train = 285, rep = { 609, 4 }, sq = 3, r = { { 15408, 5 }, { 12810, 3 }, { 7078, 3 }, { 14341, 6 } }, out = { 275616, 1 }, oq = 3 },
    [1297133] = { name = "Scalegut Belt", t = { 1, 295, 297, 300 }, scroll = 275593, train = 290, rep = { 609, 5 }, sq = 3, r = { { 15408, 7 }, { 12810, 3 }, { 7078, 3 }, { 14341, 6 } }, out = { 275617, 1 }, oq = 3 },
    [1297134] = { name = "Scalegut Treaders", t = { 1, 295, 297, 300 }, scroll = 275594, train = 295, rep = { 609, 5 }, sq = 3, r = { { 15408, 6 }, { 12810, 3 }, { 7078, 3 }, { 14341, 6 } }, out = { 275618, 1 }, oq = 3 },
    [1297135] = { name = "Broodwatcher's Clenchers", t = { 1, 290, 292, 295 }, scroll = 275595, train = 285, rep = { 609, 4 }, sq = 3, r = { { 15408, 5 }, { 12810, 3 }, { 7080, 3 }, { 14341, 6 } }, out = { 275619, 1 }, oq = 3 },
    [1297136] = { name = "Broodwatcher's Belt", t = { 1, 295, 297, 300 }, scroll = 275596, train = 290, rep = { 609, 5 }, sq = 3, r = { { 15408, 7 }, { 12810, 3 }, { 7080, 3 }, { 14341, 6 } }, out = { 275620, 1 }, oq = 3 },
    [1297137] = { name = "Broodwatcher's Treaders", t = { 1, 295, 297, 300 }, scroll = 275597, train = 295, rep = { 609, 5 }, sq = 3, r = { { 15408, 6 }, { 12810, 3 }, { 7080, 3 }, { 14341, 6 } }, out = { 275621, 1 }, oq = 3 },
    [1299914] = { name = "Spiritcaller Kilt", t = { 1, 320, 325, 330 }, scroll = 276542, train = 300, sq = 4, r = { { 274030, 5 }, { 15407, 4 }, { 248825, 24 }, { 14341, 8 } }, out = { 276538, 1 }, oq = 4 },
    [1299915] = { name = "Spiritcaller Gloves", t = { 1, 320, 325, 330 }, scroll = 276543, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 276539, 1 }, oq = 4 },
    [1299916] = { name = "Spiritcaller Mantle", t = { 1, 320, 325, 330 }, scroll = 276544, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 276540, 1 }, oq = 4 },
    [1299917] = { name = "Spiritcaller Boots", t = { 1, 320, 325, 330 }, scroll = 276545, train = 300, sq = 4, r = { { 274030, 3 }, { 15407, 2 }, { 248825, 18 }, { 14341, 8 } }, out = { 276541, 1 }, oq = 4 },
    [1301427] = { name = "Cloudy Gustwoven Harness", t = { 1, 65, 67, 70 }, scroll = 276934, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2318, 7 }, { 4231, 1 }, { 2320, 2 } }, out = { 276998, 1 }, oq = 2 },
    [1301428] = { name = "Cloudy Gustwoven Bracers", t = { 1, 55, 57, 60 }, scroll = 276935, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2318, 4 }, { 2320, 3 } }, out = { 276999, 1 }, oq = 2 },
    [1301429] = { name = "Cloudy Gustwoven Gloves", t = { 1, 60, 62, 65 }, scroll = 276936, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2318, 6 }, { 2320, 4 } }, out = { 277000, 1 }, oq = 2 },
    [1301430] = { name = "Cloudy Gustwoven Belt", t = { 1, 55, 57, 60 }, scroll = 276937, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2318, 5 }, { 2320, 3 } }, out = { 277001, 1 }, oq = 2 },
    [1301431] = { name = "Cloudy Gustwoven Trousers", t = { 1, 65, 67, 70 }, scroll = 276938, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2318, 7 }, { 2320, 2 } }, out = { 277002, 1 }, oq = 2 },
    [1301432] = { name = "Cloudy Gustwoven Boots", t = { 1, 60, 62, 65 }, scroll = 276939, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2318, 6 }, { 2320, 3 } }, out = { 277003, 1 }, oq = 2 },
    [1301433] = { name = "Cloudy Windraveled Jerkin", t = { 1, 65, 67, 70 }, scroll = 276940, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2318, 7 }, { 4231, 1 }, { 2320, 2 } }, out = { 277004, 1 }, oq = 2 },
    [1301434] = { name = "Cloudy Windraveled Armguards", t = { 1, 55, 57, 60 }, scroll = 276941, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2318, 4 }, { 2320, 3 } }, out = { 277005, 1 }, oq = 2 },
    [1301435] = { name = "Cloudy Windraveled Mitts", t = { 1, 60, 62, 65 }, scroll = 276942, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2318, 6 }, { 2320, 4 } }, out = { 277006, 1 }, oq = 2 },
    [1301436] = { name = "Cloudy Windraveled Strap", t = { 1, 55, 57, 60 }, scroll = 276943, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2318, 5 }, { 2320, 3 } }, out = { 277007, 1 }, oq = 2 },
    [1301437] = { name = "Cloudy Windraveled Pants", t = { 1, 65, 67, 70 }, scroll = 276944, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2318, 7 }, { 2320, 2 } }, out = { 277008, 1 }, oq = 2 },
    [1301438] = { name = "Cloudy Windraveled Footwraps", t = { 1, 60, 62, 65 }, scroll = 276945, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2318, 6 }, { 2320, 3 } }, out = { 277009, 1 }, oq = 2 },
    [1301451] = { name = "Azure Gustwoven Harness", t = { 1, 65, 67, 70 }, scroll = 276958, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2318, 7 }, { 4231, 1 }, { 2320, 2 } }, out = { 277022, 1 }, oq = 2 },
    [1301452] = { name = "Azure Gustwoven Bracers", t = { 1, 55, 57, 60 }, scroll = 276959, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2318, 4 }, { 2320, 3 } }, out = { 277023, 1 }, oq = 2 },
    [1301453] = { name = "Azure Gustwoven Gloves", t = { 1, 60, 62, 65 }, scroll = 276960, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2318, 6 }, { 2320, 4 } }, out = { 277024, 1 }, oq = 2 },
    [1301454] = { name = "Azure Gustwoven Belt", t = { 1, 55, 57, 60 }, scroll = 276961, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2318, 5 }, { 2320, 3 } }, out = { 277025, 1 }, oq = 2 },
    [1301455] = { name = "Azure Gustwoven Trousers", t = { 1, 65, 67, 70 }, scroll = 276962, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2318, 7 }, { 2320, 2 } }, out = { 277026, 1 }, oq = 2 },
    [1301456] = { name = "Azure Gustwoven Boots", t = { 1, 60, 62, 65 }, scroll = 276963, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2318, 6 }, { 2320, 3 } }, out = { 277027, 1 }, oq = 2 },
    [1301457] = { name = "Azure Windraveled Jerkin", t = { 1, 65, 67, 70 }, scroll = 276964, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2318, 7 }, { 4231, 1 }, { 2320, 2 } }, out = { 277028, 1 }, oq = 2 },
    [1301458] = { name = "Azure Windraveled Armguards", t = { 1, 55, 57, 60 }, scroll = 276965, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2318, 4 }, { 2320, 3 } }, out = { 277029, 1 }, oq = 2 },
    [1301459] = { name = "Azure Windraveled Mitts", t = { 1, 60, 62, 65 }, scroll = 276966, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2318, 6 }, { 2320, 4 } }, out = { 277030, 1 }, oq = 2 },
    [1301460] = { name = "Azure Windraveled Strap", t = { 1, 55, 57, 60 }, scroll = 276967, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2318, 5 }, { 2320, 3 } }, out = { 277031, 1 }, oq = 2 },
    [1301461] = { name = "Azure Windraveled Pants", t = { 1, 65, 67, 70 }, scroll = 276968, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2318, 7 }, { 2320, 2 } }, out = { 277032, 1 }, oq = 2 },
    [1301462] = { name = "Azure Windraveled Footwraps", t = { 1, 60, 62, 65 }, scroll = 276969, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2318, 6 }, { 2320, 3 } }, out = { 277033, 1 }, oq = 2 },
    [1301528] = { name = "Cloudy Gustwoven Hood", t = { 1, 185, 187, 190 }, scroll = 276978, train = 175, scrollPrice = 100000, rep = { 2787, 4 }, sq = 2, r = { { 4234, 15 }, { 4236, 3 }, { 8343, 1 }, { 2324, 8 } }, out = { 277042, 1 }, oq = 2 },
    [1301529] = { name = "Cloudy Gustwoven Spaulders", t = { 1, 185, 187, 190 }, scroll = 276979, train = 175, scrollPrice = 100000, rep = { 2787, 4 }, sq = 2, r = { { 4234, 12 }, { 4236, 2 }, { 8343, 1 }, { 2324, 6 } }, out = { 277043, 1 }, oq = 2 },
    [1301530] = { name = "Cloudy Windraveled Cover", t = { 1, 185, 187, 190 }, scroll = 276980, train = 175, scrollPrice = 100000, rep = { 2787, 4 }, sq = 2, r = { { 4234, 15 }, { 4236, 3 }, { 8343, 1 }, { 2324, 8 } }, out = { 277044, 1 }, oq = 2 },
    [1301531] = { name = "Cloudy Windraveled Drapes", t = { 1, 185, 187, 190 }, scroll = 276981, train = 175, scrollPrice = 100000, rep = { 2787, 4 }, sq = 2, r = { { 4234, 12 }, { 4236, 2 }, { 8343, 1 }, { 2324, 6 } }, out = { 277045, 1 }, oq = 2 },
    [1301536] = { name = "Azure Gustwoven Hood", t = { 1, 185, 187, 190 }, scroll = 276986, train = 175, scrollPrice = 100000, rep = { 2740, 4 }, sq = 2, r = { { 4234, 15 }, { 4236, 3 }, { 8343, 1 }, { 6260, 4 } }, out = { 277050, 1 }, oq = 2 },
    [1301537] = { name = "Azure Gustwoven Spaulders", t = { 1, 185, 187, 190 }, scroll = 276987, train = 175, scrollPrice = 100000, rep = { 2740, 4 }, sq = 2, r = { { 4234, 12 }, { 4236, 2 }, { 8343, 1 }, { 6260, 3 } }, out = { 277051, 1 }, oq = 2 },
    [1301538] = { name = "Azure Windraveled Cover", t = { 1, 185, 187, 190 }, scroll = 276988, train = 175, scrollPrice = 100000, rep = { 2740, 4 }, sq = 2, r = { { 4234, 15 }, { 4236, 3 }, { 8343, 1 }, { 6260, 4 } }, out = { 277052, 1 }, oq = 2 },
    [1301539] = { name = "Azure Windraveled Drapes", t = { 1, 185, 187, 190 }, scroll = 276989, train = 175, scrollPrice = 100000, rep = { 2740, 4 }, sq = 2, r = { { 4234, 12 }, { 4236, 2 }, { 8343, 1 }, { 6260, 3 } }, out = { 277053, 1 }, oq = 2 },
    [1302604] = { name = "Light Leather Reagent Bag", t = { 1, 40, 45, 50 }, scroll = 277716, train = 30, scrollPrice = 150, sq = 2, r = { { 2318, 8 }, { 4231, 1 }, { 2320, 3 } }, out = { 277715, 1 }, oq = 1 },
    [1306526] = { name = "Elderwild Waistcord", t = { 1, 310, 317, 325 }, scroll = 279301, train = 300, sq = 4, r = { { 274030, 2 }, { 248824, 1 }, { 248825, 12 } }, out = { 279252, 1 }, oq = 4 },
    [1306527] = { name = "Outlaw's Collar", t = { 1, 310, 317, 325 }, scroll = 279302, train = 300, sq = 4, r = { { 274030, 3 }, { 248824, 2 }, { 248825, 22 } }, out = { 279253, 1 }, oq = 4 },
    [1306528] = { name = "Elderwild Pants", t = { 1, 310, 317, 325 }, scroll = 279303, train = 300, sq = 4, r = { { 274030, 3 }, { 248824, 2 }, { 248825, 18 } }, out = { 279254, 1 }, oq = 4 },
    [1306529] = { name = "Eternity Pauldrons", t = { 1, 310, 317, 325 }, scroll = 279304, train = 300, sq = 4, r = { { 274030, 2 }, { 248824, 1 }, { 248825, 12 } }, out = { 279255, 1 }, oq = 4 },
    [1306530] = { name = "Tranquil Wristguards", t = { 1, 310, 317, 325 }, scroll = 279305, train = 300, sq = 4, r = { { 274030, 1 }, { 248824, 1 }, { 248825, 10 } }, out = { 279256, 1 }, oq = 4 },
    [1306531] = { name = "Mourning Handguards", t = { 1, 310, 317, 325 }, scroll = 279306, train = 300, sq = 4, r = { { 274030, 2 }, { 248824, 1 }, { 248825, 12 } }, out = { 279257, 1 }, oq = 4 },
    [1306532] = { name = "Wild Leather Armor Kit", t = { 1, 310, 317, 325 }, scroll = 279307, train = 300, sq = 4, r = { { 248825, 22 }, { 14341, 3 } }, out = { 279258, 1 }, oq = 3 },
    [10482] = { name = "Cured Thick Hide", intermediate = true, t = { 1, 175, 175, 175 }, train = 175, r = { { 8169, 1 }, { 8150, 1 } }, out = { 8172, 1 } }, -- no da puntos: solo para fabricar el material
    [22331] = { name = "Rugged Leather", intermediate = true, t = { 1, 225, 225, 225 }, train = 225, r = { { 4304, 6 } }, out = { 8170, 1 } }, -- no da puntos: solo para fabricar el material
  },
}

-- Herramientas: [categoría] = { objeto, máscara } (un bastón superior cubre a los inferiores)
ES.Data.Tools = ES.Data.Tools or {}
ES.Data.Tools[12] = { item = 9149, mask = 1, family = "stone" }
ES.Data.Tools[14] = { item = 6219, mask = 1, family = "spanner" }
ES.Data.Tools[15] = { item = 10498, mask = 2, family = "adjustor" }
ES.Data.Tools[162] = { item = 5956, mask = 4, family = "hammer" }
ES.Data.Tools[373] = { item = 6218, mask = 1, family = "rod" }
ES.Data.Tools[374] = { item = 6339, mask = 3, family = "rod" }
ES.Data.Tools[375] = { item = 11130, mask = 7, family = "rod" }
ES.Data.Tools[376] = { item = 11145, mask = 15, family = "rod" }
ES.Data.Tools[377] = { item = 16207, mask = 31, family = "rod" }

ES.Data.VendorPrices = ES.Data.VendorPrices or {}
ES.Data.SellPrices = ES.Data.SellPrices or {}
ES.Data.VendorPrices[2320] = 10
ES.Data.VendorPrices[2321] = 100
ES.Data.VendorPrices[2324] = 25
ES.Data.VendorPrices[2325] = 1000
ES.Data.VendorPrices[2605] = 100
ES.Data.VendorPrices[3385] = 120
ES.Data.VendorPrices[4289] = 50
ES.Data.VendorPrices[4291] = 500
ES.Data.VendorPrices[4340] = 350
ES.Data.VendorPrices[4470] = 38
ES.Data.VendorPrices[6260] = 50
ES.Data.VendorPrices[6261] = 1000
ES.Data.VendorPrices[8343] = 2000
ES.Data.VendorPrices[10940] = 800
ES.Data.VendorPrices[14341] = 5000
ES.Data.SellPrices[783] = 50
ES.Data.SellPrices[1206] = 400
ES.Data.SellPrices[1210] = 250
ES.Data.SellPrices[1529] = 700
ES.Data.SellPrices[2300] = 192
ES.Data.SellPrices[2302] = 29
ES.Data.SellPrices[2303] = 71
ES.Data.SellPrices[2304] = 15
ES.Data.SellPrices[2307] = 195
ES.Data.SellPrices[2308] = 267
ES.Data.SellPrices[2309] = 217
ES.Data.SellPrices[2310] = 112
ES.Data.SellPrices[2311] = 150
ES.Data.SellPrices[2312] = 181
ES.Data.SellPrices[2313] = 200
ES.Data.SellPrices[2314] = 743
ES.Data.SellPrices[2315] = 307
ES.Data.SellPrices[2316] = 408
ES.Data.SellPrices[2317] = 689
ES.Data.SellPrices[2318] = 15
ES.Data.SellPrices[2319] = 50
ES.Data.SellPrices[2320] = 2
ES.Data.SellPrices[2321] = 25
ES.Data.SellPrices[2324] = 6
ES.Data.SellPrices[2325] = 250
ES.Data.SellPrices[2454] = 20
ES.Data.SellPrices[2455] = 10
ES.Data.SellPrices[2457] = 15
ES.Data.SellPrices[2458] = 15
ES.Data.SellPrices[2459] = 25
ES.Data.SellPrices[2605] = 25
ES.Data.SellPrices[2934] = 7
ES.Data.SellPrices[2997] = 100
ES.Data.SellPrices[3182] = 387
ES.Data.SellPrices[3356] = 30
ES.Data.SellPrices[3383] = 100
ES.Data.SellPrices[3385] = 30
ES.Data.SellPrices[3389] = 40
ES.Data.SellPrices[3390] = 35
ES.Data.SellPrices[3391] = 20
ES.Data.SellPrices[3719] = 1027
ES.Data.SellPrices[3824] = 150
ES.Data.SellPrices[3827] = 120
ES.Data.SellPrices[3864] = 800
ES.Data.SellPrices[4096] = 608
ES.Data.SellPrices[4231] = 110
ES.Data.SellPrices[4232] = 125
ES.Data.SellPrices[4233] = 200
ES.Data.SellPrices[4234] = 150
ES.Data.SellPrices[4235] = 200
ES.Data.SellPrices[4236] = 225
ES.Data.SellPrices[4237] = 34
ES.Data.SellPrices[4239] = 71
ES.Data.SellPrices[4242] = 347
ES.Data.SellPrices[4243] = 461
ES.Data.SellPrices[4244] = 723
ES.Data.SellPrices[4246] = 125
ES.Data.SellPrices[4247] = 1049
ES.Data.SellPrices[4248] = 791
ES.Data.SellPrices[4249] = 703
ES.Data.SellPrices[4250] = 705
ES.Data.SellPrices[4251] = 659
ES.Data.SellPrices[4252] = 1457
ES.Data.SellPrices[4253] = 962
ES.Data.SellPrices[4254] = 1071
ES.Data.SellPrices[4255] = 2366
ES.Data.SellPrices[4256] = 3477
ES.Data.SellPrices[4257] = 1311
ES.Data.SellPrices[4258] = 1592
ES.Data.SellPrices[4259] = 1934
ES.Data.SellPrices[4260] = 2559
ES.Data.SellPrices[4262] = 2652
ES.Data.SellPrices[4264] = 2804
ES.Data.SellPrices[4265] = 650
ES.Data.SellPrices[4289] = 12
ES.Data.SellPrices[4291] = 125
ES.Data.SellPrices[4304] = 300
ES.Data.SellPrices[4305] = 600
ES.Data.SellPrices[4337] = 750
ES.Data.SellPrices[4338] = 250
ES.Data.SellPrices[4340] = 87
ES.Data.SellPrices[4455] = 3096
ES.Data.SellPrices[4456] = 1553
ES.Data.SellPrices[4461] = 208
ES.Data.SellPrices[4470] = 9
ES.Data.SellPrices[5081] = 250
ES.Data.SellPrices[5082] = 25
ES.Data.SellPrices[5116] = 303
ES.Data.SellPrices[5373] = 72
ES.Data.SellPrices[5498] = 200
ES.Data.SellPrices[5500] = 750
ES.Data.SellPrices[5633] = 150
ES.Data.SellPrices[5637] = 75
ES.Data.SellPrices[5739] = 2738
ES.Data.SellPrices[5780] = 260
ES.Data.SellPrices[5781] = 601
ES.Data.SellPrices[5782] = 3211
ES.Data.SellPrices[5783] = 2316
ES.Data.SellPrices[5784] = 75
ES.Data.SellPrices[5785] = 500
ES.Data.SellPrices[5957] = 40
ES.Data.SellPrices[5958] = 829
ES.Data.SellPrices[5961] = 1089
ES.Data.SellPrices[5962] = 2794
ES.Data.SellPrices[5963] = 3151
ES.Data.SellPrices[5964] = 2609
ES.Data.SellPrices[5965] = 2536
ES.Data.SellPrices[5966] = 1374
ES.Data.SellPrices[6260] = 12
ES.Data.SellPrices[6261] = 250
ES.Data.SellPrices[6466] = 413
ES.Data.SellPrices[6467] = 420
ES.Data.SellPrices[6468] = 658
ES.Data.SellPrices[6470] = 20
ES.Data.SellPrices[6471] = 500
ES.Data.SellPrices[6662] = 95
ES.Data.SellPrices[6709] = 545
ES.Data.SellPrices[7067] = 400
ES.Data.SellPrices[7069] = 400
ES.Data.SellPrices[7070] = 400
ES.Data.SellPrices[7071] = 100
ES.Data.SellPrices[7075] = 400
ES.Data.SellPrices[7076] = 400
ES.Data.SellPrices[7077] = 400
ES.Data.SellPrices[7078] = 400
ES.Data.SellPrices[7079] = 400
ES.Data.SellPrices[7080] = 400
ES.Data.SellPrices[7082] = 400
ES.Data.SellPrices[7276] = 34
ES.Data.SellPrices[7277] = 28
ES.Data.SellPrices[7278] = 25
ES.Data.SellPrices[7279] = 25
ES.Data.SellPrices[7280] = 162
ES.Data.SellPrices[7281] = 84
ES.Data.SellPrices[7282] = 599
ES.Data.SellPrices[7283] = 519
ES.Data.SellPrices[7284] = 586
ES.Data.SellPrices[7285] = 588
ES.Data.SellPrices[7286] = 25
ES.Data.SellPrices[7287] = 100
ES.Data.SellPrices[7348] = 690
ES.Data.SellPrices[7349] = 861
ES.Data.SellPrices[7352] = 1306
ES.Data.SellPrices[7358] = 885
ES.Data.SellPrices[7359] = 978
ES.Data.SellPrices[7371] = 500
ES.Data.SellPrices[7372] = 500
ES.Data.SellPrices[7373] = 3097
ES.Data.SellPrices[7374] = 3760
ES.Data.SellPrices[7375] = 3773
ES.Data.SellPrices[7377] = 2269
ES.Data.SellPrices[7378] = 2146
ES.Data.SellPrices[7386] = 2387
ES.Data.SellPrices[7387] = 2587
ES.Data.SellPrices[7390] = 4237
ES.Data.SellPrices[7391] = 4253
ES.Data.SellPrices[7392] = 200
ES.Data.SellPrices[7428] = 250
ES.Data.SellPrices[7971] = 1000
ES.Data.SellPrices[8146] = 500
ES.Data.SellPrices[8150] = 250
ES.Data.SellPrices[8151] = 250
ES.Data.SellPrices[8152] = 500
ES.Data.SellPrices[8153] = 5
ES.Data.SellPrices[8154] = 250
ES.Data.SellPrices[8165] = 500
ES.Data.SellPrices[8167] = 100
ES.Data.SellPrices[8168] = 100
ES.Data.SellPrices[8169] = 500
ES.Data.SellPrices[8170] = 500
ES.Data.SellPrices[8171] = 500
ES.Data.SellPrices[8172] = 500
ES.Data.SellPrices[8173] = 1000
ES.Data.SellPrices[8174] = 4131
ES.Data.SellPrices[8175] = 3881
ES.Data.SellPrices[8176] = 2922
ES.Data.SellPrices[8185] = 10952
ES.Data.SellPrices[8187] = 3477
ES.Data.SellPrices[8189] = 7567
ES.Data.SellPrices[8191] = 7780
ES.Data.SellPrices[8192] = 4782
ES.Data.SellPrices[8193] = 8708
ES.Data.SellPrices[8195] = 5263
ES.Data.SellPrices[8197] = 7158
ES.Data.SellPrices[8198] = 4013
ES.Data.SellPrices[8200] = 7275
ES.Data.SellPrices[8201] = 5350
ES.Data.SellPrices[8202] = 9022
ES.Data.SellPrices[8203] = 8628
ES.Data.SellPrices[8204] = 4676
ES.Data.SellPrices[8205] = 4346
ES.Data.SellPrices[8206] = 12704
ES.Data.SellPrices[8207] = 8978
ES.Data.SellPrices[8208] = 10272
ES.Data.SellPrices[8209] = 8375
ES.Data.SellPrices[8210] = 5537
ES.Data.SellPrices[8211] = 8002
ES.Data.SellPrices[8212] = 11585
ES.Data.SellPrices[8213] = 8150
ES.Data.SellPrices[8214] = 6230
ES.Data.SellPrices[8215] = 9017
ES.Data.SellPrices[8216] = 6323
ES.Data.SellPrices[8217] = 1000
ES.Data.SellPrices[8218] = 1000
ES.Data.SellPrices[8343] = 500
ES.Data.SellPrices[8345] = 7421
ES.Data.SellPrices[8346] = 5363
ES.Data.SellPrices[8347] = 5979
ES.Data.SellPrices[8348] = 10819
ES.Data.SellPrices[8349] = 14478
ES.Data.SellPrices[8367] = 18455
ES.Data.SellPrices[8368] = 1000
ES.Data.SellPrices[8949] = 200
ES.Data.SellPrices[8951] = 200
ES.Data.SellPrices[9206] = 700
ES.Data.SellPrices[10940] = 1
ES.Data.SellPrices[11083] = 1
ES.Data.SellPrices[11137] = 1
ES.Data.SellPrices[11176] = 1
ES.Data.SellPrices[12361] = 7000
ES.Data.SellPrices[12364] = 10000
ES.Data.SellPrices[12607] = 8048
ES.Data.SellPrices[12624] = 20642
ES.Data.SellPrices[12632] = 14099
ES.Data.SellPrices[12636] = 24285
ES.Data.SellPrices[12641] = 43836
ES.Data.SellPrices[12799] = 7000
ES.Data.SellPrices[12800] = 10000
ES.Data.SellPrices[12803] = 500
ES.Data.SellPrices[12804] = 2000
ES.Data.SellPrices[12809] = 10000
ES.Data.SellPrices[12810] = 500
ES.Data.SellPrices[12811] = 20000
ES.Data.SellPrices[13423] = 125
ES.Data.SellPrices[13444] = 1500
ES.Data.SellPrices[14044] = 9503
ES.Data.SellPrices[14047] = 400
ES.Data.SellPrices[14048] = 2000
ES.Data.SellPrices[14227] = 2500
ES.Data.SellPrices[14256] = 2000
ES.Data.SellPrices[14341] = 1250
ES.Data.SellPrices[14342] = 4000
ES.Data.SellPrices[15045] = 19938
ES.Data.SellPrices[15046] = 22482
ES.Data.SellPrices[15047] = 29836
ES.Data.SellPrices[15048] = 24409
ES.Data.SellPrices[15049] = 20543
ES.Data.SellPrices[15050] = 26071
ES.Data.SellPrices[15051] = 21736
ES.Data.SellPrices[15052] = 31933
ES.Data.SellPrices[15053] = 9501
ES.Data.SellPrices[15054] = 8007
ES.Data.SellPrices[15055] = 16019
ES.Data.SellPrices[15056] = 20966
ES.Data.SellPrices[15057] = 18728
ES.Data.SellPrices[15058] = 17631
ES.Data.SellPrices[15059] = 24776
ES.Data.SellPrices[15060] = 21277
ES.Data.SellPrices[15061] = 13803
ES.Data.SellPrices[15062] = 25709
ES.Data.SellPrices[15063] = 11701
ES.Data.SellPrices[15064] = 19717
ES.Data.SellPrices[15065] = 22233
ES.Data.SellPrices[15066] = 23650
ES.Data.SellPrices[15067] = 12758
ES.Data.SellPrices[15068] = 21835
ES.Data.SellPrices[15069] = 17012
ES.Data.SellPrices[15070] = 9504
ES.Data.SellPrices[15071] = 11443
ES.Data.SellPrices[15072] = 16233
ES.Data.SellPrices[15073] = 11530
ES.Data.SellPrices[15074] = 6867
ES.Data.SellPrices[15075] = 18449
ES.Data.SellPrices[15076] = 16604
ES.Data.SellPrices[15077] = 7615
ES.Data.SellPrices[15078] = 9649
ES.Data.SellPrices[15079] = 21760
ES.Data.SellPrices[15080] = 18230
ES.Data.SellPrices[15081] = 20261
ES.Data.SellPrices[15082] = 10375
ES.Data.SellPrices[15083] = 6872
ES.Data.SellPrices[15084] = 7311
ES.Data.SellPrices[15085] = 22732
ES.Data.SellPrices[15086] = 13154
ES.Data.SellPrices[15087] = 17892
ES.Data.SellPrices[15088] = 9901
ES.Data.SellPrices[15090] = 22002
ES.Data.SellPrices[15091] = 7195
ES.Data.SellPrices[15092] = 7656
ES.Data.SellPrices[15093] = 8368
ES.Data.SellPrices[15094] = 14155
ES.Data.SellPrices[15095] = 20885
ES.Data.SellPrices[15096] = 17332
ES.Data.SellPrices[15138] = 15198
ES.Data.SellPrices[15141] = 41937
ES.Data.SellPrices[15407] = 500
ES.Data.SellPrices[15408] = 500
ES.Data.SellPrices[15409] = 1000
ES.Data.SellPrices[15410] = 5000
ES.Data.SellPrices[15412] = 500
ES.Data.SellPrices[15414] = 1500
ES.Data.SellPrices[15415] = 500
ES.Data.SellPrices[15416] = 1000
ES.Data.SellPrices[15417] = 500
ES.Data.SellPrices[15419] = 600
ES.Data.SellPrices[15420] = 100
ES.Data.SellPrices[15422] = 500
ES.Data.SellPrices[15423] = 500
ES.Data.SellPrices[15564] = 1000
ES.Data.SellPrices[16982] = 24397
ES.Data.SellPrices[16983] = 25709
ES.Data.SellPrices[16984] = 32653
ES.Data.SellPrices[17010] = 2000
ES.Data.SellPrices[17011] = 2000
ES.Data.SellPrices[17012] = 1000
ES.Data.SellPrices[17721] = 2268
ES.Data.SellPrices[18238] = 3321
ES.Data.SellPrices[18251] = 5000
ES.Data.SellPrices[18504] = 14126
ES.Data.SellPrices[18506] = 21340
ES.Data.SellPrices[18508] = 17194
ES.Data.SellPrices[18509] = 23006
ES.Data.SellPrices[18510] = 20889
ES.Data.SellPrices[18511] = 20971
ES.Data.SellPrices[18512] = 4000
ES.Data.SellPrices[18662] = 5
ES.Data.SellPrices[18948] = 1589
ES.Data.SellPrices[19043] = 13291
ES.Data.SellPrices[19044] = 11116
ES.Data.SellPrices[19048] = 28061
ES.Data.SellPrices[19049] = 15576
ES.Data.SellPrices[19052] = 17621
ES.Data.SellPrices[19058] = 21845
ES.Data.SellPrices[19149] = 21248
ES.Data.SellPrices[19157] = 31943
ES.Data.SellPrices[19162] = 27831
ES.Data.SellPrices[19163] = 27931
ES.Data.SellPrices[19685] = 31644
ES.Data.SellPrices[19686] = 15880
ES.Data.SellPrices[19687] = 15939
ES.Data.SellPrices[19688] = 31993
ES.Data.SellPrices[19689] = 24082
ES.Data.SellPrices[19726] = 500
ES.Data.SellPrices[19767] = 2000
ES.Data.SellPrices[19768] = 2000
ES.Data.SellPrices[20295] = 31083
ES.Data.SellPrices[20296] = 12590
ES.Data.SellPrices[20380] = 57958
ES.Data.SellPrices[20381] = 5000
ES.Data.SellPrices[20476] = 16401
ES.Data.SellPrices[20477] = 16898
ES.Data.SellPrices[20478] = 33917
ES.Data.SellPrices[20479] = 34036
ES.Data.SellPrices[20480] = 17078
ES.Data.SellPrices[20481] = 17139
ES.Data.SellPrices[20498] = 1000
ES.Data.SellPrices[20500] = 2000
ES.Data.SellPrices[20501] = 2000
ES.Data.SellPrices[20575] = 743
ES.Data.SellPrices[21278] = 13212
ES.Data.SellPrices[22661] = 89377
ES.Data.SellPrices[22662] = 44851
ES.Data.SellPrices[22663] = 46175
ES.Data.SellPrices[22664] = 100642
ES.Data.SellPrices[22665] = 50516
ES.Data.SellPrices[22666] = 50712
ES.Data.SellPrices[22682] = 20000
ES.Data.SellPrices[22759] = 29190
ES.Data.SellPrices[22760] = 29302
ES.Data.SellPrices[22761] = 19607
ES.Data.SellPrices[213369] = 280
ES.Data.SellPrices[213379] = 280
ES.Data.SellPrices[248824] = 750
ES.Data.SellPrices[248825] = 750
ES.Data.SellPrices[249409] = 75
ES.Data.SellPrices[249410] = 125
ES.Data.SellPrices[249427] = 125
ES.Data.SellPrices[249428] = 250
ES.Data.SellPrices[249429] = 375
ES.Data.SellPrices[275610] = 11612
ES.Data.SellPrices[275611] = 11655
ES.Data.SellPrices[275612] = 17451
ES.Data.SellPrices[275613] = 11738
ES.Data.SellPrices[275614] = 11780
ES.Data.SellPrices[275615] = 16390
ES.Data.SellPrices[275616] = 13126
ES.Data.SellPrices[275617] = 13176
ES.Data.SellPrices[275618] = 19928
ES.Data.SellPrices[275619] = 13275
ES.Data.SellPrices[275620] = 13325
ES.Data.SellPrices[275621] = 20152
ES.Data.SellPrices[276538] = 40208
ES.Data.SellPrices[276539] = 20181
ES.Data.SellPrices[276540] = 30523
ES.Data.SellPrices[276541] = 30639
ES.Data.SellPrices[277715] = 100
ES.Data.SellPrices[279252] = 15518
ES.Data.SellPrices[279253] = 21404
ES.Data.SellPrices[279254] = 5252
ES.Data.SellPrices[279255] = 22503
ES.Data.SellPrices[279256] = 840
ES.Data.SellPrices[279257] = 17210
ES.Data.SellPrices[279258] = 5000

-- Nombre de cada objeto (inglés, del cliente): se muestra mientras el juego no lo ha cargado
ES.Data.ItemNames = ES.Data.ItemNames or {}
ES.Data.ItemNames[783] = "Light Hide"
ES.Data.ItemNames[1206] = "Moss Agate"
ES.Data.ItemNames[1210] = "Shadowgem"
ES.Data.ItemNames[1529] = "Jade"
ES.Data.ItemNames[2300] = "Embossed Leather Vest"
ES.Data.ItemNames[2302] = "Handstitched Leather Boots"
ES.Data.ItemNames[2303] = "Handstitched Leather Pants"
ES.Data.ItemNames[2304] = "Light Armor Kit"
ES.Data.ItemNames[2307] = "Fine Leather Boots"
ES.Data.ItemNames[2308] = "Fine Leather Cloak"
ES.Data.ItemNames[2309] = "Embossed Leather Boots"
ES.Data.ItemNames[2310] = "Embossed Leather Cloak"
ES.Data.ItemNames[2311] = "White Leather Jerkin"
ES.Data.ItemNames[2312] = "Fine Leather Gloves"
ES.Data.ItemNames[2313] = "Medium Armor Kit"
ES.Data.ItemNames[2314] = "Toughened Leather Armor"
ES.Data.ItemNames[2315] = "Gray Leather Boots"
ES.Data.ItemNames[2316] = "Dark Leather Cloak"
ES.Data.ItemNames[2317] = "Dark Leather Tunic"
ES.Data.ItemNames[2318] = "Light Leather"
ES.Data.ItemNames[2319] = "Medium Leather"
ES.Data.ItemNames[2320] = "Coarse Thread"
ES.Data.ItemNames[2321] = "Fine Thread"
ES.Data.ItemNames[2324] = "Bleach"
ES.Data.ItemNames[2325] = "Black Dye"
ES.Data.ItemNames[2454] = "Elixir of Minor Strength"
ES.Data.ItemNames[2455] = "Minor Mana Potion"
ES.Data.ItemNames[2457] = "Elixir of Minor Agility"
ES.Data.ItemNames[2458] = "Elixir of Minor Fortitude"
ES.Data.ItemNames[2459] = "Swiftness Potion"
ES.Data.ItemNames[2605] = "Green Dye"
ES.Data.ItemNames[2934] = "Ruined Leather Scraps"
ES.Data.ItemNames[2997] = "Bolt of Woolen Cloth"
ES.Data.ItemNames[3182] = "Spider's Silk"
ES.Data.ItemNames[3356] = "Kingsblood"
ES.Data.ItemNames[3383] = "Elixir of Wisdom"
ES.Data.ItemNames[3385] = "Lesser Mana Potion"
ES.Data.ItemNames[3389] = "Elixir of Lesser Defense"
ES.Data.ItemNames[3390] = "Elixir of Lesser Agility"
ES.Data.ItemNames[3391] = "Elixir of Ogre Strength"
ES.Data.ItemNames[3719] = "Hillman's Cloak"
ES.Data.ItemNames[3824] = "Shadow Oil"
ES.Data.ItemNames[3827] = "Mana Potion"
ES.Data.ItemNames[3864] = "Citrine"
ES.Data.ItemNames[4096] = "Coarse Gorilla Hair"
ES.Data.ItemNames[4231] = "Cured Light Hide"
ES.Data.ItemNames[4232] = "Medium Hide"
ES.Data.ItemNames[4233] = "Cured Medium Hide"
ES.Data.ItemNames[4234] = "Heavy Leather"
ES.Data.ItemNames[4235] = "Heavy Hide"
ES.Data.ItemNames[4236] = "Cured Heavy Hide"
ES.Data.ItemNames[4237] = "Handstitched Leather Belt"
ES.Data.ItemNames[4239] = "Embossed Leather Gloves"
ES.Data.ItemNames[4242] = "Embossed Leather Pants"
ES.Data.ItemNames[4243] = "Fine Leather Tunic"
ES.Data.ItemNames[4244] = "Hillman's Leather Vest"
ES.Data.ItemNames[4246] = "Fine Leather Belt"
ES.Data.ItemNames[4247] = "Hillman's Leather Gloves"
ES.Data.ItemNames[4248] = "Dark Leather Gloves"
ES.Data.ItemNames[4249] = "Dark Leather Belt"
ES.Data.ItemNames[4250] = "Hillman's Belt"
ES.Data.ItemNames[4251] = "Hillman's Shoulders"
ES.Data.ItemNames[4252] = "Dark Leather Shoulders"
ES.Data.ItemNames[4253] = "Toughened Leather Gloves"
ES.Data.ItemNames[4254] = "Barbaric Gloves"
ES.Data.ItemNames[4255] = "Green Leather Armor"
ES.Data.ItemNames[4256] = "Guardian Armor"
ES.Data.ItemNames[4257] = "Green Leather Belt"
ES.Data.ItemNames[4258] = "Guardian Belt"
ES.Data.ItemNames[4259] = "Green Leather Bracers"
ES.Data.ItemNames[4260] = "Guardian Leather Bracers"
ES.Data.ItemNames[4262] = "Gem-studded Leather Belt"
ES.Data.ItemNames[4264] = "Barbaric Belt"
ES.Data.ItemNames[4265] = "Heavy Armor Kit"
ES.Data.ItemNames[4289] = "Salt"
ES.Data.ItemNames[4291] = "Silken Thread"
ES.Data.ItemNames[4304] = "Thick Leather"
ES.Data.ItemNames[4305] = "Bolt of Silk Cloth"
ES.Data.ItemNames[4337] = "Thick Spider's Silk"
ES.Data.ItemNames[4338] = "Mageweave Cloth"
ES.Data.ItemNames[4340] = "Gray Dye"
ES.Data.ItemNames[4455] = "Raptor Hide Harness"
ES.Data.ItemNames[4456] = "Raptor Hide Belt"
ES.Data.ItemNames[4461] = "Raptor Hide"
ES.Data.ItemNames[4470] = "Simple Wood"
ES.Data.ItemNames[5081] = "Kodo Hide Bag"
ES.Data.ItemNames[5082] = "Thin Kodo Leather"
ES.Data.ItemNames[5116] = "Long Tail Feather"
ES.Data.ItemNames[5373] = "Lucky Charm"
ES.Data.ItemNames[5498] = "Small Lustrous Pearl"
ES.Data.ItemNames[5500] = "Iridescent Pearl"
ES.Data.ItemNames[5633] = "Great Rage Potion"
ES.Data.ItemNames[5637] = "Large Fang"
ES.Data.ItemNames[5739] = "Barbaric Harness"
ES.Data.ItemNames[5780] = "Murloc Scale Belt"
ES.Data.ItemNames[5781] = "Murloc Scale Breastplate"
ES.Data.ItemNames[5782] = "Thick Murloc Armor"
ES.Data.ItemNames[5783] = "Murloc Scale Bracers"
ES.Data.ItemNames[5784] = "Slimy Murloc Scale"
ES.Data.ItemNames[5785] = "Thick Murloc Scale"
ES.Data.ItemNames[5957] = "Handstitched Leather Vest"
ES.Data.ItemNames[5958] = "Fine Leather Pants"
ES.Data.ItemNames[5961] = "Dark Leather Pants"
ES.Data.ItemNames[5962] = "Guardian Pants"
ES.Data.ItemNames[5963] = "Barbaric Leggings"
ES.Data.ItemNames[5964] = "Barbaric Shoulders"
ES.Data.ItemNames[5965] = "Guardian Cloak"
ES.Data.ItemNames[5966] = "Guardian Gloves"
ES.Data.ItemNames[6260] = "Blue Dye"
ES.Data.ItemNames[6261] = "Orange Dye"
ES.Data.ItemNames[6466] = "Deviate Scale Cloak"
ES.Data.ItemNames[6467] = "Deviate Scale Gloves"
ES.Data.ItemNames[6468] = "Deviate Scale Belt"
ES.Data.ItemNames[6470] = "Deviate Scale"
ES.Data.ItemNames[6471] = "Perfect Deviate Scale"
ES.Data.ItemNames[6662] = "Elixir of Giant Growth"
ES.Data.ItemNames[6709] = "Moonglow Vest"
ES.Data.ItemNames[7067] = "Elemental Earth"
ES.Data.ItemNames[7069] = "Elemental Air"
ES.Data.ItemNames[7070] = "Elemental Water"
ES.Data.ItemNames[7071] = "Iron Buckle"
ES.Data.ItemNames[7075] = "Core of Earth"
ES.Data.ItemNames[7076] = "Essence of Earth"
ES.Data.ItemNames[7077] = "Heart of Fire"
ES.Data.ItemNames[7078] = "Essence of Fire"
ES.Data.ItemNames[7079] = "Globe of Water"
ES.Data.ItemNames[7080] = "Essence of Water"
ES.Data.ItemNames[7082] = "Essence of Air"
ES.Data.ItemNames[7276] = "Handstitched Leather Cloak"
ES.Data.ItemNames[7277] = "Handstitched Leather Bracers"
ES.Data.ItemNames[7278] = "Light Leather Quiver"
ES.Data.ItemNames[7279] = "Small Leather Ammo Pouch"
ES.Data.ItemNames[7280] = "Rugged Leather Pants"
ES.Data.ItemNames[7281] = "Light Leather Bracers"
ES.Data.ItemNames[7282] = "Light Leather Pants"
ES.Data.ItemNames[7283] = "Black Whelp Cloak"
ES.Data.ItemNames[7284] = "Red Whelp Gloves"
ES.Data.ItemNames[7285] = "Nimble Leather Gloves"
ES.Data.ItemNames[7286] = "Black Whelp Scale"
ES.Data.ItemNames[7287] = "Red Whelp Scale"
ES.Data.ItemNames[7348] = "Fletcher's Gloves"
ES.Data.ItemNames[7349] = "Herbalist's Gloves"
ES.Data.ItemNames[7352] = "Earthen Leather Shoulders"
ES.Data.ItemNames[7358] = "Pilferer's Gloves"
ES.Data.ItemNames[7359] = "Heavy Earthen Gloves"
ES.Data.ItemNames[7371] = "Heavy Quiver"
ES.Data.ItemNames[7372] = "Heavy Leather Ammo Pouch"
ES.Data.ItemNames[7373] = "Dusky Leather Leggings"
ES.Data.ItemNames[7374] = "Dusky Leather Armor"
ES.Data.ItemNames[7375] = "Green Whelp Armor"
ES.Data.ItemNames[7377] = "Frost Leather Cloak"
ES.Data.ItemNames[7378] = "Dusky Bracers"
ES.Data.ItemNames[7386] = "Green Whelp Bracers"
ES.Data.ItemNames[7387] = "Dusky Belt"
ES.Data.ItemNames[7390] = "Dusky Boots"
ES.Data.ItemNames[7391] = "Swift Boots"
ES.Data.ItemNames[7392] = "Green Whelp Scale"
ES.Data.ItemNames[7428] = "Shadowcat Hide"
ES.Data.ItemNames[7971] = "Black Pearl"
ES.Data.ItemNames[8146] = "Wicked Claw"
ES.Data.ItemNames[8150] = "Deeprock Salt"
ES.Data.ItemNames[8151] = "Flask of Mojo"
ES.Data.ItemNames[8152] = "Flask of Big Mojo"
ES.Data.ItemNames[8153] = "Wildvine"
ES.Data.ItemNames[8154] = "Scorpid Scale"
ES.Data.ItemNames[8165] = "Worn Dragonscale"
ES.Data.ItemNames[8167] = "Turtle Scale"
ES.Data.ItemNames[8168] = "Jet Black Feather"
ES.Data.ItemNames[8169] = "Thick Hide"
ES.Data.ItemNames[8170] = "Rugged Leather"
ES.Data.ItemNames[8171] = "Rugged Hide"
ES.Data.ItemNames[8172] = "Cured Thick Hide"
ES.Data.ItemNames[8173] = "Thick Armor Kit"
ES.Data.ItemNames[8174] = "Comfortable Leather Hat"
ES.Data.ItemNames[8175] = "Nightscape Tunic"
ES.Data.ItemNames[8176] = "Nightscape Headband"
ES.Data.ItemNames[8185] = "Turtle Scale Leggings"
ES.Data.ItemNames[8187] = "Turtle Scale Gloves"
ES.Data.ItemNames[8189] = "Turtle Scale Breastplate"
ES.Data.ItemNames[8191] = "Turtle Scale Helm"
ES.Data.ItemNames[8192] = "Nightscape Shoulders"
ES.Data.ItemNames[8193] = "Nightscape Pants"
ES.Data.ItemNames[8195] = "Nightscape Cloak"
ES.Data.ItemNames[8197] = "Nightscape Boots"
ES.Data.ItemNames[8198] = "Turtle Scale Bracers"
ES.Data.ItemNames[8200] = "Big Voodoo Robe"
ES.Data.ItemNames[8201] = "Big Voodoo Mask"
ES.Data.ItemNames[8202] = "Big Voodoo Pants"
ES.Data.ItemNames[8203] = "Tough Scorpid Breastplate"
ES.Data.ItemNames[8204] = "Tough Scorpid Gloves"
ES.Data.ItemNames[8205] = "Tough Scorpid Bracers"
ES.Data.ItemNames[8206] = "Tough Scorpid Leggings"
ES.Data.ItemNames[8207] = "Tough Scorpid Shoulders"
ES.Data.ItemNames[8208] = "Tough Scorpid Helm"
ES.Data.ItemNames[8209] = "Tough Scorpid Boots"
ES.Data.ItemNames[8210] = "Wild Leather Shoulders"
ES.Data.ItemNames[8211] = "Wild Leather Vest"
ES.Data.ItemNames[8212] = "Wild Leather Leggings"
ES.Data.ItemNames[8213] = "Wild Leather Boots"
ES.Data.ItemNames[8214] = "Wild Leather Helmet"
ES.Data.ItemNames[8215] = "Wild Leather Cloak"
ES.Data.ItemNames[8216] = "Big Voodoo Cloak"
ES.Data.ItemNames[8217] = "Quickdraw Quiver"
ES.Data.ItemNames[8218] = "Thick Leather Ammo Pouch"
ES.Data.ItemNames[8343] = "Heavy Silken Thread"
ES.Data.ItemNames[8345] = "Wolfshead Helm"
ES.Data.ItemNames[8346] = "Gauntlets of the Sea"
ES.Data.ItemNames[8347] = "Dragonscale Gauntlets"
ES.Data.ItemNames[8348] = "Helm of Fire"
ES.Data.ItemNames[8349] = "Feathered Breastplate"
ES.Data.ItemNames[8367] = "Dragonscale Breastplate"
ES.Data.ItemNames[8368] = "Thick Wolfhide"
ES.Data.ItemNames[8949] = "Elixir of Agility"
ES.Data.ItemNames[8951] = "Elixir of Defense"
ES.Data.ItemNames[9206] = "Elixir of Greater Strength"
ES.Data.ItemNames[10940] = "Strange Dust"
ES.Data.ItemNames[11083] = "Soul Dust"
ES.Data.ItemNames[11137] = "Vision Dust"
ES.Data.ItemNames[11176] = "Dream Dust"
ES.Data.ItemNames[11754] = "Black Diamond"
ES.Data.ItemNames[12361] = "Blue Sapphire"
ES.Data.ItemNames[12364] = "Huge Emerald"
ES.Data.ItemNames[12607] = "Brilliant Chromatic Scale"
ES.Data.ItemNames[12624] = "Wildthorn Mail"
ES.Data.ItemNames[12632] = "Storm Gauntlets"
ES.Data.ItemNames[12636] = "Helm of the Great Chief"
ES.Data.ItemNames[12641] = "Invulnerable Mail"
ES.Data.ItemNames[12753] = "Skin of Shadow"
ES.Data.ItemNames[12799] = "Large Opal"
ES.Data.ItemNames[12800] = "Azerothian Diamond"
ES.Data.ItemNames[12803] = "Living Essence"
ES.Data.ItemNames[12804] = "Powerful Mojo"
ES.Data.ItemNames[12809] = "Guardian Stone"
ES.Data.ItemNames[12810] = "Enchanted Leather"
ES.Data.ItemNames[12811] = "Righteous Orb"
ES.Data.ItemNames[12938] = "Blood of Heroes"
ES.Data.ItemNames[13423] = "Stonescale Oil"
ES.Data.ItemNames[13444] = "Major Mana Potion"
ES.Data.ItemNames[14044] = "Cindercloth Cloak"
ES.Data.ItemNames[14047] = "Runecloth"
ES.Data.ItemNames[14048] = "Bolt of Runecloth"
ES.Data.ItemNames[14227] = "Ironweb Spider Silk"
ES.Data.ItemNames[14256] = "Felcloth"
ES.Data.ItemNames[14341] = "Rune Thread"
ES.Data.ItemNames[14342] = "Mooncloth"
ES.Data.ItemNames[15045] = "Green Dragonscale Breastplate"
ES.Data.ItemNames[15046] = "Green Dragonscale Leggings"
ES.Data.ItemNames[15047] = "Red Dragonscale Breastplate"
ES.Data.ItemNames[15048] = "Blue Dragonscale Breastplate"
ES.Data.ItemNames[15049] = "Blue Dragonscale Shoulders"
ES.Data.ItemNames[15050] = "Black Dragonscale Breastplate"
ES.Data.ItemNames[15051] = "Black Dragonscale Shoulders"
ES.Data.ItemNames[15052] = "Black Dragonscale Leggings"
ES.Data.ItemNames[15053] = "Volcanic Breastplate"
ES.Data.ItemNames[15054] = "Volcanic Leggings"
ES.Data.ItemNames[15055] = "Volcanic Shoulders"
ES.Data.ItemNames[15056] = "Stormshroud Armor"
ES.Data.ItemNames[15057] = "Stormshroud Pants"
ES.Data.ItemNames[15058] = "Stormshroud Shoulders"
ES.Data.ItemNames[15059] = "Living Breastplate"
ES.Data.ItemNames[15060] = "Living Leggings"
ES.Data.ItemNames[15061] = "Living Shoulders"
ES.Data.ItemNames[15062] = "Devilsaur Leggings"
ES.Data.ItemNames[15063] = "Devilsaur Gauntlets"
ES.Data.ItemNames[15064] = "Warbear Harness"
ES.Data.ItemNames[15065] = "Warbear Woolies"
ES.Data.ItemNames[15066] = "Ironfeather Breastplate"
ES.Data.ItemNames[15067] = "Ironfeather Shoulders"
ES.Data.ItemNames[15068] = "Frostsaber Tunic"
ES.Data.ItemNames[15069] = "Frostsaber Leggings"
ES.Data.ItemNames[15070] = "Frostsaber Gloves"
ES.Data.ItemNames[15071] = "Frostsaber Boots"
ES.Data.ItemNames[15072] = "Chimeric Leggings"
ES.Data.ItemNames[15073] = "Chimeric Boots"
ES.Data.ItemNames[15074] = "Chimeric Gloves"
ES.Data.ItemNames[15075] = "Chimeric Vest"
ES.Data.ItemNames[15076] = "Heavy Scorpid Vest"
ES.Data.ItemNames[15077] = "Heavy Scorpid Bracers"
ES.Data.ItemNames[15078] = "Heavy Scorpid Gauntlet"
ES.Data.ItemNames[15079] = "Heavy Scorpid Leggings"
ES.Data.ItemNames[15080] = "Heavy Scorpid Helm"
ES.Data.ItemNames[15081] = "Heavy Scorpid Shoulders"
ES.Data.ItemNames[15082] = "Heavy Scorpid Belt"
ES.Data.ItemNames[15083] = "Wicked Leather Gauntlets"
ES.Data.ItemNames[15084] = "Wicked Leather Bracers"
ES.Data.ItemNames[15085] = "Wicked Leather Armor"
ES.Data.ItemNames[15086] = "Wicked Leather Headband"
ES.Data.ItemNames[15087] = "Wicked Leather Pants"
ES.Data.ItemNames[15088] = "Wicked Leather Belt"
ES.Data.ItemNames[15090] = "Runic Leather Armor"
ES.Data.ItemNames[15091] = "Runic Leather Gauntlets"
ES.Data.ItemNames[15092] = "Runic Leather Bracers"
ES.Data.ItemNames[15093] = "Runic Leather Belt"
ES.Data.ItemNames[15094] = "Runic Leather Headband"
ES.Data.ItemNames[15095] = "Runic Leather Pants"
ES.Data.ItemNames[15096] = "Runic Leather Shoulders"
ES.Data.ItemNames[15138] = "Onyxia Scale Cloak"
ES.Data.ItemNames[15141] = "Onyxia Scale Breastplate"
ES.Data.ItemNames[15407] = "Cured Rugged Hide"
ES.Data.ItemNames[15408] = "Heavy Scorpid Scale"
ES.Data.ItemNames[15409] = "Refined Deeprock Salt"
ES.Data.ItemNames[15410] = "Scale of Onyxia"
ES.Data.ItemNames[15412] = "Green Dragonscale"
ES.Data.ItemNames[15414] = "Red Dragonscale"
ES.Data.ItemNames[15415] = "Blue Dragonscale"
ES.Data.ItemNames[15416] = "Black Dragonscale"
ES.Data.ItemNames[15417] = "Devilsaur Leather"
ES.Data.ItemNames[15419] = "Warbear Leather"
ES.Data.ItemNames[15420] = "Ironfeather"
ES.Data.ItemNames[15422] = "Frostsaber Leather"
ES.Data.ItemNames[15423] = "Chimera Leather"
ES.Data.ItemNames[15564] = "Rugged Armor Kit"
ES.Data.ItemNames[16982] = "Corehound Boots"
ES.Data.ItemNames[16983] = "Molten Helm"
ES.Data.ItemNames[16984] = "Black Dragonscale Boots"
ES.Data.ItemNames[17010] = "Fiery Core"
ES.Data.ItemNames[17011] = "Lava Core"
ES.Data.ItemNames[17012] = "Core Leather"
ES.Data.ItemNames[17721] = "Gloves of the Greatfather"
ES.Data.ItemNames[18238] = "Shadowskin Gloves"
ES.Data.ItemNames[18240] = "Ogre Tannin"
ES.Data.ItemNames[18251] = "Core Armor Kit"
ES.Data.ItemNames[18258] = "Gordok Ogre Suit"
ES.Data.ItemNames[18504] = "Girdle of Insight"
ES.Data.ItemNames[18506] = "Mongoose Boots"
ES.Data.ItemNames[18508] = "Swift Flight Bracers"
ES.Data.ItemNames[18509] = "Chromatic Cloak"
ES.Data.ItemNames[18510] = "Hide of the Wild"
ES.Data.ItemNames[18511] = "Shifting Cloak"
ES.Data.ItemNames[18512] = "Larval Acid"
ES.Data.ItemNames[18662] = "Heavy Leather Ball"
ES.Data.ItemNames[18948] = "Barbaric Bracers"
ES.Data.ItemNames[19043] = "Heavy Timbermaw Belt"
ES.Data.ItemNames[19044] = "Might of the Timbermaw"
ES.Data.ItemNames[19048] = "Heavy Timbermaw Boots"
ES.Data.ItemNames[19049] = "Timbermaw Brawlers"
ES.Data.ItemNames[19052] = "Dawn Treaders"
ES.Data.ItemNames[19058] = "Golden Mantle of the Dawn"
ES.Data.ItemNames[19149] = "Lava Belt"
ES.Data.ItemNames[19157] = "Chromatic Gauntlets"
ES.Data.ItemNames[19162] = "Corehound Belt"
ES.Data.ItemNames[19163] = "Molten Belt"
ES.Data.ItemNames[19685] = "Primal Batskin Jerkin"
ES.Data.ItemNames[19686] = "Primal Batskin Gloves"
ES.Data.ItemNames[19687] = "Primal Batskin Bracers"
ES.Data.ItemNames[19688] = "Blood Tiger Breastplate"
ES.Data.ItemNames[19689] = "Blood Tiger Shoulders"
ES.Data.ItemNames[19726] = "Bloodvine"
ES.Data.ItemNames[19767] = "Primal Bat Leather"
ES.Data.ItemNames[19768] = "Primal Tiger Leather"
ES.Data.ItemNames[20295] = "Blue Dragonscale Leggings"
ES.Data.ItemNames[20296] = "Green Dragonscale Gauntlets"
ES.Data.ItemNames[20380] = "Dreamscale Breastplate"
ES.Data.ItemNames[20381] = "Dreamscale"
ES.Data.ItemNames[20476] = "Sandstalker Bracers"
ES.Data.ItemNames[20477] = "Sandstalker Gauntlets"
ES.Data.ItemNames[20478] = "Sandstalker Breastplate"
ES.Data.ItemNames[20479] = "Spitfire Breastplate"
ES.Data.ItemNames[20480] = "Spitfire Gauntlets"
ES.Data.ItemNames[20481] = "Spitfire Bracers"
ES.Data.ItemNames[20498] = "Silithid Chitin"
ES.Data.ItemNames[20500] = "Light Silithid Carapace"
ES.Data.ItemNames[20501] = "Heavy Silithid Carapace"
ES.Data.ItemNames[20575] = "Black Whelp Tunic"
ES.Data.ItemNames[21278] = "Stormshroud Gloves"
ES.Data.ItemNames[22661] = "Polar Tunic"
ES.Data.ItemNames[22662] = "Polar Gloves"
ES.Data.ItemNames[22663] = "Polar Bracers"
ES.Data.ItemNames[22664] = "Icy Scale Breastplate"
ES.Data.ItemNames[22665] = "Icy Scale Bracers"
ES.Data.ItemNames[22666] = "Icy Scale Gauntlets"
ES.Data.ItemNames[22682] = "Frozen Rune"
ES.Data.ItemNames[22759] = "Bramblewood Helm"
ES.Data.ItemNames[22760] = "Bramblewood Boots"
ES.Data.ItemNames[22761] = "Bramblewood Belt"
ES.Data.ItemNames[213369] = "Faintly Glowing Leather"
ES.Data.ItemNames[213370] = "Irradiated Leather Scraps"
ES.Data.ItemNames[213379] = "Hyperconductive Arcano-Filament"
ES.Data.ItemNames[248824] = "Fel Hide"
ES.Data.ItemNames[248825] = "Fel Leather"
ES.Data.ItemNames[249409] = "Cerulean Dye"
ES.Data.ItemNames[249410] = "Sulfuric Acid"
ES.Data.ItemNames[249427] = "Pristine Leather"
ES.Data.ItemNames[249428] = "Pristine Hide"
ES.Data.ItemNames[249429] = "Pristine Scale"
ES.Data.ItemNames[252428] = "Brawler's Leather Belt"
ES.Data.ItemNames[252429] = "Trapper's Leather Belt"
ES.Data.ItemNames[252430] = "Defender's Leather Belt"
ES.Data.ItemNames[252431] = "Totemic Leather Belt"
ES.Data.ItemNames[252432] = "Stormrider's Leather Belt"
ES.Data.ItemNames[252433] = "Wisdom's Leather Belt"
ES.Data.ItemNames[252436] = "Mystic Medium Armor Kit"
ES.Data.ItemNames[252437] = "Forceful Medium Armor Kit"
ES.Data.ItemNames[252439] = "Brawler's Leather Boots"
ES.Data.ItemNames[252440] = "Trapper's Leather Boots"
ES.Data.ItemNames[252441] = "Defender's Leather Boots"
ES.Data.ItemNames[252442] = "Totemic Leather Boots"
ES.Data.ItemNames[252443] = "Stormrider's Leather Boots"
ES.Data.ItemNames[252444] = "Wisdom's Leather Boots"
ES.Data.ItemNames[252447] = "Defender's Leather Hood"
ES.Data.ItemNames[252448] = "Totemic Leather Hood"
ES.Data.ItemNames[252449] = "Hillman's Leather Boots"
ES.Data.ItemNames[252450] = "Defender's Leather Tunic"
ES.Data.ItemNames[252451] = "Totemic Leather Tunic"
ES.Data.ItemNames[252452] = "Mystic Heavy Armor Kit"
ES.Data.ItemNames[252453] = "Forceful Heavy Armor Kit"
ES.Data.ItemNames[252457] = "Defender's Leather Kilt"
ES.Data.ItemNames[252458] = "Totemic Leather Leggings"
ES.Data.ItemNames[252462] = "Mystic Thick Armor Kit"
ES.Data.ItemNames[252463] = "Forceful Thick Armor Kit"
ES.Data.ItemNames[252467] = "Blue Suede Shoes"
ES.Data.ItemNames[252468] = "Prowler's Leather Boots"
ES.Data.ItemNames[252469] = "Skulker's Leather Boots"
ES.Data.ItemNames[252470] = "Warden's Leather Boots"
ES.Data.ItemNames[252471] = "Skycaller's Leather Boots"
ES.Data.ItemNames[252472] = "Mender's Leather Boots"
ES.Data.ItemNames[252473] = "Prowler's Leather Waistguard"
ES.Data.ItemNames[252474] = "Skulker's Leather Waistguard"
ES.Data.ItemNames[252475] = "Warden's Leather Waistguard"
ES.Data.ItemNames[252476] = "Skycaller's Leather Waistguard"
ES.Data.ItemNames[252477] = "Mender's Leather Waistguard"
ES.Data.ItemNames[252478] = "Blue Suede Pants"
ES.Data.ItemNames[252479] = "Wicked Leather Boots"
ES.Data.ItemNames[252480] = "Blue Suede Armor"
ES.Data.ItemNames[252481] = "Blue Suede Belt"
ES.Data.ItemNames[252482] = "Blue Suede Hat"
ES.Data.ItemNames[252483] = "Dawn Armor"
ES.Data.ItemNames[252484] = "Timbermaw Tunic"
ES.Data.ItemNames[252485] = "Warbear Helm"
ES.Data.ItemNames[252486] = "Ironfeather Leggings"
ES.Data.ItemNames[252487] = "Mystic Rugged Armor Kit"
ES.Data.ItemNames[252488] = "Forceful Rugged Armor Kit"
ES.Data.ItemNames[252494] = "Brawler's Leather Gloves"
ES.Data.ItemNames[252495] = "Trapper's Leather Gloves"
ES.Data.ItemNames[252496] = "Defender's Leather Gloves"
ES.Data.ItemNames[252497] = "Totemic Leather Gloves"
ES.Data.ItemNames[252498] = "Stormrider's Leather Gloves"
ES.Data.ItemNames[252499] = "Wisdom's Leather Gloves"
ES.Data.ItemNames[252504] = "Brawler's Leather Hood"
ES.Data.ItemNames[252505] = "Trapper's Leather Hood"
ES.Data.ItemNames[252506] = "Stormrider's Leather Hood"
ES.Data.ItemNames[252507] = "Wisdom's Leather Hood"
ES.Data.ItemNames[252508] = "Brawler's Leather Tunic"
ES.Data.ItemNames[252509] = "Trapper's Leather Tunic"
ES.Data.ItemNames[252510] = "Stormrider's Leather Tunic"
ES.Data.ItemNames[252511] = "Wisdom's Leather Tunic"
ES.Data.ItemNames[252516] = "Brawler's Leather Legguards"
ES.Data.ItemNames[252517] = "Trapper's Leather Legguards"
ES.Data.ItemNames[252518] = "Stormrider's Leather Kilt"
ES.Data.ItemNames[252519] = "Wisdom's Leather Leggings"
ES.Data.ItemNames[252524] = "Prowler's Leather Gloves"
ES.Data.ItemNames[252525] = "Skulker's Leather Gloves"
ES.Data.ItemNames[252526] = "Stalker's Leather Gloves"
ES.Data.ItemNames[252527] = "Warden's Leather Gloves"
ES.Data.ItemNames[252528] = "Skirmisher's Leather Gloves"
ES.Data.ItemNames[252529] = "Skycaller's Leather Gloves"
ES.Data.ItemNames[252530] = "Mender's Leather Gloves"
ES.Data.ItemNames[252534] = "Prowler's Leather Shoulders"
ES.Data.ItemNames[252535] = "Skulker's Leather Shoulder"
ES.Data.ItemNames[252536] = "Warden's Leather Shoulders"
ES.Data.ItemNames[252537] = "Skycaller's Leather Shoulders"
ES.Data.ItemNames[252538] = "Mender's Leather Shoulders"
ES.Data.ItemNames[252539] = "Prowler's Leather Bracers"
ES.Data.ItemNames[252540] = "Skulker's Leather Bracers"
ES.Data.ItemNames[252541] = "Warden's Leather Bracers"
ES.Data.ItemNames[252542] = "Skycaller's Leather Bracers"
ES.Data.ItemNames[252543] = "Mender's Leather Bracers"
ES.Data.ItemNames[252544] = "Tooled Leather Belt"
ES.Data.ItemNames[252545] = "Tooled Leather Boots"
ES.Data.ItemNames[252546] = "Blue Suede Gloves"
ES.Data.ItemNames[252552] = "Tooled Leather Armor"
ES.Data.ItemNames[252553] = "Tooled Leather Gauntlets"
ES.Data.ItemNames[252554] = "Blue Suede Shoulders"
ES.Data.ItemNames[252555] = "Tooled Leather Crown"
ES.Data.ItemNames[252556] = "Wicked Leather Shoulders"
ES.Data.ItemNames[252557] = "Tooled Leather Bracers"
ES.Data.ItemNames[252558] = "Tooled Leather Epaulets"
ES.Data.ItemNames[252559] = "Blue Suede Bracers"
ES.Data.ItemNames[252560] = "Tooled Leather Pants"
ES.Data.ItemNames[252561] = "Living Crown"
ES.Data.ItemNames[252566] = "Stalker's Mail Shoulders"
ES.Data.ItemNames[252567] = "Skycaller's Mail Shoulders"
ES.Data.ItemNames[252568] = "Skirmisher's Mail Shoulders"
ES.Data.ItemNames[252569] = "Mender's Mail Shoulders"
ES.Data.ItemNames[252570] = "Stalker's Mail Bracers"
ES.Data.ItemNames[252571] = "Skycaller's Mail Bracers"
ES.Data.ItemNames[252572] = "Skirmisher's Mail Bracers"
ES.Data.ItemNames[252573] = "Mender's Mail Bracers"
ES.Data.ItemNames[252574] = "Supple Scorpid Boots"
ES.Data.ItemNames[252575] = "Charged Scorpid Belt"
ES.Data.ItemNames[252576] = "Stalker's Mail Sabatons"
ES.Data.ItemNames[252577] = "Skycaller's Mail Sabatons"
ES.Data.ItemNames[252578] = "Skirmisher's Mail Sabatons"
ES.Data.ItemNames[252579] = "Mender's Mail Sabatons"
ES.Data.ItemNames[252580] = "Supple Scorpid Leggings"
ES.Data.ItemNames[252581] = "Charged Scorpid Helm"
ES.Data.ItemNames[252582] = "Supple Scorpid Bracers"
ES.Data.ItemNames[252583] = "Charged Scorpid Shoulders"
ES.Data.ItemNames[252588] = "Stalker's Mail Belt"
ES.Data.ItemNames[252589] = "Skycaller's Mail Belt"
ES.Data.ItemNames[252590] = "Skirmisher's Mail Belt"
ES.Data.ItemNames[252591] = "Mender's Mail Belt"
ES.Data.ItemNames[252592] = "Supple Scorpid Shoulders"
ES.Data.ItemNames[252593] = "Charged Scorpid Bracers"
ES.Data.ItemNames[252594] = "Heavy Scorpid Boots"
ES.Data.ItemNames[252595] = "Supple Scorpid Belt"
ES.Data.ItemNames[252596] = "Charged Scorpid Gauntlets"
ES.Data.ItemNames[252597] = "Supple Scorpid Helm"
ES.Data.ItemNames[252598] = "Charged Scorpid Vest"
ES.Data.ItemNames[252599] = "Supple Scorpid Vest"
ES.Data.ItemNames[252600] = "Charged Scorpid Leggings"
ES.Data.ItemNames[252601] = "Supple Scorpid Sabatons"
ES.Data.ItemNames[252602] = "Charged Scorpid Boots"
ES.Data.ItemNames[252603] = "Red Dragonscale Leggings"
ES.Data.ItemNames[252604] = "Blue Dragonscale Helm"
ES.Data.ItemNames[252605] = "Black Dragonscale Helm"
ES.Data.ItemNames[252606] = "Pristine Scorpid Leggings"
ES.Data.ItemNames[274030] = "Malleable Essence of Nature"
ES.Data.ItemNames[275610] = "Bileblister Claws"
ES.Data.ItemNames[275611] = "Bileblister Girdle"
ES.Data.ItemNames[275612] = "Bileblister Boots"
ES.Data.ItemNames[275613] = "Hivethrasher's Claws"
ES.Data.ItemNames[275614] = "Hivethrasher's Girdle"
ES.Data.ItemNames[275615] = "Hivethrasher's Boots"
ES.Data.ItemNames[275616] = "Scalegut Clenchers"
ES.Data.ItemNames[275617] = "Scalegut Belt"
ES.Data.ItemNames[275618] = "Scalegut Treaders"
ES.Data.ItemNames[275619] = "Broodwatcher's Clenchers"
ES.Data.ItemNames[275620] = "Broodwatcher's Belt"
ES.Data.ItemNames[275621] = "Broodwatcher's Treaders"
ES.Data.ItemNames[276538] = "Spiritcaller Kilt"
ES.Data.ItemNames[276539] = "Spiritcaller Gloves"
ES.Data.ItemNames[276540] = "Spiritcaller Mantle"
ES.Data.ItemNames[276541] = "Spiritcaller Boots"
ES.Data.ItemNames[276998] = "Cloudy Gustwoven Harness"
ES.Data.ItemNames[276999] = "Cloudy Gustwoven Bracers"
ES.Data.ItemNames[277000] = "Cloudy Gustwoven Gloves"
ES.Data.ItemNames[277001] = "Cloudy Gustwoven Belt"
ES.Data.ItemNames[277002] = "Cloudy Gustwoven Trousers"
ES.Data.ItemNames[277003] = "Cloudy Gustwoven Boots"
ES.Data.ItemNames[277004] = "Cloudy Windraveled Jerkin"
ES.Data.ItemNames[277005] = "Cloudy Windraveled Armguards"
ES.Data.ItemNames[277006] = "Cloudy Windraveled Mitts"
ES.Data.ItemNames[277007] = "Cloudy Windraveled Strap"
ES.Data.ItemNames[277008] = "Cloudy Windraveled Pants"
ES.Data.ItemNames[277009] = "Cloudy Windraveled Footwraps"
ES.Data.ItemNames[277022] = "Azure Gustwoven Harness"
ES.Data.ItemNames[277023] = "Azure Gustwoven Bracers"
ES.Data.ItemNames[277024] = "Azure Gustwoven Gloves"
ES.Data.ItemNames[277025] = "Azure Gustwoven Belt"
ES.Data.ItemNames[277026] = "Azure Gustwoven Trousers"
ES.Data.ItemNames[277027] = "Azure Gustwoven Boots"
ES.Data.ItemNames[277028] = "Azure Windraveled Jerkin"
ES.Data.ItemNames[277029] = "Azure Windraveled Armguards"
ES.Data.ItemNames[277030] = "Azure Windraveled Mitts"
ES.Data.ItemNames[277031] = "Azure Windraveled Strap"
ES.Data.ItemNames[277032] = "Azure Windraveled Pants"
ES.Data.ItemNames[277033] = "Azure Windraveled Footwraps"
ES.Data.ItemNames[277042] = "Cloudy Gustwoven Hood"
ES.Data.ItemNames[277043] = "Cloudy Gustwoven Spaulders"
ES.Data.ItemNames[277044] = "Cloudy Windraveled Cover"
ES.Data.ItemNames[277045] = "Cloudy Windraveled Drapes"
ES.Data.ItemNames[277050] = "Azure Gustwoven Hood"
ES.Data.ItemNames[277051] = "Azure Gustwoven Spaulders"
ES.Data.ItemNames[277052] = "Azure Windraveled Cover"
ES.Data.ItemNames[277053] = "Azure Windraveled Drapes"
ES.Data.ItemNames[277715] = "Light Leather Reagent Bag"
ES.Data.ItemNames[279252] = "Elderwild Waistcord"
ES.Data.ItemNames[279253] = "Outlaw's Collar"
ES.Data.ItemNames[279254] = "Elderwild Pants"
ES.Data.ItemNames[279255] = "Eternity Pauldrons"
ES.Data.ItemNames[279256] = "Tranquil Wristguards"
ES.Data.ItemNames[279257] = "Mourning Handguards"
ES.Data.ItemNames[279258] = "Wild Leather Armor Kit"
ES.Data.ItemNames[279941] = "Tanning Rack"
ES.Data.ItemNames[279978] = "Camp Tent"

-- Material -> profesión de recolección que lo consigue (393 Desuello, 182 Herboristería, 186 Minería).
-- Sin uso por ahora: reservado para la vía "Vender en bruto" de Ganar dinero (docs/PLAN.md, G1).
ES.Data.GatheredBy = ES.Data.GatheredBy or {}
ES.Data.GatheredBy[783] = 393
ES.Data.GatheredBy[2318] = 393
ES.Data.GatheredBy[2319] = 393
ES.Data.GatheredBy[2934] = 393
ES.Data.GatheredBy[3356] = 182
ES.Data.GatheredBy[4232] = 393
ES.Data.GatheredBy[4234] = 393
ES.Data.GatheredBy[4235] = 393
ES.Data.GatheredBy[4304] = 393
ES.Data.GatheredBy[4461] = 393
ES.Data.GatheredBy[5082] = 393
ES.Data.GatheredBy[5116] = 393
ES.Data.GatheredBy[5784] = 393
ES.Data.GatheredBy[5785] = 393
ES.Data.GatheredBy[6470] = 393
ES.Data.GatheredBy[6471] = 393
ES.Data.GatheredBy[7286] = 393
ES.Data.GatheredBy[7287] = 393
ES.Data.GatheredBy[7392] = 393
ES.Data.GatheredBy[7428] = 393
ES.Data.GatheredBy[8150] = 186
ES.Data.GatheredBy[8153] = 182
ES.Data.GatheredBy[8154] = 393
ES.Data.GatheredBy[8165] = 393
ES.Data.GatheredBy[8167] = 393
ES.Data.GatheredBy[8168] = 393
ES.Data.GatheredBy[8169] = 393
ES.Data.GatheredBy[8170] = 393
ES.Data.GatheredBy[8171] = 393
ES.Data.GatheredBy[8368] = 393
ES.Data.GatheredBy[12607] = 393
ES.Data.GatheredBy[12809] = 186
ES.Data.GatheredBy[15408] = 393
ES.Data.GatheredBy[15409] = 393
ES.Data.GatheredBy[15410] = 393
ES.Data.GatheredBy[15412] = 393
ES.Data.GatheredBy[15414] = 393
ES.Data.GatheredBy[15415] = 393
ES.Data.GatheredBy[15416] = 393
ES.Data.GatheredBy[15417] = 393
ES.Data.GatheredBy[15419] = 393
ES.Data.GatheredBy[15420] = 393
ES.Data.GatheredBy[15422] = 393
ES.Data.GatheredBy[15423] = 393
ES.Data.GatheredBy[17012] = 393
ES.Data.GatheredBy[19726] = 182
ES.Data.GatheredBy[19767] = 393
ES.Data.GatheredBy[19768] = 393
ES.Data.GatheredBy[20381] = 393
ES.Data.GatheredBy[20498] = 393
ES.Data.GatheredBy[20500] = 393
ES.Data.GatheredBy[20501] = 393
ES.Data.GatheredBy[213370] = 393
ES.Data.GatheredBy[248824] = 393
ES.Data.GatheredBy[248825] = 393
ES.Data.GatheredBy[249427] = 393
ES.Data.GatheredBy[249428] = 393
ES.Data.GatheredBy[249429] = 393

```

---

## Tailoring

```lua
-- Generado por tools/gen_profession.py (Tailoring). No editar a mano.
-- Datos: cliente de WoW Forever (wago.tools DB2), instructores de CMaNGOS classic-db, vendedores de QuestieDB.
local _, ES = ...
ES.Data = ES.Data or {}

-- t = { naranja, amarilla, verde, gris }; fee/train = precio y habilidad del instructor
-- (sin fee = se aprende de pergamino: de dónde sale, en Data/Sources.lua; scrollPrice = su precio si lo vende un PNJ)
-- rep = { facción, nivel } que pide el pergamino para aprenderla (5 amistoso, 6 honorable, 7 venerado, 8 exaltado)
-- r = { {itemID, cantidad} }; out = { itemID, cantidad }
-- sq / oq = calidad del pergamino / de lo fabricado (0 pobre, 1 común, 2 poco común, 3 raro, 4 épico)
-- faction = bando que puede aprenderla, si solo es de uno
-- bop = lo fabricado se liga al recogerlo: no se puede vender en la AH (sí al vendedor)
-- favor / favorRep = se compra con Merchant's Favor en el campamento de tu bando, y la reputación que pide
-- train ajustado a Forever: nivel de Classic menos lo que Forever bajó la amarilla de esa receta
-- basic = se aprende sola al coger la profesión; trainer = de instructor sin precio conocido
--   (receta nueva de Forever que no está en CMaNGOS: se aprende al ponerse amarilla)
ES.Data.Tailoring = {
  skillLine = 197,
  ranks = { -- { tope, precio, habilidad requerida, nivel de personaje }
    { 150, 450, 50, 10 },
    { 225, 4500, 125, 20 },
    { 300, 50000, 200, 0 },
  },
  -- { PNJ instructor, rangos que enseña: 1 aprendiz (75), 2 oficial (150), 4 experto (225), 8 artesano (300) }
  trainers = { { 1103, 1 }, { 1300, 1 }, { 1346, 4 }, { 1703, 1 }, { 2399, 8 }, { 2627, 2 }, { 2855, 1 }, { 3004, 2 }, { 3363, 2 }, { 3484, 1 }, { 3523, 1 }, { 3704, 2 }, { 4159, 2 }, { 4193, 1 }, { 4576, 4 }, { 5153, 2 }, { 5567, 2 }, { 11048, 1 }, { 11049, 2 }, { 11050, 1 }, { 11051, 1 }, { 11052, 8 }, { 251972, 2 }, { 251991, 3 }, { 252380, 3 } },
  recipes = {
    [2385] = { name = "Brown Linen Vest", t = { 1, 45, 57, 70 }, fee = 50, train = 10, r = { { 2996, 1 }, { 2320, 1 } }, out = { 2568, 1 }, oq = 1 },
    [2386] = { name = "Linen Boots", t = { 1, 65, 82, 100 }, fee = 200, train = 40, r = { { 2996, 3 }, { 2320, 1 }, { 2318, 1 } }, out = { 2569, 1 }, oq = 2 },
    [2387] = { name = "Linen Cloak", t = { 1, 35, 47, 60 }, basic = true, r = { { 2996, 1 }, { 2320, 1 } }, out = { 2570, 1 }, oq = 1 },
    [2389] = { name = "Red Linen Robe", t = { 1, 50, 67, 85 }, scroll = 2598, train = 25, sq = 2, r = { { 2996, 3 }, { 2320, 2 }, { 2604, 2 } }, out = { 2572, 1 }, oq = 2 },
    [2392] = { name = "Red Linen Shirt", t = { 1, 50, 67, 85 }, fee = 50, train = 25, r = { { 2996, 2 }, { 2320, 1 }, { 2604, 1 } }, out = { 2575, 1 }, oq = 1 },
    [2393] = { name = "White Linen Shirt", t = { 1, 35, 47, 60 }, fee = 25, train = 1, r = { { 2996, 1 }, { 2320, 1 }, { 2324, 1 } }, out = { 2576, 1 }, oq = 1 },
    [2394] = { name = "Blue Linen Shirt", t = { 1, 50, 67, 85 }, fee = 50, train = 25, r = { { 2996, 2 }, { 2320, 1 }, { 6260, 1 } }, out = { 2577, 1 }, oq = 1 },
    [2395] = { name = "Barbaric Linen Vest", t = { 1, 65, 82, 100 }, fee = 300, train = 40, r = { { 2996, 4 }, { 2318, 1 }, { 2321, 1 } }, out = { 2578, 1 }, oq = 2 },
    [2396] = { name = "Green Linen Shirt", t = { 1, 65, 82, 100 }, fee = 200, train = 40, r = { { 2996, 3 }, { 2321, 1 }, { 2605, 1 } }, out = { 2579, 1 }, oq = 1 },
    [2397] = { name = "Reinforced Linen Cape", t = { 1, 60, 77, 95 }, fee = 200, train = 35, r = { { 2996, 2 }, { 2320, 3 } }, out = { 2580, 1 }, oq = 2 },
    [2399] = { name = "Green Woolen Vest", t = { 1, 85, 102, 120 }, fee = 300, train = 60, r = { { 2997, 2 }, { 2321, 2 }, { 2605, 1 } }, out = { 2582, 1 }, oq = 2 },
    [2401] = { name = "Woolen Boots", t = { 1, 95, 112, 130 }, fee = 300, train = 70, r = { { 2997, 4 }, { 2321, 2 }, { 2318, 2 } }, out = { 2583, 1 }, oq = 2 },
    [2402] = { name = "Woolen Cape", t = { 1, 80, 97, 115 }, fee = 250, train = 55, r = { { 2997, 1 }, { 2321, 1 } }, out = { 2584, 1 }, oq = 2 },
    [2403] = { name = "Gray Woolen Robe", t = { 1, 105, 122, 140 }, scroll = 2601, train = 80, sq = 2, r = { { 2997, 4 }, { 2321, 3 }, { 4340, 1 } }, out = { 2585, 1 }, oq = 2 },
    [2406] = { name = "Gray Woolen Shirt", t = { 1, 90, 100, 110 }, fee = 200, train = 80, r = { { 2997, 2 }, { 2321, 1 }, { 4340, 1 } }, out = { 2587, 1 }, oq = 1 },
    [2963] = { name = "Bolt of Linen Cloth", t = { 1, 25, 37, 50 }, basic = true, r = { { 2589, 2 } }, out = { 2996, 1 }, oq = 1 },
    [2964] = { name = "Bolt of Woolen Cloth", t = { 1, 70, 77, 85 }, fee = 100, train = 55, r = { { 2592, 3 } }, out = { 2997, 1 }, oq = 1 },
    [3755] = { name = "Linen Bag", t = { 1, 30, 47, 65 }, basic = true, r = { { 2996, 3 }, { 2320, 3 } }, out = { 4238, 1 }, oq = 1 },
    [3757] = { name = "Woolen Bag", t = { 1, 75, 92, 110 }, fee = 200, train = 50, r = { { 2997, 3 }, { 2321, 1 } }, out = { 4240, 1 }, oq = 1 },
    [3758] = { name = "Green Woolen Bag", t = { 1, 100, 117, 135 }, scroll = 4292, train = 75, sq = 2, r = { { 2997, 5 }, { 2605, 1 }, { 2321, 1 } }, out = { 4241, 1 }, oq = 1 },
    [3813] = { name = "Small Silk Pack", t = { 1, 145, 160, 175 }, fee = 800, train = 125, r = { { 4305, 3 }, { 4234, 2 }, { 2321, 3 } }, out = { 4245, 1 }, oq = 1 },
    [3839] = { name = "Bolt of Silk Cloth", t = { 1, 110, 115, 120 }, fee = 500, train = 100, r = { { 4306, 4 } }, out = { 4305, 1 }, oq = 1 },
    [3840] = { name = "Heavy Linen Gloves", t = { 1, 50, 67, 85 }, fee = 100, train = 25, r = { { 2996, 2 }, { 2320, 1 } }, out = { 4307, 1 }, oq = 2 },
    [3841] = { name = "Green Linen Bracers", t = { 1, 60, 77, 95 }, fee = 200, train = 35, r = { { 2996, 3 }, { 2320, 2 }, { 2605, 1 } }, out = { 4308, 1 }, oq = 2 },
    [3842] = { name = "Handstitched Linen Britches", t = { 1, 70, 87, 105 }, fee = 300, train = 45, r = { { 2996, 4 }, { 2321, 2 } }, out = { 4309, 1 }, oq = 2 },
    [3843] = { name = "Heavy Woolen Gloves", t = { 1, 85, 102, 120 }, fee = 400, train = 60, r = { { 2997, 3 }, { 2321, 1 } }, out = { 4310, 1 }, oq = 2 },
    [3844] = { name = "Heavy Woolen Cloak", t = { 1, 105, 122, 140 }, scroll = 4346, train = 80, sq = 2, r = { { 2997, 3 }, { 2321, 2 }, { 5498, 2 } }, out = { 4311, 1 }, oq = 2 },
    [3845] = { name = "Soft-soled Linen Boots", t = { 1, 80, 97, 115 }, fee = 300, train = 55, r = { { 2996, 5 }, { 2318, 2 }, { 2321, 1 } }, out = { 4312, 1 }, oq = 2 },
    [3847] = { name = "Red Woolen Boots", t = { 1, 80, 97, 115 }, scroll = 4345, train = 75, sq = 2, r = { { 2997, 4 }, { 2318, 2 }, { 2321, 1 }, { 2604, 2 } }, out = { 4313, 1 }, oq = 2 },
    [3848] = { name = "Double-stitched Woolen Shoulders", t = { 1, 110, 127, 145 }, fee = 500, train = 85, r = { { 2997, 3 }, { 2321, 2 } }, out = { 4314, 1 }, oq = 2 },
    [3849] = { name = "Reinforced Woolen Shoulders", t = { 1, 120, 137, 155 }, scroll = 4347, train = 95, sq = 2, r = { { 2997, 6 }, { 2319, 2 }, { 2321, 2 } }, out = { 4315, 1 }, oq = 2 },
    [3850] = { name = "Heavy Woolen Pants", t = { 1, 110, 127, 145 }, fee = 500, train = 85, r = { { 2997, 5 }, { 2321, 4 } }, out = { 4316, 1 }, oq = 2 },
    [3851] = { name = "Phoenix Pants", t = { 1, 125, 142, 160 }, scroll = 4349, train = 100, sq = 2, r = { { 2997, 6 }, { 5500, 1 }, { 2321, 3 } }, out = { 4317, 1 }, oq = 2 },
    [3852] = { name = "Gloves of Meditation", t = { 1, 125, 140, 155 }, fee = 750, train = 105, r = { { 2997, 4 }, { 2321, 3 }, { 3383, 1 } }, out = { 4318, 1 }, oq = 2 },
    [3854] = { name = "Azure Silk Gloves", t = { 1, 140, 155, 170 }, scroll = 7114, train = 120, scrollPrice = 1000, sq = 1, r = { { 4305, 3 }, { 4234, 2 }, { 6260, 2 }, { 2321, 2 } }, out = { 4319, 1 }, oq = 2 },
    [3855] = { name = "Spidersilk Boots", t = { 1, 125, 142, 160 }, fee = 750, train = 100, r = { { 4305, 2 }, { 2319, 4 }, { 3182, 4 }, { 5500, 1 } }, out = { 4320, 1 }, oq = 3 },
    [3856] = { name = "Spider Silk Slippers", t = { 1, 135, 147, 160 }, scroll = 4350, train = 115, sq = 2, r = { { 4305, 3 }, { 3182, 1 }, { 2321, 2 } }, out = { 4321, 1 }, oq = 2 },
    [3857] = { name = "Enchanter's Cowl", t = { 1, 150, 165, 180 }, scroll = 14630, train = 130, scrollPrice = 1000, sq = 1, r = { { 4305, 3 }, { 2321, 2 }, { 4337, 2 } }, out = { 4322, 1 }, oq = 2 },
    [3858] = { name = "Shadow Hood", t = { 1, 155, 170, 185 }, scroll = 4351, train = 135, sq = 2, r = { { 4305, 4 }, { 4291, 1 }, { 3824, 1 } }, out = { 4323, 1 }, oq = 2 },
    [3859] = { name = "Azure Silk Vest", t = { 1, 145, 160, 175 }, fee = 750, train = 125, r = { { 4305, 5 }, { 6260, 4 } }, out = { 4324, 1 }, oq = 2 },
    [3860] = { name = "Boots of the Enchanter", t = { 1, 160, 175, 190 }, scroll = 4352, train = 140, sq = 2, r = { { 4305, 4 }, { 4291, 1 }, { 4337, 2 } }, out = { 4325, 1 }, oq = 2 },
    [3861] = { name = "Long Silken Cloak", t = { 1, 170, 185, 200 }, fee = 900, train = 150, r = { { 4305, 4 }, { 3827, 1 }, { 4291, 1 } }, out = { 4326, 1 }, oq = 2 },
    [3862] = { name = "Icy Cloak", t = { 1, 185, 200, 215 }, scroll = 4355, train = 165, scrollPrice = 1500, sq = 1, r = { { 4339, 3 }, { 4291, 2 }, { 3829, 1 }, { 4337, 2 } }, out = { 4327, 1 }, oq = 3 },
    [3863] = { name = "Spider Belt", t = { 1, 165, 180, 195 }, scroll = 4353, train = 145, sq = 2, r = { { 4305, 4 }, { 4337, 2 }, { 7071, 1 } }, out = { 4328, 1 }, oq = 2 },
    [3864] = { name = "Star Belt", t = { 1, 185, 200, 215 }, scroll = 4356, train = 165, sq = 2, r = { { 4339, 4 }, { 4234, 4 }, { 3864, 1 }, { 7071, 1 }, { 4291, 1 } }, out = { 4329, 1 }, oq = 2 },
    [3865] = { name = "Bolt of Mageweave", t = { 1, 145, 147, 150 }, fee = 1000, train = 140, r = { { 4338, 5 } }, out = { 4339, 1 }, oq = 1 },
    [3866] = { name = "Stylish Red Shirt", t = { 1, 110, 127, 145 }, fee = 250, train = 85, r = { { 2997, 3 }, { 2604, 2 }, { 2321, 1 } }, out = { 4330, 1 }, oq = 1 },
    [3868] = { name = "Phoenix Gloves", t = { 1, 125, 142, 160 }, scroll = 4348, train = 100, sq = 2, r = { { 2997, 4 }, { 5500, 1 }, { 2321, 4 }, { 2324, 2 } }, out = { 4331, 1 }, oq = 2 },
    [3869] = { name = "Bright Yellow Shirt", t = { 1, 120, 125, 130 }, scroll = 14627, train = 110, scrollPrice = 800, sq = 1, r = { { 4305, 1 }, { 4341, 1 }, { 2321, 1 } }, out = { 4332, 1 }, oq = 1 },
    [3870] = { name = "Dark Silk Shirt", t = { 1, 130, 135, 140 }, scroll = 6401, train = 120, scrollPrice = 1100, sq = 1, r = { { 4305, 2 }, { 4340, 2 }, { 2321, 1 } }, out = { 4333, 1 }, oq = 1 },
    [3871] = { name = "Formal White Shirt", t = { 1, 145, 150, 155 }, fee = 450, train = 135, r = { { 4305, 3 }, { 2324, 2 }, { 2321, 1 } }, out = { 4334, 1 }, oq = 1 },
    [3872] = { name = "Rich Purple Silk Shirt", t = { 1, 160, 165, 170 }, scroll = 4354, train = 150, sq = 3, r = { { 4305, 4 }, { 4342, 1 }, { 4291, 1 } }, out = { 4335, 1 }, oq = 1 },
    [3873] = { name = "Black Swashbuckler's Shirt", t = { 1, 175, 180, 185 }, scroll = 10728, train = 165, scrollPrice = 1500, sq = 1, r = { { 4305, 5 }, { 2325, 1 }, { 4291, 1 } }, out = { 4336, 1 }, oq = 1 },
    [3914] = { name = "Brown Linen Pants", t = { 1, 50, 67, 85 }, fee = 50, train = 25, r = { { 2996, 2 }, { 2320, 1 } }, out = { 4343, 1 }, oq = 2 },
    [3915] = { name = "Brown Linen Shirt", t = { 1, 35, 47, 60 }, basic = true, r = { { 2996, 1 }, { 2320, 1 } }, out = { 4344, 1 }, oq = 1 },
    [6521] = { name = "Pearl-clasped Cloak", t = { 1, 95, 112, 130 }, fee = 400, train = 70, r = { { 2997, 3 }, { 2321, 2 }, { 5498, 1 } }, out = { 5542, 1 }, oq = 2 },
    [6686] = { name = "Red Linen Bag", t = { 1, 75, 92, 110 }, scroll = 5771, train = 50, scrollPrice = 200, sq = 1, r = { { 2996, 4 }, { 2321, 1 }, { 2604, 1 } }, out = { 5762, 1 }, oq = 1 },
    [6688] = { name = "Red Woolen Bag", t = { 1, 115, 132, 150 }, scroll = 5772, train = 90, scrollPrice = 500, sq = 1, r = { { 2997, 5 }, { 2604, 1 }, { 2321, 1 } }, out = { 5763, 1 }, oq = 1 },
    [6690] = { name = "Lesser Wizard's Robe", t = { 1, 130, 145, 160 }, fee = 1000, train = 110, r = { { 4305, 2 }, { 2321, 2 }, { 3182, 2 } }, out = { 5766, 1 }, oq = 2 },
    [6692] = { name = "Robes of Arcana", t = { 1, 145, 160, 175 }, scroll = 5773, train = 125, sq = 2, r = { { 4305, 4 }, { 2321, 2 }, { 3182, 2 } }, out = { 5770, 1 }, oq = 2 },
    [6693] = { name = "Green Silk Pack", t = { 1, 160, 175, 190 }, scroll = 5774, train = 140, sq = 2, r = { { 4305, 5 }, { 4234, 3 }, { 2321, 3 }, { 2605, 1 } }, out = { 5764, 1 }, oq = 1 },
    [6695] = { name = "Black Silk Pack", t = { 1, 170, 185, 200 }, scroll = 5775, train = 150, sq = 2, r = { { 4305, 6 }, { 2325, 1 }, { 2321, 4 } }, out = { 5765, 1 }, oq = 1 },
    [7623] = { name = "Brown Linen Robe", t = { 1, 50, 67, 85 }, fee = 50, train = 25, r = { { 2996, 3 }, { 2320, 1 } }, out = { 6238, 1 }, oq = 2 },
    [7624] = { name = "White Linen Robe", t = { 1, 50, 67, 85 }, fee = 50, train = 25, r = { { 2996, 3 }, { 2320, 1 }, { 2324, 1 } }, out = { 6241, 1 }, oq = 2 },
    [7629] = { name = "Red Linen Vest", t = { 1, 60, 77, 95 }, scroll = 6271, train = 35, sq = 2, r = { { 2996, 3 }, { 2320, 1 }, { 2604, 1 } }, out = { 6239, 1 }, oq = 2 },
    [7630] = { name = "Blue Linen Vest", t = { 1, 60, 77, 95 }, scroll = 6270, train = 35, scrollPrice = 200, sq = 1, r = { { 2996, 3 }, { 2320, 1 }, { 6260, 1 } }, out = { 6240, 1 }, oq = 2 },
    [7633] = { name = "Blue Linen Robe", t = { 1, 70, 87, 105 }, scroll = 6272, train = 45, scrollPrice = 300, sq = 1, r = { { 2996, 4 }, { 2320, 2 }, { 6260, 2 } }, out = { 6242, 1 }, oq = 2 },
    [7636] = { name = "Green Woolen Robe", t = { 1, 90, 107, 125 }, scroll = 6273, train = 80, sq = 1, r = { { 2997, 3 }, { 2321, 2 }, { 2605, 1 } }, out = { 6243, 1 }, oq = 2 },
    [7639] = { name = "Blue Overalls", t = { 1, 100, 117, 135 }, scroll = 6274, train = 75, scrollPrice = 400, sq = 1, r = { { 2997, 4 }, { 2321, 2 }, { 6260, 2 } }, out = { 6263, 1 }, oq = 2 },
    [7643] = { name = "Greater Adept's Robe", t = { 1, 115, 132, 150 }, scroll = 6275, train = 90, scrollPrice = 800, sq = 1, r = { { 2997, 5 }, { 2321, 3 }, { 2604, 3 } }, out = { 6264, 1 }, oq = 2 },
    [7892] = { name = "Stylish Blue Shirt", t = { 1, 120, 137, 155 }, scroll = 6390, train = 95, sq = 2, r = { { 2997, 4 }, { 6260, 2 }, { 4340, 1 }, { 2321, 1 } }, out = { 6384, 1 }, oq = 1 },
    [7893] = { name = "Stylish Green Shirt", t = { 1, 120, 137, 155 }, scroll = 6391, train = 95, sq = 2, r = { { 2997, 4 }, { 2605, 2 }, { 4340, 1 }, { 2321, 1 } }, out = { 6385, 1 }, oq = 1 },
    [8465] = { name = "Simple Dress", t = { 1, 50, 67, 85 }, fee = 50, train = 25, r = { { 2996, 2 }, { 2320, 1 }, { 6260, 1 }, { 2324, 1 } }, out = { 6786, 1 }, oq = 1 },
    [8467] = { name = "White Woolen Dress", t = { 1, 110, 127, 145 }, fee = 250, train = 85, r = { { 2997, 3 }, { 2324, 4 }, { 2321, 1 } }, out = { 6787, 1 }, oq = 2 },
    [8483] = { name = "White Swashbuckler's Shirt", t = { 1, 135, 140, 145 }, fee = 450, train = 125, r = { { 4305, 3 }, { 2324, 2 }, { 4291, 1 } }, out = { 6795, 1 }, oq = 1 },
    [8489] = { name = "Red Swashbuckler's Shirt", t = { 1, 150, 155, 160 }, fee = 750, train = 140, r = { { 4305, 3 }, { 2604, 2 }, { 4291, 1 } }, out = { 6796, 1 }, oq = 1 },
    [8758] = { name = "Azure Silk Pants", t = { 1, 135, 150, 165 }, fee = 600, train = 115, r = { { 4305, 4 }, { 6260, 2 }, { 2321, 3 } }, out = { 7046, 1 }, oq = 2 },
    [8760] = { name = "Azure Silk Hood", t = { 1, 130, 135, 140 }, fee = 600, train = 120, r = { { 4305, 2 }, { 6260, 2 }, { 2321, 1 } }, out = { 7048, 1 }, oq = 2 },
    [8762] = { name = "Silk Headband", t = { 1, 135, 140, 145 }, fee = 750, train = 125, r = { { 4305, 3 }, { 2321, 2 } }, out = { 7050, 1 }, oq = 2 },
    [8764] = { name = "Earthen Vest", t = { 1, 155, 170, 185 }, fee = 810, train = 135, r = { { 4305, 3 }, { 7067, 1 }, { 2321, 2 } }, out = { 7051, 1 }, oq = 2 },
    [8766] = { name = "Azure Silk Belt", t = { 1, 160, 175, 190 }, fee = 900, train = 140, r = { { 4305, 4 }, { 7070, 1 }, { 6260, 2 }, { 2321, 2 }, { 7071, 1 } }, out = { 7052, 1 }, oq = 2 },
    [8770] = { name = "Robe of Power", t = { 1, 175, 190, 205 }, fee = 900, train = 155, r = { { 4339, 2 }, { 7067, 2 }, { 7070, 2 }, { 7068, 2 }, { 7069, 2 }, { 4291, 2 } }, out = { 7054, 1 }, oq = 3, bop = true },
    [8772] = { name = "Crimson Silk Belt", t = { 1, 160, 175, 190 }, fee = 900, train = 140, r = { { 4305, 4 }, { 7071, 1 }, { 2604, 2 }, { 4291, 1 } }, out = { 7055, 1 }, oq = 2 },
    [8774] = { name = "Green Silken Shoulders", t = { 1, 165, 180, 195 }, fee = 900, train = 145, r = { { 4305, 5 }, { 4291, 2 } }, out = { 7057, 1 }, oq = 2 },
    [8776] = { name = "Linen Belt", t = { 1, 50, 67, 85 }, fee = 50, train = 15, r = { { 2996, 1 }, { 2320, 1 } }, out = { 7026, 1 }, oq = 1 },
    [8778] = { name = "Boots of Darkness", t = { 1, 135, 150, 165 }, scroll = 7093, train = 125, sq = 1, r = { { 4305, 3 }, { 2319, 2 }, { 6048, 1 }, { 2321, 2 } }, out = { 7027, 1 }, oq = 2 },
    [8780] = { name = "Hands of Darkness", t = { 1, 140, 155, 170 }, scroll = 7092, train = 120, sq = 2, r = { { 4305, 3 }, { 4234, 2 }, { 6048, 2 }, { 2321, 2 } }, out = { 7047, 1 }, oq = 2 },
    [8782] = { name = "Truefaith Gloves", t = { 1, 145, 160, 175 }, scroll = 7091, train = 125, sq = 2, r = { { 4305, 3 }, { 4234, 2 }, { 929, 4 }, { 2321, 1 } }, out = { 7049, 1 }, oq = 2 },
    [8784] = { name = "Green Silk Armor", t = { 1, 150, 165, 180 }, scroll = 7090, train = 130, sq = 2, r = { { 4305, 5 }, { 2605, 2 }, { 4291, 1 } }, out = { 7065, 1 }, oq = 2 },
    [8786] = { name = "Azure Silk Cloak", t = { 1, 160, 175, 190 }, scroll = 7089, train = 140, scrollPrice = 1500, sq = 1, r = { { 4305, 3 }, { 6260, 2 }, { 2321, 2 } }, out = { 7053, 1 }, oq = 2 },
    [8789] = { name = "Crimson Silk Cloak", t = { 1, 165, 180, 195 }, scroll = 7087, train = 145, scrollPrice = 1200, sq = 1, r = { { 4305, 5 }, { 2604, 2 }, { 6371, 2 }, { 4291, 1 } }, out = { 7056, 1 }, oq = 2 },
    [8791] = { name = "Crimson Silk Vest", t = { 1, 170, 180, 190 }, fee = 2250, train = 150, r = { { 4305, 4 }, { 2604, 2 }, { 2321, 2 } }, out = { 7058, 1 }, oq = 2 },
    [8793] = { name = "Crimson Silk Shoulders", t = { 1, 175, 190, 205 }, scroll = 7084, train = 155, sq = 2, r = { { 4305, 5 }, { 6371, 2 }, { 2604, 2 }, { 4291, 2 } }, out = { 7059, 1 }, oq = 2 },
    [8795] = { name = "Azure Shoulders", t = { 1, 175, 190, 205 }, scroll = 7085, train = 155, sq = 2, r = { { 4305, 6 }, { 7072, 2 }, { 6260, 2 }, { 4291, 2 } }, out = { 7060, 1 }, oq = 2 },
    [8797] = { name = "Earthen Silk Belt", t = { 1, 180, 195, 210 }, scroll = 7086, train = 160, sq = 2, r = { { 4305, 5 }, { 7067, 4 }, { 4234, 4 }, { 7071, 1 }, { 4291, 2 } }, out = { 7061, 1 }, oq = 2 },
    [8799] = { name = "Crimson Silk Pantaloons", t = { 1, 180, 190, 200 }, fee = 3000, train = 160, r = { { 4305, 4 }, { 2604, 2 }, { 4291, 2 } }, out = { 7062, 1 }, oq = 2 },
    [8802] = { name = "Crimson Silk Robe", t = { 1, 185, 200, 215 }, scroll = 7088, train = 170, scrollPrice = 5000, sq = 1, r = { { 4305, 8 }, { 7068, 4 }, { 3827, 2 }, { 2604, 4 }, { 4291, 1 } }, out = { 7063, 1 }, oq = 2 },
    [8804] = { name = "Crimson Silk Gloves", t = { 1, 190, 205, 220 }, fee = 4500, train = 175, r = { { 4305, 6 }, { 7068, 2 }, { 6371, 2 }, { 4304, 2 }, { 2604, 4 }, { 4291, 2 } }, out = { 7064, 1 }, oq = 2 },
    [12044] = { name = "Simple Linen Pants", t = { 1, 40, 50, 60 }, basic = true, r = { { 2996, 1 }, { 2320, 1 } }, out = { 10045, 1 }, oq = 1 },
    [12045] = { name = "Simple Linen Boots", t = { 1, 50, 67, 85 }, fee = 50, train = 20, r = { { 2996, 2 }, { 2318, 1 }, { 2320, 1 } }, out = { 10046, 1 }, oq = 1 },
    [12046] = { name = "Simple Kilt", t = { 1, 75, 92, 110 }, fee = 300, train = 50, r = { { 2996, 4 }, { 2321, 1 } }, out = { 10047, 1 }, oq = 2 },
    [12047] = { name = "Colorful Kilt", t = { 1, 95, 112, 130 }, scroll = 10316, train = 70, sq = 2, r = { { 2997, 5 }, { 2604, 3 }, { 2321, 1 } }, out = { 10048, 1 }, oq = 2 },
    [12048] = { name = "Black Mageweave Vest", t = { 1, 185, 200, 215 }, fee = 3600, train = 170, r = { { 4339, 2 }, { 4291, 3 } }, out = { 9998, 1 }, oq = 2 },
    [12049] = { name = "Black Mageweave Leggings", t = { 1, 185, 200, 215 }, fee = 4000, train = 170, r = { { 4339, 2 }, { 4291, 3 } }, out = { 9999, 1 }, oq = 2 },
    [12050] = { name = "Black Mageweave Robe", t = { 1, 190, 205, 220 }, fee = 3600, train = 175, r = { { 4339, 3 }, { 8343, 1 } }, out = { 10001, 1 }, oq = 2 },
    [12052] = { name = "Shadoweave Pants", t = { 1, 190, 205, 220 }, fee = 5000, train = 175, tr = { 9584 }, r = { { 4339, 3 }, { 10285, 2 }, { 8343, 1 } }, out = { 10002, 1 }, oq = 2 },
    [12053] = { name = "Black Mageweave Gloves", t = { 1, 195, 210, 225 }, fee = 5000, train = 180, r = { { 4339, 2 }, { 8343, 2 } }, out = { 10003, 1 }, oq = 2 },
    [12055] = { name = "Shadoweave Robe", t = { 1, 195, 210, 225 }, fee = 5500, train = 180, tr = { 9584 }, r = { { 4339, 3 }, { 10285, 2 }, { 8343, 1 } }, out = { 10004, 1 }, oq = 2 },
    [12056] = { name = "Red Mageweave Vest", t = { 1, 195, 210, 225 }, scroll = 10300, train = 180, sq = 2, r = { { 4339, 3 }, { 2604, 2 }, { 8343, 1 } }, out = { 10007, 1 }, oq = 2 },
    [12059] = { name = "White Bandit Mask", t = { 1, 185, 190, 195 }, scroll = 10301, train = 180, sq = 2, r = { { 4339, 1 }, { 2324, 1 }, { 8343, 1 } }, out = { 10008, 1 }, oq = 2 },
    [12060] = { name = "Red Mageweave Pants", t = { 1, 195, 210, 225 }, scroll = 10302, train = 180, sq = 2, r = { { 4339, 3 }, { 2604, 2 }, { 8343, 1 } }, out = { 10009, 1 }, oq = 2 },
    [12061] = { name = "Orange Mageweave Shirt", t = { 1, 185, 190, 195 }, fee = 2250, train = 180, r = { { 4339, 1 }, { 6261, 1 }, { 8343, 1 } }, out = { 10056, 1 }, oq = 1 },
    [12062] = { name = "Stormcloth Pants", t = { 1, 200, 215, 230 }, scroll = 254681, train = 185, sq = 2, r = { { 4339, 4 }, { 7079, 2 }, { 8343, 2 } }, out = { 10010, 1 }, oq = 2 },
    [12063] = { name = "Stormcloth Gloves", t = { 1, 200, 215, 230 }, scroll = 254682, train = 185, scrollPrice = 6875, sq = 2, r = { { 4339, 3 }, { 7079, 2 }, { 8343, 2 } }, out = { 10011, 1 }, oq = 2 },
    [12064] = { name = "Orange Martial Shirt", t = { 1, 190, 195, 200 }, scroll = 10311, train = 185, scrollPrice = 3000, sq = 1, r = { { 4339, 2 }, { 6261, 2 }, { 8343, 1 } }, out = { 10052, 1 }, oq = 1 },
    [12065] = { name = "Mageweave Bag", t = { 1, 205, 220, 235 }, fee = 5000, train = 190, r = { { 4339, 4 }, { 4291, 2 } }, out = { 10050, 1 }, oq = 1 },
    [12066] = { name = "Red Mageweave Gloves", t = { 1, 205, 220, 235 }, scroll = 10312, train = 190, sq = 2, r = { { 4339, 3 }, { 2604, 2 }, { 8343, 2 } }, out = { 10018, 1 }, oq = 2 },
    [12067] = { name = "Dreamweave Gloves", t = { 1, 205, 220, 235 }, fee = 4500, train = 190, r = { { 4339, 4 }, { 8153, 4 }, { 10286, 2 }, { 8343, 2 } }, out = { 10019, 1 }, oq = 3 },
    [12068] = { name = "Stormcloth Vest", t = { 1, 205, 220, 235 }, scroll = 254683, train = 190, sq = 2, r = { { 4339, 5 }, { 7079, 3 }, { 8343, 2 } }, out = { 10020, 1 }, oq = 2 },
    [12069] = { name = "Cindercloth Robe", t = { 1, 205, 220, 235 }, fee = 4500, train = 190, r = { { 4339, 5 }, { 7077, 2 }, { 8343, 2 } }, out = { 10042, 1 }, oq = 2 },
    [12070] = { name = "Dreamweave Vest", t = { 1, 205, 220, 235 }, fee = 4500, train = 190, r = { { 4339, 6 }, { 8153, 6 }, { 10286, 2 }, { 8343, 2 } }, out = { 10021, 1 }, oq = 3 },
    [12071] = { name = "Shadoweave Gloves", t = { 1, 205, 220, 235 }, fee = 6000, train = 190, tr = { 9584 }, r = { { 4339, 5 }, { 10285, 5 }, { 8343, 2 } }, out = { 10023, 1 }, oq = 2 },
    [12072] = { name = "Black Mageweave Headband", t = { 1, 205, 220, 235 }, fee = 6000, train = 190, tr = { 2399, 11052 }, r = { { 4339, 3 }, { 8343, 2 } }, out = { 10024, 1 }, oq = 2 },
    [12073] = { name = "Black Mageweave Boots", t = { 1, 205, 220, 235 }, fee = 6000, train = 190, tr = { 2399, 11052 }, r = { { 4339, 3 }, { 8343, 2 }, { 4304, 2 } }, out = { 10026, 1 }, oq = 2 },
    [12074] = { name = "Black Mageweave Shoulders", t = { 1, 205, 220, 235 }, fee = 6000, train = 190, tr = { 2399, 11052 }, r = { { 4339, 3 }, { 8343, 2 } }, out = { 10027, 1 }, oq = 2 },
    [12075] = { name = "Lavender Mageweave Shirt", t = { 1, 195, 200, 205 }, scroll = 10314, train = 190, scrollPrice = 4000, sq = 1, r = { { 4339, 2 }, { 4342, 2 }, { 8343, 2 } }, out = { 10054, 1 }, oq = 1 },
    [12076] = { name = "Shadoweave Shoulders", t = { 1, 210, 225, 240 }, fee = 6500, train = 195, tr = { 9584 }, r = { { 4339, 5 }, { 10285, 4 }, { 8343, 2 } }, out = { 10028, 1 }, oq = 2 },
    [12077] = { name = "Simple Black Dress", t = { 1, 200, 205, 210 }, fee = 5000, train = 195, tr = { 2399, 11052 }, r = { { 4339, 3 }, { 2325, 1 }, { 8343, 1 }, { 2324, 1 } }, out = { 10053, 1 }, oq = 1 },
    [12078] = { name = "Red Mageweave Shoulders", t = { 1, 210, 225, 240 }, scroll = 10315, train = 195, sq = 2, r = { { 4339, 4 }, { 2604, 2 }, { 8343, 3 } }, out = { 10029, 1 }, oq = 2 },
    [12079] = { name = "Red Mageweave Bag", t = { 1, 210, 225, 240 }, fee = 6500, train = 195, tr = { 2399, 11052 }, r = { { 4339, 5 }, { 2604, 2 }, { 8343, 2 } }, out = { 10051, 1 }, oq = 1 },
    [12080] = { name = "Pink Mageweave Shirt", t = { 1, 200, 205, 210 }, scroll = 10317, train = 195, scrollPrice = 4000, sq = 1, r = { { 4339, 3 }, { 10290, 1 }, { 8343, 1 } }, out = { 10055, 1 }, oq = 1 },
    [12081] = { name = "Admiral's Hat", t = { 1, 215, 230, 245 }, scroll = 10318, train = 200, scrollPrice = 7000, sq = 1, r = { { 4339, 3 }, { 4589, 6 }, { 8343, 2 } }, out = { 10030, 1 }, oq = 2 },
    [12082] = { name = "Shadoweave Boots", t = { 1, 215, 230, 245 }, fee = 7000, train = 200, tr = { 9584 }, r = { { 4339, 6 }, { 10285, 6 }, { 8343, 3 }, { 4304, 2 } }, out = { 10031, 1 }, oq = 2 },
    [12083] = { name = "Stormcloth Headband", t = { 1, 215, 230, 245 }, scroll = 254684, train = 200, sq = 2, r = { { 4339, 4 }, { 7079, 4 }, { 8343, 2 } }, out = { 10032, 1 }, oq = 2 },
    [12084] = { name = "Red Mageweave Headband", t = { 1, 215, 230, 245 }, scroll = 10320, train = 200, sq = 2, r = { { 4339, 4 }, { 2604, 2 }, { 8343, 2 } }, out = { 10033, 1 }, oq = 2 },
    [12085] = { name = "Tuxedo Shirt", t = { 1, 205, 210, 215 }, scroll = 10321, train = 200, scrollPrice = 4500, sq = 1, r = { { 4339, 4 }, { 8343, 2 } }, out = { 10034, 1 }, oq = 1 },
    [12086] = { name = "Shadoweave Mask", t = { 1, 215, 230, 245 }, scroll = 10463, train = 200, sq = 2, r = { { 4339, 2 }, { 10285, 8 }, { 8343, 2 } }, out = { 10025, 1 }, oq = 2 },
    [12087] = { name = "Stormcloth Shoulders", t = { 1, 215, 230, 245 }, scroll = 254685, train = 200, sq = 2, r = { { 4339, 5 }, { 7079, 6 }, { 8343, 3 } }, out = { 10038, 1 }, oq = 2 },
    [12088] = { name = "Cindercloth Boots", t = { 1, 215, 230, 245 }, fee = 7500, train = 200, tr = { 2399, 11052 }, r = { { 4339, 5 }, { 7077, 1 }, { 8343, 3 }, { 4304, 2 } }, out = { 10044, 1 }, oq = 2 },
    [12089] = { name = "Tuxedo Pants", t = { 1, 205, 210, 215 }, scroll = 10323, train = 140, scrollPrice = 4500, sq = 1, r = { { 4339, 4 }, { 8343, 3 } }, out = { 10035, 1 }, oq = 1 },
    [12090] = { name = "Stormcloth Boots", t = { 1, 220, 235, 250 }, scroll = 254686, train = 205, sq = 2, r = { { 4339, 6 }, { 7079, 6 }, { 8343, 3 }, { 4304, 2 } }, out = { 10039, 1 }, oq = 2 },
    [12091] = { name = "White Wedding Dress", t = { 1, 145, 150, 155 }, scroll = 10325, train = 140, scrollPrice = 10000, sq = 1, r = { { 4339, 5 }, { 8343, 3 }, { 2324, 1 } }, out = { 10040, 1 }, oq = 1 },
    [12092] = { name = "Dreamweave Circlet", t = { 1, 220, 235, 250 }, fee = 7500, train = 205, tr = { 2399, 11052 }, r = { { 4339, 8 }, { 8153, 4 }, { 10286, 2 }, { 8343, 3 }, { 6037, 1 }, { 1529, 1 } }, out = { 10041, 1 }, oq = 3 },
    [12093] = { name = "Tuxedo Jacket", t = { 1, 155, 170, 185 }, scroll = 10326, train = 140, scrollPrice = 5000, sq = 1, r = { { 4339, 5 }, { 8343, 3 } }, out = { 10036, 1 }, oq = 1 },
    [18401] = { name = "Bolt of Runecloth", t = { 1, 210, 212, 215 }, fee = 10000, train = 205, tr = { 2399, 11052 }, r = { { 14047, 5 } }, out = { 14048, 1 }, oq = 1 },
    [18402] = { name = "Runecloth Belt", t = { 1, 225, 240, 255 }, fee = 10000, train = 210, tr = { 2399, 11052 }, r = { { 14048, 3 }, { 14341, 1 } }, out = { 13856, 1 }, oq = 2 },
    [18403] = { name = "Frostweave Tunic", t = { 1, 225, 240, 255 }, scroll = 14466, train = 210, sq = 2, r = { { 14048, 5 }, { 7079, 2 }, { 14341, 1 } }, out = { 13869, 1 }, oq = 2 },
    [18404] = { name = "Frostweave Robe", t = { 1, 225, 240, 255 }, scroll = 14467, train = 210, sq = 2, r = { { 14048, 5 }, { 7079, 2 }, { 14341, 1 } }, out = { 13868, 1 }, oq = 2 },
    [18405] = { name = "Runecloth Bag", t = { 1, 230, 245, 260 }, scroll = 14468, train = 215, scrollPrice = 12000, sq = 1, r = { { 14048, 5 }, { 8170, 2 }, { 14341, 1 }, { 249430, 4 }, { 249409, 2 } }, out = { 14046, 1 }, oq = 1 },
    [18406] = { name = "Runecloth Robe", t = { 1, 230, 245, 260 }, scroll = 14469, train = 215, scrollPrice = 12000, sq = 1, r = { { 14048, 5 }, { 14227, 1 }, { 14341, 1 } }, out = { 13858, 1 }, oq = 2 },
    [18407] = { name = "Runecloth Tunic", t = { 1, 230, 245, 260 }, scroll = 14470, train = 215, sq = 2, r = { { 14048, 5 }, { 14227, 1 }, { 14341, 1 } }, out = { 13857, 1 }, oq = 2 },
    [18408] = { name = "Cindercloth Vest", t = { 1, 230, 245, 260 }, scroll = 14471, train = 215, sq = 2, r = { { 14048, 5 }, { 7077, 3 }, { 14341, 1 } }, out = { 14042, 1 }, oq = 2 },
    [18409] = { name = "Runecloth Cloak", t = { 1, 240, 255, 270 }, scroll = 14472, train = 220, scrollPrice = 12000, sq = 1, r = { { 14048, 4 }, { 14227, 1 }, { 14341, 1 } }, out = { 13860, 1 }, oq = 2 },
    [18410] = { name = "Ghostweave Belt", t = { 1, 235, 250, 265 }, scroll = 14473, train = 220, sq = 2, r = { { 14048, 3 }, { 9210, 2 }, { 14227, 1 }, { 14341, 1 } }, out = { 14143, 1 }, oq = 2 },
    [18411] = { name = "Frostweave Gloves", t = { 1, 230, 245, 260 }, scroll = 14474, train = 215, sq = 2, r = { { 14048, 3 }, { 7080, 1 }, { 14341, 1 } }, out = { 13870, 1 }, oq = 2 },
    [18412] = { name = "Cindercloth Gloves", t = { 1, 240, 255, 270 }, scroll = 14476, train = 225, sq = 2, r = { { 14048, 4 }, { 7077, 3 }, { 14341, 1 } }, out = { 14043, 1 }, oq = 2 },
    [18413] = { name = "Ghostweave Gloves", t = { 1, 240, 255, 270 }, scroll = 14477, train = 225, sq = 2, r = { { 14048, 4 }, { 9210, 2 }, { 14227, 1 }, { 14341, 1 } }, out = { 14142, 1 }, oq = 2 },
    [18414] = { name = "Brightcloth Robe", t = { 1, 240, 255, 270 }, scroll = 14478, train = 225, sq = 2, r = { { 14048, 5 }, { 3577, 2 }, { 14341, 1 } }, out = { 14100, 1 }, oq = 2 },
    [18415] = { name = "Brightcloth Gloves", t = { 1, 240, 255, 270 }, scroll = 14479, train = 225, sq = 2, r = { { 14048, 4 }, { 3577, 2 }, { 14341, 1 } }, out = { 14101, 1 }, oq = 2 },
    [18416] = { name = "Ghostweave Vest", t = { 1, 240, 255, 270 }, scroll = 14480, train = 225, sq = 2, r = { { 14048, 6 }, { 9210, 4 }, { 14227, 1 }, { 14341, 1 } }, out = { 14141, 1 }, oq = 2 },
    [18417] = { name = "Runecloth Gloves", t = { 1, 245, 260, 275 }, scroll = 14481, train = 230, scrollPrice = 16000, sq = 1, r = { { 14048, 4 }, { 8170, 4 }, { 14341, 1 } }, out = { 13863, 1 }, oq = 2 },
    [18418] = { name = "Cindercloth Cloak", t = { 1, 245, 260, 275 }, scroll = 14482, train = 230, sq = 2, r = { { 14048, 5 }, { 7078, 1 }, { 14341, 1 } }, out = { 14044, 1 }, oq = 2 },
    [18419] = { name = "Felcloth Pants", t = { 1, 245, 260, 275 }, scroll = 14483, train = 230, scrollPrice = 16000, sq = 1, r = { { 14048, 5 }, { 14256, 4 }, { 14341, 1 } }, out = { 14107, 1 }, oq = 2 },
    [18420] = { name = "Brightcloth Cloak", t = { 1, 245, 260, 275 }, scroll = 14484, train = 230, sq = 2, r = { { 14048, 4 }, { 3577, 2 }, { 14341, 1 } }, out = { 14103, 1 }, oq = 2 },
    [18421] = { name = "Wizardweave Leggings", t = { 1, 245, 260, 275 }, scroll = 14485, train = 230, sq = 2, r = { { 14048, 6 }, { 11176, 1 }, { 14341, 1 } }, out = { 14132, 1 }, oq = 2 },
    [18422] = { name = "Cloak of Fire", t = { 1, 250, 265, 280 }, scroll = 14486, train = 235, sq = 3, r = { { 14048, 6 }, { 7078, 4 }, { 7077, 4 }, { 7068, 4 }, { 14341, 1 } }, out = { 14134, 1 }, oq = 3 },
    [18423] = { name = "Runecloth Boots", t = { 1, 250, 265, 280 }, scroll = 14488, train = 235, scrollPrice = 20000, sq = 1, r = { { 14048, 4 }, { 14227, 2 }, { 8170, 4 }, { 14341, 1 } }, out = { 13864, 1 }, oq = 2 },
    [18424] = { name = "Frostweave Pants", t = { 1, 250, 265, 280 }, scroll = 14489, train = 235, sq = 2, r = { { 14048, 6 }, { 7080, 1 }, { 14341, 1 } }, out = { 13871, 1 }, oq = 2 },
    [18434] = { name = "Cindercloth Pants", t = { 1, 250, 265, 280 }, scroll = 14490, train = 235, sq = 2, r = { { 14048, 6 }, { 7078, 1 }, { 14341, 1 } }, out = { 14045, 1 }, oq = 2 },
    [18436] = { name = "Robe of Winter Night", t = { 1, 260, 275, 290 }, scroll = 14493, train = 245, sq = 3, r = { { 14048, 10 }, { 14256, 12 }, { 12808, 4 }, { 7080, 4 }, { 14341, 1 } }, out = { 14136, 1 }, oq = 3 },
    [18437] = { name = "Felcloth Boots", t = { 1, 255, 270, 285 }, scroll = 14492, train = 240, sq = 2, r = { { 14048, 6 }, { 14256, 4 }, { 8170, 4 }, { 14341, 1 } }, out = { 14108, 1 }, oq = 2 },
    [18438] = { name = "Runecloth Pants", t = { 1, 255, 270, 285 }, scroll = 14491, train = 240, sq = 2, r = { { 14048, 6 }, { 14227, 2 }, { 14341, 1 } }, out = { 13865, 1 }, oq = 2 },
    [18439] = { name = "Brightcloth Pants", t = { 1, 260, 275, 290 }, scroll = 14494, train = 245, sq = 2, r = { { 14048, 6 }, { 3577, 4 }, { 14227, 1 }, { 14341, 1 } }, out = { 14104, 1 }, oq = 2 },
    [18440] = { name = "Mooncloth Leggings", t = { 1, 270, 285, 300 }, scroll = 14497, train = 245, sq = 3, r = { { 14048, 6 }, { 14342, 4 }, { 14341, 1 } }, out = { 14137, 1 }, oq = 3 },
    [18441] = { name = "Ghostweave Pants", t = { 1, 260, 275, 290 }, scroll = 14495, train = 245, sq = 2, r = { { 14048, 6 }, { 9210, 4 }, { 14341, 1 } }, out = { 14144, 1 }, oq = 2 },
    [18442] = { name = "Felcloth Hood", t = { 1, 260, 275, 290 }, scroll = 14496, train = 245, sq = 2, r = { { 14048, 5 }, { 14256, 4 }, { 14341, 1 } }, out = { 14111, 1 }, oq = 2 },
    [18444] = { name = "Runecloth Headband", t = { 1, 265, 280, 295 }, scroll = 14498, train = 250, sq = 2, r = { { 14048, 4 }, { 14227, 2 }, { 14341, 1 } }, out = { 13866, 1 }, oq = 2 },
    [18445] = { name = "Mooncloth Bag", t = { 1, 270, 285, 300 }, scroll = 14499, train = 255, sq = 2, r = { { 14048, 4 }, { 14342, 1 }, { 14341, 1 }, { 249431, 10 }, { 249430, 2 }, { 249409, 4 } }, out = { 14155, 1 }, oq = 2 },
    [18446] = { name = "Wizardweave Robe", t = { 1, 270, 285, 300 }, scroll = 14500, train = 255, sq = 2, r = { { 14048, 8 }, { 11176, 2 }, { 14341, 1 } }, out = { 14128, 1 }, oq = 2 },
    [18447] = { name = "Mooncloth Vest", t = { 1, 285, 300, 315 }, scroll = 14501, train = 270, sq = 3, r = { { 14048, 6 }, { 14342, 4 }, { 14341, 1 } }, out = { 14138, 1 }, oq = 3 },
    [18448] = { name = "Mooncloth Shoulders", t = { 1, 290, 305, 320 }, scroll = 14507, train = 275, sq = 3, r = { { 14048, 5 }, { 14342, 5 }, { 14341, 1 } }, out = { 14139, 1 }, oq = 3 },
    [18449] = { name = "Runecloth Shoulders", t = { 1, 275, 290, 305 }, scroll = 14504, train = 260, sq = 2, r = { { 14048, 7 }, { 14227, 2 }, { 8170, 4 }, { 14341, 1 } }, out = { 13867, 1 }, oq = 2 },
    [18450] = { name = "Wizardweave Turban", t = { 1, 275, 290, 305 }, scroll = 14505, train = 260, sq = 2, r = { { 14048, 6 }, { 11176, 4 }, { 7910, 1 }, { 14341, 1 } }, out = { 14130, 1 }, oq = 2 },
    [18451] = { name = "Felcloth Robe", t = { 1, 275, 290, 305 }, scroll = 14506, train = 260, sq = 2, r = { { 14048, 8 }, { 14256, 8 }, { 12662, 4 }, { 14341, 2 } }, out = { 14106, 1 }, oq = 2 },
    [18452] = { name = "Mooncloth Circlet", t = { 1, 295, 310, 325 }, scroll = 14509, train = 280, sq = 3, r = { { 14048, 4 }, { 14342, 6 }, { 12800, 1 }, { 12810, 2 }, { 14341, 2 } }, out = { 14140, 1 }, oq = 3 },
    [18453] = { name = "Felcloth Shoulders", t = { 1, 280, 295, 310 }, scroll = 14508, train = 265, sq = 2, r = { { 14048, 7 }, { 14256, 6 }, { 12662, 4 }, { 8170, 4 }, { 14341, 2 } }, out = { 14112, 1 }, oq = 2 },
    [18454] = { name = "Gloves of Spell Mastery", t = { 1, 310, 325, 340 }, scroll = 14511, train = 295, sq = 4, r = { { 14048, 10 }, { 14342, 8 }, { 9210, 8 }, { 13926, 4 }, { 12364, 4 }, { 12810, 6 }, { 14341, 2 }, { 249431, 10 } }, out = { 14146, 1 }, oq = 4 },
    [18455] = { name = "Bottomless Bag", t = { 1, 315, 330, 345 }, scroll = 14510, train = 300, sq = 3, r = { { 14048, 8 }, { 14342, 12 }, { 14344, 2 }, { 249429, 5 }, { 249428, 5 }, { 249431, 8 }, { 14341, 2 } }, out = { 14156, 1 }, oq = 3 },
    [18456] = { name = "Truefaith Vestments", t = { 1, 310, 325, 340 }, scroll = 14512, train = 295, sq = 4, r = { { 14048, 12 }, { 14342, 8 }, { 12811, 2 }, { 13926, 2 }, { 9210, 8 }, { 14341, 2 }, { 249431, 10 } }, out = { 14154, 1 }, oq = 4, bop = true },
    [18457] = { name = "Robe of the Archmage", t = { 1, 310, 325, 340 }, scroll = 14513, train = 295, sq = 4, r = { { 14048, 12 }, { 7078, 8 }, { 7082, 8 }, { 7076, 8 }, { 7080, 8 }, { 14341, 2 }, { 249431, 10 } }, out = { 14152, 1 }, oq = 4, bop = true },
    [18458] = { name = "Robe of the Void", t = { 1, 310, 325, 340 }, scroll = 14514, train = 295, sq = 4, r = { { 14048, 12 }, { 12662, 20 }, { 14256, 40 }, { 7078, 8 }, { 12808, 8 }, { 14341, 2 }, { 249431, 10 } }, out = { 14153, 1 }, oq = 4, bop = true },
    [18560] = { name = "Mooncloth", t = { 1, 270, 285, 300 }, scroll = 14526, train = 230, scrollPrice = 20000, sq = 1, r = { { 14256, 2 } }, out = { 14342, 1 }, oq = 1 },
    [19435] = { name = "Mooncloth Boots", t = { 1, 285, 300, 315 }, r = { { 14048, 6 }, { 14342, 4 }, { 7971, 2 }, { 14341, 1 } }, out = { 15802, 1 }, oq = 3 },
    [20848] = { name = "Flarecore Mantle", t = { 1, 315, 330, 345 }, scroll = 17017, train = 300, rep = { 59, 5 }, sq = 1, r = { { 14048, 12 }, { 17010, 4 }, { 17011, 4 }, { 12810, 6 }, { 14341, 2 } }, out = { 16980, 1 }, oq = 4 },
    [20849] = { name = "Flarecore Gloves", t = { 1, 315, 330, 345 }, scroll = 17018, train = 300, rep = { 59, 4 }, sq = 1, r = { { 14048, 8 }, { 17010, 6 }, { 7078, 4 }, { 12810, 2 }, { 14341, 2 } }, out = { 16979, 1 }, oq = 4 },
    [21945] = { name = "Green Holiday Shirt", t = { 1, 165, 170, 175 }, scroll = 17724, train = 155, sq = 1, r = { { 4305, 5 }, { 2605, 4 }, { 4291, 1 } }, out = { 17723, 1 }, oq = 1 },
    [22759] = { name = "Flarecore Wraps", t = { 1, 320, 335, 350 }, scroll = 18265, train = 300, sq = 3, r = { { 14342, 6 }, { 17010, 8 }, { 7078, 2 }, { 12810, 6 }, { 14341, 4 } }, out = { 18263, 1 }, oq = 4 },
    [22813] = { name = "Gordok Ogre Suit", t = { 1, 285, 290, 295 }, r = { { 14048, 2 }, { 8170, 4 }, { 18240, 1 }, { 14341, 1 } }, out = { 18258, 1 }, oq = 2 },
    [22866] = { name = "Belt of the Archmage", t = { 1, 310, 325, 340 }, scroll = 18414, train = 295, sq = 4, r = { { 14048, 16 }, { 9210, 8 }, { 14342, 8 }, { 7080, 10 }, { 7078, 10 }, { 14344, 4 }, { 14341, 6 }, { 249431, 10 } }, out = { 18405, 1 }, oq = 4 },
    [22867] = { name = "Felcloth Gloves", t = { 1, 295, 310, 325 }, scroll = 18415, train = 280, sq = 3, r = { { 14048, 12 }, { 14256, 20 }, { 12662, 6 }, { 12808, 8 }, { 14341, 2 } }, out = { 18407, 1 }, oq = 3 },
    [22868] = { name = "Inferno Gloves", t = { 1, 295, 310, 325 }, scroll = 18416, train = 280, sq = 3, r = { { 14048, 12 }, { 7078, 10 }, { 7910, 2 }, { 14341, 2 } }, out = { 18408, 1 }, oq = 3 },
    [22869] = { name = "Mooncloth Gloves", t = { 1, 295, 310, 325 }, scroll = 18417, train = 280, sq = 3, r = { { 14048, 12 }, { 14342, 6 }, { 13926, 2 }, { 14341, 2 } }, out = { 18409, 1 }, oq = 3 },
    [22870] = { name = "Cloak of Warding", t = { 1, 295, 310, 325 }, scroll = 18418, train = 280, sq = 3, r = { { 14048, 12 }, { 12809, 4 }, { 12360, 1 }, { 14341, 2 } }, out = { 18413, 1 }, oq = 3 },
    [22902] = { name = "Mooncloth Robe", t = { 1, 290, 305, 320 }, scroll = 18487, train = 275, sq = 1, r = { { 14048, 6 }, { 14342, 4 }, { 13926, 2 }, { 14341, 2 } }, out = { 18486, 1 }, oq = 3 },
    [23662] = { name = "Wisdom of the Timbermaw", t = { 1, 270, 285, 300 }, scroll = 19215, train = 255, scrollPrice = 22000, rep = { 576, 5 }, sq = 1, r = { { 14048, 8 }, { 7076, 3 }, { 12803, 3 }, { 14227, 2 } }, out = { 19047, 1 }, oq = 3 },
    [23663] = { name = "Mantle of the Timbermaw", t = { 1, 305, 319, 334 }, scroll = 19218, train = 290, scrollPrice = 40000, rep = { 576, 6 }, sq = 3, r = { { 14342, 5 }, { 7076, 5 }, { 12803, 5 }, { 14227, 2 } }, out = { 19050, 1 }, oq = 3 },
    [23664] = { name = "Argent Boots", t = { 1, 270, 285, 300 }, scroll = 19216, train = 255, scrollPrice = 22000, rep = { 529, 5 }, sq = 1, r = { { 14048, 6 }, { 12810, 4 }, { 13926, 2 }, { 12809, 2 }, { 14227, 2 } }, out = { 19056, 1 }, oq = 3 },
    [23665] = { name = "Argent Shoulders", t = { 1, 305, 320, 335 }, scroll = 19217, train = 290, scrollPrice = 40000, rep = { 529, 6 }, sq = 1, r = { { 14342, 5 }, { 12809, 2 }, { 14227, 2 } }, out = { 19059, 1 }, oq = 3 },
    [23666] = { name = "Flarecore Robe", t = { 1, 315, 330, 345 }, scroll = 19219, train = 300, rep = { 59, 5 }, sq = 1, r = { { 14342, 10 }, { 17010, 2 }, { 17011, 3 }, { 7078, 6 }, { 14227, 4 } }, out = { 19156, 1 }, oq = 4 },
    [23667] = { name = "Flarecore Leggings", t = { 1, 315, 330, 345 }, scroll = 19220, train = 300, rep = { 59, 6 }, sq = 1, r = { { 14342, 8 }, { 17010, 5 }, { 17011, 3 }, { 7078, 10 }, { 14227, 4 } }, out = { 19165, 1 }, oq = 4 },
    [24091] = { name = "Bloodvine Vest", t = { 1, 315, 330, 345 }, scroll = 19764, train = 300, scrollPrice = 50000, rep = { 270, 6 }, sq = 1, r = { { 14342, 3 }, { 19726, 5 }, { 12804, 4 }, { 14048, 4 }, { 14227, 2 } }, out = { 19682, 1 }, oq = 3 },
    [24092] = { name = "Bloodvine Leggings", t = { 1, 315, 330, 345 }, scroll = 19765, train = 300, scrollPrice = 50000, rep = { 270, 5 }, sq = 1, r = { { 14342, 4 }, { 19726, 4 }, { 12804, 4 }, { 14048, 4 }, { 14227, 2 } }, out = { 19683, 1 }, oq = 3 },
    [24093] = { name = "Bloodvine Boots", t = { 1, 315, 330, 345 }, scroll = 19766, train = 300, scrollPrice = 50000, rep = { 270, 4 }, sq = 1, r = { { 14342, 3 }, { 19726, 3 }, { 12810, 4 }, { 14048, 4 }, { 14227, 4 } }, out = { 19684, 1 }, oq = 3 },
    [24901] = { name = "Runed Stygian Leggings", t = { 1, 300, 315, 330 }, scroll = 20546, train = 285, sq = 3, r = { { 14048, 6 }, { 20520, 8 }, { 14256, 6 }, { 14227, 2 } }, out = { 20538, 1 }, oq = 3 },
    [24902] = { name = "Runed Stygian Belt", t = { 1, 300, 315, 330 }, scroll = 20548, train = 285, sq = 3, r = { { 14048, 2 }, { 20520, 6 }, { 14256, 2 }, { 12810, 2 }, { 14227, 2 } }, out = { 20539, 1 }, oq = 3 },
    [24903] = { name = "Runed Stygian Boots", t = { 1, 300, 315, 330 }, scroll = 20547, train = 285, sq = 3, r = { { 14048, 4 }, { 20520, 6 }, { 14256, 4 }, { 12810, 2 }, { 14227, 2 } }, out = { 20537, 1 }, oq = 3 },
    [26085] = { name = "Soul Pouch", t = { 1, 230, 245, 260 }, scroll = 21358, train = 215, scrollPrice = 12000, sq = 1, r = { { 14048, 6 }, { 8170, 4 }, { 7972, 2 }, { 14341, 1 } }, out = { 21340, 1 }, oq = 2 },
    [26086] = { name = "Felcloth Bag", t = { 1, 260, 275, 290 }, scroll = 21369, train = 250, sq = 1, r = { { 14256, 12 }, { 12810, 6 }, { 20520, 2 }, { 14227, 4 } }, out = { 21341, 1 }, oq = 3 },
    [26087] = { name = "Core Felcloth Bag", t = { 1, 315, 330, 345 }, scroll = 21371, train = 300, sq = 3, r = { { 14256, 20 }, { 17012, 16 }, { 19726, 8 }, { 7078, 4 }, { 14227, 4 } }, out = { 21342, 1 }, oq = 4 },
    [26403] = { name = "Festival Dress", t = { 1, 220, 235, 250 }, scroll = 21722, train = 205, sq = 2, r = { { 14048, 4 }, { 4625, 2 }, { 2604, 2 }, { 14341, 1 } }, out = { 21154, 1 }, oq = 1 },
    [26407] = { name = "Festival Suit", t = { 1, 220, 235, 250 }, scroll = 21723, train = 205, sq = 2, r = { { 14048, 4 }, { 4625, 2 }, { 2604, 2 }, { 14341, 1 } }, out = { 21542, 1 }, oq = 1 },
    [27658] = { name = "Enchanted Mageweave Pouch", t = { 1, 205, 220, 235 }, scroll = 22307, train = 190, scrollPrice = 6000, sq = 1, r = { { 4339, 4 }, { 11137, 4 }, { 8343, 2 } }, out = { 22246, 1 }, oq = 2 },
    [27659] = { name = "Enchanted Runecloth Bag", t = { 1, 245, 260, 275 }, scroll = 22308, train = 230, scrollPrice = 20000, sq = 1, r = { { 14048, 5 }, { 16203, 2 }, { 14341, 2 } }, out = { 22248, 1 }, oq = 2 },
    [27660] = { name = "Big Bag of Enchantment", t = { 1, 270, 285, 300 }, scroll = 22309, train = 255, sq = 2, r = { { 14048, 6 }, { 14344, 4 }, { 12810, 4 }, { 14227, 4 } }, out = { 22249, 1 }, oq = 2 },
    [27724] = { name = "Cenarion Herb Bag", t = { 1, 245, 260, 275 }, scroll = 22310, train = 230, scrollPrice = 20000, rep = { 609, 4 }, sq = 1, r = { { 14048, 5 }, { 8831, 10 }, { 11040, 8 }, { 14341, 2 } }, out = { 22251, 1 }, oq = 2 },
    [27725] = { name = "Satchel of Cenarius", t = { 1, 270, 285, 300 }, scroll = 22312, train = 255, scrollPrice = 50000, rep = { 609, 6 }, sq = 1, r = { { 14048, 6 }, { 14342, 2 }, { 13468, 1 }, { 14227, 4 } }, out = { 22252, 1 }, oq = 2 },
    [28205] = { name = "Glacial Gloves", t = { 1, 315, 330, 345 }, scroll = 22684, train = 305, sq = 1, r = { { 22682, 5 }, { 14048, 4 }, { 7080, 4 }, { 14227, 4 } }, out = { 22654, 1 }, oq = 4 },
    [28207] = { name = "Glacial Vest", t = { 1, 315, 330, 345 }, scroll = 22686, train = 305, sq = 1, r = { { 22682, 7 }, { 14048, 8 }, { 7080, 6 }, { 14227, 8 } }, out = { 22652, 1 }, oq = 4 },
    [28208] = { name = "Glacial Cloak", t = { 1, 315, 330, 345 }, scroll = 236691, train = 305, sq = 1, r = { { 22682, 5 }, { 14048, 4 }, { 7080, 2 }, { 14227, 4 } }, out = { 22658, 1 }, oq = 4 },
    [28209] = { name = "Glacial Wrists", t = { 1, 315, 330, 345 }, scroll = 22687, train = 305, sq = 1, r = { { 22682, 4 }, { 14048, 2 }, { 7080, 2 }, { 14227, 4 } }, out = { 22655, 1 }, oq = 4 },
    [28210] = { name = "Gaea's Embrace", t = { 1, 315, 330, 345 }, scroll = 22683, train = 300, scrollPrice = 90000, rep = { 609, 6 }, sq = 1, r = { { 19726, 1 }, { 14342, 2 }, { 12803, 4 }, { 14227, 4 } }, out = { 22660, 1 }, oq = 3 },
    [28480] = { name = "Sylvan Vest", t = { 1, 315, 330, 345 }, scroll = 22774, train = 300, scrollPrice = 50000, rep = { 609, 6 }, sq = 1, r = { { 14048, 4 }, { 19726, 2 }, { 12803, 2 }, { 14227, 2 } }, out = { 22756, 1 }, oq = 3 },
    [28481] = { name = "Sylvan Crown", t = { 1, 315, 330, 345 }, scroll = 22773, train = 300, scrollPrice = 50000, rep = { 609, 5 }, sq = 1, r = { { 14048, 4 }, { 14342, 2 }, { 12803, 2 }, { 14227, 2 } }, out = { 22757, 1 }, oq = 3 },
    [28482] = { name = "Sylvan Shoulders", t = { 1, 315, 330, 345 }, scroll = 22772, train = 300, scrollPrice = 50000, rep = { 609, 4 }, sq = 1, r = { { 14048, 2 }, { 12803, 4 }, { 14227, 2 } }, out = { 22758, 1 }, oq = 3 },
    [44950] = { name = "Green Winter Clothes", t = { 1, 250, 252, 255 }, scroll = 34261, train = 250, sq = 2, r = { { 14048, 4 }, { 2997, 1 }, { 2605, 2 }, { 14341, 1 } }, out = { 34087, 1 }, oq = 1 },
    [44958] = { name = "Red Winter Clothes", t = { 1, 250, 252, 255 }, scroll = 34319, train = 250, sq = 2, r = { { 14048, 4 }, { 2997, 1 }, { 2604, 2 }, { 14341, 1 } }, out = { 34085, 1 }, oq = 1 },
    [428424] = { name = "Phoenix Bindings", t = { 1, 125, 137, 150 }, scroll = 211247, train = 125, sq = 2, r = { { 2997, 6 }, { 814, 2 }, { 2321, 2 } }, out = { 210781, 1 }, oq = 3 },
    [435827] = { name = "Hyperconductive Arcano-Filament", t = { 1, 200, 210, 220 }, scroll = 215368, train = 200, sq = 3, r = { { 4339, 2 }, { 213378, 5 }, { 8343, 5 } }, out = { 213379, 1 }, oq = 3 },
    [435841] = { name = "Invoker's Cord", t = { 1, 170, 185, 200 }, scroll = 215369, train = 150, sq = 2, r = { { 4305, 3 }, { 1210, 1 }, { 2321, 1 }, { 4340, 1 } }, out = { 215366, 1 }, oq = 2 },
    [435848] = { name = "Invoker's Mantle", t = { 1, 170, 185, 200 }, scroll = 215370, train = 150, sq = 2, r = { { 4305, 4 }, { 4340, 4 }, { 2321, 1 }, { 6260, 4 } }, out = { 215365, 1 }, oq = 2 },
    [461692] = { name = "Synthetic Gordok Ogre Suit", t = { 1, 285, 290, 295 }, scroll = 228115, train = 275, sq = 1, r = { { 8170, 4 }, { 14048, 2 }, { 18240, 1 }, { 14341, 1 } }, out = { 227855, 1 }, oq = 1 },
    [461708] = { name = "Incandescent Mooncloth Robe", t = { 1, 315, 330, 345 }, scroll = 228303, train = 300, gone = true, sq = 1, r = { { 14048, 6 }, { 14342, 4 }, { 13926, 2 }, { 14341, 2 } }, out = { 227861, 1 }, oq = 1 },
    [461727] = { name = "Leather-Reinforced Runecloth Bag", t = { 1, 315, 330, 345 }, scroll = 228121, train = 300, gone = true, sq = 2, r = { { 14048, 5 }, { 8170, 2 }, { 14341, 1 }, { 15407, 1 } }, out = { 227844, 1 }, oq = 3 },
    [461747] = { name = "Incandescent Mooncloth Vest", t = { 1, 315, 330, 345 }, scroll = 228316, train = 300, sq = 3, r = { { 14048, 6 }, { 14342, 4 }, { 14341, 1 } }, out = { 227860, 1 }, oq = 1 },
    [461750] = { name = "Incandescent Mooncloth Circlet", t = { 1, 315, 330, 345 }, scroll = 228317, train = 300, sq = 3, r = { { 14048, 4 }, { 14342, 6 }, { 12800, 1 }, { 12810, 2 }, { 14341, 2 } }, out = { 227863, 1 }, oq = 1 },
    [461752] = { name = "Incandescent Mooncloth Leggings", t = { 1, 305, 320, 335 }, scroll = 228318, train = 290, sq = 3, r = { { 14048, 6 }, { 14342, 4 }, { 14341, 1 } }, out = { 227864, 1 }, oq = 1 },
    [462282] = { name = "Embroidered Belt of the Archmage", t = { 1, 315, 330, 345 }, scroll = 228477, train = 300, sq = 4, r = { { 14048, 16 }, { 9210, 10 }, { 14342, 10 }, { 7080, 12 }, { 7078, 12 }, { 14344, 6 }, { 14341, 6 } }, out = { 228476, 1 }, oq = 1 },
    [1214306] = { name = "Dreamscale Bracers", t = { 1, 320, 330, 340 }, scroll = 234483, train = 310, sq = 1, r = { { 14048, 30 }, { 20381, 4 }, { 12803, 4 }, { 14342, 4 }, { 14227, 6 } }, out = { 234484, 1 }, oq = 1 },
    [1214307] = { name = "Dreamscale Mitts", t = { 1, 320, 330, 340 }, scroll = 234486, train = 310, sq = 1, r = { { 14048, 30 }, { 20381, 5 }, { 12803, 4 }, { 14342, 4 }, { 14227, 6 } }, out = { 234485, 1 }, oq = 1 },
    [1224607] = { name = "Scarlet Augur's Hood", t = { 1, 285, 295, 305 }, scroll = 238298, train = 280, sq = 3, r = { { 12938, 1 }, { 12811, 2 }, { 14048, 12 } }, out = { 238264, 1 }, oq = 1 },
    [1224608] = { name = "Scarlet Augur's Mantle", t = { 1, 285, 295, 305 }, scroll = 238299, train = 280, sq = 3, r = { { 12811, 1 }, { 14048, 10 } }, out = { 238265, 1 }, oq = 1 },
    [1224609] = { name = "Scarlet Augur's Vestments", t = { 1, 285, 295, 305 }, scroll = 238300, train = 280, sq = 3, r = { { 12938, 1 }, { 12811, 1 }, { 14048, 12 } }, out = { 238266, 1 }, oq = 1 },
    [1224610] = { name = "Scarlet Augur's Cuffs", t = { 1, 260, 282, 305 }, scroll = 238301, train = 250, sq = 3, r = { { 14048, 8 } }, out = { 238267, 1 }, oq = 1 },
    [1224611] = { name = "Scarlet Augur's Mitts", t = { 1, 270, 287, 305 }, scroll = 238302, train = 260, sq = 3, r = { { 12811, 1 }, { 14048, 10 } }, out = { 238268, 1 }, oq = 1 },
    [1224612] = { name = "Scarlet Augur's Strap", t = { 1, 260, 282, 305 }, scroll = 238303, train = 250, sq = 3, r = { { 12811, 1 }, { 14048, 10 } }, out = { 238269, 1 }, oq = 1 },
    [1224613] = { name = "Scarlet Augur's Leggings", t = { 1, 280, 292, 305 }, scroll = 238304, train = 270, sq = 3, r = { { 12938, 1 }, { 12811, 1 }, { 14048, 12 } }, out = { 238270, 1 }, oq = 1 },
    [1224614] = { name = "Scarlet Augur's Soles", t = { 1, 270, 287, 305 }, scroll = 238305, train = 260, sq = 3, r = { { 12811, 1 }, { 14048, 10 } }, out = { 238271, 1 }, oq = 1 },
    [1227723] = { name = "Crusader's Knapsack", t = { 1, 260, 262, 265 }, scroll = 239149, train = 250, sq = 3, r = { { 12811, 1 }, { 14048, 14 }, { 2604, 8 }, { 14227, 3 } }, out = { 239147, 1 }, oq = 3 },
    [1227724] = { name = "Crimson Dawnwoven Bag", t = { 1, 300, 302, 305 }, scroll = 239150, train = 290, sq = 4, r = { { 12938, 1 }, { 14048, 24 }, { 2604, 4 }, { 12808, 2 }, { 12811, 2 } }, out = { 239148, 1 }, oq = 4 },
    [1229504] = { name = "Faction Banner", t = { 1, 20, 20, 20 }, fee = 0, train = 20, faction = "Horde", r = { { 2996, 1 }, { 2320, 1 } }, out = { 279972, 1 }, oq = 1 },
    [1257013] = { name = "Linen Reagent Bag", t = { 1, 30, 47, 65 }, scroll = 253665, train = 5, scrollPrice = 150, sq = 2, r = { { 2996, 6 }, { 2320, 6 } }, out = { 253664, 1 }, oq = 1 },
    [1257017] = { name = "Woolen Reagent Bag", t = { 1, 75, 92, 110 }, scroll = 253668, train = 70, scrollPrice = 250, sq = 2, r = { { 2997, 3 }, { 2321, 1 }, { 249409, 1 } }, out = { 253667, 1 }, oq = 1 },
    [1257370] = { name = "Pristine Boots", t = { 1, 85, 102, 120 }, scroll = 253890, train = 60, sq = 3, favor = 30, r = { { 2997, 8 }, { 2321, 2 }, { 249409, 2 }, { 249427, 1 } }, out = { 253889, 1 }, oq = 3, bop = true },
    [1257371] = { name = "Silky Boots", t = { 1, 85, 102, 120 }, scroll = 253892, train = 60, sq = 3, favor = 30, r = { { 2997, 8 }, { 2321, 2 }, { 249409, 2 }, { 3182, 1 } }, out = { 253891, 1 }, oq = 3, bop = true },
    [1257372] = { name = "Flame Boots", t = { 1, 85, 102, 120 }, scroll = 253894, train = 60, sq = 3, favor = 30, r = { { 2997, 8 }, { 2321, 2 }, { 249409, 2 }, { 6371, 1 } }, out = { 253893, 1 }, oq = 3, bop = true },
    [1257373] = { name = "Shadow Boots", t = { 1, 85, 102, 120 }, scroll = 253896, train = 60, sq = 3, favor = 30, r = { { 2997, 8 }, { 2321, 2 }, { 249409, 2 }, { 1210, 1 } }, out = { 253895, 1 }, oq = 3, bop = true },
    [1257374] = { name = "Pearly Boots", t = { 1, 85, 102, 120 }, scroll = 253898, train = 60, sq = 3, favor = 30, r = { { 2997, 8 }, { 2321, 2 }, { 249409, 2 }, { 5498, 1 } }, out = { 253897, 1 }, oq = 3, bop = true },
    [1257375] = { name = "Shining Boots", t = { 1, 85, 102, 120 }, scroll = 253900, train = 60, sq = 3, favor = 30, r = { { 2997, 8 }, { 2321, 2 }, { 249409, 2 }, { 249391, 1 } }, out = { 253899, 1 }, oq = 3, bop = true },
    [1257382] = { name = "Pristine Gloves", t = { 1, 100, 117, 135 }, scroll = 253914, train = 75, sq = 3, favor = 30, r = { { 2997, 6 }, { 2321, 4 }, { 249409, 3 }, { 249427, 2 } }, out = { 253913, 1 }, oq = 3, bop = true },
    [1257383] = { name = "Silky Gloves", t = { 1, 100, 117, 135 }, scroll = 253916, train = 75, sq = 3, favor = 30, r = { { 2997, 6 }, { 2321, 4 }, { 249409, 3 }, { 3182, 2 } }, out = { 253915, 1 }, oq = 3, bop = true },
    [1257384] = { name = "Flame Gloves", t = { 1, 100, 117, 135 }, scroll = 253918, train = 75, sq = 3, favor = 30, r = { { 2997, 6 }, { 2321, 4 }, { 249409, 3 }, { 6371, 2 } }, out = { 253917, 1 }, oq = 3, bop = true },
    [1257385] = { name = "Shadow Gloves", t = { 1, 100, 117, 135 }, scroll = 253920, train = 75, sq = 3, favor = 30, r = { { 2997, 6 }, { 2321, 4 }, { 249409, 3 }, { 1210, 2 } }, out = { 253919, 1 }, oq = 3, bop = true },
    [1257386] = { name = "Pearly Gloves", t = { 1, 100, 117, 135 }, scroll = 253922, train = 75, sq = 3, favor = 30, r = { { 2997, 6 }, { 2321, 4 }, { 249409, 3 }, { 5498, 2 } }, out = { 253921, 1 }, oq = 3, bop = true },
    [1257387] = { name = "Shining Gloves", t = { 1, 100, 117, 135 }, scroll = 253924, train = 75, sq = 3, favor = 30, r = { { 2997, 6 }, { 2321, 4 }, { 249409, 3 }, { 249391, 2 } }, out = { 253923, 1 }, oq = 3, bop = true },
    [1257388] = { name = "Pristine Sash", t = { 1, 110, 127, 145 }, scroll = 253926, train = 85, sq = 3, favor = 30, r = { { 4305, 8 }, { 2321, 4 }, { 249409, 3 }, { 249427, 3 } }, out = { 253925, 1 }, oq = 3, bop = true },
    [1257389] = { name = "Silky Sash", t = { 1, 110, 127, 145 }, scroll = 253928, train = 85, sq = 3, favor = 30, r = { { 4305, 8 }, { 2321, 4 }, { 249409, 3 }, { 3182, 3 } }, out = { 253927, 1 }, oq = 3, bop = true },
    [1257390] = { name = "Flame Sash", t = { 1, 110, 127, 145 }, scroll = 253930, train = 85, sq = 3, favor = 30, r = { { 4305, 8 }, { 2321, 4 }, { 249409, 3 }, { 6371, 3 } }, out = { 253929, 1 }, oq = 3, bop = true },
    [1257391] = { name = "Shadow Sash", t = { 1, 110, 127, 145 }, scroll = 253932, train = 85, sq = 3, favor = 30, r = { { 4305, 8 }, { 2321, 4 }, { 249409, 3 }, { 1210, 3 } }, out = { 253931, 1 }, oq = 3, bop = true },
    [1257392] = { name = "Pearly Sash", t = { 1, 110, 127, 145 }, scroll = 253934, train = 85, sq = 3, favor = 30, r = { { 4305, 8 }, { 2321, 4 }, { 249409, 3 }, { 5498, 3 } }, out = { 253933, 1 }, oq = 3, bop = true },
    [1257393] = { name = "Shining Sash", t = { 1, 110, 127, 145 }, scroll = 253936, train = 85, sq = 3, favor = 30, r = { { 4305, 8 }, { 2321, 4 }, { 249409, 3 }, { 249391, 3 } }, out = { 253935, 1 }, oq = 3, bop = true },
    [1257400] = { name = "Pristine Circlet", t = { 1, 125, 142, 160 }, scroll = 253950, train = 100, sq = 3, favor = 30, r = { { 4305, 10 }, { 4291, 2 }, { 249409, 4 }, { 249427, 4 }, { 2842, 1 }, { 11082, 2 } }, out = { 253949, 1 }, oq = 3, bop = true },
    [1257401] = { name = "Silky Circlet", t = { 1, 125, 142, 160 }, scroll = 253952, train = 100, sq = 3, favor = 30, r = { { 4305, 10 }, { 4291, 2 }, { 249409, 4 }, { 3182, 4 }, { 2842, 1 }, { 11082, 2 } }, out = { 253951, 1 }, oq = 3, bop = true },
    [1257402] = { name = "Flame Circlet", t = { 1, 125, 142, 160 }, scroll = 253954, train = 100, sq = 3, favor = 30, r = { { 4305, 10 }, { 4291, 2 }, { 249409, 4 }, { 6371, 4 }, { 2842, 1 }, { 11082, 2 } }, out = { 253953, 1 }, oq = 3, bop = true },
    [1257403] = { name = "Shadow Circlet", t = { 1, 125, 142, 160 }, scroll = 253956, train = 100, sq = 3, favor = 30, r = { { 4305, 10 }, { 4291, 2 }, { 249409, 4 }, { 1210, 4 }, { 2842, 1 }, { 11082, 2 } }, out = { 253955, 1 }, oq = 3, bop = true },
    [1257404] = { name = "Pearly Circlet", t = { 1, 125, 142, 160 }, scroll = 253958, train = 100, sq = 3, favor = 30, r = { { 4305, 10 }, { 4291, 2 }, { 249409, 4 }, { 5498, 4 }, { 2842, 1 }, { 11082, 2 } }, out = { 253957, 1 }, oq = 3, bop = true },
    [1257405] = { name = "Shining Circlet", t = { 1, 125, 142, 160 }, scroll = 253960, train = 100, sq = 3, favor = 30, r = { { 4305, 10 }, { 4291, 2 }, { 249409, 4 }, { 249391, 4 }, { 2842, 1 }, { 11082, 2 } }, out = { 253959, 1 }, oq = 3, bop = true },
    [1257406] = { name = "Pristine Gown", t = { 1, 130, 145, 160 }, scroll = 253962, train = 110, sq = 3, favor = 30, r = { { 4305, 12 }, { 4291, 2 }, { 249409, 6 }, { 249427, 6 }, { 2842, 2 }, { 11082, 2 } }, out = { 253961, 1 }, oq = 3, bop = true },
    [1257407] = { name = "Silky Gown", t = { 1, 130, 145, 160 }, scroll = 253964, train = 110, sq = 3, favor = 30, r = { { 4305, 12 }, { 4291, 2 }, { 249409, 6 }, { 3182, 6 }, { 2842, 2 }, { 11082, 2 } }, out = { 253963, 1 }, oq = 3, bop = true },
    [1257408] = { name = "Flame Gown", t = { 1, 130, 145, 160 }, scroll = 253966, train = 110, sq = 3, favor = 30, r = { { 4305, 12 }, { 4291, 2 }, { 249409, 6 }, { 6371, 6 }, { 2842, 2 }, { 11082, 2 } }, out = { 253965, 1 }, oq = 3, bop = true },
    [1257409] = { name = "Shadow Gown", t = { 1, 130, 145, 160 }, scroll = 253968, train = 110, sq = 3, favor = 30, r = { { 4305, 12 }, { 4291, 2 }, { 249409, 6 }, { 1210, 6 }, { 2842, 2 }, { 11082, 2 } }, out = { 253967, 1 }, oq = 3, bop = true },
    [1257410] = { name = "Pearly Gown", t = { 1, 130, 145, 160 }, scroll = 253970, train = 110, sq = 3, favor = 30, r = { { 4305, 12 }, { 4291, 2 }, { 249409, 6 }, { 5498, 6 }, { 2842, 2 }, { 11082, 2 } }, out = { 253969, 1 }, oq = 3, bop = true },
    [1257411] = { name = "Shining Gown", t = { 1, 130, 145, 160 }, scroll = 253972, train = 110, sq = 3, favor = 30, r = { { 4305, 12 }, { 4291, 2 }, { 249409, 6 }, { 249391, 6 }, { 2842, 2 }, { 11082, 2 } }, out = { 253971, 1 }, oq = 3, bop = true },
    [1257412] = { name = "Silk Reagent Bag", t = { 1, 135, 137, 140 }, scroll = 253974, train = 125, scrollPrice = 1000, sq = 2, r = { { 4305, 3 }, { 4234, 2 }, { 2321, 3 }, { 249409, 3 } }, out = { 253973, 1 }, oq = 1 },
    [1257419] = { name = "Pristine Leggings", t = { 1, 145, 160, 175 }, scroll = 253988, train = 125, sq = 3, favor = 30, r = { { 4305, 14 }, { 2321, 3 }, { 249409, 8 }, { 249427, 8 }, { 2842, 2 }, { 11082, 3 } }, out = { 253987, 1 }, oq = 3, bop = true },
    [1257420] = { name = "Silky Leggings", t = { 1, 145, 160, 175 }, scroll = 253990, train = 125, sq = 3, favor = 30, r = { { 4305, 14 }, { 2321, 3 }, { 249409, 8 }, { 3182, 8 }, { 2842, 2 }, { 11082, 3 } }, out = { 253989, 1 }, oq = 3, bop = true },
    [1257421] = { name = "Flame Leggings", t = { 1, 145, 160, 175 }, scroll = 253992, train = 125, sq = 3, favor = 30, r = { { 4305, 14 }, { 2321, 3 }, { 249409, 8 }, { 6371, 8 }, { 2842, 2 }, { 11082, 3 } }, out = { 253991, 1 }, oq = 3, bop = true },
    [1257422] = { name = "Shadow Leggings", t = { 1, 145, 160, 175 }, scroll = 253994, train = 125, sq = 3, favor = 30, r = { { 4305, 14 }, { 2321, 3 }, { 249409, 8 }, { 1210, 8 }, { 2842, 2 }, { 11082, 3 } }, out = { 253993, 1 }, oq = 3, bop = true },
    [1257423] = { name = "Pearly Leggings", t = { 1, 145, 160, 175 }, scroll = 253996, train = 125, sq = 3, favor = 30, r = { { 4305, 14 }, { 2321, 3 }, { 249409, 8 }, { 5498, 8 }, { 2842, 2 }, { 11082, 3 } }, out = { 253995, 1 }, oq = 3, bop = true },
    [1257424] = { name = "Shining Leggings", t = { 1, 145, 160, 175 }, scroll = 253998, train = 125, sq = 3, favor = 30, r = { { 4305, 14 }, { 2321, 3 }, { 249409, 8 }, { 249391, 8 }, { 2842, 2 }, { 11082, 3 } }, out = { 253997, 1 }, oq = 3, bop = true },
    [1257425] = { name = "Earthen Leggings", t = { 1, 160, 175, 190 }, scroll = 254000, train = 140, sq = 2, r = { { 4305, 4 }, { 7067, 1 }, { 2321, 2 } }, out = { 253999, 1 }, oq = 2 },
    [1257432] = { name = "Earthen Silk Slippers", t = { 1, 165, 180, 195 }, scroll = 254014, train = 145, sq = 2, r = { { 4305, 4 }, { 7067, 1 }, { 2321, 2 }, { 4234, 2 } }, out = { 254013, 1 }, oq = 2 },
    [1257433] = { name = "Earthen Silk Hood", t = { 1, 170, 185, 200 }, scroll = 254016, train = 150, sq = 2, r = { { 4305, 4 }, { 7067, 2 }, { 2321, 2 } }, out = { 254015, 1 }, oq = 2 },
    [1257434] = { name = "Earthen Silk Gloves", t = { 1, 180, 195, 210 }, scroll = 254018, train = 160, sq = 2, r = { { 4305, 5 }, { 7067, 2 }, { 4291, 2 } }, out = { 254017, 1 }, oq = 2 },
    [1257435] = { name = "Earthen Silk Cuffs", t = { 1, 185, 200, 215 }, scroll = 254020, train = 165, sq = 2, r = { { 4305, 4 }, { 7067, 1 }, { 4291, 1 } }, out = { 254019, 1 }, oq = 2 },
    [1257436] = { name = "Gilded Handwraps", t = { 1, 185, 200, 215 }, scroll = 254022, train = 165, sq = 3, r = { { 4339, 12 }, { 8343, 4 }, { 249430, 2 }, { 249409, 1 }, { 3577, 4 } }, out = { 254021, 1 }, oq = 3 },
    [1257437] = { name = "Frothing Handwraps", t = { 1, 185, 200, 215 }, scroll = 254024, train = 165, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 12 }, { 8343, 4 }, { 249430, 2 }, { 249409, 1 }, { 7079, 4 } }, out = { 254023, 1 }, oq = 3, bop = true },
    [1257438] = { name = "Fiery Handwraps", t = { 1, 185, 200, 215 }, scroll = 254026, train = 165, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 12 }, { 8343, 4 }, { 249430, 2 }, { 249409, 1 }, { 7077, 4 } }, out = { 254025, 1 }, oq = 3, bop = true },
    [1257439] = { name = "Black Handwraps", t = { 1, 185, 200, 215 }, scroll = 254028, train = 165, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 12 }, { 8343, 4 }, { 249430, 2 }, { 249409, 1 }, { 7971, 4 } }, out = { 254027, 1 }, oq = 3, bop = true },
    [1257440] = { name = "Golden Handwraps", t = { 1, 185, 200, 215 }, scroll = 254030, train = 165, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 12 }, { 8343, 4 }, { 249430, 2 }, { 249409, 1 }, { 13926, 4 } }, out = { 254029, 1 }, oq = 3, bop = true },
    [1257441] = { name = "Radiant Handwraps", t = { 1, 185, 200, 215 }, scroll = 254032, train = 165, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 12 }, { 8343, 4 }, { 249430, 2 }, { 249409, 1 }, { 11178, 4 } }, out = { 254031, 1 }, oq = 3, bop = true },
    [1257442] = { name = "Earthen Silk Shoulders", t = { 1, 185, 200, 215 }, scroll = 254034, train = 170, sq = 2, r = { { 4305, 6 }, { 7067, 2 }, { 4291, 3 } }, out = { 254033, 1 }, oq = 2 },
    [1257443] = { name = "Mageweave Reagent Bag", t = { 1, 205, 210, 215 }, scroll = 254036, train = 190, sq = 2, favor = 60, favorRep = 5, r = { { 4339, 4 }, { 8343, 2 }, { 249430, 1 }, { 249409, 1 } }, out = { 254035, 1 }, oq = 1 },
    [1257450] = { name = "Nethergeld Shoulders", t = { 1, 210, 225, 240 }, scroll = 254050, train = 195, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 16 }, { 8343, 3 }, { 249430, 4 }, { 249409, 3 }, { 3577, 8 }, { 11175, 2 } }, out = { 254049, 1 }, oq = 3, bop = true },
    [1257451] = { name = "Netherfroth Shoulders", t = { 1, 210, 225, 240 }, scroll = 254052, train = 195, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 16 }, { 8343, 3 }, { 249430, 4 }, { 249409, 3 }, { 7079, 8 }, { 11175, 2 } }, out = { 254051, 1 }, oq = 3, bop = true },
    [1257452] = { name = "Netherflame Shoulders", t = { 1, 210, 225, 240 }, scroll = 254054, train = 195, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 16 }, { 8343, 3 }, { 249430, 4 }, { 249409, 3 }, { 7077, 8 }, { 11175, 2 } }, out = { 254053, 1 }, oq = 3, bop = true },
    [1257453] = { name = "Netherpearl Shoulders", t = { 1, 210, 225, 240 }, scroll = 254056, train = 195, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 16 }, { 8343, 3 }, { 249430, 4 }, { 249409, 3 }, { 7971, 8 }, { 11175, 2 } }, out = { 254055, 1 }, oq = 3, bop = true },
    [1257454] = { name = "Nethershine Shoulders", t = { 1, 210, 225, 240 }, scroll = 254058, train = 195, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 16 }, { 8343, 3 }, { 249430, 4 }, { 249409, 3 }, { 13926, 8 }, { 11175, 2 } }, out = { 254057, 1 }, oq = 3, bop = true },
    [1257455] = { name = "Netherlight Shoulders", t = { 1, 210, 225, 240 }, scroll = 254060, train = 195, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 16 }, { 8343, 3 }, { 249430, 4 }, { 249409, 3 }, { 11178, 8 }, { 11175, 2 } }, out = { 254059, 1 }, oq = 3, bop = true },
    [1257456] = { name = "Nethergeld Cuffs", t = { 1, 220, 235, 250 }, scroll = 254062, train = 205, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 18 }, { 8343, 3 }, { 249430, 6 }, { 249409, 4 }, { 3577, 10 }, { 11175, 4 } }, out = { 254061, 1 }, oq = 3, bop = true },
    [1257457] = { name = "Netherfroth Cuffs", t = { 1, 220, 235, 250 }, scroll = 254064, train = 205, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 18 }, { 8343, 3 }, { 249430, 6 }, { 249409, 4 }, { 7079, 10 }, { 11175, 4 } }, out = { 254063, 1 }, oq = 3, bop = true },
    [1257458] = { name = "Netherflame Cuffs", t = { 1, 220, 235, 250 }, scroll = 254066, train = 205, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 18 }, { 8343, 3 }, { 249430, 6 }, { 249409, 4 }, { 7077, 10 }, { 11175, 4 } }, out = { 254065, 1 }, oq = 3, bop = true },
    [1257459] = { name = "Netherpearl Cuffs", t = { 1, 220, 235, 250 }, scroll = 254068, train = 205, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 18 }, { 8343, 3 }, { 249430, 6 }, { 249409, 4 }, { 7971, 10 }, { 11175, 4 } }, out = { 254067, 1 }, oq = 3, bop = true },
    [1257460] = { name = "Nethershine Cuffs", t = { 1, 220, 235, 250 }, scroll = 254070, train = 205, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 18 }, { 8343, 3 }, { 249430, 6 }, { 249409, 4 }, { 13926, 10 }, { 11175, 4 } }, out = { 254069, 1 }, oq = 3, bop = true },
    [1257461] = { name = "Netherlight Cuffs", t = { 1, 220, 235, 250 }, scroll = 254072, train = 205, sq = 3, favor = 60, favorRep = 5, r = { { 4339, 18 }, { 8343, 3 }, { 249430, 6 }, { 249409, 4 }, { 11178, 10 }, { 11175, 4 } }, out = { 254071, 1 }, oq = 3, bop = true },
    [1257462] = { name = "Ghostweave Cord", t = { 1, 230, 245, 260 }, scroll = 254074, train = 215, sq = 2, r = { { 14048, 4 }, { 9210, 1 }, { 14227, 1 }, { 14341, 1 } }, out = { 254073, 1 }, oq = 2 },
    [1257463] = { name = "Earthenweave Gloves", t = { 1, 230, 245, 260 }, scroll = 254076, train = 215, sq = 2, r = { { 14048, 6 }, { 7076, 1 }, { 14341, 1 } }, out = { 254075, 1 }, oq = 2 },
    [1257464] = { name = "Earthenweave Cord", t = { 1, 230, 245, 260 }, scroll = 254078, train = 215, sq = 2, r = { { 14048, 4 }, { 7076, 2 }, { 14341, 1 } }, out = { 254077, 1 }, oq = 2 },
    [1257465] = { name = "Runecloth Reagent Bag", t = { 1, 230, 245, 260 }, scroll = 254080, train = 215, sq = 2, favor = 60, favorRep = 5, r = { { 14048, 5 }, { 8170, 2 }, { 14341, 1 }, { 249431, 1 } }, out = { 254079, 1 }, oq = 1 },
    [1257466] = { name = "Gilded Waistcord", t = { 1, 230, 245, 260 }, scroll = 254082, train = 215, sq = 3, favor = 60, favorRep = 5, r = { { 14048, 8 }, { 8343, 4 }, { 249430, 8 }, { 249409, 5 }, { 3577, 12 } }, out = { 254081, 1 }, oq = 3, bop = true },
    [1257467] = { name = "Frothing Waistcord", t = { 1, 230, 245, 260 }, scroll = 254084, train = 215, sq = 3, favor = 60, favorRep = 5, r = { { 14048, 8 }, { 8343, 4 }, { 249430, 8 }, { 249409, 5 }, { 7079, 12 } }, out = { 254083, 1 }, oq = 3, bop = true },
    [1257468] = { name = "Fiery Waistcord", t = { 1, 230, 245, 260 }, scroll = 254086, train = 215, sq = 3, favor = 60, favorRep = 5, r = { { 14048, 8 }, { 8343, 4 }, { 249430, 8 }, { 249409, 5 }, { 7077, 12 } }, out = { 254085, 1 }, oq = 3, bop = true },
    [1257469] = { name = "Black Waistcord", t = { 1, 230, 245, 260 }, scroll = 254088, train = 215, sq = 3, favor = 60, favorRep = 5, r = { { 14048, 8 }, { 8343, 4 }, { 249430, 8 }, { 249409, 5 }, { 7971, 12 } }, out = { 254087, 1 }, oq = 3, bop = true },
    [1257470] = { name = "Golden Waistcord", t = { 1, 230, 245, 260 }, scroll = 254090, train = 215, sq = 3, favor = 60, favorRep = 5, r = { { 14048, 8 }, { 8343, 4 }, { 249430, 8 }, { 249409, 5 }, { 13926, 12 } }, out = { 254089, 1 }, oq = 3, bop = true },
    [1257471] = { name = "Radiant Waistcord", t = { 1, 230, 245, 260 }, scroll = 254092, train = 215, sq = 3, favor = 60, favorRep = 5, r = { { 14048, 8 }, { 8343, 4 }, { 249430, 8 }, { 249409, 5 }, { 11178, 12 } }, out = { 254091, 1 }, oq = 3, bop = true },
    [1257472] = { name = "Earthenweave Boots", t = { 1, 240, 255, 270 }, scroll = 254094, train = 225, sq = 2, r = { { 14048, 4 }, { 7076, 2 }, { 8170, 2 }, { 14341, 1 } }, out = { 254093, 1 }, oq = 2 },
    [1257479] = { name = "Gilded Sandals", t = { 1, 250, 265, 280 }, scroll = 254108, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 14048, 10 }, { 8343, 4 }, { 249430, 10 }, { 249409, 6 }, { 3577, 14 }, { 249427, 4 } }, out = { 254107, 1 }, oq = 3, bop = true },
    [1257480] = { name = "Frothing Sandals", t = { 1, 250, 265, 280 }, scroll = 254110, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 14048, 10 }, { 8343, 4 }, { 249430, 10 }, { 249409, 6 }, { 7079, 14 }, { 249427, 4 } }, out = { 254109, 1 }, oq = 3, bop = true },
    [1257481] = { name = "Fiery Sandals", t = { 1, 250, 265, 280 }, scroll = 254112, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 14048, 10 }, { 8343, 4 }, { 249430, 10 }, { 249409, 6 }, { 7077, 14 }, { 249427, 4 } }, out = { 254111, 1 }, oq = 3, bop = true },
    [1257482] = { name = "Black Sandals", t = { 1, 250, 265, 280 }, scroll = 254114, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 14048, 10 }, { 8343, 4 }, { 249430, 10 }, { 249409, 6 }, { 7971, 14 }, { 249427, 4 } }, out = { 254113, 1 }, oq = 3, bop = true },
    [1257483] = { name = "Golden Sandals", t = { 1, 250, 265, 280 }, scroll = 254116, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 14048, 10 }, { 8343, 4 }, { 249430, 10 }, { 249409, 6 }, { 13926, 14 }, { 249427, 4 } }, out = { 254115, 1 }, oq = 3, bop = true },
    [1257484] = { name = "Radiant Sandals", t = { 1, 250, 265, 280 }, scroll = 254118, train = 235, sq = 3, favor = 90, favorRep = 6, r = { { 14048, 10 }, { 8343, 4 }, { 249430, 10 }, { 249409, 6 }, { 11178, 14 }, { 249427, 4 } }, out = { 254117, 1 }, oq = 3, bop = true },
    [1257485] = { name = "Earthenweave Mantle", t = { 1, 255, 270, 285 }, scroll = 254120, train = 240, sq = 2, r = { { 14048, 6 }, { 7076, 1 }, { 14341, 1 } }, out = { 254119, 1 }, oq = 2 },
    [1257486] = { name = "Earthenweave Vest", t = { 1, 265, 280, 295 }, scroll = 254122, train = 250, sq = 2, r = { { 14048, 8 }, { 7076, 1 }, { 14341, 1 } }, out = { 254121, 1 }, oq = 2 },
    [1257487] = { name = "Runecloth Cuffs", t = { 1, 265, 280, 295 }, scroll = 254124, train = 250, scrollPrice = 100000, sq = 2, r = { { 14048, 5 }, { 14227, 1 }, { 14341, 1 } }, out = { 254123, 1 }, oq = 2 },
    [1257488] = { name = "Earthenweave Leggings", t = { 1, 260, 275, 290 }, scroll = 254126, train = 245, sq = 2, r = { { 14048, 6 }, { 7076, 2 }, { 14341, 1 } }, out = { 254125, 1 }, oq = 2 },
    [1257489] = { name = "Ghostweave Mantle", t = { 1, 265, 280, 295 }, scroll = 254128, train = 250, sq = 2, r = { { 14048, 5 }, { 9210, 3 }, { 14227, 1 }, { 14341, 1 } }, out = { 254127, 1 }, oq = 2 },
    [1257490] = { name = "Ghostweave Boots", t = { 1, 265, 280, 295 }, scroll = 254130, train = 255, sq = 2, r = { { 14048, 4 }, { 9210, 2 }, { 14227, 1 }, { 8170, 2 }, { 14341, 1 } }, out = { 254129, 1 }, oq = 2 },
    [1257491] = { name = "Earthenweave Cuffs", t = { 1, 270, 285, 300 }, scroll = 254132, train = 255, sq = 2, r = { { 14048, 5 }, { 7076, 1 }, { 14341, 1 } }, out = { 254131, 1 }, oq = 2 },
    [1257492] = { name = "Mooncloth Reagent Bag", t = { 1, 270, 285, 300 }, scroll = 254134, train = 255, sq = 2, r = { { 14048, 4 }, { 14342, 1 }, { 14341, 1 }, { 249431, 10 }, { 249430, 1 }, { 249409, 1 } }, out = { 254133, 1 }, oq = 1 },
    [1257493] = { name = "Ghostweave Hood", t = { 1, 275, 290, 305 }, scroll = 254136, train = 260, sq = 2, r = { { 14048, 6 }, { 9210, 3 }, { 14227, 2 }, { 14341, 1 } }, out = { 254135, 1 }, oq = 2 },
    [1257494] = { name = "Earthenweave Crown", t = { 1, 275, 290, 305 }, scroll = 254138, train = 260, sq = 2, r = { { 14048, 6 }, { 7076, 3 }, { 14341, 1 } }, out = { 254137, 1 }, oq = 2 },
    [1257495] = { name = "Bottomless Reagent Bag", t = { 1, 315, 330, 345 }, scroll = 254140, train = 300, sq = 2, r = { { 14048, 8 }, { 14342, 12 }, { 14344, 2 }, { 249427, 5 }, { 14341, 2 }, { 249428, 5 }, { 249429, 5 } }, out = { 254139, 1 }, oq = 1 },
    [1263032] = { name = "Spinning Wheel", t = { 1, 140, 140, 140 }, scroll = 273099, train = 140, sq = 2, r = { { 4470, 2 }, { 4305, 5 }, { 2321, 3 } }, out = { 279943, 1 }, oq = 1 },
    [1263425] = { name = "Faction Banner", t = { 1, 20, 20, 20 }, fee = 0, train = 20, faction = "Alliance", r = { { 2996, 1 }, { 2320, 1 } }, out = { 279973, 1 }, oq = 1 },
    [1292941] = { name = "Manaflare Pants", t = { 1, 320, 325, 330 }, scroll = 273972, train = 300, sq = 4, r = { { 274030, 5 }, { 14342, 3 }, { 14048, 22 }, { 14341, 8 } }, out = { 273904, 1 }, oq = 1 },
    [1292942] = { name = "Manaflare Gloves", t = { 1, 320, 325, 330 }, scroll = 273973, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273905, 1 }, oq = 1 },
    [1292943] = { name = "Manaflare Mantle", t = { 1, 320, 325, 330 }, scroll = 273974, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273906, 1 }, oq = 1 },
    [1292944] = { name = "Manaflare Boots", t = { 1, 320, 325, 330 }, scroll = 273975, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273907, 1 }, oq = 1 },
    [1292957] = { name = "Pants of Conviction", t = { 1, 320, 325, 330 }, scroll = 273988, train = 300, sq = 4, r = { { 274030, 5 }, { 14342, 3 }, { 14048, 22 }, { 14341, 8 } }, out = { 273920, 1 }, oq = 1 },
    [1292958] = { name = "Gloves of Conviction", t = { 1, 320, 325, 330 }, scroll = 273989, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273921, 1 }, oq = 1 },
    [1292959] = { name = "Mantle of Conviction", t = { 1, 320, 325, 330 }, scroll = 273990, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273922, 1 }, oq = 1 },
    [1292960] = { name = "Treads of Conviction", t = { 1, 320, 325, 330 }, scroll = 273991, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273923, 1 }, oq = 1 },
    [1292961] = { name = "Leggings of Conviction", t = { 1, 320, 325, 330 }, scroll = 273992, train = 300, sq = 4, r = { { 274030, 5 }, { 14342, 3 }, { 14048, 22 }, { 14341, 8 } }, out = { 273924, 1 }, oq = 1 },
    [1292962] = { name = "Handguards of Conviction", t = { 1, 320, 325, 330 }, scroll = 273993, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273925, 1 }, oq = 1 },
    [1292963] = { name = "Pauldrons of Conviction", t = { 1, 320, 325, 330 }, scroll = 273994, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273926, 1 }, oq = 1 },
    [1292964] = { name = "Boots of Conviction", t = { 1, 320, 325, 330 }, scroll = 273995, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273927, 1 }, oq = 1 },
    [1292977] = { name = "Demonheart Leggings", t = { 1, 320, 325, 330 }, scroll = 274008, train = 300, sq = 4, r = { { 274030, 5 }, { 14342, 3 }, { 14048, 22 }, { 14341, 8 } }, out = { 273940, 1 }, oq = 1 },
    [1292978] = { name = "Demonheart Gloves", t = { 1, 320, 325, 330 }, scroll = 274009, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273941, 1 }, oq = 1 },
    [1292979] = { name = "Demonheart Spaulders", t = { 1, 320, 325, 330 }, scroll = 274010, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273942, 1 }, oq = 1 },
    [1292980] = { name = "Demonheart Boots", t = { 1, 320, 325, 330 }, scroll = 274011, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 2 }, { 14048, 16 }, { 14341, 8 } }, out = { 273943, 1 }, oq = 1 },
    [1297120] = { name = "Venomspew Gloves", t = { 1, 290, 292, 295 }, scroll = 275580, train = 285, scrollPrice = 75000, rep = { 609, 4 }, sq = 3, r = { { 14048, 4 }, { 14343, 1 }, { 7082, 3 }, { 14341, 6 } }, out = { 275604, 1 }, oq = 3 },
    [1297121] = { name = "Venomspew Cord", t = { 1, 295, 297, 300 }, scroll = 275581, train = 290, scrollPrice = 75000, rep = { 609, 5 }, sq = 3, r = { { 14048, 6 }, { 14343, 1 }, { 7082, 3 }, { 14341, 6 } }, out = { 275605, 1 }, oq = 3 },
    [1297122] = { name = "Venomspew Footpads", t = { 1, 295, 297, 300 }, scroll = 275582, train = 295, scrollPrice = 75000, rep = { 609, 5 }, sq = 3, r = { { 14048, 5 }, { 14343, 1 }, { 7082, 3 }, { 14341, 6 } }, out = { 275606, 1 }, oq = 3 },
    [1297123] = { name = "Swarmtender's Gloves", t = { 1, 290, 292, 295 }, scroll = 275583, train = 285, scrollPrice = 75000, rep = { 609, 4 }, sq = 3, r = { { 14048, 4 }, { 14343, 1 }, { 7080, 3 }, { 14341, 6 } }, out = { 275607, 1 }, oq = 3 },
    [1297124] = { name = "Swarmtender's Cord", t = { 1, 295, 297, 300 }, scroll = 275584, train = 290, scrollPrice = 75000, rep = { 609, 5 }, sq = 3, r = { { 14048, 6 }, { 14343, 1 }, { 7080, 3 }, { 14341, 6 } }, out = { 275608, 1 }, oq = 3 },
    [1297125] = { name = "Swarmtender's Footpads", t = { 1, 295, 297, 300 }, scroll = 275585, train = 295, scrollPrice = 75000, rep = { 609, 5 }, sq = 3, r = { { 14048, 5 }, { 14343, 1 }, { 7080, 3 }, { 14341, 6 } }, out = { 275609, 1 }, oq = 3 },
    [1301439] = { name = "Cloudy Stormsewn Vest", t = { 1, 65, 67, 70 }, scroll = 276946, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2996, 5 }, { 2320, 2 } }, out = { 277010, 1 }, oq = 2 },
    [1301440] = { name = "Cloudy Stormsewn Cuffs", t = { 1, 55, 57, 60 }, scroll = 276947, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2996, 3 }, { 2320, 3 } }, out = { 277011, 1 }, oq = 2 },
    [1301441] = { name = "Cloudy Stormsewn Handwraps", t = { 1, 60, 62, 65 }, scroll = 276948, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2996, 4 }, { 2320, 4 } }, out = { 277012, 1 }, oq = 2 },
    [1301442] = { name = "Cloudy Stormsewn Cord", t = { 1, 55, 57, 60 }, scroll = 276949, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2996, 3 }, { 2320, 3 } }, out = { 277013, 1 }, oq = 2 },
    [1301443] = { name = "Cloudy Stormsewn Leggings", t = { 1, 65, 67, 70 }, scroll = 276950, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2996, 5 }, { 2320, 2 } }, out = { 277014, 1 }, oq = 2 },
    [1301444] = { name = "Cloudy Stormsewn Shoes", t = { 1, 60, 62, 65 }, scroll = 276951, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2996, 4 }, { 2320, 3 } }, out = { 277015, 1 }, oq = 2 },
    [1301463] = { name = "Azure Stormsewn Vest", t = { 1, 65, 67, 70 }, scroll = 276970, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2996, 5 }, { 2320, 2 } }, out = { 277034, 1 }, oq = 2 },
    [1301464] = { name = "Azure Stormsewn Cuffs", t = { 1, 55, 57, 60 }, scroll = 276971, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2996, 3 }, { 2320, 3 } }, out = { 277035, 1 }, oq = 2 },
    [1301465] = { name = "Azure Stormsewn Handwraps", t = { 1, 60, 62, 65 }, scroll = 276972, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2996, 4 }, { 2320, 4 } }, out = { 277036, 1 }, oq = 2 },
    [1301466] = { name = "Azure Stormsewn Cord", t = { 1, 55, 57, 60 }, scroll = 276973, train = 50, scrollPrice = 950, rep = { 2758, 4 }, sq = 2, r = { { 2996, 3 }, { 2320, 3 } }, out = { 277037, 1 }, oq = 2 },
    [1301468] = { name = "Azure Stormsewn Leggings", t = { 1, 65, 67, 70 }, scroll = 276974, train = 60, scrollPrice = 1250, rep = { 2758, 5 }, sq = 2, r = { { 2996, 5 }, { 2320, 2 } }, out = { 277038, 1 }, oq = 2 },
    [1301469] = { name = "Azure Stormsewn Shoes", t = { 1, 60, 62, 65 }, scroll = 276975, train = 55, scrollPrice = 1100, rep = { 2758, 4 }, sq = 2, r = { { 2996, 4 }, { 2320, 3 } }, out = { 277039, 1 }, oq = 2 },
    [1301532] = { name = "Cloudy Stormsewn Cowl", t = { 1, 185, 187, 190 }, scroll = 276982, train = 175, scrollPrice = 100000, rep = { 2787, 4 }, sq = 2, r = { { 4305, 7 }, { 11134, 2 }, { 8343, 1 }, { 2324, 8 } }, out = { 277046, 1 }, oq = 2 },
    [1301533] = { name = "Cloudy Stormsewn Epaulets", t = { 1, 185, 187, 190 }, scroll = 276983, train = 175, scrollPrice = 100000, rep = { 2787, 4 }, sq = 2, r = { { 4305, 5 }, { 11134, 1 }, { 8343, 1 }, { 2324, 6 } }, out = { 277047, 1 }, oq = 2 },
    [1301540] = { name = "Azure Stormsewn Cowl", t = { 1, 185, 187, 190 }, scroll = 276990, train = 175, scrollPrice = 100000, rep = { 2740, 4 }, sq = 2, r = { { 4305, 7 }, { 11134, 2 }, { 8343, 1 }, { 6260, 4 } }, out = { 277054, 1 }, oq = 2 },
    [1301541] = { name = "Azure Stormsewn Epaulets", t = { 1, 185, 187, 190 }, scroll = 276991, train = 175, scrollPrice = 100000, rep = { 2740, 4 }, sq = 2, r = { { 4305, 5 }, { 11134, 1 }, { 8343, 1 }, { 6260, 3 } }, out = { 277055, 1 }, oq = 2 },
    [1306540] = { name = "Robes of Fiery Devastation", t = { 1, 310, 317, 325 }, scroll = 279315, train = 300, sq = 4, r = { { 274030, 3 }, { 14342, 3 }, { 14048, 9 } }, out = { 279266, 1 }, oq = 4 },
    [1306541] = { name = "Mana-infused Cord", t = { 1, 310, 317, 325 }, scroll = 279316, train = 300, sq = 4, r = { { 274030, 2 }, { 14342, 2 }, { 14048, 7 } }, out = { 279267, 1 }, oq = 4 },
    [1306542] = { name = "Rime-encrusted Boots", t = { 1, 310, 317, 325 }, scroll = 279317, train = 300, sq = 4, r = { { 274030, 2 }, { 14342, 2 }, { 14048, 7 } }, out = { 279268, 1 }, oq = 4 },
    [1306543] = { name = "Fel Cape", t = { 1, 310, 317, 325 }, scroll = 279318, train = 300, sq = 4, r = { { 274030, 1 }, { 14342, 1 }, { 14048, 5 } }, out = { 279269, 1 }, oq = 4 },
    [1306544] = { name = "Cloak of Earth and Sky", t = { 1, 310, 317, 325 }, scroll = 279319, train = 300, sq = 4, r = { { 274030, 1 }, { 14342, 1 }, { 14048, 5 } }, out = { 279270, 1 }, oq = 4 },
    [1306545] = { name = "Felblood Soul Bag", t = { 1, 310, 317, 325 }, scroll = 279320, train = 300, sq = 4, r = { { 14256, 8 }, { 14048, 6 } }, out = { 279271, 1 }, oq = 4 },
  },
}

-- Herramientas: [categoría] = { objeto, máscara } (un bastón superior cubre a los inferiores)
ES.Data.Tools = ES.Data.Tools or {}
ES.Data.Tools[12] = { item = 9149, mask = 1, family = "stone" }
ES.Data.Tools[14] = { item = 6219, mask = 1, family = "spanner" }
ES.Data.Tools[15] = { item = 10498, mask = 2, family = "adjustor" }
ES.Data.Tools[162] = { item = 5956, mask = 4, family = "hammer" }
ES.Data.Tools[373] = { item = 6218, mask = 1, family = "rod" }
ES.Data.Tools[374] = { item = 6339, mask = 3, family = "rod" }
ES.Data.Tools[375] = { item = 11130, mask = 7, family = "rod" }
ES.Data.Tools[376] = { item = 11145, mask = 15, family = "rod" }
ES.Data.Tools[377] = { item = 16207, mask = 31, family = "rod" }

ES.Data.VendorPrices = ES.Data.VendorPrices or {}
ES.Data.SellPrices = ES.Data.SellPrices or {}
ES.Data.VendorPrices[929] = 300
ES.Data.VendorPrices[2320] = 10
ES.Data.VendorPrices[2321] = 100
ES.Data.VendorPrices[2324] = 25
ES.Data.VendorPrices[2325] = 1000
ES.Data.VendorPrices[2604] = 50
ES.Data.VendorPrices[2605] = 100
ES.Data.VendorPrices[4291] = 500
ES.Data.VendorPrices[4340] = 350
ES.Data.VendorPrices[4341] = 500
ES.Data.VendorPrices[4342] = 2500
ES.Data.VendorPrices[4470] = 38
ES.Data.VendorPrices[6260] = 50
ES.Data.VendorPrices[6261] = 1000
ES.Data.VendorPrices[8343] = 2000
ES.Data.VendorPrices[10290] = 2500
ES.Data.VendorPrices[14341] = 5000
ES.Data.SellPrices[814] = 25
ES.Data.SellPrices[929] = 75
ES.Data.SellPrices[1210] = 250
ES.Data.SellPrices[1529] = 700
ES.Data.SellPrices[2318] = 15
ES.Data.SellPrices[2319] = 50
ES.Data.SellPrices[2320] = 2
ES.Data.SellPrices[2321] = 25
ES.Data.SellPrices[2324] = 6
ES.Data.SellPrices[2325] = 250
ES.Data.SellPrices[2568] = 31
ES.Data.SellPrices[2569] = 87
ES.Data.SellPrices[2570] = 11
ES.Data.SellPrices[2572] = 99
ES.Data.SellPrices[2575] = 25
ES.Data.SellPrices[2576] = 75
ES.Data.SellPrices[2577] = 75
ES.Data.SellPrices[2578] = 224
ES.Data.SellPrices[2579] = 37
ES.Data.SellPrices[2580] = 67
ES.Data.SellPrices[2582] = 216
ES.Data.SellPrices[2583] = 359
ES.Data.SellPrices[2584] = 142
ES.Data.SellPrices[2585] = 638
ES.Data.SellPrices[2587] = 200
ES.Data.SellPrices[2589] = 13
ES.Data.SellPrices[2592] = 33
ES.Data.SellPrices[2604] = 12
ES.Data.SellPrices[2605] = 25
ES.Data.SellPrices[2842] = 100
ES.Data.SellPrices[2996] = 40
ES.Data.SellPrices[2997] = 100
ES.Data.SellPrices[3182] = 387
ES.Data.SellPrices[3383] = 100
ES.Data.SellPrices[3577] = 600
ES.Data.SellPrices[3824] = 150
ES.Data.SellPrices[3827] = 120
ES.Data.SellPrices[3829] = 150
ES.Data.SellPrices[3864] = 800
ES.Data.SellPrices[4234] = 150
ES.Data.SellPrices[4238] = 200
ES.Data.SellPrices[4240] = 300
ES.Data.SellPrices[4241] = 450
ES.Data.SellPrices[4245] = 2000
ES.Data.SellPrices[4291] = 125
ES.Data.SellPrices[4304] = 300
ES.Data.SellPrices[4305] = 600
ES.Data.SellPrices[4306] = 150
ES.Data.SellPrices[4307] = 29
ES.Data.SellPrices[4308] = 45
ES.Data.SellPrices[4309] = 226
ES.Data.SellPrices[4310] = 180
ES.Data.SellPrices[4311] = 475
ES.Data.SellPrices[4312] = 237
ES.Data.SellPrices[4313] = 416
ES.Data.SellPrices[4314] = 331
ES.Data.SellPrices[4315] = 425
ES.Data.SellPrices[4316] = 743
ES.Data.SellPrices[4317] = 1076
ES.Data.SellPrices[4318] = 610
ES.Data.SellPrices[4319] = 815
ES.Data.SellPrices[4320] = 979
ES.Data.SellPrices[4321] = 1120
ES.Data.SellPrices[4322] = 1810
ES.Data.SellPrices[4323] = 1999
ES.Data.SellPrices[4324] = 1874
ES.Data.SellPrices[4325] = 2272
ES.Data.SellPrices[4326] = 2496
ES.Data.SellPrices[4327] = 3788
ES.Data.SellPrices[4328] = 1524
ES.Data.SellPrices[4329] = 2120
ES.Data.SellPrices[4330] = 250
ES.Data.SellPrices[4331] = 526
ES.Data.SellPrices[4332] = 500
ES.Data.SellPrices[4333] = 1200
ES.Data.SellPrices[4334] = 550
ES.Data.SellPrices[4335] = 1500
ES.Data.SellPrices[4336] = 1500
ES.Data.SellPrices[4337] = 750
ES.Data.SellPrices[4338] = 250
ES.Data.SellPrices[4339] = 1250
ES.Data.SellPrices[4340] = 87
ES.Data.SellPrices[4341] = 125
ES.Data.SellPrices[4342] = 625
ES.Data.SellPrices[4343] = 60
ES.Data.SellPrices[4344] = 11
ES.Data.SellPrices[4470] = 9
ES.Data.SellPrices[4589] = 530
ES.Data.SellPrices[4625] = 250
ES.Data.SellPrices[5498] = 200
ES.Data.SellPrices[5500] = 750
ES.Data.SellPrices[5542] = 370
ES.Data.SellPrices[5762] = 250
ES.Data.SellPrices[5763] = 700
ES.Data.SellPrices[5764] = 3000
ES.Data.SellPrices[5765] = 4000
ES.Data.SellPrices[5766] = 1338
ES.Data.SellPrices[5770] = 1807
ES.Data.SellPrices[6037] = 1250
ES.Data.SellPrices[6048] = 100
ES.Data.SellPrices[6238] = 98
ES.Data.SellPrices[6239] = 160
ES.Data.SellPrices[6240] = 161
ES.Data.SellPrices[6241] = 99
ES.Data.SellPrices[6242] = 243
ES.Data.SellPrices[6243] = 445
ES.Data.SellPrices[6260] = 12
ES.Data.SellPrices[6261] = 250
ES.Data.SellPrices[6263] = 589
ES.Data.SellPrices[6264] = 884
ES.Data.SellPrices[6371] = 12
ES.Data.SellPrices[6384] = 250
ES.Data.SellPrices[6385] = 250
ES.Data.SellPrices[6786] = 59
ES.Data.SellPrices[6787] = 466
ES.Data.SellPrices[6795] = 500
ES.Data.SellPrices[6796] = 750
ES.Data.SellPrices[7026] = 22
ES.Data.SellPrices[7027] = 1125
ES.Data.SellPrices[7046] = 1494
ES.Data.SellPrices[7047] = 824
ES.Data.SellPrices[7048] = 745
ES.Data.SellPrices[7049] = 914
ES.Data.SellPrices[7050] = 999
ES.Data.SellPrices[7051] = 2696
ES.Data.SellPrices[7052] = 1488
ES.Data.SellPrices[7053] = 2240
ES.Data.SellPrices[7054] = 4700
ES.Data.SellPrices[7055] = 1503
ES.Data.SellPrices[7056] = 2314
ES.Data.SellPrices[7057] = 2323
ES.Data.SellPrices[7058] = 2052
ES.Data.SellPrices[7059] = 2781
ES.Data.SellPrices[7060] = 2791
ES.Data.SellPrices[7061] = 2017
ES.Data.SellPrices[7062] = 2430
ES.Data.SellPrices[7063] = 4741
ES.Data.SellPrices[7064] = 2569
ES.Data.SellPrices[7065] = 2398
ES.Data.SellPrices[7067] = 400
ES.Data.SellPrices[7068] = 400
ES.Data.SellPrices[7069] = 400
ES.Data.SellPrices[7070] = 400
ES.Data.SellPrices[7071] = 100
ES.Data.SellPrices[7072] = 150
ES.Data.SellPrices[7076] = 400
ES.Data.SellPrices[7077] = 400
ES.Data.SellPrices[7078] = 400
ES.Data.SellPrices[7079] = 400
ES.Data.SellPrices[7080] = 400
ES.Data.SellPrices[7082] = 400
ES.Data.SellPrices[7910] = 5000
ES.Data.SellPrices[7971] = 1000
ES.Data.SellPrices[7972] = 400
ES.Data.SellPrices[8153] = 5
ES.Data.SellPrices[8170] = 500
ES.Data.SellPrices[8343] = 500
ES.Data.SellPrices[8831] = 300
ES.Data.SellPrices[9210] = 750
ES.Data.SellPrices[9998] = 4815
ES.Data.SellPrices[9999] = 4832
ES.Data.SellPrices[10001] = 5257
ES.Data.SellPrices[10002] = 5276
ES.Data.SellPrices[10003] = 2859
ES.Data.SellPrices[10004] = 5738
ES.Data.SellPrices[10007] = 5799
ES.Data.SellPrices[10008] = 3492
ES.Data.SellPrices[10009] = 5284
ES.Data.SellPrices[10010] = 5729
ES.Data.SellPrices[10011] = 2875
ES.Data.SellPrices[10018] = 3275
ES.Data.SellPrices[10019] = 3944
ES.Data.SellPrices[10020] = 6597
ES.Data.SellPrices[10021] = 7946
ES.Data.SellPrices[10023] = 3334
ES.Data.SellPrices[10024] = 5421
ES.Data.SellPrices[10025] = 6790
ES.Data.SellPrices[10026] = 5459
ES.Data.SellPrices[10027] = 5479
ES.Data.SellPrices[10028] = 5938
ES.Data.SellPrices[10029] = 5391
ES.Data.SellPrices[10030] = 6007
ES.Data.SellPrices[10031] = 6030
ES.Data.SellPrices[10032] = 6052
ES.Data.SellPrices[10033] = 6075
ES.Data.SellPrices[10034] = 2000
ES.Data.SellPrices[10035] = 1735
ES.Data.SellPrices[10036] = 1741
ES.Data.SellPrices[10038] = 6620
ES.Data.SellPrices[10039] = 7110
ES.Data.SellPrices[10040] = 1767
ES.Data.SellPrices[10041] = 8593
ES.Data.SellPrices[10042] = 6644
ES.Data.SellPrices[10044] = 6765
ES.Data.SellPrices[10045] = 23
ES.Data.SellPrices[10046] = 32
ES.Data.SellPrices[10047] = 164
ES.Data.SellPrices[10048] = 935
ES.Data.SellPrices[10050] = 2500
ES.Data.SellPrices[10051] = 2500
ES.Data.SellPrices[10052] = 1500
ES.Data.SellPrices[10053] = 4499
ES.Data.SellPrices[10054] = 3000
ES.Data.SellPrices[10055] = 3000
ES.Data.SellPrices[10056] = 1500
ES.Data.SellPrices[10285] = 1000
ES.Data.SellPrices[10286] = 400
ES.Data.SellPrices[10290] = 625
ES.Data.SellPrices[11040] = 1
ES.Data.SellPrices[11082] = 1
ES.Data.SellPrices[11134] = 1
ES.Data.SellPrices[11137] = 1
ES.Data.SellPrices[11175] = 1
ES.Data.SellPrices[11176] = 1
ES.Data.SellPrices[11178] = 1
ES.Data.SellPrices[12360] = 5000
ES.Data.SellPrices[12364] = 10000
ES.Data.SellPrices[12662] = 600
ES.Data.SellPrices[12800] = 10000
ES.Data.SellPrices[12803] = 500
ES.Data.SellPrices[12804] = 2000
ES.Data.SellPrices[12808] = 1000
ES.Data.SellPrices[12809] = 10000
ES.Data.SellPrices[12810] = 500
ES.Data.SellPrices[12811] = 20000
ES.Data.SellPrices[13468] = 1000
ES.Data.SellPrices[13856] = 5112
ES.Data.SellPrices[13857] = 10878
ES.Data.SellPrices[13858] = 10917
ES.Data.SellPrices[13860] = 8741
ES.Data.SellPrices[13863] = 6617
ES.Data.SellPrices[13864] = 9553
ES.Data.SellPrices[13865] = 13555
ES.Data.SellPrices[13866] = 11358
ES.Data.SellPrices[13867] = 12570
ES.Data.SellPrices[13868] = 9665
ES.Data.SellPrices[13869] = 9702
ES.Data.SellPrices[13870] = 5471
ES.Data.SellPrices[13871] = 13436
ES.Data.SellPrices[13926] = 10000
ES.Data.SellPrices[14042] = 10561
ES.Data.SellPrices[14043] = 5955
ES.Data.SellPrices[14044] = 9503
ES.Data.SellPrices[14045] = 13480
ES.Data.SellPrices[14046] = 5000
ES.Data.SellPrices[14047] = 400
ES.Data.SellPrices[14048] = 2000
ES.Data.SellPrices[14100] = 12089
ES.Data.SellPrices[14101] = 6066
ES.Data.SellPrices[14103] = 9716
ES.Data.SellPrices[14104] = 15484
ES.Data.SellPrices[14106] = 18053
ES.Data.SellPrices[14107] = 13140
ES.Data.SellPrices[14108] = 11112
ES.Data.SellPrices[14111] = 10775
ES.Data.SellPrices[14112] = 13509
ES.Data.SellPrices[14128] = 16093
ES.Data.SellPrices[14130] = 12768
ES.Data.SellPrices[14132] = 12441
ES.Data.SellPrices[14134] = 11280
ES.Data.SellPrices[14136] = 17025
ES.Data.SellPrices[14137] = 18113
ES.Data.SellPrices[14138] = 20042
ES.Data.SellPrices[14139] = 15840
ES.Data.SellPrices[14140] = 16693
ES.Data.SellPrices[14141] = 12859
ES.Data.SellPrices[14142] = 6087
ES.Data.SellPrices[14143] = 5763
ES.Data.SellPrices[14144] = 14374
ES.Data.SellPrices[14146] = 14084
ES.Data.SellPrices[14152] = 28815
ES.Data.SellPrices[14153] = 28920
ES.Data.SellPrices[14154] = 29028
ES.Data.SellPrices[14155] = 20000
ES.Data.SellPrices[14156] = 40000
ES.Data.SellPrices[14227] = 2500
ES.Data.SellPrices[14256] = 2000
ES.Data.SellPrices[14341] = 1250
ES.Data.SellPrices[14342] = 4000
ES.Data.SellPrices[14343] = 1
ES.Data.SellPrices[14344] = 1
ES.Data.SellPrices[15407] = 500
ES.Data.SellPrices[15802] = 11648
ES.Data.SellPrices[16203] = 1
ES.Data.SellPrices[16979] = 14902
ES.Data.SellPrices[16980] = 21365
ES.Data.SellPrices[17010] = 2000
ES.Data.SellPrices[17011] = 2000
ES.Data.SellPrices[17012] = 1000
ES.Data.SellPrices[17723] = 750
ES.Data.SellPrices[18263] = 16911
ES.Data.SellPrices[18405] = 14744
ES.Data.SellPrices[18407] = 11139
ES.Data.SellPrices[18408] = 11178
ES.Data.SellPrices[18409] = 11219
ES.Data.SellPrices[18413] = 17070
ES.Data.SellPrices[18486] = 21683
ES.Data.SellPrices[19047] = 9232
ES.Data.SellPrices[19050] = 18758
ES.Data.SellPrices[19056] = 12941
ES.Data.SellPrices[19059] = 17541
ES.Data.SellPrices[19156] = 34911
ES.Data.SellPrices[19165] = 45006
ES.Data.SellPrices[19682] = 25035
ES.Data.SellPrices[19683] = 25129
ES.Data.SellPrices[19684] = 18915
ES.Data.SellPrices[19726] = 500
ES.Data.SellPrices[20381] = 5000
ES.Data.SellPrices[20520] = 2000
ES.Data.SellPrices[20537] = 17736
ES.Data.SellPrices[20538] = 23733
ES.Data.SellPrices[20539] = 11908
ES.Data.SellPrices[21154] = 1
ES.Data.SellPrices[21340] = 5000
ES.Data.SellPrices[21341] = 20000
ES.Data.SellPrices[21342] = 80000
ES.Data.SellPrices[21542] = 1
ES.Data.SellPrices[22246] = 2500
ES.Data.SellPrices[22248] = 10000
ES.Data.SellPrices[22249] = 30000
ES.Data.SellPrices[22251] = 10000
ES.Data.SellPrices[22252] = 30000
ES.Data.SellPrices[22652] = 69171
ES.Data.SellPrices[22654] = 34846
ES.Data.SellPrices[22655] = 34973
ES.Data.SellPrices[22658] = 53045
ES.Data.SellPrices[22660] = 24601
ES.Data.SellPrices[22682] = 20000
ES.Data.SellPrices[22756] = 33164
ES.Data.SellPrices[22757] = 24961
ES.Data.SellPrices[22758] = 25051
ES.Data.SellPrices[34085] = 7
ES.Data.SellPrices[34087] = 7
ES.Data.SellPrices[210781] = 744
ES.Data.SellPrices[213379] = 280
ES.Data.SellPrices[215365] = 1371
ES.Data.SellPrices[215366] = 864
ES.Data.SellPrices[227844] = 40000
ES.Data.SellPrices[249391] = 100
ES.Data.SellPrices[249409] = 75
ES.Data.SellPrices[249427] = 125
ES.Data.SellPrices[249428] = 250
ES.Data.SellPrices[249429] = 375
ES.Data.SellPrices[249430] = 250
ES.Data.SellPrices[249431] = 375
ES.Data.SellPrices[253664] = 200
ES.Data.SellPrices[253667] = 1250
ES.Data.SellPrices[253889] = 351
ES.Data.SellPrices[253891] = 320
ES.Data.SellPrices[253893] = 323
ES.Data.SellPrices[253895] = 325
ES.Data.SellPrices[253897] = 328
ES.Data.SellPrices[253899] = 330
ES.Data.SellPrices[253913] = 327
ES.Data.SellPrices[253915] = 330
ES.Data.SellPrices[253917] = 341
ES.Data.SellPrices[253919] = 344
ES.Data.SellPrices[253921] = 346
ES.Data.SellPrices[253923] = 349
ES.Data.SellPrices[253925] = 465
ES.Data.SellPrices[253927] = 468
ES.Data.SellPrices[253929] = 471
ES.Data.SellPrices[253931] = 429
ES.Data.SellPrices[253933] = 445
ES.Data.SellPrices[253935] = 448
ES.Data.SellPrices[253949] = 948
ES.Data.SellPrices[253951] = 955
ES.Data.SellPrices[253953] = 962
ES.Data.SellPrices[253955] = 970
ES.Data.SellPrices[253957] = 977
ES.Data.SellPrices[253959] = 984
ES.Data.SellPrices[253961] = 1643
ES.Data.SellPrices[253963] = 1655
ES.Data.SellPrices[253965] = 1548
ES.Data.SellPrices[253967] = 1560
ES.Data.SellPrices[253969] = 1572
ES.Data.SellPrices[253971] = 1584
ES.Data.SellPrices[253973] = 200
ES.Data.SellPrices[253987] = 2076
ES.Data.SellPrices[253989] = 2092
ES.Data.SellPrices[253991] = 2108
ES.Data.SellPrices[253993] = 2124
ES.Data.SellPrices[253995] = 2139
ES.Data.SellPrices[253997] = 2155
ES.Data.SellPrices[253999] = 2990
ES.Data.SellPrices[254013] = 2351
ES.Data.SellPrices[254015] = 2675
ES.Data.SellPrices[254017] = 2095
ES.Data.SellPrices[254019] = 2279
ES.Data.SellPrices[254021] = 2754
ES.Data.SellPrices[254023] = 2773
ES.Data.SellPrices[254025] = 2528
ES.Data.SellPrices[254029] = 2567
ES.Data.SellPrices[254031] = 2656
ES.Data.SellPrices[254033] = 3613
ES.Data.SellPrices[254035] = 200
ES.Data.SellPrices[254049] = 6779
ES.Data.SellPrices[254051] = 6828
ES.Data.SellPrices[254053] = 6879
ES.Data.SellPrices[254055] = 6928
ES.Data.SellPrices[254057] = 6979
ES.Data.SellPrices[254059] = 7028
ES.Data.SellPrices[254061] = 5835
ES.Data.SellPrices[254063] = 5463
ES.Data.SellPrices[254065] = 5505
ES.Data.SellPrices[254067] = 5546
ES.Data.SellPrices[254069] = 5587
ES.Data.SellPrices[254071] = 5628
ES.Data.SellPrices[254073] = 5359
ES.Data.SellPrices[254075] = 5398
ES.Data.SellPrices[254077] = 5437
ES.Data.SellPrices[254079] = 200
ES.Data.SellPrices[254081] = 6149
ES.Data.SellPrices[254083] = 6196
ES.Data.SellPrices[254085] = 6242
ES.Data.SellPrices[254087] = 6289
ES.Data.SellPrices[254089] = 6336
ES.Data.SellPrices[254091] = 6383
ES.Data.SellPrices[254093] = 9030
ES.Data.SellPrices[254107] = 11236
ES.Data.SellPrices[254109] = 11319
ES.Data.SellPrices[254111] = 11704
ES.Data.SellPrices[254113] = 11787
ES.Data.SellPrices[254115] = 11870
ES.Data.SellPrices[254117] = 10816
ES.Data.SellPrices[254119] = 10205
ES.Data.SellPrices[254121] = 15262
ES.Data.SellPrices[254123] = 7688
ES.Data.SellPrices[254125] = 14756
ES.Data.SellPrices[254127] = 12020
ES.Data.SellPrices[254129] = 12714
ES.Data.SellPrices[254131] = 8536
ES.Data.SellPrices[254133] = 200
ES.Data.SellPrices[254135] = 13637
ES.Data.SellPrices[254137] = 12426
ES.Data.SellPrices[254139] = 200
ES.Data.SellPrices[275604] = 9017
ES.Data.SellPrices[275605] = 9050
ES.Data.SellPrices[275606] = 13626
ES.Data.SellPrices[275607] = 9117
ES.Data.SellPrices[275608] = 9149
ES.Data.SellPrices[275609] = 13774
ES.Data.SellPrices[279266] = 21117
ES.Data.SellPrices[279267] = 3262
ES.Data.SellPrices[279268] = 17158
ES.Data.SellPrices[279269] = 9999
ES.Data.SellPrices[279270] = 9999
ES.Data.SellPrices[279271] = 80000

-- Nombre de cada objeto (inglés, del cliente): se muestra mientras el juego no lo ha cargado
ES.Data.ItemNames = ES.Data.ItemNames or {}
ES.Data.ItemNames[814] = "Flask of Oil"
ES.Data.ItemNames[929] = "Healing Potion"
ES.Data.ItemNames[1210] = "Shadowgem"
ES.Data.ItemNames[1529] = "Jade"
ES.Data.ItemNames[2318] = "Light Leather"
ES.Data.ItemNames[2319] = "Medium Leather"
ES.Data.ItemNames[2320] = "Coarse Thread"
ES.Data.ItemNames[2321] = "Fine Thread"
ES.Data.ItemNames[2324] = "Bleach"
ES.Data.ItemNames[2325] = "Black Dye"
ES.Data.ItemNames[2568] = "Brown Linen Vest"
ES.Data.ItemNames[2569] = "Linen Boots"
ES.Data.ItemNames[2570] = "Linen Cloak"
ES.Data.ItemNames[2572] = "Red Linen Robe"
ES.Data.ItemNames[2575] = "Red Linen Shirt"
ES.Data.ItemNames[2576] = "White Linen Shirt"
ES.Data.ItemNames[2577] = "Blue Linen Shirt"
ES.Data.ItemNames[2578] = "Barbaric Linen Vest"
ES.Data.ItemNames[2579] = "Green Linen Shirt"
ES.Data.ItemNames[2580] = "Reinforced Linen Cape"
ES.Data.ItemNames[2582] = "Green Woolen Vest"
ES.Data.ItemNames[2583] = "Woolen Boots"
ES.Data.ItemNames[2584] = "Woolen Cape"
ES.Data.ItemNames[2585] = "Gray Woolen Robe"
ES.Data.ItemNames[2587] = "Gray Woolen Shirt"
ES.Data.ItemNames[2589] = "Linen Cloth"
ES.Data.ItemNames[2592] = "Wool Cloth"
ES.Data.ItemNames[2604] = "Red Dye"
ES.Data.ItemNames[2605] = "Green Dye"
ES.Data.ItemNames[2842] = "Silver Bar"
ES.Data.ItemNames[2996] = "Bolt of Linen Cloth"
ES.Data.ItemNames[2997] = "Bolt of Woolen Cloth"
ES.Data.ItemNames[3182] = "Spider's Silk"
ES.Data.ItemNames[3383] = "Elixir of Wisdom"
ES.Data.ItemNames[3577] = "Gold Bar"
ES.Data.ItemNames[3824] = "Shadow Oil"
ES.Data.ItemNames[3827] = "Mana Potion"
ES.Data.ItemNames[3829] = "Frost Oil"
ES.Data.ItemNames[3864] = "Citrine"
ES.Data.ItemNames[4234] = "Heavy Leather"
ES.Data.ItemNames[4238] = "Linen Bag"
ES.Data.ItemNames[4240] = "Woolen Bag"
ES.Data.ItemNames[4241] = "Green Woolen Bag"
ES.Data.ItemNames[4245] = "Small Silk Pack"
ES.Data.ItemNames[4291] = "Silken Thread"
ES.Data.ItemNames[4304] = "Thick Leather"
ES.Data.ItemNames[4305] = "Bolt of Silk Cloth"
ES.Data.ItemNames[4306] = "Silk Cloth"
ES.Data.ItemNames[4307] = "Heavy Linen Gloves"
ES.Data.ItemNames[4308] = "Green Linen Bracers"
ES.Data.ItemNames[4309] = "Handstitched Linen Britches"
ES.Data.ItemNames[4310] = "Heavy Woolen Gloves"
ES.Data.ItemNames[4311] = "Heavy Woolen Cloak"
ES.Data.ItemNames[4312] = "Soft-soled Linen Boots"
ES.Data.ItemNames[4313] = "Red Woolen Boots"
ES.Data.ItemNames[4314] = "Double-Stitched Woolen Shoulders"
ES.Data.ItemNames[4315] = "Reinforced Woolen Shoulders"
ES.Data.ItemNames[4316] = "Heavy Woolen Pants"
ES.Data.ItemNames[4317] = "Phoenix Pants"
ES.Data.ItemNames[4318] = "Gloves of Meditation"
ES.Data.ItemNames[4319] = "Azure Silk Gloves"
ES.Data.ItemNames[4320] = "Spidersilk Boots"
ES.Data.ItemNames[4321] = "Spider Silk Slippers"
ES.Data.ItemNames[4322] = "Enchanter's Cowl"
ES.Data.ItemNames[4323] = "Shadow Hood"
ES.Data.ItemNames[4324] = "Azure Silk Vest"
ES.Data.ItemNames[4325] = "Boots of the Enchanter"
ES.Data.ItemNames[4326] = "Long Silken Cloak"
ES.Data.ItemNames[4327] = "Icy Cloak"
ES.Data.ItemNames[4328] = "Spider Belt"
ES.Data.ItemNames[4329] = "Star Belt"
ES.Data.ItemNames[4330] = "Stylish Red Shirt"
ES.Data.ItemNames[4331] = "Phoenix Gloves"
ES.Data.ItemNames[4332] = "Bright Yellow Shirt"
ES.Data.ItemNames[4333] = "Dark Silk Shirt"
ES.Data.ItemNames[4334] = "Formal White Shirt"
ES.Data.ItemNames[4335] = "Rich Purple Silk Shirt"
ES.Data.ItemNames[4336] = "Black Swashbuckler's Shirt"
ES.Data.ItemNames[4337] = "Thick Spider's Silk"
ES.Data.ItemNames[4338] = "Mageweave Cloth"
ES.Data.ItemNames[4339] = "Bolt of Mageweave"
ES.Data.ItemNames[4340] = "Gray Dye"
ES.Data.ItemNames[4341] = "Yellow Dye"
ES.Data.ItemNames[4342] = "Purple Dye"
ES.Data.ItemNames[4343] = "Brown Linen Pants"
ES.Data.ItemNames[4344] = "Brown Linen Shirt"
ES.Data.ItemNames[4470] = "Simple Wood"
ES.Data.ItemNames[4589] = "Long Elegant Feather"
ES.Data.ItemNames[4625] = "Firebloom"
ES.Data.ItemNames[5498] = "Small Lustrous Pearl"
ES.Data.ItemNames[5500] = "Iridescent Pearl"
ES.Data.ItemNames[5542] = "Pearl-clasped Cloak"
ES.Data.ItemNames[5762] = "Red Linen Bag"
ES.Data.ItemNames[5763] = "Red Woolen Bag"
ES.Data.ItemNames[5764] = "Green Silk Pack"
ES.Data.ItemNames[5765] = "Black Silk Pack"
ES.Data.ItemNames[5766] = "Lesser Wizard's Robe"
ES.Data.ItemNames[5770] = "Robes of Arcana"
ES.Data.ItemNames[6037] = "Truesilver Bar"
ES.Data.ItemNames[6048] = "Shadow Protection Potion"
ES.Data.ItemNames[6238] = "Brown Linen Robe"
ES.Data.ItemNames[6239] = "Red Linen Vest"
ES.Data.ItemNames[6240] = "Blue Linen Vest"
ES.Data.ItemNames[6241] = "White Linen Robe"
ES.Data.ItemNames[6242] = "Blue Linen Robe"
ES.Data.ItemNames[6243] = "Green Woolen Robe"
ES.Data.ItemNames[6260] = "Blue Dye"
ES.Data.ItemNames[6261] = "Orange Dye"
ES.Data.ItemNames[6263] = "Blue Overalls"
ES.Data.ItemNames[6264] = "Greater Adept's Robe"
ES.Data.ItemNames[6371] = "Fire Oil"
ES.Data.ItemNames[6384] = "Stylish Blue Shirt"
ES.Data.ItemNames[6385] = "Stylish Green Shirt"
ES.Data.ItemNames[6786] = "Simple Dress"
ES.Data.ItemNames[6787] = "White Woolen Dress"
ES.Data.ItemNames[6795] = "White Swashbuckler's Shirt"
ES.Data.ItemNames[6796] = "Red Swashbuckler's Shirt"
ES.Data.ItemNames[7026] = "Linen Belt"
ES.Data.ItemNames[7027] = "Boots of Darkness"
ES.Data.ItemNames[7046] = "Azure Silk Pants"
ES.Data.ItemNames[7047] = "Hands of Darkness"
ES.Data.ItemNames[7048] = "Azure Silk Hood"
ES.Data.ItemNames[7049] = "Truefaith Gloves"
ES.Data.ItemNames[7050] = "Silk Headband"
ES.Data.ItemNames[7051] = "Earthen Vest"
ES.Data.ItemNames[7052] = "Azure Silk Belt"
ES.Data.ItemNames[7053] = "Azure Silk Cloak"
ES.Data.ItemNames[7054] = "Robe of Power"
ES.Data.ItemNames[7055] = "Crimson Silk Belt"
ES.Data.ItemNames[7056] = "Crimson Silk Cloak"
ES.Data.ItemNames[7057] = "Green Silken Shoulders"
ES.Data.ItemNames[7058] = "Crimson Silk Vest"
ES.Data.ItemNames[7059] = "Crimson Silk Shoulders"
ES.Data.ItemNames[7060] = "Azure Shoulders"
ES.Data.ItemNames[7061] = "Earthen Silk Belt"
ES.Data.ItemNames[7062] = "Crimson Silk Pantaloons"
ES.Data.ItemNames[7063] = "Crimson Silk Robe"
ES.Data.ItemNames[7064] = "Crimson Silk Gloves"
ES.Data.ItemNames[7065] = "Green Silk Armor"
ES.Data.ItemNames[7067] = "Elemental Earth"
ES.Data.ItemNames[7068] = "Elemental Fire"
ES.Data.ItemNames[7069] = "Elemental Air"
ES.Data.ItemNames[7070] = "Elemental Water"
ES.Data.ItemNames[7071] = "Iron Buckle"
ES.Data.ItemNames[7072] = "Naga Scale"
ES.Data.ItemNames[7076] = "Essence of Earth"
ES.Data.ItemNames[7077] = "Heart of Fire"
ES.Data.ItemNames[7078] = "Essence of Fire"
ES.Data.ItemNames[7079] = "Globe of Water"
ES.Data.ItemNames[7080] = "Essence of Water"
ES.Data.ItemNames[7082] = "Essence of Air"
ES.Data.ItemNames[7910] = "Star Ruby"
ES.Data.ItemNames[7971] = "Black Pearl"
ES.Data.ItemNames[7972] = "Ichor of Undeath"
ES.Data.ItemNames[8153] = "Wildvine"
ES.Data.ItemNames[8170] = "Rugged Leather"
ES.Data.ItemNames[8343] = "Heavy Silken Thread"
ES.Data.ItemNames[8831] = "Purple Lotus"
ES.Data.ItemNames[9210] = "Ghost Dye"
ES.Data.ItemNames[9998] = "Black Mageweave Vest"
ES.Data.ItemNames[9999] = "Black Mageweave Leggings"
ES.Data.ItemNames[10001] = "Black Mageweave Robe"
ES.Data.ItemNames[10002] = "Shadoweave Pants"
ES.Data.ItemNames[10003] = "Black Mageweave Gloves"
ES.Data.ItemNames[10004] = "Shadoweave Robe"
ES.Data.ItemNames[10007] = "Red Mageweave Vest"
ES.Data.ItemNames[10008] = "White Bandit Mask"
ES.Data.ItemNames[10009] = "Red Mageweave Pants"
ES.Data.ItemNames[10010] = "Stormcloth Pants"
ES.Data.ItemNames[10011] = "Stormcloth Gloves"
ES.Data.ItemNames[10018] = "Red Mageweave Gloves"
ES.Data.ItemNames[10019] = "Dreamweave Gloves"
ES.Data.ItemNames[10020] = "Stormcloth Vest"
ES.Data.ItemNames[10021] = "Dreamweave Vest"
ES.Data.ItemNames[10023] = "Shadoweave Gloves"
ES.Data.ItemNames[10024] = "Black Mageweave Headband"
ES.Data.ItemNames[10025] = "Shadoweave Mask"
ES.Data.ItemNames[10026] = "Black Mageweave Boots"
ES.Data.ItemNames[10027] = "Black Mageweave Shoulders"
ES.Data.ItemNames[10028] = "Shadoweave Shoulders"
ES.Data.ItemNames[10029] = "Red Mageweave Shoulders"
ES.Data.ItemNames[10030] = "Admiral's Hat"
ES.Data.ItemNames[10031] = "Shadoweave Boots"
ES.Data.ItemNames[10032] = "Stormcloth Headband"
ES.Data.ItemNames[10033] = "Red Mageweave Headband"
ES.Data.ItemNames[10034] = "Tuxedo Shirt"
ES.Data.ItemNames[10035] = "Tuxedo Pants"
ES.Data.ItemNames[10036] = "Tuxedo Jacket"
ES.Data.ItemNames[10038] = "Stormcloth Shoulders"
ES.Data.ItemNames[10039] = "Stormcloth Boots"
ES.Data.ItemNames[10040] = "White Wedding Dress"
ES.Data.ItemNames[10041] = "Dreamweave Circlet"
ES.Data.ItemNames[10042] = "Cindercloth Robe"
ES.Data.ItemNames[10044] = "Cindercloth Boots"
ES.Data.ItemNames[10045] = "Simple Linen Pants"
ES.Data.ItemNames[10046] = "Simple Linen Boots"
ES.Data.ItemNames[10047] = "Simple Kilt"
ES.Data.ItemNames[10048] = "Colorful Kilt"
ES.Data.ItemNames[10050] = "Mageweave Bag"
ES.Data.ItemNames[10051] = "Red Mageweave Bag"
ES.Data.ItemNames[10052] = "Orange Martial Shirt"
ES.Data.ItemNames[10053] = "Simple Black Dress"
ES.Data.ItemNames[10054] = "Lavender Mageweave Shirt"
ES.Data.ItemNames[10055] = "Pink Mageweave Shirt"
ES.Data.ItemNames[10056] = "Orange Mageweave Shirt"
ES.Data.ItemNames[10285] = "Shadow Silk"
ES.Data.ItemNames[10286] = "Heart of the Wild"
ES.Data.ItemNames[10290] = "Pink Dye"
ES.Data.ItemNames[11040] = "Morrowgrain"
ES.Data.ItemNames[11082] = "Greater Astral Essence"
ES.Data.ItemNames[11134] = "Lesser Mystic Essence"
ES.Data.ItemNames[11137] = "Vision Dust"
ES.Data.ItemNames[11175] = "Greater Nether Essence"
ES.Data.ItemNames[11176] = "Dream Dust"
ES.Data.ItemNames[11178] = "Large Radiant Shard"
ES.Data.ItemNames[12360] = "Arcanite Bar"
ES.Data.ItemNames[12364] = "Huge Emerald"
ES.Data.ItemNames[12662] = "Demonic Rune"
ES.Data.ItemNames[12800] = "Azerothian Diamond"
ES.Data.ItemNames[12803] = "Living Essence"
ES.Data.ItemNames[12804] = "Powerful Mojo"
ES.Data.ItemNames[12808] = "Essence of Undeath"
ES.Data.ItemNames[12809] = "Guardian Stone"
ES.Data.ItemNames[12810] = "Enchanted Leather"
ES.Data.ItemNames[12811] = "Righteous Orb"
ES.Data.ItemNames[12938] = "Blood of Heroes"
ES.Data.ItemNames[13468] = "Black Lotus"
ES.Data.ItemNames[13856] = "Runecloth Belt"
ES.Data.ItemNames[13857] = "Runecloth Tunic"
ES.Data.ItemNames[13858] = "Runecloth Robe"
ES.Data.ItemNames[13860] = "Runecloth Cloak"
ES.Data.ItemNames[13863] = "Runecloth Gloves"
ES.Data.ItemNames[13864] = "Runecloth Boots"
ES.Data.ItemNames[13865] = "Runecloth Pants"
ES.Data.ItemNames[13866] = "Runecloth Headband"
ES.Data.ItemNames[13867] = "Runecloth Shoulders"
ES.Data.ItemNames[13868] = "Frostweave Robe"
ES.Data.ItemNames[13869] = "Frostweave Tunic"
ES.Data.ItemNames[13870] = "Frostweave Gloves"
ES.Data.ItemNames[13871] = "Frostweave Pants"
ES.Data.ItemNames[13926] = "Golden Pearl"
ES.Data.ItemNames[14042] = "Cindercloth Vest"
ES.Data.ItemNames[14043] = "Cindercloth Gloves"
ES.Data.ItemNames[14044] = "Cindercloth Cloak"
ES.Data.ItemNames[14045] = "Cindercloth Pants"
ES.Data.ItemNames[14046] = "Runecloth Bag"
ES.Data.ItemNames[14047] = "Runecloth"
ES.Data.ItemNames[14048] = "Bolt of Runecloth"
ES.Data.ItemNames[14100] = "Brightcloth Robe"
ES.Data.ItemNames[14101] = "Brightcloth Gloves"
ES.Data.ItemNames[14103] = "Brightcloth Cloak"
ES.Data.ItemNames[14104] = "Brightcloth Pants"
ES.Data.ItemNames[14106] = "Felcloth Robe"
ES.Data.ItemNames[14107] = "Felcloth Pants"
ES.Data.ItemNames[14108] = "Felcloth Boots"
ES.Data.ItemNames[14111] = "Felcloth Hood"
ES.Data.ItemNames[14112] = "Felcloth Shoulders"
ES.Data.ItemNames[14128] = "Wizardweave Robe"
ES.Data.ItemNames[14130] = "Wizardweave Turban"
ES.Data.ItemNames[14132] = "Wizardweave Leggings"
ES.Data.ItemNames[14134] = "Cloak of Fire"
ES.Data.ItemNames[14136] = "Robe of Winter Night"
ES.Data.ItemNames[14137] = "Mooncloth Leggings"
ES.Data.ItemNames[14138] = "Mooncloth Vest"
ES.Data.ItemNames[14139] = "Mooncloth Shoulders"
ES.Data.ItemNames[14140] = "Mooncloth Circlet"
ES.Data.ItemNames[14141] = "Ghostweave Vest"
ES.Data.ItemNames[14142] = "Ghostweave Gloves"
ES.Data.ItemNames[14143] = "Ghostweave Belt"
ES.Data.ItemNames[14144] = "Ghostweave Pants"
ES.Data.ItemNames[14146] = "Gloves of Spell Mastery"
ES.Data.ItemNames[14152] = "Robe of the Archmage"
ES.Data.ItemNames[14153] = "Robe of the Void"
ES.Data.ItemNames[14154] = "Truefaith Vestments"
ES.Data.ItemNames[14155] = "Mooncloth Bag"
ES.Data.ItemNames[14156] = "Bottomless Bag"
ES.Data.ItemNames[14227] = "Ironweb Spider Silk"
ES.Data.ItemNames[14256] = "Felcloth"
ES.Data.ItemNames[14341] = "Rune Thread"
ES.Data.ItemNames[14342] = "Mooncloth"
ES.Data.ItemNames[14343] = "Small Brilliant Shard"
ES.Data.ItemNames[14344] = "Large Brilliant Shard"
ES.Data.ItemNames[15407] = "Cured Rugged Hide"
ES.Data.ItemNames[15802] = "Mooncloth Boots"
ES.Data.ItemNames[16203] = "Greater Eternal Essence"
ES.Data.ItemNames[16979] = "Flarecore Gloves"
ES.Data.ItemNames[16980] = "Flarecore Mantle"
ES.Data.ItemNames[17010] = "Fiery Core"
ES.Data.ItemNames[17011] = "Lava Core"
ES.Data.ItemNames[17012] = "Core Leather"
ES.Data.ItemNames[17723] = "Green Holiday Shirt"
ES.Data.ItemNames[18240] = "Ogre Tannin"
ES.Data.ItemNames[18258] = "Gordok Ogre Suit"
ES.Data.ItemNames[18263] = "Flarecore Wraps"
ES.Data.ItemNames[18405] = "Belt of the Archmage"
ES.Data.ItemNames[18407] = "Felcloth Gloves"
ES.Data.ItemNames[18408] = "Inferno Gloves"
ES.Data.ItemNames[18409] = "Mooncloth Gloves"
ES.Data.ItemNames[18413] = "Cloak of Warding"
ES.Data.ItemNames[18486] = "Mooncloth Robe"
ES.Data.ItemNames[19047] = "Wisdom of the Timbermaw"
ES.Data.ItemNames[19050] = "Mantle of the Timbermaw"
ES.Data.ItemNames[19056] = "Argent Boots"
ES.Data.ItemNames[19059] = "Argent Shoulders"
ES.Data.ItemNames[19156] = "Flarecore Robe"
ES.Data.ItemNames[19165] = "Flarecore Leggings"
ES.Data.ItemNames[19682] = "Bloodvine Vest"
ES.Data.ItemNames[19683] = "Bloodvine Leggings"
ES.Data.ItemNames[19684] = "Bloodvine Boots"
ES.Data.ItemNames[19726] = "Bloodvine"
ES.Data.ItemNames[20381] = "Dreamscale"
ES.Data.ItemNames[20520] = "Dark Rune"
ES.Data.ItemNames[20537] = "Runed Stygian Boots"
ES.Data.ItemNames[20538] = "Runed Stygian Leggings"
ES.Data.ItemNames[20539] = "Runed Stygian Belt"
ES.Data.ItemNames[21154] = "Festival Dress"
ES.Data.ItemNames[21340] = "Soul Pouch"
ES.Data.ItemNames[21341] = "Felcloth Bag"
ES.Data.ItemNames[21342] = "Core Felcloth Bag"
ES.Data.ItemNames[21542] = "Festival Suit"
ES.Data.ItemNames[22246] = "Enchanted Mageweave Pouch"
ES.Data.ItemNames[22248] = "Enchanted Runecloth Bag"
ES.Data.ItemNames[22249] = "Big Bag of Enchantment"
ES.Data.ItemNames[22251] = "Cenarion Herb Bag"
ES.Data.ItemNames[22252] = "Satchel of Cenarius"
ES.Data.ItemNames[22652] = "Glacial Vest"
ES.Data.ItemNames[22654] = "Glacial Gloves"
ES.Data.ItemNames[22655] = "Glacial Wrists"
ES.Data.ItemNames[22658] = "Glacial Cloak"
ES.Data.ItemNames[22660] = "Gaea's Embrace"
ES.Data.ItemNames[22682] = "Frozen Rune"
ES.Data.ItemNames[22756] = "Sylvan Vest"
ES.Data.ItemNames[22757] = "Sylvan Crown"
ES.Data.ItemNames[22758] = "Sylvan Shoulders"
ES.Data.ItemNames[34085] = "Red Winter Clothes"
ES.Data.ItemNames[34087] = "Green Winter Clothes"
ES.Data.ItemNames[210781] = "Phoenix Bindings"
ES.Data.ItemNames[213378] = "Unstable Microfilament"
ES.Data.ItemNames[213379] = "Hyperconductive Arcano-Filament"
ES.Data.ItemNames[215365] = "Invoker's Mantle"
ES.Data.ItemNames[215366] = "Invoker's Cord"
ES.Data.ItemNames[227844] = "Leather-Reinforced Runecloth Bag"
ES.Data.ItemNames[239147] = "Crusader's Knapsack"
ES.Data.ItemNames[239148] = "Crimson Dawnwoven Bag"
ES.Data.ItemNames[249391] = "Pyrite"
ES.Data.ItemNames[249409] = "Cerulean Dye"
ES.Data.ItemNames[249427] = "Pristine Leather"
ES.Data.ItemNames[249428] = "Pristine Hide"
ES.Data.ItemNames[249429] = "Pristine Scale"
ES.Data.ItemNames[249430] = "Magenta Dye"
ES.Data.ItemNames[249431] = "Viridian Dye"
ES.Data.ItemNames[253664] = "Linen Reagent Bag"
ES.Data.ItemNames[253667] = "Woolen Reagent Bag"
ES.Data.ItemNames[253889] = "Pristine Boots"
ES.Data.ItemNames[253891] = "Silky Boots"
ES.Data.ItemNames[253893] = "Flame Boots"
ES.Data.ItemNames[253895] = "Shadow Boots"
ES.Data.ItemNames[253897] = "Pearly Boots"
ES.Data.ItemNames[253899] = "Shining Boots"
ES.Data.ItemNames[253913] = "Pristine Gloves"
ES.Data.ItemNames[253915] = "Silky Gloves"
ES.Data.ItemNames[253917] = "Flame Gloves"
ES.Data.ItemNames[253919] = "Shadow Gloves"
ES.Data.ItemNames[253921] = "Pearly Gloves"
ES.Data.ItemNames[253923] = "Shining Gloves"
ES.Data.ItemNames[253925] = "Pristine Sash"
ES.Data.ItemNames[253927] = "Silky Sash"
ES.Data.ItemNames[253929] = "Flame Sash"
ES.Data.ItemNames[253931] = "Shadow Sash"
ES.Data.ItemNames[253933] = "Pearly Sash"
ES.Data.ItemNames[253935] = "Shining Sash"
ES.Data.ItemNames[253949] = "Pristine Circlet"
ES.Data.ItemNames[253951] = "Silky Circlet"
ES.Data.ItemNames[253953] = "Flame Circlet"
ES.Data.ItemNames[253955] = "Shadow Circlet"
ES.Data.ItemNames[253957] = "Pearly Circlet"
ES.Data.ItemNames[253959] = "Shining Circlet"
ES.Data.ItemNames[253961] = "Pristine Gown"
ES.Data.ItemNames[253963] = "Silky Gown"
ES.Data.ItemNames[253965] = "Flame Gown"
ES.Data.ItemNames[253967] = "Shadow Gown"
ES.Data.ItemNames[253969] = "Pearly Gown"
ES.Data.ItemNames[253971] = "Shining Gown"
ES.Data.ItemNames[253973] = "Silk Reagent Bag"
ES.Data.ItemNames[253987] = "Pristine Leggings"
ES.Data.ItemNames[253989] = "Silky Leggings"
ES.Data.ItemNames[253991] = "Flame Leggings"
ES.Data.ItemNames[253993] = "Shadow Leggings"
ES.Data.ItemNames[253995] = "Pearly Leggings"
ES.Data.ItemNames[253997] = "Shining Leggings"
ES.Data.ItemNames[253999] = "Earthen Leggings"
ES.Data.ItemNames[254013] = "Earthen Silk Slippers"
ES.Data.ItemNames[254015] = "Earthen Silk Hood"
ES.Data.ItemNames[254017] = "Earthen Silk Gloves"
ES.Data.ItemNames[254019] = "Earthen Silk Cuffs"
ES.Data.ItemNames[254021] = "Gilded Handwraps"
ES.Data.ItemNames[254023] = "Frothing Handwraps"
ES.Data.ItemNames[254025] = "Fiery Handwraps"
ES.Data.ItemNames[254027] = "Black Handwraps"
ES.Data.ItemNames[254029] = "Golden Handwraps"
ES.Data.ItemNames[254031] = "Radiant Handwraps"
ES.Data.ItemNames[254033] = "Earthen Silk Shoulders"
ES.Data.ItemNames[254035] = "Mageweave Reagent Bag"
ES.Data.ItemNames[254049] = "Nethergeld Shoulders"
ES.Data.ItemNames[254051] = "Netherfroth Shoulders"
ES.Data.ItemNames[254053] = "Netherflame Shoulders"
ES.Data.ItemNames[254055] = "Netherpearl Shoulders"
ES.Data.ItemNames[254057] = "Nethershine Shoulders"
ES.Data.ItemNames[254059] = "Netherlight Shoulders"
ES.Data.ItemNames[254061] = "Nethergeld Cuffs"
ES.Data.ItemNames[254063] = "Netherfroth Cuffs"
ES.Data.ItemNames[254065] = "Netherflame Cuffs"
ES.Data.ItemNames[254067] = "Netherpearl Cuffs"
ES.Data.ItemNames[254069] = "Nethershine Cuffs"
ES.Data.ItemNames[254071] = "Netherlight Cuffs"
ES.Data.ItemNames[254073] = "Ghostweave Cord"
ES.Data.ItemNames[254075] = "Earthenweave Gloves"
ES.Data.ItemNames[254077] = "Earthenweave Cord"
ES.Data.ItemNames[254079] = "Runecloth Reagent Bag"
ES.Data.ItemNames[254081] = "Gilded Waistcord"
ES.Data.ItemNames[254083] = "Frothing Waistcord"
ES.Data.ItemNames[254085] = "Fiery Waistcord"
ES.Data.ItemNames[254087] = "Black Waistcord"
ES.Data.ItemNames[254089] = "Golden Waistcord"
ES.Data.ItemNames[254091] = "Radiant Waistcord"
ES.Data.ItemNames[254093] = "Earthenweave Boots"
ES.Data.ItemNames[254107] = "Gilded Sandals"
ES.Data.ItemNames[254109] = "Frothing Sandals"
ES.Data.ItemNames[254111] = "Fiery Sandals"
ES.Data.ItemNames[254113] = "Black Sandals"
ES.Data.ItemNames[254115] = "Golden Sandals"
ES.Data.ItemNames[254117] = "Radiant Sandals"
ES.Data.ItemNames[254119] = "Earthenweave Mantle"
ES.Data.ItemNames[254121] = "Earthenweave Vest"
ES.Data.ItemNames[254123] = "Runecloth Cuffs"
ES.Data.ItemNames[254125] = "Earthenweave Leggings"
ES.Data.ItemNames[254127] = "Ghostweave Mantle"
ES.Data.ItemNames[254129] = "Ghostweave Boots"
ES.Data.ItemNames[254131] = "Earthenweave Cuffs"
ES.Data.ItemNames[254133] = "Mooncloth Reagent Bag"
ES.Data.ItemNames[254135] = "Ghostweave Hood"
ES.Data.ItemNames[254137] = "Earthenweave Crown"
ES.Data.ItemNames[254139] = "Bottomless Reagent Bag"
ES.Data.ItemNames[274030] = "Malleable Essence of Nature"
ES.Data.ItemNames[275604] = "Venomspew Gloves"
ES.Data.ItemNames[275605] = "Venomspew Cord"
ES.Data.ItemNames[275606] = "Venomspew Footpads"
ES.Data.ItemNames[275607] = "Swarmtender's Gloves"
ES.Data.ItemNames[275608] = "Swarmtender's Cord"
ES.Data.ItemNames[275609] = "Swarmtender's Footpads"
ES.Data.ItemNames[277010] = "Cloudy Stormsewn Vest"
ES.Data.ItemNames[277011] = "Cloudy Stormsewn Cuffs"
ES.Data.ItemNames[277012] = "Cloudy Stormsewn Handwraps"
ES.Data.ItemNames[277013] = "Cloudy Stormsewn Cord"
ES.Data.ItemNames[277014] = "Cloudy Stormsewn Leggings"
ES.Data.ItemNames[277015] = "Cloudy Stormsewn Shoes"
ES.Data.ItemNames[277034] = "Azure Stormsewn Vest"
ES.Data.ItemNames[277035] = "Azure Stormsewn Cuffs"
ES.Data.ItemNames[277036] = "Azure Stormsewn Handwraps"
ES.Data.ItemNames[277037] = "Azure Stormsewn Cord"
ES.Data.ItemNames[277038] = "Azure Stormsewn Leggings"
ES.Data.ItemNames[277039] = "Azure Stormsewn Shoes"
ES.Data.ItemNames[277046] = "Cloudy Stormsewn Cowl"
ES.Data.ItemNames[277047] = "Cloudy Stormsewn Epaulets"
ES.Data.ItemNames[277054] = "Azure Stormsewn Cowl"
ES.Data.ItemNames[277055] = "Azure Stormsewn Epaulets"
ES.Data.ItemNames[279266] = "Robes of Fiery Devastation"
ES.Data.ItemNames[279267] = "Mana-infused Cord"
ES.Data.ItemNames[279268] = "Rime-encrusted Boots"
ES.Data.ItemNames[279269] = "Fel Cape"
ES.Data.ItemNames[279270] = "Cloak of Earth and Sky"
ES.Data.ItemNames[279271] = "Felblood Soul Bag"
ES.Data.ItemNames[279943] = "Spinning Wheel"
ES.Data.ItemNames[279972] = "Faction Banner"
ES.Data.ItemNames[279973] = "Faction Banner"

-- Material -> profesión de recolección que lo consigue (393 Desuello, 182 Herboristería, 186 Minería).
-- Sin uso por ahora: reservado para la vía "Vender en bruto" de Ganar dinero (docs/PLAN.md, G1).
ES.Data.GatheredBy = ES.Data.GatheredBy or {}
ES.Data.GatheredBy[2318] = 393
ES.Data.GatheredBy[2319] = 393
ES.Data.GatheredBy[2842] = 186
ES.Data.GatheredBy[4234] = 393
ES.Data.GatheredBy[4304] = 393
ES.Data.GatheredBy[4625] = 182
ES.Data.GatheredBy[8153] = 182
ES.Data.GatheredBy[8170] = 393
ES.Data.GatheredBy[8831] = 182
ES.Data.GatheredBy[12809] = 186
ES.Data.GatheredBy[13468] = 182
ES.Data.GatheredBy[17012] = 393
ES.Data.GatheredBy[19726] = 182
ES.Data.GatheredBy[20381] = 393
ES.Data.GatheredBy[249391] = 186
ES.Data.GatheredBy[249427] = 393
ES.Data.GatheredBy[249428] = 393
ES.Data.GatheredBy[249429] = 393

```
