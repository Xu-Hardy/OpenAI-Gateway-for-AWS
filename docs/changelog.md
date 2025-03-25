# Changelog

本项目遵循 [Semantic Versioning 2.0.0](https://semver.org/lang/zh-CN/) 语义化版本规范。

## [0.1.0] - 2025-03-24
### ✨ 新增
- 接入 DeepSeek 模型，完成基础推理能力验证
- 实现 `POST /v1/chat/completions` 接口的非流式调用兼容
- 支持 OpenAI 消息格式向 Bedrock 格式的转换逻辑（`content -> [{text}]`）

---

## [Unreleased]
### 🚧 开发中
- [ ] 支持 `stream=true` 的 SSE 流式响应
- [ ] 集成 SageMaker 后端，作为 Bedrock 补充选项
- [ ] 增加模型参数统一映射（temperature, top_p 等）
- [] 提供完整调用示例（curl, Python client, Postman）
- [] 增加日志系统与错误处理机制


