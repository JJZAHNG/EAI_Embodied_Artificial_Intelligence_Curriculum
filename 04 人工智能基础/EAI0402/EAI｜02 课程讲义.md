# EAI｜02 图像数据建模与训练集质量优化

课程名称：人工智能基础 

单元主题：图像识别与模型训练提升 

授课年级：初中高年级 / 高一 

计划课时：90分钟

## 课程概括

本节课聚焦图像识别模型训练质量的优化策略，系统讲解图像特征的表达方式、样本构建规范与模型过拟合问题，并引导学生理解混淆矩阵的含义。通过Teachable Machine工具，学生将亲手构建一个三分类的情绪识别模型，并从模型准确率出发进行训练数据的诊断与优化。

## 教学目标

### 🎯知识与技能

- 理解图像特征提取与卷积感知机制的基本概念；
- 掌握图像数据采集与训练集构建的常见规范与技巧；
- 认识过拟合现象及其成因，初步掌握提升模型泛化能力的方法；
- 能够使用混淆矩阵分析模型分类性能。

### 🎯过程与方法

- 通过案例讲解和模型演示掌握图像建模原理；
- 分组采集“表情图像”，训练三分类模型；
- 结合混淆矩阵结果分析分类错误原因，优化训练集设计。

### 🎯情感态度价值观

- 引导学生以科学方法优化实验设计，注重数据质量；
- 培养学生追踪误差与持续迭代的AI开发意识；
- 强调模型性能不只是“调参数”，更是“设计数据”。

## 重点难点

| 教学重点                 | 教学难点                   |
| ------------------------ | -------------------------- |
| 图像样本规范与训练集构建 | 理解过拟合与泛化的数学机制 |
| 混淆矩阵的结果分析与解读 | 准确率与类别偏误的关系     |

## 教学准备

| 软件              | 硬件                   | 扩展                    |
| ----------------- | ---------------------- | ----------------------- |
| Teachable Machine | 学生个人电脑，网络环境 | 拍摄工具 / 表情示范图集 |

## 教学过程

| 环节     | 主要内容                                                     | 预计时长 | 素材附件                |
| -------- | ------------------------------------------------------------ | -------- | ----------------------- |
| 导入     | 展示AI情绪识别案例：识别“愤怒/快乐/中性”表情，引发数据质量思考 | 10分钟   | 视频片段2.mp4           |
| 知识讲解 | 图像特征 → 样本规范 → 训练误差；引入过拟合和泛化；混淆矩阵结构讲解 | 25分钟   | 课件PPT_02.pdf          |
| 工具实操 | 构建“微笑/生气/中性”三分类模型，演示模型训练与测试           | 25分钟   | 示例图像数据 / 工具指南 |
| 分组练习 | 学生分组采集3类表情数据，自定义训练样本集，训练并测试分类模型 | 20分钟   | 小组数据采集表.xlsx     |
| 数据分析 | 分析混淆矩阵结果，识别分类偏差，教师指导优化方向与数据扩展建议 | 10分钟   | 混淆矩阵模板.png        |

## 课程总结

| 内容     | 主要内容                                                     | 预计时长 | 素材附件        |
| -------- | ------------------------------------------------------------ | -------- | --------------- |
| 知识回顾 | 回顾过拟合、泛化、混淆矩阵、图像规范四个关键词               | 5分钟    | 回顾PPT小结.pdf |
| 学生反思 | 学生填写“训练集中可能出现的问题”清单，并写出改进建议         | 5分钟    | 反思卡片.docx   |
| 作业布置 | 选择一类表情，在课后采集不少于20张图片，用于后续模型迭代训练 | 2分钟    | -               |