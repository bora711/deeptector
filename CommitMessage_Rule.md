# 커밋 메세지 규칙

> 커밋 메세지 통일화를 위한 규칙입니다.
>
> 커밋 전에 읽어주세요...

### 참고 사이트

https://blog.ull.im/engineering/2019/03/10/logs-on-git.html

#### 동명사보다 명사를 사용

#### 관사를 사용하지 않는다.

#### 부정문 `Don't`를 사용

#### 오타 수정은 `Fix typo`

### FIX

##### 올바르지 않은 것을 고친 경우

Fix A : A를 수정합니다

Fix A in B : B의 A를 수정합니다

FIx A which B, Fix A that B : B절인 A를 수정합니다

- 필수인 부분은 아니지만 디테일하게 표현하고 싶을 때

Fix A to B : B를 위해 A를 수정합니다

Fix A so that B : A를 수정해서 B가 되었습니다

- Fix A to B 와 의미는 비슷하나 어감이 다릅니다. 고쳐진 B의 상태가 보다 강조됩니다

Fix A where B : B처럼 발생하는 A를 수정했습니다

- 여기서 A는 보통 'issue', 'error', 'crash'등이 들어갑니다. B는 문제가 발생한 모습 적어주기

Fix A when B : B일때 발생하는 A를 수정했습니다.

- 여기서 A는 보통 'issue', 'error', 'crash'등이 들어갑니다. B는 문제가 발생하는 상황을 적어주면 됩니다

### ADD

##### 코드나 테스트, 예제, 문서 등의 추가가 있을 때 사용합니다.

Add A : A를 추가합니다.

Add A for B : B를 위해 A를 추가했습니다

Add A to B : B에 A를 추가했습니다

### REMOVE

##### 코드의 삭제가 있을 때

##### 보통 a앞에 'unnecessary','useless','unneeded','unused','duplicated'가 붙는 경우가 많다.

Remove A : A를 삭제합니다.

Remove A from B : B에서 A를 삭제합니다

### USE

##### 특별히 무언가를 사용해 구현을 하는 경우입니다.

USE A for B : B에 A를 사용합니다

USE A to B : B가 되도록 A를 사용합니다

USE A in B : B에서 A를 사용합니다

USE A instead of B : B 대신 A를 사용합니다

### REFACTOR

##### 전면 수정이 있을 때 사용합니다

Refactor A

### SIMPLIFY

##### 복잡한 코드를 단순화 할때, 약한수정의 경우 이용하면 좋습니다.

Simplify A : A를 단순화합니다.

### UPDATE

##### 원래도 정상적으로 동작, 수정,추가 보완, 한다는 개념

##### 코드보다는 문서, 리소스, 라이브러리등에 사용

Update A to B : A를 B로 업데이트 합니다, A를 B하기 위해 업데이트 합니다

### CORRECT

##### 주로 문법의 오류나 타입의 변경, 이름 변경 등에 사용

Correct A : A를 고칩니다

### PREVENT

##### 특정한 처리를 못하게 막습니다.

Prevent A : A하지 못하게 막습니다

Prevent A from B : A를 B하지 못하게 막습니다

### RENAME

##### 이름변경이 있을 때 사용합니다

Rename A to B : A를 B로 이름 변경합니다

### SET

##### 변수값을 변경하는 등의 작은 수정에 사용합니다

Set A to B : A를 B로 설정합니다

------

### REVISE

##### Update와 비슷하나 문서의 개정이 있을 때 사용

Revise A : A 문서를 개정합니다.