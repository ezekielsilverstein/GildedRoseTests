# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)

    def test_quality_decrease_by_two(self):
        item = Item(name="+5 Dexterity Vest", sell_in=-3, quality=5)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality-2, item.quality)

    def test_no_neg_quality(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=0)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality, item.quality)
       
    def test_aged_brie_lt50(self):
        item = Item(name="Aged Brie", sell_in=5, quality=5)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality + 1, item.quality)

    def test_aged_brie_50(self):
        item = Item(name="Aged Brie", sell_in=5, quality=50)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality, item.quality)

    def test_quality_max_50(self):
        item = Item(name="Aged Brie", sell_in=5, quality=50)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality, item.quality)

    def test_sulfuras_quality(self):
        item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality, item.quality, 80)

    def test_conjured_quality(self):
        item = Item(name="Conjured", sell_in=5, quality=30)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality - 2, item.quality)
       

    def test_backstage_passes_gt_10days(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality +1, item.quality)

    def test_backstage_passes_gt_5days(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=20)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality +2, item.quality)

    def test_backstage_passes_lt_5days(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=20)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(yday_item_quality +3, item.quality)

    def test_backstage_passes_0days(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)
        yday_item_quality = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(item.quality, 0)


if __name__ == '__main__':
    unittest.main()
