# WoW Forever: recipes whose recipe item is a QUEST REWARD

Source: Crafter's Journal `Data/Sources.lua` (`q` field = quest IDs that give the recipe item), joined with quest rows decoded from the QuestieDB Forever database (CBOR). 69 recipe items / ~72 quests across all professions.

Notes for the consumer:
- `Turn-in items` are the item IDs the quest requires. **Counts are not stored as numbers; they're in the objective text** (e.g. 'Bring 6 Copper Axes and 6 Copper Chain Belts...'), so read the text for quantities.
- Many are multi-step chains. `Prereq quests` must be done first, and `Next in chain` gives the following quest. The reward recipe may be given at the end of the chain, so total cost = sum of every quest's turn-ins in the chain.
- To price a quest: for each turn-in item, cost = min(AH price, cost to craft it from its own reagents, from the recipe data file `wow-forever-recipe-data.md`), times the quantity from the text. Subtract the value of what you'd otherwise sell the turned-in items for (opportunity cost), or compare against buying the recipe item from the AH.
- `requiredSkill` is [professionSkillLineID, minimumSkill] (164 = Blacksmithing). Reputation is [factionID, value].

---

## Lesser Stoneshield Potion  (Alchemy)
- Recipe item ID: 4624; crafting spell: 4942; product item ID: 4623
- **Quest 715: Liquid Stone** (requires level 35, quest level 37)
  - Objective text: Bring a Healing Potion and a Lesser Invisibility Potion to Lucien Tosselwrench in the Badlands.
  - Turn-in item IDs: 929 (Healing Potion), 3823 (Lesser Invisibility Potion)
  - Prereq quests (any one): [714]
  - Started by NPC IDs: [[2920]]
  - Finished at NPC IDs: [[2920]]

## Barbaric Iron Boots  (Blacksmithing)
- Recipe item ID: 7981; crafting spell: 9818; product item ID: 7916
- **Quest 2753: Trampled Under Foot** (requires level 32, quest level 36)
  - Objective text: Bring four Green Iron Helms, four Green Iron Bracers, and two Green Iron Leggings to Orokk Omosh in Orgrimmar.
  - Turn-in item IDs: 3836 (Green Iron Helm), 3835 (Green Iron Bracers), 3842 (Green Iron Leggings)
  - requiredSkill (skillLine, min skill): [164, 1]
  - Prereq quests (any one): [2752]
  - Next in chain: 2754
  - Started by NPC IDs: [[7790]]
  - Finished at NPC IDs: [[7790]]

## Barbaric Iron Breastplate  (Blacksmithing)
- Recipe item ID: 7979; crafting spell: 9813; product item ID: 7914
- **Quest 2751: Barbaric Battlements** (requires level 32, quest level 32)
  - Objective text: Bring two Patterned Bronze Bracers, two Bronze Greatswords, and two Sharp Claws to Orokk Omosh in Orgrimmar.
  - Turn-in item IDs: 2868 (Patterned Bronze Bracers), 7957 (Bronze Greatsword), 5635 (Sharp Claw)
  - requiredSkill (skillLine, min skill): [164, 140]
  - Next in chain: 2752
  - Started by NPC IDs: [[7790]]
  - Finished at NPC IDs: [[7790]]

## Barbaric Iron Gloves  (Blacksmithing)
- Recipe item ID: 7982; crafting spell: 9820; product item ID: 7917
- **Quest 2755: Joys of Omosh** (requires level 32, quest level 36)
  - Objective text: Watch and learn the Omosh Dance of Joy.
  - requiredSkill (skillLine, min skill): [164, 1]
  - Prereq quests (any one): [2754]
  - Started by NPC IDs: [[7790]]
  - Finished at NPC IDs: [[7790]]

## Barbaric Iron Helm  (Blacksmithing)
- Recipe item ID: 7980; crafting spell: 9814; product item ID: 7915
- **Quest 2754: Horns of Frenzy** (requires level 32, quest level 36)
  - Objective text: Bring two Solid Iron Mauls, two Silvered Bronze Boots, and two Silvered Bronze Gauntlets to Orokk Omosh in Orgrimmar.
  - Turn-in item IDs: 3851 (Solid Iron Maul), 3482 (Silvered Bronze Boots), 3483 (Silvered Bronze Gauntlets)
  - requiredSkill (skillLine, min skill): [164, 1]
  - Prereq quests (any one): [2753]
  - Next in chain: 2755
  - Started by NPC IDs: [[7790]]
  - Finished at NPC IDs: [[7790]]

## Blazing Rapier  (Blacksmithing)
- Recipe item ID: 12825; crafting spell: 16978; product item ID: 12777
- **Quest 5307: Corruption** (requires level 50, quest level 60)
  - Objective text: Find the Black Guard Swordsmith in Stratholme and destroy him. Recover the Insignia of the Black Guard and return to Seril Scourgebane.
  - Turn-in item IDs: 13350
  - requiredSkill (skillLine, min skill): [164, 250]
  - Started by NPC IDs: [[11193]]
  - Finished at NPC IDs: [[11193]]

## Copper Chain Vest  (Blacksmithing)
- Recipe item ID: 3609; crafting spell: 3321; product item ID: 3471
- **Quest 1578: Supplying the Front** (requires level 1, quest level 12)
  - Objective text: Bring 6 Copper Axes and 6 Copper Chain Belts to Thorvald in the southern guard tower of Loch Modan.
  - Turn-in item IDs: 2845 (Copper Axe), 2851 (Copper Chain Belt)
  - requiredSkill (skillLine, min skill): [164, 25]
  - Started by NPC IDs: [[6031]]
  - Finished at NPC IDs: [[6030]]

## Dawn's Edge  (Blacksmithing)
- Recipe item ID: 12821; crafting spell: 16970; product item ID: 12774
- **Quest 5306: Snakestone of the Shadow Huntress** (requires level 50, quest level 60)
  - Objective text: Travel to Blackrock Spire and slay Shadow Hunter Vosh'gajin. Recover Vosh'gajin's Snakestone and return to Kilram.
  - Turn-in item IDs: 13352
  - requiredSkill (skillLine, min skill): [164, 250]
  - Started by NPC IDs: [[11192]]
  - Finished at NPC IDs: [[11192]]

## Demon Forged Breastplate  (Blacksmithing)
- Recipe item ID: 12696; crafting spell: 16667; product item ID: 12628
- **Quest 5127: The Demon Forge** (requires level 55, quest level 60)
  - Objective text: Travel to Blackrock Spire and find Goraluk Anvilcrack. Slay him and then use the Blood Stained Pike upon his corpse. After his soul has been siphoned, the pike will be Soul Stained. You must also find the Unforged Rune Covered Breastplate. Return both the Soul Stained Pike and the Unforged Rune Covered Breastplate to Lorax in Winterspring.
  - Turn-in item IDs: 12847, 12806
  - requiredSkill (skillLine, min skill): [164, 270]
  - Prereq quests (any one): [5126]
  - Started by NPC IDs: [[10918]]
  - Finished at NPC IDs: [[10918]]

## Enchanted Battlehammer  (Blacksmithing)
- Recipe item ID: 12824; crafting spell: 16973; product item ID: 12776
- **Quest 5305: Sweet Serenity** (requires level 50, quest level 60)
  - Objective text: Travel to Stratholme and kill the Crimson Hammersmith. Recover the Crimson Hammersmith's Apron and return to Lilith.
  - Turn-in item IDs: 13351
  - requiredSkill (skillLine, min skill): [164, 250]
  - Started by NPC IDs: [[11191]]
  - Finished at NPC IDs: [[11191]]
- **Quest 8869: Sweet Serenity** (requires level 50, quest level 60)
  - Objective text: Travel to Stratholme and kill the Crimson Hammersmith. Recover the Crimson Hammersmith's Apron and return to Lilith.
  - Turn-in item IDs: 13351
  - requiredSkill (skillLine, min skill): [164, 0]

## Enchanted Thorium Breastplate  (Blacksmithing)
- Recipe item ID: 12727; crafting spell: 16745; product item ID: 12618
- **Quest 7649: Enchanted Thorium Platemail: Volume I** (requires level 60, quest level 60)
  - Objective text: Return the book to its rightful owners.
  - requiredSkill (skillLine, min skill): [164, 300]
  - Started by NPC IDs: {'3': [18769]}
  - Finished at NPC IDs: [[14368]]

## Enchanted Thorium Helm  (Blacksmithing)
- Recipe item ID: 12725; crafting spell: 16742; product item ID: 12620
- **Quest 7651: Enchanted Thorium Platemail: Volume III** (requires level 55, quest level 60)
  - Objective text: Return the book to its rightful owners.
  - requiredSkill (skillLine, min skill): [164, 300]
  - Started by NPC IDs: {'3': [18771]}
  - Finished at NPC IDs: [[14368]]

## Enchanted Thorium Leggings  (Blacksmithing)
- Recipe item ID: 12726; crafting spell: 16744; product item ID: 12619
- **Quest 7650: Enchanted Thorium Platemail: Volume II** (requires level 60, quest level 60)
  - Objective text: Return the book to its rightful owners.
  - requiredSkill (skillLine, min skill): [164, 300]
  - Started by NPC IDs: {'3': [18770]}
  - Finished at NPC IDs: [[14368]]

## Fiery Plate Gauntlets  (Blacksmithing)
- Recipe item ID: 12699; crafting spell: 16655; product item ID: 12631
- **Quest 5124: Fiery Plate Gauntlets** (requires level 55, quest level 60)
  - Objective text: Bring Malyfous Darkhammer 6 Enchanted Thorium Bars, 2 Essence of Fire, and 4 Star Rubies. You will also need to turn in your Unfired Plate Gauntlets.
  - Turn-in item IDs: 12812, 12655 (Enchanted Thorium Bar), 7078 (Essence of Fire), 7910 (Star Ruby)
  - requiredSkill (skillLine, min skill): [164, 275]
  - Prereq quests (any one): [5103]
  - Started by NPC IDs: [[10637]]
  - Finished at NPC IDs: [[10637]]

## Golden Scale Gauntlets  (Blacksmithing)
- Recipe item ID: 9367; crafting spell: 11643; product item ID: 9366
- **Quest 2758: The Origins of Smithing** (requires level 40, quest level 40)
  - Objective text: Bring six Golden Scale Bracers to Hank the Hammer in Stormwind.
  - Turn-in item IDs: 6040 (Golden Scale Bracers)
  - requiredSkill (skillLine, min skill): [164, 210]
  - Next in chain: 2759
  - Started by NPC IDs: [[7798]]
  - Finished at NPC IDs: [[7798]]

## Imperial Plate Belt  (Blacksmithing)
- Recipe item ID: 12688; crafting spell: 16647; product item ID: 12424
- **Quest 7653: Imperial Plate Belt** (requires level 50, quest level 60)
  - Turn-in item IDs: 12359 (Thorium Bar)
  - requiredSkill (skillLine, min skill): [164, 265]
  - Prereq quests (any one): [7652]
  - Started by NPC IDs: [[14567]]
  - Finished at NPC IDs: [[14567]]

## Imperial Plate Boots  (Blacksmithing)
- Recipe item ID: 12700; crafting spell: 16657; product item ID: 12426
- **Quest 7654: Imperial Plate Boots** (requires level 50, quest level 60)
  - Turn-in item IDs: 12359 (Thorium Bar)
  - requiredSkill (skillLine, min skill): [164, 265]
  - Prereq quests (any one): [7652]
  - Started by NPC IDs: [[14567]]
  - Finished at NPC IDs: [[14567]]

## Imperial Plate Bracers  (Blacksmithing)
- Recipe item ID: 12690; crafting spell: 16649; product item ID: 12425
- **Quest 7655: Imperial Plate Bracer** (requires level 50, quest level 60)
  - Turn-in item IDs: 12359 (Thorium Bar)
  - requiredSkill (skillLine, min skill): [164, 265]
  - Prereq quests (any one): [7652]
  - Started by NPC IDs: [[14567]]
  - Finished at NPC IDs: [[14567]]

## Imperial Plate Chest  (Blacksmithing)
- Recipe item ID: 12705; crafting spell: 16663; product item ID: 12422
- **Quest 7656: Imperial Plate Chest** (requires level 50, quest level 60)
  - Turn-in item IDs: 12359 (Thorium Bar)
  - requiredSkill (skillLine, min skill): [164, 265]
  - Prereq quests (any one): [7652]
  - Started by NPC IDs: [[14567]]
  - Finished at NPC IDs: [[14567]]

## Imperial Plate Helm  (Blacksmithing)
- Recipe item ID: 12701; crafting spell: 16658; product item ID: 12427
- **Quest 7657: Imperial Plate Helm** (requires level 50, quest level 60)
  - Turn-in item IDs: 12359 (Thorium Bar)
  - requiredSkill (skillLine, min skill): [164, 265]
  - Prereq quests (any one): [7652]
  - Started by NPC IDs: [[14567]]
  - Finished at NPC IDs: [[14567]]

## Imperial Plate Leggings  (Blacksmithing)
- Recipe item ID: 12715; crafting spell: 16730; product item ID: 12429
- **Quest 7658: Imperial Plate Leggings** (requires level 50, quest level 60)
  - Turn-in item IDs: 12359 (Thorium Bar)
  - requiredSkill (skillLine, min skill): [164, 265]
  - Prereq quests (any one): [7652]
  - Started by NPC IDs: [[14567]]
  - Finished at NPC IDs: [[14567]]

## Imperial Plate Shoulders  (Blacksmithing)
- Recipe item ID: 12687; crafting spell: 16646; product item ID: 12428
- **Quest 7659: Imperial Plate Shoulders** (requires level 50, quest level 60)
  - Turn-in item IDs: 12359 (Thorium Bar)
  - requiredSkill (skillLine, min skill): [164, 265]
  - Prereq quests (any one): [7652]
  - Started by NPC IDs: [[14567]]
  - Finished at NPC IDs: [[14567]]

## Ornate Mithril Gloves  (Blacksmithing)
- Recipe item ID: 7984; crafting spell: 9950; product item ID: 7927
- **Quest 2762: The Great Silver Deceiver** (requires level 40, quest level 45)
  - Objective text: Bring forty Mithril Bars and five Truesilver Bars to Galvan the Ancient in Stranglethorn.
  - Turn-in item IDs: 3860 (Mithril Bar), 6037 (Truesilver Bar)
  - requiredSkill (skillLine, min skill): [164, 210]
  - Prereq quests (any one): [2760]
  - Started by NPC IDs: [[7802]]
  - Finished at NPC IDs: [[7802]]

## Ornate Mithril Pants  (Blacksmithing)
- Recipe item ID: 7983; crafting spell: 9945; product item ID: 7926
- **Quest 2761: Smelt On, Smelt Off** (requires level 40, quest level 45)
  - Objective text: Bring forty Mithril Bars and forty Iron Bars to Galvan the Ancient in Stranglethorn.
  - Turn-in item IDs: 3575 (Iron Bar), 3860 (Mithril Bar)
  - requiredSkill (skillLine, min skill): [164, 210]
  - Prereq quests (any one): [2760]
  - Next in chain: 2764
  - Started by NPC IDs: [[7802]]
  - Finished at NPC IDs: [[7802]]

## Ornate Mithril Shoulders  (Blacksmithing)
- Recipe item ID: 7985; crafting spell: 9952; product item ID: 7928
- **Quest 2763: The Art of the Imbue** (requires level 40, quest level 45)
  - Objective text: Bring forty Mithril Bars and four Citrines to Galvan the Ancient in Stranglethorn.
  - Turn-in item IDs: 3860 (Mithril Bar), 3864 (Citrine)
  - requiredSkill (skillLine, min skill): [164, 210]
  - Prereq quests (any one): [2760]
  - Started by NPC IDs: [[7802]]
  - Finished at NPC IDs: [[7802]]

## Rough Copper Chain Boots  (Blacksmithing)
- Recipe item ID: 277673; crafting spell: 1302598; product item ID: 277672
- **Quest 95217: The Quarry's Smith** (requires level 7, quest level 10)
  - Objective text: Collect 12 Copper Bars and 4 Toughened Boar Hides and deliver them to Frast Dokner.
  - Turn-in item IDs: 2840 (Copper Bar), 267416
  - requiredSkill (skillLine, min skill): [164, 1]
  - Started by NPC IDs: [[1698]]
  - Finished at NPC IDs: [[1698]]
- **Quest 96874: This Is Spinal Axe** (requires level 6, quest level 10)
  - Objective text: Ug'thok in Orgrimmar wants you to collect 5 Weathered Spines from beasts in Thunder Ridge, along with 5 Rough Grinding Stones.
  - Turn-in item IDs: 275719, 3470 (Rough Grinding Stone)
  - requiredSkill (skillLine, min skill): [164, 1]
  - Started by NPC IDs: [[10266]]
  - Finished at NPC IDs: [[10266]]

## Sulfuron Hammer  (Blacksmithing)
- Recipe item ID: 18592; crafting spell: 21161; product item ID: 17193
- **Quest 7604: A Binding Contract** (requires level 60, quest level 60)
  - Objective text: Turn the Thorium Brotherhood Contract in to Lokhtos Darkbargainer if you would like to receive the plans for Sulfuron.
  - Turn-in item IDs: 17203 (Sulfuron Ingot)
  - Started by NPC IDs: {'3': [18628]}
  - Finished at NPC IDs: [[12944]]

## Beer Basted Boar Ribs  (Cooking)
- Recipe item ID: 2889; crafting spell: 2795; product item ID: 2888
- **Quest 384: Beer Basted Boar Ribs** (requires level 5, quest level 7)
  - Objective text: Ragnar Thunderbrew in Kharanos wants 6 Crag Boar Ribs and a mug of Rhapsody Malt.
  - Turn-in item IDs: 2886 (Crag Boar Rib), 2894 (Rhapsody Malt)
  - Started by NPC IDs: [[1267]]
  - Finished at NPC IDs: [[1267]]

## Big Bear Steak  (Cooking)
- Recipe item ID: 3734; crafting spell: 3397; product item ID: 3726
- **Quest 498: The Rescue** (requires level 17, quest level 22)
  - Objective text: Krusk in Tarren Mill needs you to free Drull and Tog'thar from Durnholde Keep.
  - Next in chain: 533
  - Started by NPC IDs: [[2229]]
  - Finished at NPC IDs: [[2229]]

## Blood Sausage  (Cooking)
- Recipe item ID: 3679; crafting spell: 3371; product item ID: 3220
- **Quest 418: Thelsamar Blood Sausages** (requires level 7, quest level 11)
  - Objective text: Bring 3 pieces of Bear Meat, 3 Boar Intestines, and 3 Spider Ichor to Vidra Hearthstove in Thelsamar.
  - Turn-in item IDs: 3172 (Boar Intestines), 3173 (Bear Meat), 3174 (Spider Ichor)
  - Started by NPC IDs: [[1963]]
  - Finished at NPC IDs: [[1963]]

## Crocolisk Gumbo  (Cooking)
- Recipe item ID: 3681; crafting spell: 3373; product item ID: 3664
- **Quest 471: Apprentice's Duties** (requires level 18, quest level 26)
  - Objective text: Collect 6 Giant Crocolisk Skins and bring them to James Halloran in Menethil Harbor.
  - Turn-in item IDs: 3348
  - Prereq quests (any one): [484]
  - Started by NPC IDs: [[2094]]
  - Finished at NPC IDs: [[2094]]

## Crocolisk Steak  (Cooking)
- Recipe item ID: 3678; crafting spell: 3370; product item ID: 3662
- **Quest 385: Crocolisk Hunting** (requires level 10, quest level 15)
  - Objective text: Get 5 pieces of Crocolisk Meat and 6 Crocolisk Skins for Marek Ironheart at the Farstrider Lodge.
  - Turn-in item IDs: 2924 (Crocolisk Meat), 2925
  - Started by NPC IDs: [[1154]]
  - Finished at NPC IDs: [[1154]]

## Curiously Tasty Omelet  (Cooking)
- Recipe item ID: 3682; crafting spell: 3376; product item ID: 3665
- **Quest 296: Ormer's Revenge** (requires level 22, quest level 29)
  - Objective text: Ormer Ironbraid at the Whelgar Excavation Site wants you to kill Sarltooth and return to him with one of his talons once the task is fulfilled.
  - Turn-in item IDs: 3638
  - Prereq quests (any one): [295]
  - Started by NPC IDs: [[1078]]
  - Finished at NPC IDs: [[1078]]

## Dig Rat Stew  (Cooking)
- Recipe item ID: 5487; crafting spell: 6417; product item ID: 5478
- **Quest 862: Dig Rat Stew** (requires level 15, quest level 23)
  - Objective text: Bring 8 Dig Rats to Grub east of the Crossroads.
  - Turn-in item IDs: 5051 (Dig Rat)
  - requiredSkill (skillLine, min skill): [185, 15]
  - Started by NPC IDs: [[3443]]
  - Finished at NPC IDs: [[3443]]

## Dirge's Kickin' Chimaerok Chops  (Cooking)
- Recipe item ID: 21025; crafting spell: 25659; product item ID: 21023
- **Quest 8586: Dirge's Kickin' Chimaerok Chops** (requires level 60, quest level 60)
  - Objective text: Dirge Quikcleave in Gadgetzan wants you to bring him 20 Goblin Rocket Fuel and 20 Deeprock Salt.
  - Turn-in item IDs: 9061 (Goblin Rocket Fuel), 8150 (Deeprock Salt)
  - requiredMinRep: [910, 0]
  - Prereq quests (any one): [8585]
  - Next in chain: 8587
  - Started by NPC IDs: [[8125]]
  - Finished at NPC IDs: [[8125]]

## Hot Lion Chops  (Cooking)
- Recipe item ID: 3735; crafting spell: 3398; product item ID: 3727
- **Quest 501: Elixir of Pain** (requires level 21, quest level 24)
  - Objective text: Bring 10 vials of Mountain Lion Blood to Apothecary Lydon in Tarren Mill.
  - Turn-in item IDs: 3496
  - Next in chain: 502
  - Started by NPC IDs: [[2216]]
  - Finished at NPC IDs: [[2216]]

## Murloc Fin Soup  (Cooking)
- Recipe item ID: 3680; crafting spell: 3372; product item ID: 3663
- **Quest 127: Selling Fish** (requires level 16, quest level 21)
  - Objective text: Bring 10 Spotted Sunfish to Dockmaster Baren in Lakeshire.
  - Turn-in item IDs: 1467
  - Started by NPC IDs: [[381]]
  - Finished at NPC IDs: [[381]]

## Pincer Bites  (Cooking)
- Recipe item ID: 263513; crafting spell: 1270635; product item ID: 263512
- **Quest 93317: Crab Season** (requires level 4, quest level 9)
  - Objective text: Collect 6 pieces of Windsong Crawler Meat.
  - Turn-in item IDs: 257941
  - Started by NPC IDs: [[257006]]
  - Finished at NPC IDs: [[257006]]

## Seasoned Wolf Kabob  (Cooking)
- Recipe item ID: 2701; crafting spell: 2549; product item ID: 1017
- **Quest 90: Seasoned Wolf Kabobs** (requires level 18, quest level 25)
  - Objective text: Gather 10 Lean Wolf Flanks and Stormwind Seasoning Herbs and return to Chef Grual in Darkshire.
  - Turn-in item IDs: 1015 (Lean Wolf Flank), 2665
  - requiredSkill (skillLine, min skill): [185, 50]
  - Started by NPC IDs: [[272]]
  - Finished at NPC IDs: [[272]]

## Skywall Souffle  (Cooking)
- Recipe item ID: 263511; crafting spell: 1270633; product item ID: 263509
- **Quest 92553: Restocking the Larders** (requires level 4, quest level 6)
  - Objective text: Collect 3 Small Eggs and 8 Strider Meat from creatures found throughout the Shen'dar Highlands.
  - Turn-in item IDs: 6889 (Small Egg), 5469 (Strider Meat)
  - Prereq quests (any one): [92514, 93461]
  - Started by NPC IDs: [[251905]]
  - Finished at NPC IDs: [[251905]]

## Soothing Turtle Bisque  (Cooking)
- Recipe item ID: 3737; crafting spell: 3400; product item ID: 3729
- **Quest 555: Soothing Turtle Bisque** (requires level 28, quest level 31)
  - Objective text: Bring 10 pieces of Turtle Meat and some Soothing Spices to Chef Jessen in Southshore.
  - Turn-in item IDs: 3712 (Turtle Meat), 3713 (Soothing Spices)
  - Started by NPC IDs: [[2430]]
  - Finished at NPC IDs: [[2430]]
- **Quest 7321: Soothing Turtle Bisque** (requires level 28, quest level 31)
  - Objective text: Bring 10 pieces of Turtle Meat and some Soothing Spices to Christoph Jeffcoat in Tarren Mill.
  - Turn-in item IDs: 3712 (Turtle Meat), 3713 (Soothing Spices)
  - requiredSkill (skillLine, min skill): [185, 1]
  - Started by NPC IDs: [[2393]]
  - Finished at NPC IDs: [[2393]]

## Strider Stew  (Cooking)
- Recipe item ID: 5486; crafting spell: 6416; product item ID: 5477
- **Quest 2178: Easy Strider Living** (requires level 9, quest level 12)
  - Objective text: Bring back 5 Strider Meat to Alanndarian Nightsong in Auberdine.
  - Turn-in item IDs: 5469 (Strider Meat)
  - requiredSkill (skillLine, min skill): [185, 10]
  - Started by NPC IDs: [[3702]]
  - Finished at NPC IDs: [[3702]]

## Tasty Lion Steak  (Cooking)
- Recipe item ID: 3736; crafting spell: 3399; product item ID: 3728
- **Quest 564: Costly Menace** (requires level 30, quest level 34)
  - Objective text: Darren Malvew of Southshore wants you to kill 8 Mountain Lions and 10 Hulking Mountain Lions.
  - Started by NPC IDs: [[2382]]
  - Finished at NPC IDs: [[2382]]

## Thistle Tea  (Cooking)
- Recipe item ID: 18160; crafting spell: 9513; product item ID: 7676
- **Quest 2359: Klaven's Tower** (requires level 20, quest level 24)
  - Objective text: Steal the Defias Tower Key, break into the Defias Tower and uncover the contents of the Duskwood Chest. Take whatever information you find back to Mathias Shaw in Stormwind. Read Kearnen's Journal to gain insight about the tower.
  - Turn-in item IDs: 7908, 7923
  - Prereq quests (any one): [2360]
  - Next in chain: 2607
  - Started by NPC IDs: [[7024]]
  - Finished at NPC IDs: [[332]]
- **Quest 2478: Mission: Possible But Not Probable** (requires level 20, quest level 24)
  - Objective text: Steal Silixiz's Tower Key from Foreman Silixiz, then kill two Mutated Venture Co. Drones, two Venture Co. Patrollers, and two Venture Co. Lookouts. Assassinate Grand Foreman Gallywix and take his head, then pick the lock on Gallywix's lockbox and steal the Cache of Zanzil's Altered Mixture. Take the Cache and Gallywix's Head back to Shenthul in Orgrimmar for further instruction.
  - Prereq quests (any one): [2458]
  - Next in chain: 2479
  - Started by NPC IDs: [[7233]]
  - Finished at NPC IDs: [[3401]]

## Westfall Stew  (Cooking)
- Recipe item ID: 728; crafting spell: 2543; product item ID: 733
- **Quest 38: Westfall Stew** (requires level 9, quest level 13)
  - Objective text: Salma Saldean wants 3 Stringy Vulture Meat, 3 Goretusk Snouts, 3 Murloc Eyes, 3 Okra.
  - Turn-in item IDs: 729 (Stringy Vulture Meat), 730 (Murloc Eye), 731 (Goretusk Snout), 732
  - Prereq quests (any one): [36]
  - Started by NPC IDs: [[235]]
  - Finished at NPC IDs: [[235]]

## Enchant Bracer - Lesser Healing Power  (Enchanting)
- Recipe item ID: 249489; crafting spell: 1248498; product item ID: None
- **Quest 92755: Mysterious Mysticism** (requires level 30, quest level 35)
  - Objective text: Maintain your reputation with the Gelkis, and bring 3 Greater Mystic Essences to Halea in the Gelkis Village in Desolace.
  - Prereq quests (any one): [1370]
  - Started by NPC IDs: [[253096]]
  - Finished at NPC IDs: [[253096]]

## Firework Cluster Launcher  (Engineering)
- Recipe item ID: 21737; crafting spell: 26443; product item ID: 21570
- **Quest 8882: Cluster Launcher** (requires level 55, quest level 60)
  - Turn-in item IDs: 21100
  - Started by NPC IDs: [[15909]]
  - Finished at NPC IDs: [[15909]]

## Firework Launcher  (Engineering)
- Recipe item ID: 21738; crafting spell: 26442; product item ID: 21569
- **Quest 8877: Firework Launcher** (requires level 45, quest level 60)
  - Turn-in item IDs: 21100
  - Started by NPC IDs: [[15909]]
  - Finished at NPC IDs: [[15909]]

## Flash Bomb  (Engineering)
- Recipe item ID: 6672; crafting spell: 8243; product item ID: 4852
- **Quest 1559: Flash Bomb Recipe** (requires level 30, quest level 37)
  - requiredSkill (skillLine, min skill): [202, 1]
  - Prereq quests (any one): [705]
  - Started by NPC IDs: [[2817]]
  - Finished at NPC IDs: [[2817]]

## Harvester Override Signalcaster  (Engineering)
- Recipe item ID: 277470; crafting spell: 1302161; product item ID: 277132
- **Quest 92911: Harvesting the Harvesters** (requires level 8, quest level 15)
  - Objective text: Ozwin Ironsprocket at Saldean's Farm wants you to bring him 8 Golem Isosprings, 4 Copper Modulators, and a Crude Scope.
  - Turn-in item IDs: 255007 (Golem Isospring), 4363 (Copper Modulator), 4405 (Crude Scope)
  - requiredSkill (skillLine, min skill): [202, 1]
  - Prereq quests (any one): [92910]
  - Started by NPC IDs: [[253395]]
  - Finished at NPC IDs: [[253395]]

## Deviate Scale Belt  (Leatherworking)
- Recipe item ID: 6476; crafting spell: 7955; product item ID: 6468
- **Quest 1487: Deviate Eradication** (requires level 15, quest level 21)
  - Objective text: Ebru in the Wailing Caverns wants you to kill 7 Deviate Ravagers, 7 Deviate Vipers, 7 Deviate Shamblers and 7 Deviate Dreadfangs.
  - Started by NPC IDs: [[5768]]
  - Finished at NPC IDs: [[5768]]

## Kodo Hide Bag  (Leatherworking)
- Recipe item ID: 5083; crafting spell: 5244; product item ID: 5081
- **Quest 769: Kodo Hide Bag** (requires level 4, quest level 10)
  - Objective text: Bring 4 Light Leather and 4 Coarse Thread to Veren Tallstrider in Thunder Bluff.
  - Turn-in item IDs: 2318 (Light Leather), 2320 (Coarse Thread)
  - requiredSkill (skillLine, min skill): [165, 10]
  - Started by NPC IDs: [[3050]]
  - Finished at NPC IDs: [[3050]]

## Light Leather Reagent Bag  (Leatherworking)
- Recipe item ID: 277716; crafting spell: 1302604; product item ID: 277715
- **Quest 96875: Beasts of Thunder Ridge** (requires level 6, quest level 10)
  - Objective text: Kamari in Orgrimmar wants you to collect 5 Rough Lizard Hide from beasts in Thunder Ridge, along with 2 Cured Light Hides.
  - Turn-in item IDs: 275720, 4231 (Cured Light Hide)
  - requiredSkill (skillLine, min skill): [165, 1]
  - Started by NPC IDs: [[5811]]
  - Finished at NPC IDs: [[5811]]

## Moonglow Vest  (Leatherworking)
- Recipe item ID: 6710; crafting spell: 8322; product item ID: 6709
- **Quest 1582: Moonglow Vest** (requires level 8, quest level 18)
  - Objective text: Bring 1 Embossed Leather Gloves, 5 Embossed Leather Boots and 5 Embossed Leather Cloaks to Lotherias in Darnassus.
  - Turn-in item IDs: 4239 (Embossed Leather Gloves), 2309 (Embossed Leather Boots), 2310 (Embossed Leather Cloak)
  - requiredSkill (skillLine, min skill): [165, 90]
  - Started by NPC IDs: [[6034]]
  - Finished at NPC IDs: [[6034]]

## Wild Leather Boots  (Leatherworking)
- Recipe item ID: 8406; crafting spell: 10566; product item ID: 8213
- **Quest 2851: Wild Leather Boots** (requires level 30, quest level 45)
  - Objective text: Bring 2 Nightscape Pants, 2 Nightscape Boots, and 2 Wildvines to Pratt McGrubben in Feathermoon Stronghold.
  - Turn-in item IDs: 8193 (Nightscape Pants), 8197 (Nightscape Boots), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (all): [2848, 2849, 2850]
  - Started by NPC IDs: [[7852]]
  - Finished at NPC IDs: [[7852]]
- **Quest 2858: Wild Leather Boots** (requires level 30, quest level 48)
  - Objective text: Bring 2 Nightscape Pants, 2 Nightscape Boots, and 2 Wildvines to Jangdor Swiftstrider in Camp Mojache.
  - Turn-in item IDs: 8193 (Nightscape Pants), 8197 (Nightscape Boots), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (all): [2855, 2856, 2857]
  - Started by NPC IDs: [[7854]]
  - Finished at NPC IDs: [[7854]]

## Wild Leather Cloak  (Leatherworking)
- Recipe item ID: 8408; crafting spell: 10574; product item ID: 8215
- **Quest 2853: Master of the Wild Leather** (requires level 30, quest level 45)
  - Objective text: Give Pratt's Letter to Telonis, the master leatherworker of Darnassus.
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (all): [2851, 2852]
  - Next in chain: 5143
  - Started by NPC IDs: [[7852]]
  - Finished at NPC IDs: [[4212]]
- **Quest 2860: Master of the Wild Leather** (requires level 30, quest level 45)
  - Objective text: Give Jangdor's Letter to Una, the master leatherworker of Thunder Bluff.
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (all): [2858, 2859]
  - Next in chain: 5148
  - Started by NPC IDs: [[7854]]
  - Finished at NPC IDs: [[3007]]

## Wild Leather Helmet  (Leatherworking)
- Recipe item ID: 8405; crafting spell: 10546; product item ID: 8214
- **Quest 2850: Wild Leather Helmet** (requires level 30, quest level 45)
  - Objective text: Bring 2 Nightscape Tunics, 2 Nightscape Headbands, and a Wildvine to Pratt McGrubben in Feathermoon Stronghold.
  - Turn-in item IDs: 8175 (Nightscape Tunic), 8176 (Nightscape Headband), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (any one): [2847]
  - Started by NPC IDs: [[7852]]
  - Finished at NPC IDs: [[7852]]
- **Quest 2857: Wild Leather Helmet** (requires level 30, quest level 45)
  - Objective text: Bring 2 Nightscape Tunics, 2 Nightscape Headbands, and a Wildvine to Jangdor Swiftstrider in Camp Mojache.
  - Turn-in item IDs: 8175 (Nightscape Tunic), 8176 (Nightscape Headband), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (any one): [2854]
  - Started by NPC IDs: [[7854]]
  - Finished at NPC IDs: [[7854]]

## Wild Leather Leggings  (Leatherworking)
- Recipe item ID: 8407; crafting spell: 10572; product item ID: 8212
- **Quest 2852: Wild Leather Leggings** (requires level 30, quest level 45)
  - Objective text: Bring 2 Turtle Scale Helms, 2 Turtle Scale Bracers, and 2 Wildvines to Pratt McGrubben in Feathermoon Stronghold.
  - Turn-in item IDs: 8191 (Turtle Scale Helm), 8198 (Turtle Scale Bracers), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (all): [2848, 2849, 2850]
  - Started by NPC IDs: [[7852]]
  - Finished at NPC IDs: [[7852]]
- **Quest 2859: Wild Leather Leggings** (requires level 30, quest level 45)
  - Objective text: Bring 2 Turtle Scale Helms, 2 Turtle Scale Bracers, and 2 Wildvines to Jangdor Swiftstrider in Camp Mojache.
  - Turn-in item IDs: 8191 (Turtle Scale Helm), 8198 (Turtle Scale Bracers), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (all): [2855, 2856, 2857]
  - Started by NPC IDs: [[7854]]
  - Finished at NPC IDs: [[7854]]

## Wild Leather Shoulders  (Leatherworking)
- Recipe item ID: 8403; crafting spell: 10529; product item ID: 8210
- **Quest 2848: Wild Leather Shoulders** (requires level 30, quest level 45)
  - Objective text: Bring 6 Thick Armor Kits and a Wildvine to Pratt McGrubben in Feathermoon Stronghold.
  - Turn-in item IDs: 8173 (Thick Armor Kit), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (any one): [2847]
  - Started by NPC IDs: [[7852]]
  - Finished at NPC IDs: [[7852]]
- **Quest 2855: Wild Leather Shoulders** (requires level 30, quest level 45)
  - Objective text: Bring 6 Thick Armor Kits and a Wildvine to Jangdor Swiftstrider in Camp Mojache.
  - Turn-in item IDs: 8173 (Thick Armor Kit), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (any one): [2854]
  - Started by NPC IDs: [[7854]]
  - Finished at NPC IDs: [[7854]]

## Wild Leather Vest  (Leatherworking)
- Recipe item ID: 8404; crafting spell: 10544; product item ID: 8211
- **Quest 2849: Wild Leather Vest** (requires level 30, quest level 45)
  - Objective text: Bring 2 Turtle Scale Breastplates, 2 Turtle Scale Gloves, and a Wildvine to Pratt McGrubben in Feathermoon Stronghold.
  - Turn-in item IDs: 8189 (Turtle Scale Breastplate), 8187 (Turtle Scale Gloves), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (any one): [2847]
  - Started by NPC IDs: [[7852]]
  - Finished at NPC IDs: [[7852]]
- **Quest 2856: Wild Leather Vest** (requires level 30, quest level 45)
  - Objective text: Bring 2 Turtle Scale Breastplates, 2 Turtle Scale Gloves, and a Wildvine to Jangdor Swiftstrider in Camp Mojache.
  - Turn-in item IDs: 8189 (Turtle Scale Breastplate), 8187 (Turtle Scale Gloves), 8153 (Wildvine)
  - requiredSkill (skillLine, min skill): [165, 225]
  - Prereq quests (any one): [2854]
  - Started by NPC IDs: [[7854]]
  - Finished at NPC IDs: [[7854]]

## Festival Dress  (Tailoring)
- Recipe item ID: 21722; crafting spell: 26403; product item ID: 21154
- **Quest 8878: Festive Recipes** (requires level 50, quest level 60)
  - Turn-in item IDs: 21100
  - Started by NPC IDs: [[15909]]
  - Finished at NPC IDs: [[15909]]

## Festival Suit  (Tailoring)
- Recipe item ID: 21723; crafting spell: 26407; product item ID: 21542
- **Quest 8878: Festive Recipes** (requires level 50, quest level 60)
  - Turn-in item IDs: 21100
  - Started by NPC IDs: [[15909]]
  - Finished at NPC IDs: [[15909]]
