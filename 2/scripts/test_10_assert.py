"""回顾：断言"""
# 断言概念：让程序代替认为去判断程序执行的结果是否符合预期结果的过程
# 断言方法：
#     1. python自带断言 assert
#     2. unittest框架内学习断言 self.assertIn
import unittest



class Test01(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,1)
        list1=[1,2,3,4]
        list2=[1,2,3,4]
        desc={"name":"张三","age":18}
        self.assertIn("张三",desc)
        self.assertListEqual(list1,list2)
        assert "张三" == desc,"出错啦，这俩货不相等"
        assert "a" in "admin"