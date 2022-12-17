# README

## 麻將(Mahjong)

## Intro your game

台灣十六張麻將

## Tech Stack
1. Tech Stack：
   * 後端語言：Python
     * Framework：Fast API － 輕量化、好上手
     * DB： MongoDB PyMongo
   * 前端：Vue或React  (暫定)
2. Practice Stack：
   * Test-Driven Development
   * Domain-Driven Design
   * Clean Architecture
3. Analysis & Design：
   * Event Storming
   * Example Mapping
   * OOA/D
4. DevOps：
   * Github Action
5. Development：
   *   待定


## Git Commit message

- **feat:** 新增/修改功能 (feature)。
- **bug:** 修補 bug (bug fix)。
- **docs:** 文件 (documentation)。
- **refactor:** 重構 (既不是新增功能，也不是修補 bug 的程式碼變動)。
- **test:** 增加測試 (when adding missing tests)。
- **chore:** 建構程序或輔助工具的變動 (maintain)。
- **revert:** 撤銷回覆先前的 commit 例如：revert: type(scope): subject (回覆版本：xxxx)。


## GitHub Flow

1. 團隊任一人皆可依據功能建立issue，並依據需求類型添加lebel及指派人員處理
2. 分支的建立規則：
    1. 分支名稱為dev和左斜線與 issue 編號結合
    2. Pattern: `dev/${issueId}`，範例： feat/1 
3. 本地開發測試完成之後，並push本地分支到遠端
4. 發出Pull Request，於commit裡填寫issue link，請求Reviewer Review Code
5. 需有2人Review PR
    1. 後端Reviewer：Saker、Fuyao
    2. 前端Reviewer：待定
6. 待兩位Reviewer確認無誤後，通知開發人員已確認完成
7. 開發人員將此PR合進Master並closed issue
