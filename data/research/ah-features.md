# AH site feature survey (from general knowledge; sites not re-fetched, verify details)

Data tags: S = hourly snapshot, L = live AH API, R = recipe/item static data, B = browser localStorage.

1. Crafting profit calculator - TSM, Nexus Hub, Undermine Exchange (retail). Profit = sell price minus reagent cost per recipe. Needs S/L, R.
2. Flip finder (cross-item, buy low / relist) - Saddlebag Exchange, TSM Shopping/Sniper. Spread vs 7-day median. Needs S history.
3. Vendor flips - Saddlebag, TSM. AH items priced under NPC vendor sell price. Needs S, vendor prices.
4. Deal finder / below-market list - Nexus Hub, TSM Sniper, Oribos Exchange. Listings under X% of median. Needs L or latest S, median history.
5. Price history charts + volume - Nexus Hub, wowauctions.net, Undermine Exchange. Min/median/quantity over time. Needs accumulated S.
6. Shopping list / farm list - TSM Shopping, Undermine. Item list with live total and cheapest buy. Needs L, B.
7. Price alerts - TSM app, Saddlebag. Notify when threshold crossed. Needs S, B + Notification API or webhook (static limits).
8. Disenchant / prospect / mill value - TSM, Oribos. Expected value from yield tables vs item price. Needs R drop tables, S.
9. Reagent shopping for a crafting queue - TSM Crafting. Aggregated materials, buy-vs-craft per reagent. Needs R, L.
10. Realm/connected-realm comparison and region price - Undermine, wowauctions, Saddlebag. Needs S per realm.
11. Market-value / "sells per day" estimate - TSM (DBRegionSaleRate), Nexus Hub. Needs S deltas of quantity (approximate).
12. Item search with filters (category, ilvl, profit) - all sites. Needs S, item index.
13. Auction house cut and deposit calculator - TSM. Net after 5% cut. Pure client math.
14. Vendor reputation/favor calculators (this Waylaid tab) - Wowhead guides, theforeverguides. Cost per favor/rep using live prices. Needs L, waylaid.json.
15. Trending movers (biggest 24h gainers/losers) - Nexus Hub, Undermine. Needs 2+ S.
