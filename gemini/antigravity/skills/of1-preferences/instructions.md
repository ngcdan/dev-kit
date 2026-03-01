# OF1 CRM Developer Onboarding & Coding Standards

## 1. Tech Stack
- **Language:** Java 21
- **Framework:** Spring Boot (Security, OAuth2 Resource Server)
- **Build:** Gradle (Multi-module)
- **Database:** PostgreSQL (implied), interacting via `SqlMapRecord` / Custom DB module.
- **Libraries:** Lombok, SLF4J, JUnit 5.

## 2. Project Structure
- **Root:** `build.gradle`, `settings.gradle`
- **Modules:**
  - `module/core`: Core logic (Forwarding, Quotations, Reports).
  - `module/price`: Pricing logic.
  - `module/sales`: Sales logic.
  - `webui`: Frontend/Web interface.

## 3. Architecture & Patterns

### Service Layer
- **Naming:** explicit service names, e.g., `@Service("BDService")`.
- **Inheritance:** Must extend `BaseComponent`.
- **Transaction:** Explicitly use `@Transactional(readOnly = true)` for search/get methods.
- **Dependency Injection:** Field injection (`@Autowired`) is the standard pattern.
- **Logic Delegation:** Services often delegate complex logic to "Logic" classes (e.g., `BusinessReportLogic`), keeping the Service clean as a facade/transaction boundary.

### Data Transfer Objects (DTOs) & Entities
- **Lombok:** Use `@Getter`, `@Setter`, `@NoArgsConstructor`. **Avoid `@Data`**.
- **Fields:** Use wrapper types (`Long`, `Double`) instead of primitives.
- **Mapping Logic:**
  - **Pattern:** Static factory/helper methods *inside* the DTO are used for mapping.
  - **Source:** Often maps from `SqlMapRecord` (a generic DB result map).
  - **Example:**
    ```java
    public static List<MyReport> computeFromMapRecords(List<SqlMapRecord> records) {
        // Logic to group, sum, and transform records into DTOs
    }
    ```

### Naming Conventions
- **Packages:** `cloud.datatp.fforwarder.core...`, `net.datatp...`
- **Classes:** PascalCase (e.g., `QuotationReport`, `BDService`).
- **Variables:** camelCase.

## 4. Common Tasks

### Creating a New Service
1. Create class in `cloud.datatp.fforwarder...`
2. Annotate `@Service("MyServiceName")`.
3. Extend `BaseComponent`.
4. Inject necessary Logic/Repository components using `@Autowired`.

### Querying Data
- Use `SqlQueryParams` for passing parameters.
- Return types are often `List<SqlMapRecord>` for raw data or mapped DTOs for reports.

## 5. Testing
- **Framework:** JUnit 5 (`junit-jupiter`).
- **Tags:** Use tags like `unit`, `integration` to separate test suites.
