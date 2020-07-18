## 学习笔记

### 第一周学习总结

我是在参加了7天体验营之后才下定决心报名训练营的，在7天的体验营以及衔接而来的第一周训练营内容，我觉得学习到的最重要的内容并不是数据结构的概念知识，而是超哥教的“五毒神掌”，“切题四件套” 以及如何通过搜索找到平时我们所需要的内容或遇到的困难的解决方案。根据学到的这些方法，我同时开启了LeetCode刷题的道路，曾经的我只会用暴力法解决2Sum题，而现在我也在慢慢地进步着，学习别人写的好的代码和思路。不得不说训练营的内容对小白来说真的是指路明灯，我现在刷题也逐渐上头，而且每当懒散的时候我都会去看大厂的招聘信息，看看自己是否能够符合意向岗位所要求的内容（不能），算是给自己一针又一针的鸡血，然后对自己说“滚去刷题/学习”。

希望我能在接下来的6周学习中坚持下去。

第一周刷题记录：31题，其中9题为上周的复刷。简单18/中等9/困难4

| 题目                        | 难度                           | 总次数 |
| --------------------------- | ------------------------------ | ------ |
| [1] 两数之和                | <font color=009A74>简单</font> | 3      |
| [11] 盛水最多的容器         | <font color=EF7C44>中等</font> | 3      |
| [15] 三数之和               | <font color=EF7C44>中等</font> | 2      |
| [20] 有效的括号             | <font color=009A74>简单</font> | 2      |
| [21] 合并两个有序链表       | <font color=009A74>简单</font> | 1      |
| [24] 两两交换链表中的节点   | <font color=EF7C44>中等</font> | 3      |
| [26] 删除排序数组中的重复项 | <font color=009A74>简单</font> | 3      |
| [35] 搜索插入位置           | <font color=009A74>简单</font> | 1      |
| [49] 字母异位词分组         | <font color=EF7C44>中等</font> | 1      |
| [66] 加一                   | <font color=009A74>简单</font> | 1      |
| [70] 爬楼梯                 | <font color=009A74>简单</font> | 2      |
| [84] 柱状图中最大的矩形     | <font color=EC4C46>困难</font> | 1      |
| [88] 合并两个有序数组       | <font color=009A74>简单</font> | 1      |
| [96] 不同的二叉搜索树       | <font color=EF7C44>中等</font> | 2      |
| [97] 交错字符串             | <font color=EC4C46>困难</font> | 1      |
| [98] 验证二叉搜索树         | <font color=EF7C44>中等</font> | 2      |
| [104] 二叉树的最大深度      | <font color=009A74>简单</font> | 3      |
| [111] 二叉树的最小深度      | <font color=009A74>简单</font> | 3      |
| [141] 三角形的最小路径和    | <font color=009A74>简单</font> | 2      |
| [120] 环形链表              | <font color=EF7C44>中等</font> | 3      |
| [155] 最小栈                | <font color=009A74>简单</font> | 2      |
| [189] 旋转数组              | <font color=009A74>简单</font> | 2      |
| [206] 旋转数组              | <font color=009A74>简单</font> | 1      |
| [239] 滑动窗口最大值        | <font color=EC4C46>困难</font> | 1      |
| [242] 有效的字母异位词      | <font color=009A74>简单</font> | 1      |
| [283] 移动零                | <font color=009A74>简单</font> | 2      |
| [312] 戳气球                | <font color=EC4C46>困难</font> | 1      |
| [350] 两个数组的交集 II     | <font color=009A74>简单</font> | 3      |
| [589] N叉树的前序遍历       | <font color=009A74>简单</font> | 3      |
| [641] 设计循环双端队列      | <font color=EF7C44>中等</font> | 1      |
| [758] 判断二分图            | <font color=EF7C44>中等</font> | 3      |

以及总结了超哥教的“**三步走**”的脑图

![](./pics/CPF.png)



### 学习总结主题 #1 

**用 add first 或 add last 这套新的 API 改写 Deque 的代码。**

```java
Deque<String> deque = new LinkedList<String>();

deque.addFirst("a");
deque.addFirst("b");
deque.addFirst("c");
System.out.println(deque);

String str = deque.peekFirst();
System.out.println(str);
System.out.println(deque);

while (deque.size > 0) {
  System.out.println(deque.removeFirst());
}
System.out.println(deque);
```



### 学习总结主题 #2

**分析 Queue 和 Priority Queue 的源码。**