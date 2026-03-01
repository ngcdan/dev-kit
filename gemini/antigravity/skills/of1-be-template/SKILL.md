---
name: of1-be-template
description: Template chuẩn để implement Backend Layer (Controller/Service/Logic/Repository) vào dự án OF1. Cung cấp boilerplate code cho hệ thống Spring Boot + RPC call đặc thù của nền tảng OF1.
---

# Template Backend OF1 (Service/Logic/Repository)

Dự án OF1 triển khai kiến trúc BE đặc thù không sử dụng REST Controller truyền thống cho các API gọi từ WebUI, thay vào đó WebUI sử dụng `createHttpBackendCall` mapping trực tiếp tới các `@Service` / `@Transactional` Bean.

Theo pattern đó, Backend sẽ chia làm 3 lớp:
1. **Service Layer**: Nơi định nghĩa các function entry-point (nhận request từ WebUI qua HTTP RPC), quản lý Transaction boundaries (`@Transactional`), và check permission/ClientContext.
2. **Logic Layer**: Chứa pure business logic, xử lý data validation, call external service.
3. **Repository Layer**: Kế thừa `JpaRepository`, thực hiện query Database (`@Query`).
4. **Entity Layer**: Kế thừa `PersistableEntity<Long>` cho JPA Model.

Sử dụng skill này khi bạn cần làm tính năng mới ở Backend để đảm bảo tuân thủ thiết kế kiến trúc chuẩn.

## 1. Entity (`YourEntity.java`)

```java
package [your.package.entity];

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonInclude;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import net.datatp.module.data.db.entity.PersistableEntity;
import net.datatp.util.text.DateUtil;

import java.util.Date;

/**
 * Model ánh xạ DB table.
 * TODO: Đổi tên Table, các trường và index.
 */
@Entity
@Table(
  name = YourEntity.TABLE_NAME,
  indexes = {
    @Index(name = YourEntity.TABLE_NAME + "_code_idx", columnList = "code")
  }
)
@JsonInclude(JsonInclude.Include.NON_NULL)
@NoArgsConstructor
@Getter @Setter
public class YourEntity extends PersistableEntity<Long> {
  public static final String TABLE_NAME = "your_project_table_name";
  // TODO: Add thêm properties mapping ở đây
}
```

## 2. Repository (`YourEntityRepository.java`)

```java
package [your.package.repository];

import java.io.Serializable;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import [your.package.entity].YourEntity;

/**
 * JPA Repository Interface
 */
@Repository
public interface YourEntityRepository extends JpaRepository<YourEntity, Serializable> {

  @Query("SELECT e FROM YourEntity e WHERE e.id = :id")
  YourEntity getById(@Param("id") Long id);

  @Query("SELECT e FROM YourEntity e WHERE e.code = :code")
  List<YourEntity> findByCode(@Param("code") String code);

  // TODO: Add các Native Query hoặc JPA Query khác
}
```

## 3. Logic Layer (`YourEntityLogic.java`)

```java
package [your.package];

import java.util.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import net.datatp.module.service.BaseComponent;
import net.datatp.security.client.ClientContext;
import net.datatp.util.error.ErrorType;
import net.datatp.util.error.RuntimeError;

import [your.package.entity].YourEntity;
import [your.package.repository].YourEntityRepository;

/**
 * Logic Component chứa strict business rules, không mở transaction ở đây để tái sử dụng.
 */
@Component
public class YourEntityLogic extends BaseComponent {

  @Autowired
  private YourEntityRepository repository;

  public YourEntity getById(ClientContext ctx, Long id) {
    if (id == null) return null;
    return repository.getById(id);
  }

  public YourEntity saveEntity(ClientContext ctx, YourEntity entity) {
    // 1. Validation
    if (entity.getCode() == null || entity.getCode().isEmpty()) {
      throw new RuntimeError(ErrorType.IllegalArgument, "Code is required!");
    }

    // 2. Audit Tracking
    if (entity.getId() == null) {
      entity.setDateCreated(new Date());
    }
    entity.setDateModified(new Date());

    // 3. TODO: Business rules (check trùng code, tính toán trường phụ, ...)

    // 4. Persist
    return repository.save(entity);
  }

  public int deleteEntities(ClientContext ctx, List<Long> targetIds) {
    // TODO: Add logic để check liên kết trước khi xóa (VD: không cho xóa nếu record đang active)
    repository.deleteAllById(targetIds);
    return targetIds.size();
  }
}
```

## 4. Service Layer (`YourEntityService.java` -> Cổng giao tiếp với WebUI)

```java
package [your.package];

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import net.datatp.module.service.BaseComponent;
import net.datatp.security.client.ClientContext;

import [your.package.entity].YourEntity;

/**
 * Boundary Service nhận calls từ WebUI (Framework sẽ auto map `appContext.createHttpBackendCall`).
 * QUAN TRỌNG: Must specify proper `transactionManager` if available (e.g. `crmTransactionManager`)
 */
@Service("YourEntityService") // <- Tên Bean này sẽ được gọi từ FE: appContext.createHttpBackendCall("YourEntityService", ...)
@Transactional // (transactionManager = "crmTransactionManager") -> TODO: Bật tùy config module
public class YourEntityService extends BaseComponent {

  @Autowired
  private YourEntityLogic logic;

  // READ methods
  @Transactional(readOnly = true)
  public YourEntity getEntity(ClientContext client, Long id) {
    return logic.getById(client, id);
  }

  // WRITE methods
  @Transactional
  public YourEntity saveEntity(ClientContext client, YourEntity entity) {
    return logic.saveEntity(client, entity);
  }

  @Transactional
  public int deleteEntities(ClientContext client, List<Long> targetIds) {
    return logic.deleteEntities(client, targetIds);
  }

  // TODO: Add custom methods ví dụ fetchList, search...
  // Object trả về hoặc nhận vào có thể dùng SqlMapRecord hoặc POJO
}
```
