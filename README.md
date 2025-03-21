# 具身人工智能（EAI）预备课程：数据结构与算法

[![STEMHUB ROBOTICS](https://img.shields.io/badge/STEMHUB-ROBOTICS-black?style=flat-square&color=black&labelColor=red)](https://your-website-or-repo-link.com)
[![课程徽章](https://img.shields.io/badge/EAI-Curriculum-00B0FF.svg)](https://embodied-ai.org) 
[![许可证](https://img.shields.io/badge/License-CC_BY_NC_SA_4.0-EF9421)](https://creativecommons.org/licenses/by-nc-sa/4.0/) 
[![Python版本](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org)

> **一句话简介**：本课程从 Python 编程基础到高级算法，全面结合具身AI（Embodied AI）理念，让学习者在理解数据结构与算法的同时，掌握机器人感知、决策和行动的闭环智能实现。

---

![img_1.png](assests/EAI_ROBOT.png)

## 🌟 课程简介

本课程是针对**数据结构与算法**的系统化学习项目，融合**具身人工智能**的教学理念，旨在帮助学生与教育工作者在「**编程思维**」与「**实体机器人应用**」之间搭建桥梁。课程内容涵盖从基础编程语法到高级算法设计，并通过丰富的**机器人实例**与**工业级案例**，让学习者在动手实验中掌握智能算法的思维和技术。

- **目标人群**：对数据结构与算法感兴趣、并希望深入了解智能机器人应用的高校学生、教师及相关从业人员  
- **教学特点**：  
  - 结合具身AI场景（感知-决策-行动闭环）  
  - 提供可复用的**工业级代码模板**  
  - 强调**三维教育目标**（认知、技能、价值观）  
- **成果产出**：掌握**高效算法**与**机器人系统开发**的核心技能，完成可在真实或仿真环境运行的项目演示。

---

## 🚀 课程亮点

1. **具身AI导向设计**  
   每个知识点都与真实机器人场景相呼应，从扫地机器人到自动驾驶示例，全流程体验「感知-决策-行动」的闭环。

2. **工业级案例库**  
   课程素材结合波士顿动力、特斯拉FSD等20+真实工业级系统，提供高含金量的**案例分析**与**实践项目**。

3. **软硬件协同思维**  
   教学代码以模块化设计方式封装，可轻松对接不同**传感器/执行器**，为后续硬件扩展奠定基础。

4. **三维能力培养**  
   - **认知层面**：掌握算法复杂度、数据结构原理  
   - **技能层面**：从搭建环境到工业级项目开发规范  
   - **价值观层面**：贯穿AI伦理、安全和责任设计理念

---

## 🏗️ 课程架构

以下是课程的核心模块，每个模块包括若干节课，共计**15节**。

![img.png](assests/cu_flow.png)


### 基础编程模块（1-5节）

Python编程范式与环境
数据结构入门：列表、字典、集合
基础案例：简易机器人控制脚本

### 核心算法模块（6-10节）

线性结构：栈、队列
树与堆：遍历、优先级调度
图与路径规划：BFS、A* 算法
核心案例：智能避障小车

### 高级算法模块（11-14节）

查找与排序：二分法、快速排序
分治策略与递归：DFS、背包问题
动态规划：路线优化、策略决策
算法案例：多机器人协同路径规划

### 综合实践模块（第15节）

智能体系统开发
整合感知-决策-行动链路

### 毕业项目：结合硬件或仿真环境的完整具身AI项目

## 📂 目录结构
```plaintext
eai-dsa-course/
├── README.md                 # 项目说明（当前文件）
├── requirements.txt          # Python依赖列表
├── CONTRIBUTING.md           # 贡献指南
├── examples/                 # 示例代码
│   ├── robot_simulator.py    # 虚拟机器人仿真脚本
│   └── vacuum_robot.py       # 扫地机器人路径规划示例
├── modules/                  # 课程核心模块
│   ├── data_structures/      # 数据结构相关资料
│   ├── algorithms/           # 核心与高级算法
│   └── eai_integration/      # 具身AI相关接口
└── docs/                     # 文档与课件
    ├── lesson1_intro.md
    ├── lesson2_lists.md
    ├── ...
    └── lesson15_capstone.md
```

## 🛠️ 如何开始
1. 克隆与安装
bash
复制
编辑
### 克隆课程仓库
```bash
git clone https://github.com/<your-username>/eai-dsa-course.git
cd eai-dsa-course
```


### 安装Python依赖
```bash
pip install -r requirements.txt
```
提示：建议使用 virtualenv 或 conda 等工具创建虚拟环境，以避免依赖冲突。


## 🤝 贡献指南
我们非常欢迎您对本项目做出贡献，包括但不限于：

- **提交Issue**：报告您在学习或项目实践过程中的任何问题、错误或建议
- **文档改进**：为课程材料、注释和使用教程做出修订或扩展
- **新案例分享**：分享更多有趣且具备教学价值的机器人应用场景或代码示例
- **如需贡献，请参见 CONTRIBUTING.md 以了解更多细节。我们也鼓励您通过 Pull Request 的方式提交改进。**

## 📜 许可证
本项目采用 CC BY-NC-SA 4.0 协议发布，意味着：

- 署名（BY）：STEMHUB®️ | Yinshen Wang, JJ Zhang
- 非商业使用（NC）：您不可以将本项目用于商业目的
- 相同方式共享（SA）：若再发布，需使用相同的授权条款
- 如有其他使用需求，请联系我们以获得授权许可。

## 📞 联系方式
- **课程咨询:** wangyinshen@worldshaper.cn
- **技术支持：** wangyinshen@worldshaper.cn
- **社区讨论：** 可以加入我们的 Discord讨论组（示例链接）或通过 Issue 与我们互动
- **一起探索机器人感知、决策与行动的无限可能，构建智能新时代的核心算法能力！**

## 常见问题（FAQ）
Q：课程需要什么先修知识？
A：需要具备基础的编程常识（变量、控制流等），若对Python不熟悉，可从课程前几节入门。

Q：是否需要真实的机器人硬件？
A：并非必需。课程中自带仿真环境和示例代码，但如果有硬件设备可获得更真实的实践体验。

Q：学习过程中遇到报错、疑问该怎么办？
A：欢迎随时在 GitHub Issue 区提问，或者加入社区讨论组与其他学习者及助教互动。

