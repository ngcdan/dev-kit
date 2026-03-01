---
name: antigravity-preferences-pack
description: Preferences + coding-style rules pack for Google Antigravity IDE (agent-first IDE). Use when generating, refactoring, or reviewing code for Đàn in OF1 projects (Java/Spring + React/TypeScript) và khi chuẩn bị tham chiếu.
---

# Antigravity Preferences Pack (Đàn's style)

Skill này chứa tổng hợp các quy định thiết yếu mà AI Agent (Antigravity/Gemini) phải tuân theo khi tạo, chỉnh sửa hoặc đánh giá mã nguồn trong các workspace của dự án OpenFreightOne (OF1).

## 1. Ngôn Ngữ & Framework Stack
- Backend: `Java 17+` / `Spring Framework`, JPA/Hibernate (không dùng Spring Boot Controller truyền thống mà dùng custom RPC config qua `appContext.createHttpBackendCall`).
- Frontend: `React` / `TypeScript` (Class Component based) cùng UI Kit nội bộ `@of1-webui/lib`. Cấm mix JSX HTML thông thường nếu có component tương đương phía `of1-webui`.

## 2. Java Coding Style
- **Indentation**: 2 spaces (Tuyệt đối không dùng tabs).
- **Line Length**: Max 120 characters/line.
- **Line Breaks**: Sử dụng ngắt dòng có chủ đích thay vì word-wrap vô thức. Khuyến khích nhóm các method parameters logic trên cùng 1 dòng nếu ngắn gọn.
- **Imports**: Khai báo rõ class cụ thể, hạn chế dùng wildcard import (`.*`) trừ khi có >5 class từ cùng 1 package dài.
- **Layering rules**:
  - `Controller/Service`: Đặt annotation `@Transactional` cẩn thận, pass `ClientContext client` đầu tiên vào mọi method, wrap các request logic xuống `Logic Layer` thay vì viết thẳng.

## 3. TypeScript & React UI Style Mở Rộng
- **Class Components**: Tất cả màn hình UI, Editor, Form, ListView đều PHẢI viết bằng `Class Component` extend từ `app.AppComponent` hoặc họ `entity.AppDbComplexEntityEditor`.
- **Tuyệt đối cấm**: Không tự ý đổi project sang `React Hooks` (useState, useEffect, Functional Component) làm gãy kiến trúc OOP quản lý View State của framework OF1.
- **Variable Naming**: `camelCase` cho parameter/variable và `PascalCase` cho class, Component.
- **UI Toolkit `@of1-webui/lib` ưu tiên tối thượng**:
  - `bs`: Dùng Layout (`bs.Scrollable`, `bs.Row`, `bs.Col span={3}`, `bs.Toolbar`, `bs.Button`).
  - `input`: Form (`input.BBStringField`, `input.BBSelectField`, `input.BBTextField`) cho string, select, textarea liên kết binding trực tiếp thông qua `{bean}` và `field='...'`.
  - `entity`: Các nút Save tự động (`entity.ButtonEntityCommit`), bảng dữ liệu phức tạp.
- **Force Update**: Khi biến đổi ngầm Object `bean` do OF1 observer theo dõi, chủ động gọi `this.forceUpdate()` để render lại UI thay vì setState.
- **Event Handling**: Viết event method theo dạng arrow function: `onXxxAction = (param) => { ... }` để giữ Context `this` thay vì `.bind(this)`.

## 4. Documentation & Comments
- **Bình luận ngắn gọn, tập trung vào "Tại sao" thay vì "Cái gì"**: Không bình luận những thứ quá hiển nhiên như `// Get user by id` đứng trên methods `getUserById()`.
- Chú thích Javadocs/TypeDoc ở đầu phương thức phức tạp public hoặc Class Logic giải thích Flow hoặc cấu trúc Data trả về.

## 5. Refactoring & Testing
- *Thông báo/Hỏi ý kiến trước khi thực hiện large/wide refactors ảnh hưởng nhiều file liên đới, hay những kiến trúc khó khôi phục (hard-to-rollback changes).*
- Mặc định: Không nhồi nhét file Logs trừ khi Đàn yêu cầu rõ (*no logging unless explicitly requested*).
- System Tests (Unit Tests/ Integration Test) chỉ write **on request** (khi có yêu cầu).

## 6. Project Rules
Sử dụng các skill template chi tiết của project khi tạo Class liên quan:
- `of1-be-template`: Cho Logic layer, Service Boundary layer, Repository, Entity.
- `of1-fe-template`: Cho các form Editor của WebUI, pattern Call HTTP đặc chế và Design System của OF1.
- `kafka-implementation-template`: Khi code event/messaging.
