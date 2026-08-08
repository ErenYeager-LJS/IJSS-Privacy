# GPT + Codex 协作规范

## 目标

建立稳定、高效、可追踪的 AI 协作流程：

- ChatGPT 负责思考、设计、拆解、审查
- Codex 负责实现、测试、提交、创建 PR
- GitHub 负责记录、交付、追踪
- 用户负责决策、验收、合并

核心原则：所有可交付代码、文档和审查意见都围绕 GitHub 的 Branch、Commit、Pull Request、Diff、Review 和 Handoff 展开，避免在聊天窗口里反复传递代码文件。

---

## 角色分工

### ChatGPT

负责：

- 理解需求
- 澄清目标和边界
- 制定方案
- 拆分任务
- 设计架构
- Review PR
- 分析 Bug
- 判断下一步任务

ChatGPT 不直接承担大规模编码任务。Review 时以 PR Diff 为入口，但可以读取必要上下文文件、测试文件、接口定义和相关文档，以判断跨模块影响。

### Codex

负责：

- 编写代码
- 修改代码
- 编写文档
- 编写测试
- 执行测试
- 修复 Bug
- 提交 Commit
- 创建 Pull Request
- 更新 Handoff

Codex 不主动改变需求，不擅自扩大任务范围，不擅自修改未授权模块。发现需求矛盾、设计风险、测试缺口或实现会影响范围外模块时，应停止并报告，由用户决定下一步。

### 用户

负责：

- 提出需求
- 确认方案
- 明确任务优先级
- 决定是否接受风险
- 决定是否合并 PR
- 决定项目方向

### GitHub

GitHub 是唯一事实来源（Single Source of Truth）。

所有协作均围绕：

- Branch
- Commit
- Pull Request
- Diff
- Review
- Handoff
- Issue 或任务记录

禁止通过聊天窗口反复传递代码文件。聊天窗口可以用于讨论方案、解释 Diff、确认风险和做决策，但最终实现状态以 GitHub 为准。

---

## 任务输入模板

每个任务交给 Codex 前，尽量提供以下信息：

```text
Task ID:
Goal:
Scope:
Do not touch:
Acceptance criteria:
Test command:
Risk notes:
```

说明：

- `Goal` 写最终要达到的行为，不只写“改一下”。
- `Scope` 写允许修改的模块、页面、接口或文档。
- `Do not touch` 写明确禁止改动的文件、模块或行为。
- `Acceptance criteria` 写用户验收标准。
- `Test command` 写必须运行的测试命令；没有自动测试时写手动检查方式。
- `Risk notes` 写已知兼容性、数据、安全或部署风险。

---

## 工作流程

1. ChatGPT 分析需求并拆分任务。
2. 用户确认任务边界。
3. 用户将任务交给 Codex。
4. Codex 从 `main` 创建任务分支。
5. Codex 仅修改本任务涉及文件。
6. Codex 完成后运行必要测试。
7. Codex 更新 Handoff。
8. Codex Push 并创建 Pull Request。
9. 用户将 PR 链接发送给 ChatGPT。
10. ChatGPT Review PR，重点看 Diff，并在必要时读取相关上下文。
11. 用户决定 Merge、要求继续修改，或关闭 PR。
12. Merge 后删除任务分支。

分支命名：

```text
task-编号-简短描述
```

示例：

```text
task-001-login
task-002-fix-payment-timeout
task-003-docs-collaboration-flow
```

---

## 分支与 PR 规则

默认规则：

- 不直接修改 `main`
- 一个任务一个 Branch
- 一个 Branch 一个 PR
- PR 合并后删除任务分支
- 未合并的任务不叠加无关修改

允许例外：

- 文案、注释、格式、单行配置等低风险小改，可以合并到一个 `chore-*` 分支或一个批量 PR。
- 例外 PR 仍然必须说明修改范围、测试结果和风险。
- 不允许把功能开发、重构、Bug 修复混在一个无法审查的大 PR 里。

---

## Pull Request 要求

每个 PR 应包含：

- 修改目的
- 修改文件列表
- 修改内容说明
- 测试结果
- 未运行的测试及原因
- 已知问题
- 风险说明
- 回滚方式
- 下一步建议

推荐 PR 模板：

```markdown
## Purpose

## Changed files

## What changed

## Tests run

## Tests not run

## Known issues

## Risks

## Rollback

## Next steps
```

---

## 修改原则

Codex 必须遵守：

- 不直接修改 `main`
- 不修改任务范围外代码
- 不做未经要求的重构
- 不增加无意义抽象
- 不修改无关文件
- 不猜测需求
- 不绕过测试失败
- 不隐藏未完成项
- 不把聊天讨论当作最终事实来源
- 有疑问先停止并询问

Codex 可以主动做的事：

- 修复本任务范围内明显相关的小问题
- 补充必要测试
- 补充必要文档
- 删除本任务引入的无用代码
- 报告发现的范围外问题，但不擅自修改

---

## 测试规范

每个任务至少说明测试情况：

```text
Tests run:
- npm test
- npm run lint
- manual check: login with valid account

Tests not run:
- e2e tests not run because local service dependency is unavailable
```

要求：

- 能运行自动测试时必须运行相关测试。
- 测试失败时不能直接提交为“完成”，必须说明失败原因。
- 没有自动测试时，必须写清楚手动检查步骤。
- 涉及公共模块、权限、安全、数据迁移、支付、登录、文件删除等高风险改动时，测试范围必须扩大。

---

## ChatGPT Review 原则

ChatGPT Review 时重点关注：

- 是否符合需求
- 是否存在逻辑错误
- 是否影响其它模块
- 是否存在安全风险
- 是否有更简单方案
- 是否存在多余修改
- 是否缺少测试
- 是否有回滚风险

Review 以 Diff 为入口，而不是只看 Diff。以下情况必须读取相关上下文：

- 修改公共模块
- 修改权限、登录、支付、删除、上传、下载等敏感逻辑
- 修改数据结构、数据库迁移或接口契约
- 测试失败或测试缺失
- Diff 中出现不熟悉的抽象、全局状态或副作用
- PR 描述与代码行为不一致

Review 输出应优先列问题，再给总结。问题按严重程度排序，并引用具体文件和行号。

---

## Handoff

每个任务结束必须更新 Handoff。

保留历史文件：

```text
docs/handoff/task-001-login.md
docs/handoff/task-002-fix-payment-timeout.md
```

同时维护最新指针：

```text
docs/handoff/latest.md
```

`latest.md` 可以复制最新任务内容，也可以只指向最新任务文件，但不能导致历史 Handoff 丢失。

每个 Handoff 至少包含：

- Task ID
- Branch
- PR
- Changed files
- What changed
- Tests run
- Tests not run
- Risks
- Known issues
- Rollback
- Next task

推荐模板：

```markdown
# Handoff: task-001-login

## Branch

## PR

## Changed files

## What changed

## Tests run

## Tests not run

## Risks

## Known issues

## Rollback

## Next task
```

确保任何 AI 或人类维护者都可以继续接手项目。

---

## 决策与升级规则

遇到以下情况，Codex 必须停止并请求用户决策：

- 需求不明确
- 需要修改任务范围外模块
- 需要重构公共架构
- 测试失败且原因不确定
- 需要删除数据或迁移数据
- 涉及权限、安全、支付、隐私、账号、密钥
- 实现方案会改变用户可见行为
- 需要新增重大依赖或服务

遇到以下情况，ChatGPT Review 必须明确标记风险：

- PR 缺少测试
- PR 修改范围明显大于任务范围
- PR 描述和 Diff 不一致
- 回滚方式不清楚
- 涉及安全、隐私、权限或数据完整性

---

## 协作原则

ChatGPT 负责想清楚。

Codex 负责做出来。

GitHub 负责记录全过程。

用户负责最终决策。

整个流程始终围绕 GitHub PR，而不是聊天窗口传递代码。

对话可以推动思考，但交付必须落在 Branch、Commit、PR、Diff、Review 和 Handoff 上。
