import asyncio
import unittest
from unittest import TestCase

from models.creators import Person
from utils.mgp import producer_template_exists, get_producer_templates, producer_cat_exists, get_producer_cats


class TestProducerTemplate(TestCase):
    # def test_template_exists(self):
    #     true = ["Wowaka", "针原翼"]
    #     for t in true:
    #         self.assertTrue(asyncio.run(producer_template_exists(t)))
    #         # print("Template " + t + " exists.")
    #     false = ["黑幕", "这是一个不存在的模板"]
    #     for t in false:
    #         self.assertFalse(asyncio.run(producer_template_exists(t)))
    #         # print("Template " + t + " does not exist.")

    def test_get_producer_templates(self):
        producers = [Person("WowakaP", ["黑幕"]),
                     Person("谁也不是", ["胡话P", "LyricsKai"]),
                     Person("什么鬼", ["HarryP", "针原翼"])]
        result = asyncio.run(get_producer_templates(producers))
        self.assertEqual(['Wowaka', '针原翼'], result)


class TestProducerCat(TestCase):
    # def test_cat_exists(self):
    #     true = ["wowaka"]
    #     for t in true:
    #         self.assertTrue(producer_cat_exists(t)))
    #     false = ["黑幕", "这是一个不存在的分类"]
    #     for t in false:
    #         self.assertFalse(asyncio.run(producer_cat_exists(t)))

    def test_get_producer_cats(self):
        producers = [Person("黑幕", ["wowakaP"]),
                     Person("谁也不是", ["胡话P", "LyricsKai"])]
        self.assertEqual(['wowaka'], asyncio.run(get_producer_cats(producers)))


if __name__ == "__main__":
    unittest.main()
