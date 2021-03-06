"""
动态规划（DP）：
    https://blog.csdn.net/qq_1932568757/article/details/82725132
    https://www.sohu.com/a/153858619_466939
    通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法，适用于有重叠子问题和最优子结构性质的问题，耗时远远小于朴素算法
    动态规划问题满足三大重要性质：
        最优子结构性质：如果问题的最优解所包含的子问题的解也是最优的，我们就称该问题具有最优子结构性质，
                     最优子接口性质为动态规划算法解决问题提供了重要算法；
        子问题重叠性质：子问题重叠性质是指在用递归算法自顶向下对问题进行求解时候，每次产生的子问题并不总是新问题，有些子问题会被重复计算多次
                     动态规划中，对这些子问题只计算一次，保存计算结果，再次需要计算的时候，知识在表格中查看结果，获得较高的效率
        后无效性：将各阶段按照一定的次序排列好后，对于某个给定的阶段状态，它以前各计算的状态无法直接影响它未来的决策，而只能通过当前的这个状态
"""