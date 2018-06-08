[English](https://github.com/yunshuipiao/algorithms/blob/master/README.md) | 简体中文

Python版数据结构和算法
=========================================

python版数据结构和算法实现的简约版小示例  

谢谢关注。有多种方法可以贡献你的代码。[从这里开始吧](https://github.com/keon/algorithms/blob/master/CONTRIBUTING.md)  

[或者可以用不同语言来完成上述算法，期待加入](https://github.com/yunshuipiao/sw-algorithms)：https://github.com/yunshuipiao/sw-algorithms

## 测试

### 单元测试
如下代码可以运行全部测试：  
```

python3 -m unittest discover tests

```

针对特定模块(比如：sort)的测试， 可以使用如下代码：  
```

python3 -m unittest tests.test_sort

```

### 使用pytest
如下代码运行所有测试代码：  
```

pyhton3 -m pytest tests

```

## 安装
如果想在代码中使用算法API， 可按如下步骤进行：
```

pip3 install git+https://github.com/keon/algorithms

```

通过创建python文件(比如：在sort模块使用merge_sort)进行测试： 
```

from sort import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort.merge_sort(my_list)
    print(my_list)
    
```

## 卸载
如下代码可卸载该API：

```

pip3 uninstall -y algorithms

```

## 实现列表

- [array:数组](arrays)
    - [delete_nth: 删除第n项](arrays/delete_nth.py)
    - [flatten：数组降维](arrays/flatten.py)
    - [garage：停车场](arrays/garage.py)
    - [josephus_problem: 约瑟夫问题](arrays/josephus_problem.py)
    - [longest_non_repeat：最长不重复子串](arrays/longest_non_repeat.py/)
    - [merge_intervals：合并重叠间隔](arrays/merge_intervals.py)
    - [missing_ranges：遗失的范围](arrays/missing_ranges.py)
    - [plus_one：加一运算](arrays/plus_one.py)
    - [rotate_array：反转数组](arrays/rotate_array.py)
    - [summary_ranges：数组范围](arrays/summary_ranges.py)
    - [three_sum：三数和为零](arrays/three_sum.py)
    - [two_sum：两数和](arrays/two_sum.py)
    - [move_zeros_to_end: 0后置问题](arrays/move_zeros_to_end.py)
- [backtrack：回溯](backtrack)
    - [general_solution.md：一般方法](backtrack/)
    - [anagram：同字母异序词](backtrack/anagram.py)
    - [array_sum_combinations：数组和](backtrack/array_sum_combinations.py)
    - [combination_sum：和的合并](backtrack/combination_sum.py)
    - [expression_add_operators：给表达式添加运算符](backtrack/expression_add_operators.py)
    - [factor_combinations：因素组合](backtrack/factor_combinations.py)
    - [generate_abbreviations：缩写生成](backtrack/generate_abbreviations.py)
    - [generate_parenthesis：括号生成](backtrack/generate_parenthesis.py)
    - [letter_combination：字母组合](backtrack/letter_combination.py)
    - [palindrome_partitioning：字符串的所有回文子串](backtrack/palindrome_partitioning.py)
    - [pattern_match：模式匹配](backtrack/pattern_match.py)
    - [permute：排列](backtrack/permute.py)
    - [permute_unique：唯一排列](backtrack/permute_unique.py)
    - [subsets：子集](backtrack/subsets.py)
    - [subsets_unique：唯一子集](backtrack/subsets_unique.py)
- [bfs：广度优先搜索](bfs)
    - [shortest_distance_from_all_buildings：所有建筑物的最短路径：](bfs/shortest_distance_from_all_buildings.py)
    - [word_ladder：词语阶梯](bfs/word_ladder.py)
- [bit：位操作](bit)
    - [bytes_int_conversion：字节整数转换](bit/bytes_int_conversion.py)
    - [count_ones：统计1出现的次数](bit/count_ones.py)
    - [find_missing_number：寻找缺失数](bit/find_missing_number.py)
    - [power_of_two：2的n次方数判断](bit/power_of_two.py)
    - [reverse_bits：反转位](bit/reverse_bits.py)
    - [single_number2：寻找出现1次的数（2)](bit/single_number2.py)
    - [single_number:寻找出现1次的数（1)](bit/single_number.py)
    - [subsets: 求所有子集](bit/subsets.py)
    - [add_bitwise_operator：无操作符的加法](bit/add_bitwise_operator.py)
- [calculator：计算](calculator)
    - [math_parser: 数字解析](calculator/math_parser.py)
- [dfs：深度优先搜索](dfs)
    - [all_factors：因素分解](dfs/all_factors.py)
    - [count_islands：岛计数](dfs/count_islands.py)
    - [pacific_atlantic：太平洋大西洋](dfs/pacific_atlantic.py)
    - [sudoku_solver：数独解法](dfs/sudoku_solver.py)
    - [walls_and_gates：墙和门](dfs/walls_and_gates.py)
- [dp：动态规划](dp)
    - [buy_sell_stock：股票买卖](dp/buy_sell_stock.py)
    - [climbing_stairs：爬梯子问题](dp/climbing_stairs.py)
    - [combination_sum：和组合问题](dp/combination_sum.py)
    - [house_robber：打家劫舍](dp/house_robber.py)
    - [knapsack：背包问题](dp/knapsack.py)
    - [longest_increasing：最长递增子序列](dp/longest_increasing.py)
    - [max_product_subarray：最大子数组乘积](dp/max_product_subarray.py)
    - [max_subarray：最大子数组](dp/max_subarray.py)
    - [num_decodings：数字解码](dp/num_decodings.py)
    - [regex_matching：正则匹配](dp/regex_matching.py)
    - [word_break：单词分割](dp/word_break.py)
- [graph：图](graph)
    - [2-sat：2-sat](graph/satisfiability.py)
    - [clone_graph：克隆图](graph/clone_graph.py)
    - [cycle_detection：判断圈算法](graph/cycle_detection.py)
    - [find_path：发现路径](graph/find_path.py)
    - [graph：图](graph/graph.py)
    - [traversal：遍历](graph/traversal.py)
    - [markov_chain：马尔可夫链](graph/markov_chain.py)
- [heap：堆](heap)
    - [merge_sorted_k_lists：合并k个有序链](heap/merge_sorted_k_lists.py)
    - [skyline：天际线](heap/skyline.py)
    - [sliding_window_max：滑动窗口最大值](heap/sliding_window_max.py)
- [linkedlist：链表](linkedlist)
    - [add_two_numbers：链表数相加](linkedlist/add_two_numbers.py)
    - [copy_random_pointer：复制带有随机指针的链表](linkedlist/copy_random_pointer.py)
    - [delete_node：删除节点](linkedlist/delete_node.py)
    - [first_cyclic_node：环链表的第一个节点](linkedlist/first_cyclic_node.py)
    - [is_cyclic：判断环链表](linkedlist/is_cyclic.py)
    - [is_palindrome：回文链表](linkedlist/is_palindrome.py)
    - [kth_to_last：倒数第k个节点](linkedlist/kth_to_last.py)
    - [linkedlist： 链表](linkedlist/linkedlist.py)
    - [remove_duplicates：删除重复元素](linkedlist/remove_duplicates.py)
    - [reverse：反转链表](linkedlist/reverse.py)
    - [rotate_list：旋转链表](linkedlist/rotate_list.py)
    - [swap_in_pairs：链表节点交换](linkedlist/swap_in_pairs.py)
- [map：映射](map)
    - [hashtable：哈希表](map/hashtable.py)
    - [separate_chaining_hashtable：拉链法哈希表](map/separate_chaining_hashtable.py)
    - [longest_common_subsequence：最长公共子序列](map/longest_common_subsequence.py)
    - [randomized_set：随机集](map/randomized_set.py)
    - [valid_sudoku：有效数独](map/valid_sudoku.py)
- [math：数学问题](maths)
    - [extended_gcd：扩展欧几里得算法](maths/extended_gcd.py)
    - [gcd/lcm：最大公约数和最小公倍数](maths/gcd.py)
    - [prime_test：主要测试](maths/prime_test.py)
    - [primes_sieve_of_eratosthenes：埃拉托色尼的质数筛](maths/primes_sieve_of_eratosthenes.py)
    - [generate_strobogrammtic：生成对称数](maths/generate_strobogrammtic.py)
    - [is_strobogrammatic：判断对称数](maths/is_strobogrammatic.py)
    - [nth_digit：第n位](maths/nth_digit.py)
    - [rabin_miller：米勒-拉宾素性检验](maths/rabin_miller.py)
    - [rsa：rsa加密](maths/rsa.py)
    - [sqrt_precision_factor：开发精度因素](maths/sqrt_precision_factor.py)
    - [pythagoras：毕达哥拉斯](maths/pythagoras.py)
- [matrix：矩阵](matrix)
    - [matrix_rotation：矩阵旋转](matrix/matrix_rotation.txt)
    - [copy_transform：复制变换](matrix/copy_transform.py)
    - [bomb_enemy：炸弹人](matrix/bomb_enemy.py)
    - [rotate_image：旋转图像](matrix/rotate_image.py)
    - [sparse_dot_vector：解析点向量](matrix/sparse_dot_vector.py)
    - [sparse_mul：稀疏矩阵](matrix/sparse_mul.py)
    - [spiral_traversal：循环遍历](matrix/spiral_traversal.py)
    - [count_paths：计算路径](matrix/count_paths.py)
- [queue：队列](queues)
    - [max_sliding_window：最大移动窗口](queues/max_sliding_window.py)
    - [moving_average：移动平均](queues/moving_average.py)
    - [queue：队列](queues/queue.py)
    - [reconstruct_queue：重建队列](queues/reconstruct_queue.py)
    - [zigzagiterator：锯齿形迭代](queues/zigzagiterator.py)
- [search：查找](search)
    - [binary_search：二分查找](search/binary_search.py)
    - [count_elem：元素计数](search/count_elem.py)
    - [first_occurance：首次出现](search/first_occurance.py)
    - [last_occurance：最后一次出现](search/last_occurance.py)
- [set：集合](set)
    - [randomized_set：随机集合](set/randomized_set.py)
    - [set_covering：集合覆盖](set/set_covering.py)
- [sort：排序](sort)
    - [bubble_sort：冒泡排序](sort/bubble_sort.py)
    - [comb_sort：梳排序](sort/comb_sort.py)
    - [counting_sort：计数排序](sort/counting_sort.py)
    - [heap_sort：堆排序](sort/heap_sort.py)
    - [insertion_sort：插入排序](sort/insertion_sort.py)
    - [meeting_rooms：会议室](sort/meeting_rooms.py)
    - [merge_sort：归并排序](sort/merge_sort.py)
    - [quick_sort：快速排序](sort/quick_sort.py)
    - [selection_sort：选择排序](sort/selection_sort.py)
    - [sort_colors：颜色排序](sort/sort_colors.py)
    - [topsort：top排序](sort/topsort.py)
    - [wiggle_sort：摇摆排序](sort/wiggle_sort.py)
- [stack：栈](stack)
    - [longest_abs_path：最长相对路径](stack/longest_abs_path.py)
    - [simplify_path：简化路径](stack/simplify_path.py)
    - [stack：栈](stack/stack.py)
    - [valid_parenthesis：验证括号](stack/valid_parenthesis.py)
- [string：字符串](strings)
    - [add_binary：二进制数相加](strings/add_binary.py)
    - [breaking_bad：打破坏](strings/breaking_bad.py)
    - [decode_string：字符串编码](strings/decode_string.py)
    - [encode_decode：编解码](strings/encode_decode.py)
    - [group_anagrams：群组错位词](strings/group_anagrams.py)
    - [int_to_roman：整数转换罗马数字](strings/int_to_roman.py)
    - [is_palindrome：回文字符串](strings/is_palindrome.py)
    - [license_number：拍照号码](strings/license_number.py)
    - [make_sentence：造句](strings/make_sentence.py)
    - [multiply_strings：字符串相乘](strings/multiply_strings.py)
    - [one_edit_distance：一个编辑距离](strings/one_edit_distance.py)
    - [rabin_karp：Rabin-Karp 算法](strings/rabin_karp.py)
    - [reverse_string：反转字符串](strings/reverse_string.py)
    - [reverse_vowel：反转元音](strings/reverse_vowel.py)
    - [reverse_words：反转单词](strings/reverse_words.py)
    - [roman_to_int：罗马数转换整数](strings/roman_to_int.py)
    - [word_squares：单词平方](strings/word_squares.py)
- [tree：树](tree)
    - [segment-tree：线段树](tree/segment_tree)
        - [segment_tree：线段树](tree/segment_tree/segment_tree.py)
    - [binary_tree_paths：二叉树路径](tree/binary_tree_paths.py)
    - [bintree2list：二叉树转换链表](tree/bintree2list.py)
    - [bst：二叉搜索树](tree/tree/bst)
        - [array2bst：数组转换](tree/bst/array2bst.py)
        - [bst_closest_value：最近二叉搜索树值](tree/bst/bst_closest_value.py)
        - [BSTIterator：二叉搜索树迭代](tree/bst/BSTIterator.py)
        - [delete_node：删除节点](tree/bst/delete_node.py)
        - [is_bst：判断二叉搜索树](tree/bst/is_bst.py)
        - [kth_smallest：二叉搜索树的第k小节点](tree/bst/kth_smallest.py)
        - [lowest_common_ancestor：最近公共祖先](tree/bst/lowest_common_ancestor.py)
        - [predecessor：前任](tree/bst/predecessor.py)
        - [serialize_deserialize：序列化反序列化](tree/bst/serialize_deserialize.py)
        - [successor：继承者](tree/bst/successor.py)
        - [unique_bst：唯一BST](tree/bst/unique_bst.py)
    - [deepest_left：最深叶子节点](tree/deepest_left.py)
    - [invert_tree：反转树](tree/invert_tree.py)
    - [is_balanced：判断平衡树](tree/is_balanced.py)
    - [is_subtree：判断子树](tree/is_subtree.py)
    - [is_symmetric：判断对称树](tree/is_symmetric.py)
    - [longest_consecutive：最长连续节点](tree/longest_consecutive.py)
    - [lowest_common_ancestor：最近公共祖先](tree/lowest_common_ancestor.py)
    - [max_height：最大高度](tree/max_height.py)
    - [max_path_sum：最长路径和](tree/max_path_sum.py)
    - [min_height：最小高度](tree/min_height.py)
    - [path_sum2：路径和2](tree/path_sum2.py)
    - [path_sum：路径和](tree/path_sum.py)
    - [pretty_print：完美打印](tree/pretty_print.py)
    - [same_tree：相同树](tree/same_tree.py)
    - [traversal：遍历](tree/traversal)
        - [inorder：中序遍历](tree/traversal/inorder.py)
        - [level_order：层次遍历](tree/traversal/level_order.py)
        - [zigzag：锯齿形遍历](tree/traversal/zigzag.py)
    - [tree：树](tree/tree.py)
    - [trie：字典树](tree/trie)
        - [add_and_search：添加和查找](tree/trie/add_and_search.py)
        - [trie：字典](tree/trie/trie.py)
- [union-find：并查集](union-find)
    - [count_islands：岛计数](union-find/count_islands.py)
 

## 贡献
谢谢主要维护人员：

* [Keon Kim](https://github.com/keon)
* [Rahul Goswami](https://github.com/goswami-rahul)
* [Christian Bender](https://github.com/christianbender)
* [Ankit Agarwal](https://github.com/ankit167)
* [Hai Hoang Dang](https://github.com/danghai)
* [Saad](https://github.com/SaadBenn)

以及[所有贡献者](https://github.com/keon/algorithms/graphs/contributors)

