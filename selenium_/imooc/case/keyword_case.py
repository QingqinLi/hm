# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import sys
sys.path.append("..")
from util.excel_util import ExcelUtil
from key_word.actionMethod import ActionMethod


class KeywordCase:
    def __init__(self):
        self.action_method = ActionMethod()

    def run_main(self):
        excel_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/common/keyword.xls"
        handle_excel = ExcelUtil(excel_path)
        # 拿到数据的行数
        case_lines = handle_excel.get_lines()
        # 循环行数，执行每一行的case
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                if is_run == 'yes':
                    case_method = handle_excel.get_col_value(i, 4)
                    case_value = handle_excel.get_col_value(i, 5)
                    case_element = handle_excel.get_col_value(i, 6)
                    case_except_method = handle_excel.get_col_value(i, 7)
                    case_except_content = handle_excel.get_col_value(i, 8)
                    # 取出来是''不是None
                    self.run_method(case_method, case_value, case_element)
                    if case_except_method:
                        except_value = self.get_except_result_value(case_except_content)
                        if except_value[0] == 'text':
                            result = self.run_method(case_except_method)
                            if case_except_content in result:
                                # case运行成功，写入结果
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(case_except_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')

        # 判断是否执行
        # 拿到执行方法
        # 拿到操作值
        # 拿到操作元素
            # 根据是否有输入数据，判断方法

    def run_method(self, case_method, case_value=None, case_element=None):
        m = getattr(self.action_method, case_method)
        # print("case_value", case_value)
        # print(case_method, case_value, case_element)
        if case_value and case_element:
            result = m(case_element, case_value)
        elif case_element:
            result = m(case_element)
        elif case_value:
            result = m(case_value)
        else:
            result = m()
        return result

    # 获取预期结果值
    def get_except_result_value(self, data):
        return data.split("=")


if __name__ == '__main__':
    keywordcase = KeywordCase()
    keywordcase.run_main()