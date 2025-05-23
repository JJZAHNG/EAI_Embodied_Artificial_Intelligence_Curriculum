# EAI｜03 音频数据建模与非语义信号处理

课程名称：人工智能基础 

单元主题：声音识别与音频建模初探 

授课年级：初中高年级 / 高一 

计划课时：90分钟

## 课程概括

本节课聚焦人工智能中的音频建模任务，引导学生了解声音的数字化方式、非语义音频（如拍手、敲击、哨声）在识别系统中的应用方法，并理解音频与语音识别任务的区别。通过Teachable Machine实操，学生将构建一个音频三分类模型，实现简单声控交互系统雏形，培养学生对声音特征提取的理解与应用能力。

## 教学目标

### 🎯知识与技能

- 了解声音信号的基本数字化方式（采样率、频率特征）；
- 掌握非语义音频分类模型的构建方法；
- 初步理解MFCC（梅尔频率倒谱系数）与音频特征提取原理；
- 能够使用 Teachable Machine 训练并测试一个音频识别模型。

### 🎯过程与方法

- 通过现场体验不同声音的波形差异引发兴趣；
- 分析声音信号与图像数据的结构区别；
- 分组采集拍手 / 敲击 / 哨声等音频数据进行训练；
- 观察模型训练中对输入声音的敏感性与区分度。

### 🎯情感态度价值观

- 激发学生对日常声音背后规律的观察力；
- 鼓励学生从生活中发现问题、提出AI解决方案；
- 培养跨模态数据理解能力与模型应用意识。

## 重点难点

| 教学重点                     | 教学难点                         |
| ---------------------------- | -------------------------------- |
| 非语义声音建模的任务定义     | 理解声音信号中蕴含的可分类特征   |
| 音频信号的采样特性与建模方式 | 区分音频分类 vs 语音识别本质区别 |

## 教学准备

| 软件              | 硬件                     | 扩展                   |
| ----------------- | ------------------------ | ---------------------- |
| Teachable Machine | 学生个人电脑、麦克风模块 | Audacity / 音频采集APP |

## 教学过程

| 环节     | 主要内容                                                     | 预计时长 | 素材附件            |
| -------- | ------------------------------------------------------------ | -------- | ------------------- |
| 导入     | 播放不同非语义声音（拍手、咳嗽、哨声）引导学生听辨与模式识别意识 | 10分钟   | 声音素材包1.zip     |
| 知识讲解 | 声音信号的本质、采样率、频谱图、MFCC简介，音频模型结构       | 25分钟   | 课件PPT_03.pdf      |
| 工具实操 | 使用 Teachable Machine 构建音频三分类模型，进行测试与反馈演示 | 25分钟   | 操作视频 / 示范模型 |
| 小组建模 | 学生分组采集各类声音，自定义模型训练并进行对比测试           | 20分钟   | 分组记录表.xlsx     |
| 模型分析 | 比较不同录音条件下模型表现差异，引导学生理解背景噪声对模型的影响 | 10分钟   | 分析图表模板.png    |

## 课程总结

| 内容     | 主要内容                                                     | 预计时长 | 素材附件        |
| -------- | ------------------------------------------------------------ | -------- | --------------- |
| 知识回顾 | 回顾音频建模流程、非语义分类任务、声音与图像建模对比         | 5分钟    | 总结PPT_03.pdf  |
| 学生反思 | 每人反思一次录音中最具挑战的环节，并提出改进建议             | 5分钟    | 反思卡片03.docx |
| 作业布置 | 回家录制3种环境下的拍手声，记录时长、清晰度、背景噪声进行归档 | 2分钟    | -               |