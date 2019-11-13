# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import xlrd
from xlutils.copy import copy


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if not excel_path:
            excel_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/common/data_case.xlsx"
        self.excel_path = excel_path
        if not index:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        # 行数
        # self.rows = self.table.nrows
        # [[], []]

    # 获取excel数据，按照每一行一个list，添加到一个大的list中
    def get_data(self):
        # 拿出全部的数据
        result = []
        if self.get_lines():
            for i in range(self.get_lines()):
                # 取某一行的数据
                col = self.table.row_values(i)
                result.append(col)
            return result
        else:
            return None

    def get_lines(self):
        """
        获取excel行数
        优化：
            判断行数，没有返回None
        :return:
        """
        rows = self.table.nrows
        if rows >= 1:
            return rows
        else:
            return None

    def get_col_value(self, row, col):
        """
        获取单元格的数据
        :return:
        """
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    def write_value(self, row, col, value):
        """
        写入数据
            可能存在的问题：覆盖的问题
            使用xlutils
        :return:
        """
        # 拿到整个excel的数据-复制
        read_value = self.data
        write_data = copy(read_value)
        print(write_data)
        write_data.get_sheet(0).write(row, 3, value)
        write_data.save(self.excel_path)
        print(self.excel_path)


if __name__ == '__main__':
    file_path = '/Users/qing.li/PycharmProjects/hm/selenium_/imooc/common/keyword.xls'
    ex = ExcelUtil(file_path)
    print(ex.write_value(8, 1, "追加的内容为什么不展示呢"))
    print(ex.get_data())
